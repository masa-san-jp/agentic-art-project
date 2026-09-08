# Repo-local private workspace

このリポジトリをcloneまたはfork由来でcloneしたcheckoutでは、制作中の非公開・中間データをroot直下の`.agentic-art/`に置けます。これは公開カタログの一部ではありません。remoteの有無、owner名、GitHubのPublic/Private設定に依存せず、Projectの内容契約は同じです。

## 固定layout

```text
.agentic-art/
├── config.yaml  # 利用者ローカル設定（必要な場合だけ作成）
├── state/       # run/recovery evidence（必要な場合だけ作成）
├── internal/    # research/production/handoff等の非公開出力
└── staging/     # 公開transactionの一時検証領域
```

`.agentic-art/`全体と上記の子pathはGit追跡禁止です。ディレクトリやplaceholderを事前にcommitする必要はありません。`.gitignore`の規則を変更せず、固定pathやその子をsymlinkにしないでください。

## clone後の利用

fresh cloneではディレクトリがないままでも正常です。必要なときだけ、利用者のローカル環境で次のように作成します。

```sh
mkdir -p .agentic-art/state .agentic-art/internal .agentic-art/staging
# 必要な場合だけ .agentic-art/config.yaml を作成する
python3 tools/validate.py --check
git check-ignore -q --no-index .agentic-art/probe
test -z "$(git ls-files -- .agentic-art)"
git status --short --untracked-files=all
```

最後のコマンドに`.agentic-art/`配下の差分が出ないことを確認します。validatorは検査中にこの領域を作成したり、ファイルを書き換えたりしません。

## 公開昇格前の境界

`internal/`から`plans/`や`works/`へrecursive copyしません。公開recordを追加・更新する場合は、公開に必要なファイルを明示的なallowlistとして用意し、既存の受信契約を通します。

- planはProductionの`03_plan/production-plan.md`と同一bytesで、canonical attestation、stable identity/revision、列挙asset、権利・同意・安全性の審査が一致する必要があります。
- workはplanのattestationを流用せず、work固有のprovenance、権利、同意、安全性、公開証拠を確認します。
- `metadata.yaml`、`index.yaml`、`lineage.json`、README、result fixtureへ、workspaceのpath・内容・設定値・credential・run state・絶対pathを転記しません。
- 公開READMEとcatalogは紹介と公開recordへのリンクだけを持ち、workspace内へのリンクやmedia pathを持ちません。

公開前後に実行する検査:

```sh
python3 tools/catalog_sync.py --check
python3 tools/validate.py --check
python3 -m unittest discover -s tests -v
git diff --check
```

## BLOCK時の非破壊復旧

validatorが`LOCAL_WORKSPACE_*`または`PUBLIC_LOCAL_WORKSPACE_*`を返した場合、対象の値や内容を出力・公開せず、まずfindingの種類だけを記録します。

1. `LOCAL_WORKSPACE_TRACKED`なら、対象内容を確認して保全し、通常のレビューで追跡解除を判断します。validatorは`git rm`、削除、history rewriteを実行しません。
2. `LOCAL_WORKSPACE_IGNORE`なら、root-anchoredの`/.agentic-art/`規則と実効ignore結果を確認します。既存データは移動・削除しません。
3. `LOCAL_WORKSPACE_SYMLINK`またはlayout errorなら、リンク先を読まず、利用者が安全な通常file/directoryへ戻してから再検証します。
4. `PUBLIC_LOCAL_WORKSPACE_REFERENCE`なら、公開record・catalog・lineageから私的pathを除去し、公開allowlistの内容だけを明示的に再作成します。workspaceの本文を公開recordへコピーしません。

事故時も`.agentic-art/`の内容、remote、Git設定、既存の公開recordは自動変更されません。検査結果が再現可能になった後、通常のbranch・commit・Draft PR・人間レビューの手順へ戻ります。

## Gitのないexport tree

`.git`がない配布・export treeでも、layout、固定path、`.gitignore`、公開参照の静的検査は実行されます。この場合、Gitのignore実効性とtracked file件数は`NOT_APPLICABLE`であり、PASSと偽装されません。Git checkoutへ戻してから、Git境界の3コマンドを実行してください。
