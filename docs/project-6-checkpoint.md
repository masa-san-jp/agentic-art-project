# Project #6 canonical receiver and migration checkpoint

Issue #6の受信契約と実データ移行を実装した。公開カタログは、Productionが生成した完全なMarkdown本文、公開証明、列挙済みasset、stable source identity/revision、Orchestration projection/v2来歴が一致するレコードだけを受理する。見出し名や章数は本リポジトリの契約にしない。

## 適用した移行

- P0004「必要な後退」は、保存されていたHO006 source bundleから現行Productionで再materialize・再renderした。
- plan.mdはProductionの03_plan/production-plan.mdと同一バイトで、SHA-256は`b6d103079c84ab1b6e9f6a12fe00346ca1f17300a38bda2ee201a4f792ffdc5f`。
- Production commit `69567e88131e3f033d010791fb5849e1b2ebff8d`のvalidatorと`production-public-plan-attestation/v1`を通し、本文、aggregate、coverage、公開審査、2点のSVG assetをhashで固定した。
- P0001・P0002・P0003・P0005・P0006・P0007は、検証可能な現行Production正本がないため、公開一覧と現在のrecord directoryから外した。ID、source候補、阻害理由、復旧条件は`plans/migration.yaml`に保持する。旧本文はGit履歴から復元できる。

## 受入結果

- `python3 tools/validate.py --check`: PASS
- `python3 tools/catalog_sync.py --check`: PASS
- `python3 -m unittest discover -s tests -v`: 20 tests PASS
- Production → Orchestration → Projectの実コード境界テスト: PASS
- summary、見出し模倣、1-byte改変、偽attestation、欠落provenance、asset改変、rights未確認、symlinkはfail closedする。

計画のcanonical/public状態は、物理制作、購入、契約、外部連絡、展示、完成作品公開の承認とは別である。P0004の本文内に記録されたblocking gapとapproval boundaryはそのまま残しており、公開のために削除・要約していない。

内部handoff、研究台帳、会話、credential、PRIVATE_RAW、RESTRICTED、ローカル絶対pathは公開レコードへ追加していない。元のOutput-資料はread-onlyで参照し、変更していない。
