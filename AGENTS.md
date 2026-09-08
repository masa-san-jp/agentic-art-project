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
7. AAK-13では[カタログ系譜と参照](docs/catalog-lineage.md)、`lineage.json`、生成`plans/lineage-index.json`を読む。

AAK-13の正本は[仕様](https://github.com/masa-san-jp/agentic-art-orchestration/blob/b0e7c7f8d0a1f756fa708deef4fb380a62e45e0d/docs/20260905-agentic-art-autonomy-and-knowledge-cycle-specification.md#aak-13)と[実装計画](https://github.com/masa-san-jp/agentic-art-orchestration/blob/b0e7c7f8d0a1f756fa708deef4fb380a62e45e0d/docs/20260905-agentic-art-autonomy-and-knowledge-cycle-implementation-plan.md#aak-13)。公開projectionのexport-only境界を維持し、独立したread-onlyの`catalog-reference/v1`を追加する限定変更である。

## Canonical plan invariant

- 正規の`plans/*/plan.md`は、`agentic-art-production`の`03_plan/production-plan.md`を`agentic-art-orchestration`の`AUTOMATIC_PLAN`経路がbyte-for-byteで投影したものだけである。
- エージェントは`plan.md`を執筆、要約、翻訳、再構成、抜粋しない。紹介文や要約は`README.md`にだけ置く。
- 公開安全検査に失敗した正本を編集して通さない。公開をblockedにし、親Issueへ解除条件を返す。
- Issue #6の更新契約に従い、正本不明の旧要約は現行公開カタログへ複製せず、P ID/source候補/理由/解除条件をmetadata-onlyのplans/migration.yamlへ予約する。予約IDを再利用せず、正本回収時だけ同じP IDへ復帰させる。
- 正規planは`canonical-plan-projection/v2`、`AUTOMATIC_PLAN`、`body_transform: none`、stable identity/revision、Production repository/commit、run ID、body/attestation SHA-256とproduction-public-plan-attestation/v1を持つ。Productionの見出し・意味schemaは複製しない。
- `lineage.json`は本文と別の帰属・系譜metadata。既存作者/originをactive creatorへ置換しない。不明な帰属はunknownのままにし、Git commit作者から作品作者を推定しない。
- 新規recordのannotationは明示instance-profileのinstance/creatorを使い、履歴にあるP/W IDをnew扱いにしない。revision更新は以前のcommitと参照を保持する。生成indexは手編集しない。
- `catalog_lineage.py export`は正規recordをcleanなGit snapshotから読み、参照だけを返す。BLOCKED/unknownを成功扱いせず、`code_commit`/`code_dirty`と`knowledge_commit`を区別する。
- planはPLANNEDであり、制作/展示の実績ではない。workの段階には別のreview済み公開証拠を要求し、simulatedをobservedと数えない。

## Work protocol

1. Issueを読み、対象pathと現在のGit状態を確認する。
2. index、metadata、本文、README、validatorへの影響を同時に計画する。
3. 最小差分で編集し、生成catalogは`python3 tools/catalog_sync.py --write`で同期する。
4. `python3 tools/validate.py --check`、`python3 -m unittest discover -s tests -v`、`git diff --check`を実行する。
5. repoごとのcommitとDraft PRを作り、Issueへ検証結果を記録する。

## Safety and authority

- このrepoはexport-onlyであり、入力knowledge、親run state、内部log、会話、prompt、handoff、credential、PRIVATE_RAW、RESTRICTEDを所有しない。
- read-only catalog-referenceは上記projectionとは別能力であり、親のknowledge write dispatchを許可するものではない。任意の出力repoは明示rootまたは外部output-destinations/v1から解決する。
- `public-project.yaml`はlayoutとcanonical plan受理契約、`plans/index.yaml`はplan catalogの正本である。
- `.agentic-art/`はroot直下の非追跡ローカル作業領域である。設定、run state、内部出力、一時stagingをここへ置き、公開record・catalog・lineageへ参照を持ち込まない。fresh cloneで不在でも正常であり、validatorは必要な場合だけ利用者が作成した領域を読み取り検査する。
- workの公開、GitHubへのpush/PR、既定branchへのmerge、release、visibility変更は別の人間gateに従う。
- branch作成、commit、Draft PRはIssueで明示されたtaskに限る。merge、release、削除、force pushを自動実行しない。

## Completion report

- Issue、対象record、canonical/blocked分類
- 本文SHA-256とsource repository@commit
- validator、unit tests、diff check
- commit、PR、未解決、次の一操作
- 機微情報と内部artifactを保存していないこと

## Repo-local workspace

- `.agentic-art/`は公開成果物ではなく、root-anchored `.gitignore`で除外されたローカル専用領域です。`config.yaml`、`state/`、`internal/`、`staging/`だけを固定用途として使用します。
- fresh cloneでこのディレクトリが存在しない状態は正常です。必要になった利用者だけが作成し、既存の内部資料を自動移動・コピーしません。
- 公開昇格は`staging/`からのrecursive copyではありません。Production正本、attestation、権利・同意・安全性、provenanceを受信validatorで確認してから、公開allowlistのrecordだけを通常のレビュー付きworkflowで追加します。
- BLOCK時はvalidatorのfindingを記録し、`.agentic-art/`の内容を削除・移動せず、原因を解消して再検証します。tracked fileが見つかっても`git rm`やhistory rewriteは自動実行しません。
- 利用手順と非破壊復旧は[`docs/local-workspace.md`](docs/local-workspace.md)を正本とします。
