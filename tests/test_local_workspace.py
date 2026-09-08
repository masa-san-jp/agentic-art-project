import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.validate import validate


ROOT = Path(__file__).resolve().parents[1]


class LocalWorkspaceTests(unittest.TestCase):
    def checkout(self, *, git: bool = True) -> tuple[tempfile.TemporaryDirectory, Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name).resolve()
        shutil.copytree(
            ROOT,
            root,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.py[cod]"),
        )
        if git:
            self.git(root, "init", "-q")
            self.git(root, "add", ".")
            self.git(
                root,
                "-c",
                "user.name=fixture",
                "-c",
                "user.email=fixture@example.invalid",
                "commit",
                "-qm",
                "initial fixture",
            )
        return temporary, root

    @staticmethod
    def git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )

    def test_fresh_checkout_without_workspace_passes(self):
        temporary, root = self.checkout()
        self.addCleanup(temporary.cleanup)
        self.assertFalse((root / ".agentic-art").exists())
        self.assertEqual([], validate(root))

    def test_workspace_contents_are_ignored_and_validator_does_not_write(self):
        temporary, root = self.checkout()
        self.addCleanup(temporary.cleanup)
        workspace = root / ".agentic-art"
        (workspace / "state").mkdir(parents=True)
        (workspace / "internal").mkdir()
        (workspace / "staging").mkdir()
        config = workspace / "config.yaml"
        config.write_text("private: true\n", encoding="utf-8")
        before = config.read_bytes()

        self.assertEqual([], validate(root))
        self.assertEqual(before, config.read_bytes())
        status = self.git(root, "status", "--porcelain", "--untracked-files=all")
        self.assertEqual("", status.stdout)
        self.assertEqual(0, self.git(root, "check-ignore", "-q", "--no-index", ".agentic-art/probe").returncode)

    def test_force_added_private_file_is_rejected_without_printing_content(self):
        temporary, root = self.checkout()
        self.addCleanup(temporary.cleanup)
        secret = "DO NOT PRINT THIS PRIVATE BODY"
        path = root / ".agentic-art/secret.txt"
        path.parent.mkdir()
        path.write_text(secret, encoding="utf-8")
        self.git(root, "add", "-f", ".agentic-art/secret.txt")

        errors = validate(root)
        self.assertTrue(any(error.startswith("LOCAL_WORKSPACE_TRACKED:") for error in errors))
        self.assertNotIn(secret, "\n".join(errors))
        self.assertEqual(errors, validate(root))
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/validate.py"), "--check", "--root", str(root)],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertNotEqual(0, result.returncode)
        self.assertNotIn(secret, result.stdout + result.stderr)

    def test_missing_or_non_root_ignore_rule_fails_closed(self):
        temporary, root = self.checkout()
        self.addCleanup(temporary.cleanup)
        (root / ".gitignore").write_text(".agentic-art/\n", encoding="utf-8")
        errors = validate(root)
        self.assertTrue(any(error.startswith("LOCAL_WORKSPACE_IGNORE:") for error in errors))

    def test_workspace_symlink_and_child_symlink_fail_without_following(self):
        temporary, root = self.checkout()
        self.addCleanup(temporary.cleanup)
        target_temporary = tempfile.TemporaryDirectory()
        self.addCleanup(target_temporary.cleanup)
        target = Path(target_temporary.name).resolve()
        (root / ".agentic-art").symlink_to(target, target_is_directory=True)
        errors = validate(root)
        self.assertTrue(any(error.startswith("LOCAL_WORKSPACE_SYMLINK:") for error in errors))

        (root / ".agentic-art").unlink()
        (root / ".agentic-art").mkdir()
        (root / ".agentic-art/state").symlink_to(target, target_is_directory=True)
        errors = validate(root)
        self.assertTrue(any(error.startswith("LOCAL_WORKSPACE_SYMLINK:") for error in errors))

    def test_path_escape_and_public_record_reference_fail(self):
        temporary, root = self.checkout()
        self.addCleanup(temporary.cleanup)
        layout = root / "public-project.yaml"
        original = layout.read_text(encoding="utf-8")
        for field, expected in (
            ("root", ".agentic-art"),
            ("config", ".agentic-art/config.yaml"),
            ("state", ".agentic-art/state"),
            ("internal", ".agentic-art/internal"),
            ("staging", ".agentic-art/staging"),
        ):
            for bad in ("../escape", "/absolute/path"):
                with self.subTest(field=field, bad=bad):
                    changed = original.replace(f"  {field}: {expected}", f"  {field}: {bad}")
                    layout.write_text(changed, encoding="utf-8")
                    errors = validate(root)
                    self.assertTrue(any("local_workspace" in error for error in errors))

        layout.write_text(original, encoding="utf-8")
        record_readme = root / "plans/P0004-necessary-retreat/README.md"
        record_readme.write_text(record_readme.read_text(encoding="utf-8") + "\n[private](../../.agentic-art/internal/secret.txt)\n", encoding="utf-8")
        errors = validate(root)
        self.assertTrue(any(error.startswith("PUBLIC_LOCAL_WORKSPACE_REFERENCE:") for error in errors))

        record_readme.write_text(record_readme.read_text(encoding="utf-8").split("\n[private]")[0] + "\n", encoding="utf-8")
        metadata = root / "plans/P0004-necessary-retreat/metadata.yaml"
        metadata.write_text(metadata.read_text(encoding="utf-8") + "private_path: .agentic-art/internal/secret.txt\n", encoding="utf-8")
        errors = validate(root)
        self.assertTrue(any(error.startswith("PUBLIC_LOCAL_WORKSPACE_REFERENCE:") for error in errors))

    def test_remote_configuration_does_not_change_local_validation(self):
        temporary, root = self.checkout()
        self.addCleanup(temporary.cleanup)
        self.assertEqual([], validate(root))
        self.git(root, "remote", "add", "origin", "https://github.com/example/private.git")
        self.assertEqual([], validate(root))
        self.git(root, "remote", "set-url", "origin", "https://github.com/example/public.git")
        self.assertEqual([], validate(root))

    def test_exported_tree_without_git_uses_static_checks(self):
        temporary, root = self.checkout(git=False)
        self.addCleanup(temporary.cleanup)
        self.assertFalse((root / ".git").exists())
        self.assertEqual([], validate(root))
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/validate.py"), "--check", "--root", str(root)],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(0, result.returncode)
        self.assertIn("NOT_APPLICABLE", result.stdout)


if __name__ == "__main__":
    unittest.main()
