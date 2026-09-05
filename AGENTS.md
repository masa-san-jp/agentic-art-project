# Repository instructions

## Mission

`agentic-art-orchestration`から受け取った公開可能な成果を、人が読め、エージェントが誤解なく再利用できる公開カタログとして保持する。

## Read order

1. この`AGENTS.md`
2. `README.md`
3. `public-project.yaml`
4. `plans/index.yaml`または`works/index.yaml`
5. 対象recordの`metadata.yaml`、`README.md`、本文
6. Issue SSOTと最も近いtest

## Canonical plan invariant

- 正規の`plans/*/plan.md`は、`agentic-art-production`の`03_plan/production-plan.md`を`agentic-art-orchestration`の`AUTOMATIC_PLAN`経路がbyte-for-byteで投影したものだけである。
- エージェントは`plan.md`を執筆、要約、翻訳、再構成、抜粋しない。紹介文や要約は`README.md`にだけ置く。
- 公開安全検査に失敗した正本を編集して通さない。公開をblockedにし、親Issueへ解除条件を返す。
- Issue #6の更新契約に従い、正本不明の旧要約は現行公開カタログへ複製せず、P ID/source候補/理由/解除条件をmetadata-onlyのplans/migration.yamlへ予約する。実レコード移行は別のhuman gateであり、本実装中は適用せず阻害理由を保存する。
- 正規planは`canonical-plan-projection/v2`、`AUTOMATIC_PLAN`、`body_transform: none`、stable identity/revision、Production repository/commit、run ID、body/attestation SHA-256とproduction-public-plan-attestation/v1を持つ。Productionの見出し・意味schemaは複製しない。

## Work protocol

1. Issueを読み、対象pathと現在のGit状態を確認する。
2. index、metadata、本文、README、validatorへの影響を同時に計画する。
3. 最小差分で編集し、生成catalogは`python3 tools/catalog_sync.py --write`で同期する。
4. `python3 tools/validate.py --check`、`python3 -m unittest discover -s tests -v`、`git diff --check`を実行する。
5. repoごとのcommitとDraft PRを作り、Issueへ検証結果を記録する。

## Safety and authority

- このrepoはexport-onlyであり、入力knowledge、親run state、内部log、会話、prompt、handoff、credential、PRIVATE_RAW、RESTRICTEDを所有しない。
- `public-project.yaml`はlayoutとcanonical plan受理契約、`plans/index.yaml`はplan catalogの正本である。
- workの公開、GitHubへのpush/PR、既定branchへのmerge、release、visibility変更は別の人間gateに従う。
- branch作成、commit、Draft PRはIssueで明示されたtaskに限る。merge、release、削除、force pushを自動実行しない。

## Completion report

- Issue、対象record、canonical/blocked分類
- 本文SHA-256とsource repository@commit
- validator、unit tests、diff check
- commit、PR、未解決、次の一操作
- 機微情報と内部artifactを保存していないこと
