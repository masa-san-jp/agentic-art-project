# Agentic Art Project

<img width="1920" height="1076" alt="image" src="https://github.com/user-attachments/assets/f811d9af-5fb9-4710-9f50-650c7da3e3df" />

Agentic Artは、かつて精霊やミューズが芸術塚たちにインスピレーションを与えたように、AIが作家にインスピレーションを与えるための仕組みです。

## コンセプト

### 根底にある問い

古代から中世において、芸術家は、精霊やミューズなど霊的な存在からインスピレーション（霊感）を受け取って絵画や彫刻を制作する媒介者と考えられていました。
ルネサンス以降、人間中心主義的思想が広まり、ラファエロやミケランジェロは「神に等しい才能」を持つ芸術家と呼ばれました。

啓蒙主義時代を経て、インスピレーションが、「才能あるものの直感的なひらめき」として捉えられるようになり、かつて守護霊や精霊を意味していたラテン語の「ジーニアス」は、才能ある人間を表す言葉に変容していきました。
以後、心理学や脳科学の立場からは、インスピレーションは人間の内的なプロセスであるという考え方が主流となっています。

そして現代、生成AIが人間を超えるような推論ができるようになりました。芸術におけるインスピレーションの中心は、生成AIに移りうるのでしょうか？

## Agentic Art　とは

Agentic Artは、この問いに対する態度として、芸術の契機を「AIが運び、人間が受け取って具象化するもの」と捉え、その過程を支える制作プランと系譜を残します。
作り手が自分の創造性を手放し、生成AIの創造性に身を委ねることで、この問いを実作を通じて検証し続けます。

芸術創作のための調査、内省、解釈、計画などプロセスごとにエージェントハーネスを設計し、エージェントが自律的に順次実行することで芸術創作のためのプランが出力されます。
このリポジトリ、`Agentic Art Project` は、エージェントハーネスに従ってAIが考案した制作プランと、そこから生まれた作品・制作記録の公開カタログです。

エージェントハーネスであるリポジトリ群のオーケストレーションは、 [`agentic-art-orchestration`](https://github.com/masa-san-jp/agentic-art-orchestration) が担って居ます。

## このリポジトリの地図

- Agentic Artによる制作プラン：[plans/](https://github.com/masa-san-jp/agentic-art-project/tree/main/plans)
- 実際に制作された作品：[works/](https://github.com/masa-san-jp/agentic-art-project/tree/main/works)
- 制作システムの説明：[`docs/production-system.md`](docs/production-system.md)
- エージェント群の全体像：[`docs/repository-map.md`](docs/repository-map.md)
- 実行・契約の正本：[`agentic-art-orchestration`](https://github.com/masa-san-jp/agentic-art-orchestration)

## エージェントハーネス群の全体像

各リポジトリは別々の知識や成果を所有し、`agentic-art-orchestration` がそれらをオーケストレーションします。

```text
self-model-notes ─┐
art-history-notes ├─ 入力signal ─┐
marketing-trends-notes ┘        │
                                 ▼
viewer-response-notes ─ feedback → agentic-art-orchestration
                                      │ 制御・pin・検証
                                      ▼
                              agentic-art-research
                                      │ research handoff
                                      ▼
                              agentic-art-production
                                      │ 検証済みcanonical plan / result
                                      ▼
                              agentic-art-project
                                  公開カタログ
```

<!-- agentic-art:repositories:start -->
| リポジトリ | 役割 | このプロジェクトとの関係 |
|---|---|---|
| [agentic-art-orchestration](https://github.com/masa-san-jp/agentic-art-orchestration) | オーケストレーション親・制御面 | 入力、研究、制作をつなぎ、公開可能な制作プランをこのリポジトリへ投影する |
| [agentic-art-project](https://github.com/masa-san-jp/agentic-art-project) | 公開成果物カタログ | 公開projectionはexport-onlyで収録し、正規履歴のcatalog-reference/v1を独立したread-only能力として提供する |
| [agentic-art-research](https://github.com/masa-san-jp/agentic-art-research) | 制作リサーチ実行・成果物 | オーケストレーションから参照される下流リポジトリで、内部資料はこのカタログへ複製しない |
| [agentic-art-production](https://github.com/masa-san-jp/agentic-art-production) | 制作実行・結果記録 | 制作引き渡しを受けて制作物と記録を扱い、作品公開は別の人間ゲートを通る |
| [self-model-notes](https://github.com/masa-san-jp/self-model-notes) | 自己モデル入力ナレッジベース | オーケストレーションが参照する上流入力であり、このカタログの収録対象ではない |
| [art-history-notes](https://github.com/masa-san-jp/art-history-notes) | 美術史入力ナレッジベース | オーケストレーションが参照する上流入力であり、このカタログの収録対象ではない |
| [marketing-trends-notes](https://github.com/masa-san-jp/marketing-trends-notes) | 市場変化入力ナレッジベース | オーケストレーションが参照する上流入力であり、このカタログの収録対象ではない |
| [viewer-response-notes](https://github.com/masa-san-jp/viewer-response-notes) | 鑑賞者反応・フィードバック | 作品への反応を集計し、将来の制作要件を評価する上流フィードバックである |
<!-- agentic-art:repositories:end -->

各リポジトリの詳しい契約、実行手順、現在の状態は、それぞれのREADMEと [`docs/repositories.yaml`](docs/repositories.yaml) を参照してください。このREADMEでは、各リポジトリの内部仕様を複製しません。

8リポジトリの責務とデータの流れを一枚で確認したい場合は、[リポジトリ関係図](docs/repository-map.md)を先に読んでください。`docs/repositories.yaml`は機械可読な定義、`agentic-art-orchestration/docs/repository-map.md`はシステム全体の正本案内です。

## 公開カタログ

制作プランは、同じ入力から分岐した制作上の仮説と、その仮説を検証するための条件を読むための記録です。完成作品や展示実績を意味しません。

<!-- agentic-art:catalog:start -->
- [必要な後退 — 単位を視認限界の下へ置いた一枚の大判プリント](plans/P0004-necessary-retreat/README.md)
<!-- agentic-art:catalog:end -->

作品は [works/README.md](works/README.md) から一覧できます。プランと作品の関係は、各レコードのREADMEとmetadataで確認できます。

## 公開しないもの

このリポジトリに収録するのは、公開を確認できた資料だけです。次のものは収録しません。

- エージェントの内部ログ、会話、プロンプト、handoff、実行状態
- 認証情報、秘密、個人情報、ローカル環境固有のパス
- 公開許諾のない第三者の素材
- 公開可否や権利状態が確認できない資料

制作プランの正本性、権利確認、系譜、移行待ちレコードの扱いは、[制作システム](docs/production-system.md) と [カタログ系譜](docs/catalog-lineage.md) にまとめています。

## 自動投影とリモート公開の違い

このカタログへの「公開」は、二つの段階を含みます。

1. `agentic-art-orchestration`が、Productionで検証されたcanonical planをこのProjectのcheckoutへ投影し、Project側のvalidatorで受け入れを確認する。
2. その変更をGitへcommitし、GitHubへpush・PR・mergeして、リモートのカタログとして公開する。

自動ハーネスが担当するのは第1段階の公開投影です。第2段階のGit操作、merge、release、外部共有、権利・同意範囲の変更は、投影が成功しただけでは実行されません。したがって、ローカルcheckoutに存在するrecordは、リモートの`main`へ公開済みであることを意味しません。

## 技術者・運用者向け

この節は、公開カタログを更新する人のための入口です。初めて読む場合は、上のコンセプト、全体像、`plans/`、`works/`だけを読めば構いません。

個別レコードでは、次のファイルを使い分けます。

- `README.md`：人が読むための紹介
- `plan.md`：公開を承認された制作プラン本文
- `record.md`：作品の制作記録
- `metadata.yaml`：ID、状態、権利、関連するプランや作品
- `media/`：公開可能な画像、映像、音声など

更新時は、一覧の正本を編集してからREADMEの管理ブロックを同期します。

```bash
python3 tools/catalog_sync.py --write
python3 tools/catalog_sync.py --check
python3 tools/validate.py --check
python3 -m unittest discover -s tests -v
git diff --check
```

ローカルの非公開作業領域を使う場合は [`docs/local-workspace.md`](docs/local-workspace.md) を先に読みます。`.agentic-art/` の内容や内部出力を公開レコードへコピーしてはいけません。

公開projectionの詳細、正規 `plan.md` の受入条件、系譜の確認方法は、次の文書を正本とします。

- [`docs/production-system.md`](docs/production-system.md)
- [`docs/catalog-lineage.md`](docs/catalog-lineage.md)
- [`docs/local-workspace.md`](docs/local-workspace.md)
- [`public-project.yaml`](public-project.yaml)
- [`plans/index.yaml`](plans/index.yaml)

## ライセンス

公開範囲と権利状態を確認した資料だけを収録し、ライセンスは [`LICENSE`](LICENSE) に従います。

## ローカル納品の確認

Projectへのローカル納品確認には `python3 tools/local_delivery.py --root <catalog> --expected <external-json>` を使用します。本文・画像・帰属をownerが検証し、commit/push済みとは区別したreceiptを返します。[入力と再検証手順](docs/catalog-lineage.md#local-delivery-receipt-issue-18)。
