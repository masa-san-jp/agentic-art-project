# 制作プラン

Agentic Art の制作プラン一覧です。

制作プランは一件につき一つのディレクトリで管理します。各プランのディレクトリ名は `P0001-short-slug` の形式とし、詳細は個別の `README.md` と `plan.md` に記載します。

現時点では、公開可否と正本の確認状態を `index.yaml` の `plan_state` に明示します。`canonical-plan` は Production が生成した `production-plan.md` の無変換正本、`blocked-missing-canonical` は旧要約を保持したまま制作可能一覧から隔離したレコードです。

全件の機械可読一覧は [`index.yaml`](index.yaml) を参照してください。`index.yaml` が制作プランのSSOTであり、下の一覧とルートREADMEの制作プラン一覧は `python3 tools/catalog_sync.py --write` で同期します。

## 取り込み方針

参照元にある旧版、別形式の同一計画、`.gdoc`の参照ファイル、研究・handoff・実行ツリーは、そのまま複製していません。`plan.md` は要約・翻訳・再構成せず、Production が生成した正本を無変換で収録します。正本を確認できない旧要約は `blocked-missing-canonical` として残し、制作可能なプランとして扱いません。

100件規模のプランを生み出す仕組みの説明は、個別プランではなく [`docs/production-system.md`](../docs/production-system.md) に収録しています。実物作品、原寸データ、大容量メディア、制作手順は、作品の公開可否と権利状態を確認したうえで `works/` に別途収録します。

<!-- agentic-art:catalog:start -->
- [選択の持ち主 — 翻訳のあとに残るもの](P0001-owner-of-choice/README.md)
- [移動する隙間による近接場の交換](P0002-moving-gap/README.md)
- [関わり方を選び直す距離 — 余白の呼吸](P0003-yohaku-breath/README.md)
- [必要な後退 — 単位を視認限界の下へ置いた一枚の大判プリント](P0004-necessary-retreat/README.md)
- [近いのに届かない — 枠を見る側に置く](P0005-close-but-cannot-reach/README.md)
- [距離が選ぶ境界 — 近づいても触れない休止の場](P0006-distance-selects-boundary/README.md)
- [近接不在 — Near, Not Received](P0007-near-not-received/README.md)
<!-- agentic-art:catalog:end -->

管理対象ブロックを直接編集した場合は、`python3 tools/catalog_sync.py --check` が失敗します。オーケストレーションの自動plan投影は、新しいプランのレコード、`plans/index.yaml`、この一覧、およびルートREADMEに管理対象markerがある場合のルート一覧を同じローカルtransactionで更新します。
