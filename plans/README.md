# 制作プラン

Agentic Art の制作プラン一覧です。

制作プランは一件につき一つのディレクトリで管理します。各プランのディレクトリ名は `P0001-short-slug` の形式とし、紹介は`README.md`、Production正本の無変換投影は`plan.md`に置きます。

`ready-for-publication`はProduction正本、公開証明、無変換投影の来歴を確認済みです。正本を確認できない旧レコードは一覧や個別ディレクトリに残さず、IDと復旧条件だけを[`migration.yaml`](migration.yaml)に記録します。旧本文はGit履歴からのみ参照できます。

全件の機械可読一覧は [`index.yaml`](index.yaml) を参照してください。`index.yaml` が制作プランのSSOTであり、下の一覧とルートREADMEの制作プラン一覧は `python3 tools/catalog_sync.py --write` で同期します。

## 取り込み方針

正規`plan.md`は`agentic-art-production`の`03_plan/production-plan.md`を`agentic-art-orchestration`の`AUTOMATIC_PLAN`経路がbyte-for-byteで投影します。要約、翻訳、再構成、抜粋はせず、紹介文だけを`README.md`に置きます。内部パス、個人由来の原資料、非公開URL、会話、認証情報が検出された場合は、正本を編集して公開せずblockedにします。

100件規模のプランを生み出す仕組みの説明は、個別プランではなく [`docs/production-system.md`](../docs/production-system.md) に収録しています。実物作品、原寸データ、大容量メディア、制作手順は、作品の公開可否と権利状態を確認したうえで `works/` に別途収録します。

<!-- agentic-art:catalog:start -->
- [必要な後退 — 単位を視認限界の下へ置いた一枚の大判プリント](P0004-necessary-retreat/README.md)
- [aak07-agent-20260910-p4](P0008-aak07-agent-20260910-p4/README.md)
- [選択の所有 — Owner of Choice（旧P0001復旧版）](P0009-legacy-owner-of-choice/README.md)
- [移動する空白 — Moving Gap（旧P0002復旧版）](P0010-legacy-moving-gap/README.md)
- [余白の呼吸 — Yohaku Breath（旧P0003復旧版）](P0011-legacy-yohaku-breath/README.md)
<!-- agentic-art:catalog:end -->

管理対象ブロックを直接編集した場合は、`python3 tools/catalog_sync.py --check` が失敗します。オーケストレーションの自動plan投影は、新しいプランのレコード、`plans/index.yaml`、この一覧、およびルートREADMEに管理対象markerがある場合のルート一覧を同じローカルtransactionで更新します。
