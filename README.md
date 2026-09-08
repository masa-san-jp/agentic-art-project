# Agentic Art Project

このリポジトリは、`agentic-art-orchestration` の出力から、Agentic Art プロジェクトの公開資料だけを収録するためのリポジトリです。

ルートの `README.md` は、このプロジェクトを初めて訪れた人のための展示入口です。プロジェクトのコンセプトと代表的な作品を紹介し、すべての制作プランと作品記録へ案内します。

## Agentic Art全体との関係と利用方法

8リポジトリ全体の人間向け案内は、親repoの[repository map](https://github.com/masa-san-jp/agentic-art-orchestration/blob/main/docs/repository-map.md)を正本とします。このREADMEにも、役割と利用入口を次の通り表示します。

```text
self-model-notes ─┐
art-history-notes ├─ normalized research signal ─┐
marketing-trends ┘                               │
                                                 ▼
viewer-response-notes ─ feedback ─→ agentic-art-orchestration
                                                 │
                                                 ▼
                                       agentic-art-research
                                                 │ production-handoff
                                                 ▼
                                       agentic-art-production
                                                 │ canonical plan
                                                 ▼
                                       agentic-art-project
                                           公開カタログ
```

| リポジトリ | 役割 |
|---|---|
| [agentic-art-orchestration](https://github.com/masa-san-jp/agentic-art-orchestration) | 全体のcontrol plane。workspace、pin、retrieval、実行、再開、検証 |
| [self-model-notes](https://github.com/masa-san-jp/self-model-notes) | 本人の明示的・同意済みの自己モデル |
| [art-history-notes](https://github.com/masa-san-jp/art-history-notes) | 美術史上の作品、技法、関係、根拠 |
| [marketing-trends-notes](https://github.com/masa-san-jp/marketing-trends-notes) | 社会・市場の変化と鮮度付きの根拠 |
| [agentic-art-research](https://github.com/masa-san-jp/agentic-art-research) | 入力知識を使った調査、仮説、要件、判断 |
| [agentic-art-production](https://github.com/masa-san-jp/agentic-art-production) | handoffを受けた制作プラン、試作、制作結果 |
| [viewer-response-notes](https://github.com/masa-san-jp/viewer-response-notes) | 鑑賞者反応の集計と保守的な評価 |
| [agentic-art-project](https://github.com/masa-san-jp/agentic-art-project) | 検証済みの公開プラン、作品、制作記録のカタログ |

### 利用者の入口

- 制作を始める: [OrchestrationのREADME](https://github.com/masa-san-jp/agentic-art-orchestration#利用者向けの最短ルート)と[agent-runtime-guide](https://github.com/masa-san-jp/agentic-art-orchestration/blob/main/docs/agent-runtime-guide.md)から始める。個別repoを順番に手操作しない。
- 知識を更新する: 更新対象repoのREADME、Issue、schema、validatorを正本として使い、親へ本文をコピーしない。
- Research/Productionを確認する: [agentic-art-research](https://github.com/masa-san-jp/agentic-art-research)と[agentic-art-production](https://github.com/masa-san-jp/agentic-art-production)の各入口を読む。
- 公開プランや作品を見る: [agentic-art-projectのplans/とworks/](https://github.com/masa-san-jp/agentic-art-project)を開く。
- 鑑賞者反応を戻す: [viewer-response-notes](https://github.com/masa-san-jp/viewer-response-notes)で集計し、次回Researchで再検証する。

各repoは独立した正本を持ち、内部log、会話、prompt、credential、PRIVATE_RAW、RESTRICTEDを兄弟repoへ渡しません。

### このrepoの使い方

このrepoは公開成果物を読むcatalogです。検証済みのplan、作品、制作記録を閲覧し、作者・origin・revisionの系譜を保持します。入力knowledge、run state、handoff、内部logのwrite ownerではなく、公開recordはOrchestrationのexport-only経路から受け取ります。


## コンセプト

芸術の契機を「精霊や風が運び、人間が受け取って具象化する」と捉え、その過程を支える制作プランと系譜を残します。

Agentic Art は、人間が一つひとつの作品を直接設計するのではなく、エージェント群が与えられたテーマや条件をもとに、複数の制作プランを自律的に考案し、そのプランから制作物と制作記録を生み出していく試みです。

ここでいう自律性は、単一のエージェントが孤立して作品を生成することを意味しません。制作に必要な役割や判断をエージェント群に分担させ、オーケストレーションの仕組みによって、プランの生成、展開、記録を一連の制作プロセスとして実行することを意味します。

一つの入力から一つの答えを得るのではなく、複数の制作プランと、そのプランから生まれる複数の作品を蓄積・比較できることが、このプロジェクトの重要な特徴です。

## 制作システム

制作プロセス全体は、概念的には次のように進みます。

```text
テーマ・目的・条件
        │
        ▼
agentic-art-orchestration
        │
        ├── エージェント群が制作プランを自律的に生成
        ├── 複数のプランを個別のレコードとして整理
        ├── プランに基づく制作物と制作記録を生成
        └── 生成結果を Agentic-Art-Output に出力
                │
                ▼
        公開対象を確認・整理
                │
                ▼
        agentic-art-project
```

`agentic-art-orchestration` は、エージェントが制作プランを生み出し、制作物と記録を出力するための仕組みを管理します。このリポジトリは、その出力のうち公開可能な制作プラン、作品、制作記録を、他の人が読めるカタログとして整理します。

正規の`plan.md`はProductionの完全な無変換bytesとattestation/v1、projection/v2の来歴を要求します。正本不明の旧要約は現行カタログへ残さず、metadata-onlyの`plans/migration.yaml`でIDを予約します。2026-09-06の移行ではP0004を現行Productionから再生成した完全な正本へ置換し、正本を証明できないP0001・P0002・P0003・P0005・P0006・P0007を移行待ちへ隔離しました。詳細は[実装checkpoint](docs/project-6-checkpoint.md)を参照してください。

このリポジトリはオーケストレーションの実行環境や内部ログを収録する場所ではありません。自律的な制作の結果を、個別の制作プランと作品記録として追跡可能な形で公開する場所です。

## ローカル制作作業領域

cloneしたcheckout内で制作の中間出力や非公開stateを扱う場合は、root直下の`.agentic-art/`を利用できます。この領域はGitから除外され、fresh cloneに存在しなくても正常です。公開対象へ昇格できるのは、Production正本・attestation・権利と同意の検証を通過した成果だけです。

利用者向けの作成、検証、公開前check、BLOCK時の非破壊復旧は[`docs/local-workspace.md`](docs/local-workspace.md)にまとめています。内部出力を公開recordへrecursive copyしたり、設定値・run state・絶対pathをmetadataやREADMEへ転記したりしないでください。

## 作者・系譜と履歴の再参照

各recordの`lineage.json`で、origin、creator、改訂、派生元と元planを本文から分離して管理します。
clone/forkは元作者の作品を引き継ぎます。新しい利用者の自作へ読み替えません。P/W IDは保存し、
別catalogに同じIDがある場合もoriginとIDを組にして参照します。既存P0004は正本を確認済みですが、
作者とoriginの記録はまだないためunknownです。能動的な利用者やGit commit作者で補完しません。

公開projectionは出力専用のまま、`catalog-reference/v1`が比較用の独立した読み取り能力を提供します。
正本・権利・hash・帰属の検査を通ったrecordだけを、固定Git commitと本文locatorで返します。
exportは元catalogを書き換えません。計画はPLANNED、作品の実績は別の公開証拠に基づく段階として示し、
simulatedとobservedを分けます。詳しい入口と訂正手順は[カタログ系譜と参照](docs/catalog-lineage.md)を参照してください。

```sh
python3 tools/catalog_lineage.py migration --root <absolute-catalog-root>
python3 tools/catalog_lineage.py export --root <absolute-catalog-root> --repository <owner/catalog> --snapshot <knowledge-commit>
```

外部`output-destinations/v1`を使う場合は`--root`の代わりに`--destinations-file <external-profile.yaml>`を指定します。
未記録の帰属は`UNKNOWN_ATTRIBUTION`としてBLOCKEDに残ります。現在のP0004がこの状態であることは、
planの正本検証に通っていることとは別です。生成[系譜index](plans/lineage-index.json)を手編集せず、
`python3 tools/catalog_sync.py --write`で同期します。

公開対象の選定と、100件規模の制作プランを生み出す仕組みについては [`docs/production-system.md`](docs/production-system.md) を参照してください。リポジトリ群のURLと関係性は [`docs/repositories.yaml`](docs/repositories.yaml) を正本とします。

## 関連リポジトリと関係性

`agentic-art-orchestration` を親の制御面とし、入力ナレッジ、リサーチ、制作実行を経て、このリポジトリへ公開用レコードを `export-only` で投影します。このリポジトリは入力ナレッジや実行状態を所有せず、オーケストレーション内部のログ・会話・handoff・認証情報を受け取りません。

```text
入力ナレッジ / 鑑賞者反応
          │
          ▼
agentic-art-orchestration（親・制御面）
          │
          ├── agentic-art-research（リサーチ）
          ├── agentic-art-production（制作実行・結果記録）
          └── agentic-art-project（公開カタログへexport-only投影）
```

関係性の表は [`docs/repositories.yaml`](docs/repositories.yaml) から生成されています。追加・変更時は同ファイルを更新し、`python3 tools/catalog_sync.py --write` を実行してください。

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

制作プロセスやエージェントの仕組みを確認したい場合は `agentic-art-orchestration` を参照してください。実際に生成された公開作品や制作記録を閲覧したい場合は、このリポジトリの `plans/` と `works/` を参照してください。

## 代表作品

ここには、全作品のうち代表的な作品を画像付きで紹介します。全件を掲載する場所ではありません。全作品は [`works/README.md`](works/README.md) から参照できます。

<!--
例:

### [W0001 — 作品タイトル](works/W0001-title/README.md)

![作品タイトル](works/W0001-title/media/cover.png)

作品の短い紹介文。
-->

## 公開された制作プラン

制作プランは、同じ入力から分岐した制作上の仮説と、その仮説を検証するための条件を読むための記録です。完成作品や受入試験の通過を意味しません。以下の一覧は [`plans/index.yaml`](plans/index.yaml) から生成されます。

<!-- agentic-art:catalog:start -->
- [必要な後退 — 単位を視認限界の下へ置いた一枚の大判プリント](plans/P0004-necessary-retreat/README.md)
<!-- agentic-art:catalog:end -->

## リポジトリの構造

```text
.
├── README.md                 # コンセプトと代表作品の紹介
├── public-project.yaml       # 公開projectionのレイアウト契約
├── LICENSE                   # 公開資料のライセンス
├── docs/                     # プロジェクト全体に関する公開資料
│   ├── production-system.md  # 自律的な制作システムの説明
│   └── repositories.yaml      # 関連リポジトリのURL・役割・関係性
├── tools/                    # カタログ同期・検証ツール
│   └── catalog_sync.py       # index.yamlからREADMEの管理ブロックを同期
├── .github/workflows/        # リポジトリ上の自動検証
│   └── catalog.yml           # READMEとindexの不一致を検出
├── plans/                    # 制作プランの集合
│   ├── README.md             # 全制作プランの一覧
│   ├── index.yaml            # 制作プランの機械可読インデックス
│   └── P0001-title/          # 個別の制作プラン
│       ├── README.md         # 個別プランの紹介
│       ├── plan.md           # 制作プラン本文
│       ├── metadata.yaml     # 識別子・状態・関連作品など
│       └── media/            # プラン固有の図・参考画像
├── works/                    # 作品と制作記録の集合
│   ├── README.md             # 全作品の一覧
│   ├── index.yaml            # 作品の機械可読インデックス
│   └── W0001-title/          # 個別の作品
│       ├── README.md         # 個別作品の紹介
│       ├── record.md         # 制作記録
│       ├── metadata.yaml     # 識別子・状態・元プランなど
│       ├── process/           # 公開可能な制作スクリプト・手順
│       │   ├── README.md      # 再現手順
│       │   └── *.py           # 公開可能な制作スクリプト
│       └── media/            # 作品画像・映像・音声・制作過程
└── shared/                   # 特定の作品に属さない共通素材
    ├── branding/             # ロゴ・共通キービジュアル
    └── diagrams/             # プロジェクト全体の説明図
```

`public-project.yaml` は公開projectionの対象レイアウトを宣言します。`docs/`、`shared/` は必要な資料が存在する場合だけ作成します。作品に属する画像やその他のメディアを、ルートの `shared/` に置いてはいけません。

## 制作プランと作品記録

### 制作プラン

制作プランは `plans/` の下に一件ずつディレクトリを作成します。制作プランが100件以上になっても扱えるよう、個別ファイルを一つのディレクトリに平置きしません。

```text
plans/
├── README.md
├── index.yaml
├── P0001-title/
├── P0002-title/
└── ...
```

### 作品

作品とその制作記録は `works/` の下に一件ずつディレクトリを作成します。作品に属する実ファイルは、その作品の `media/` に置きます。

```text
works/W0001-title/
├── README.md
├── record.md
├── metadata.yaml
├── process/
│   ├── generate-artwork.py
│   └── split-artwork.py
└── media/
    ├── cover.png
    ├── artwork.png
    └── process/
```

`README.md`は紹介ページ、`plan.md`はattestationで検証するProduction正本、`metadata.yaml`とindexはstable source identity、revision、body/attestation hashを共有します。公開IDは本文hashから分離します。`plans/migration.yaml`の予約IDも再利用しません。意味的coverageとrendererはProductionだけが所有します。

## 識別子と命名

- 制作プランには `P`、作品には `W` を付けた4桁以上の連番を使用します。例: `P0001`、`W0001`。
- 識別子は一度付与したら再利用しません。削除された項目の番号も再利用しません。
- ディレクトリ名は `識別子-短いslug` とします。slugは小文字のASCII英数字とハイフンだけで構成します。例: `W0001-generative-garden`。
- タイトル変更だけでは識別子を変更しません。
- 追加前に既存のディレクトリと `index.yaml` を確認し、識別子の重複がないことを確認します。

### ファイル名

- 標準ファイル名は大文字・空白・アンダースコアを使わず、小文字のASCII英数字とハイフンで統一します。
- 個別プランでは `README.md`、`plan.md`、`metadata.yaml` を使用します。
- 個別作品では `README.md`、`record.md`、`metadata.yaml`、`media/` を使用します。
- 作品に属する公開可能な制作スクリプトや再現手順は `process/` に置きます。スクリプトを `media/` に置きません。
- 制作手順の本文は `process/README.md` に統一し、作品の意味・仕様・経緯は `record.md` に記載します。
- 一覧は `plans/README.md`、`plans/index.yaml`、`works/README.md`、`works/index.yaml` に固定します。
- 作品のメイン画像は `media/cover.<拡張子>`、作品本体は `media/artwork.<拡張子>` とします。複数ある場合は `artwork-01.<拡張子>` のように連番を付けます。
- 制作過程のファイルは `media/process/`、プラン固有の参考資料は `plans/.../media/` に置きます。
- 拡張子も小文字にします。ファイル名に日付、版数、元ファイル名を追加せず、それらは `metadata.yaml` に記録します。

参照元の内部ID（例: `PL001`、`HO006`、`DL001`）はプロジェクトごとに重複し得るため、公開リポジトリのディレクトリ名には使用しません。必要な場合は `metadata.yaml` の出典情報として保持し、公開レコードにはグローバルに一意な `P0001` または `W0001` を付与します。

## 関連付け

一つの制作プランから複数の作品が生まれることを想定します。制作プランと作品の関係は、本文中の記述だけでなく `metadata.yaml` にも記録します。

```yaml
# plans/P0001-title/metadata.yaml
id: P0001
title: 制作プランのタイトル
status: ready-for-publication
visibility: public
rights_status: cleared
related_works:
  - W0001
  - W0002
```

```yaml
# works/W0001-title/metadata.yaml
id: W0001
title: 作品タイトル
status: published
visibility: public
rights_status: cleared
source_plans:
  - P0001
```

プランと作品の追加・変更時は、個別の `metadata.yaml`、`plans/index.yaml` または `works/index.yaml`、関連する一覧ページを必要に応じて同時に更新します。制作プランについては `plans/index.yaml` がSSOTです。READMEの管理ブロックを手で編集せず、`python3 tools/catalog_sync.py --write` で同期し、コミット前に `python3 tools/catalog_sync.py --check` を実行します。

## 公開範囲

このリポジトリに収録するのは、公開を前提とした資料だけです。次のものは、明示的に公開対象と決められていない限り収録しません。

- エージェントの内部ログ、実行用プロンプト、デバッグ出力
- 制作途中の一時ファイルや重複した中間生成物
- 非公開の個人情報、認証情報、秘密鍵、ローカル環境固有のパス
- 公開許諾のない第三者の画像・文章・音声・データ

公開レコードの `metadata.yaml` には、少なくとも `visibility: public` と `rights_status: cleared` を設定します。公開可否または権利状態が `unknown`、`internal`、`restricted` の資料は、このリポジトリへ収録しません。

`agentic-art-orchestration` の出力を取り込む場合も、公開対象を確認してから、このリポジトリの構造に合わせて整理します。オーケストレーション側の内部ディレクトリ構造を、そのままコピーしません。ただしProduction正本の`production-plan.md`だけは本文を変換せず`plan.md`へコピーします。

## 参照元からの取り込み

参照元の一つのフォルダを、そのまま一つの公開レコードにコピーするとは限りません。次の基準で整理します。

- 正規制作プランは`AUTOMATIC_PLAN`経路がProductionの`03_plan/production-plan.md`をbyte-for-byteで`plans/Pxxxx-slug/plan.md`へ投影します。手作業で本文を作りません。
- 作品と制作物の記録は `works/Wxxxx-slug/record.md` に整理します。
- 作品固有の画像、印刷データ、映像、音声、公開可能な制作スクリプトは、対応する作品の `media/` に整理します。
- 100件のプラン生成方法など、個別作品に属さない仕組みの説明は `docs/production-system.md` に整理します。
- 同じプロジェクトの旧版・別形式の文書はすべて個別レコードにしません。公開する正本を一つ選び、必要な版情報を `metadata.yaml` に記録します。
- `.gdoc` はGoogle Docsへの参照情報であり、公開本文ではありません。`.gdoc`ファイルをそのままコピーせず、公開可能性を確認したうえで本文をMarkdownに変換するか、公開URLを明示します。
- `handoff/`、`research-project/`、`production-plan/08_runtime/` などの内部運用ツリーは、そのまま公開ディレクトリへ移しません。planの紹介は`README.md`、作品記録の編集は`record.md`で行い、正規`plan.md`は要約しません。
- 正本不明の旧要約はmetadata-only migrationの対象です。`python3 tools/migration_plan.py`は読取専用で対象と解除条件を出し、実移行・削除・公開を行いません。
- 同一内容のbundle、canonical source、export結果を重複して収録しません。正本と出典を `metadata.yaml` で示します。

## 人間とエージェントの作業ルール

1. 作業前にルートの `README.md`、対象カテゴリの一覧ページ、対象レコードの `README.md` と `metadata.yaml` を確認します。
2. 新しい制作プランまたは作品を追加するときは、既存の識別子を確認して新しいIDを付与します。
3. 新しいplan recordは親の`AUTOMATIC_PLAN`投影だけで追加し、個別の`README.md`、無変換`plan.md`、`metadata.yaml`を揃えます。
4. 作品固有のメディアは、必ず対応する `works/Wxxxx-title/media/` に置きます。
5. プランと作品の関係を、双方のメタデータと本文のリンクで追跡できるようにします。
6. 相対リンク、画像リンク、一覧ページのリンクが有効であることを確認します。
7. 既存のレコードを変更するときは、変更理由と影響範囲を確認し、無関係なレコードを変更しません。
8. 公開可否が判断できないファイルは追加せず、確認が必要なものとして扱います。
9. `python3 tools/validate.py --check`でcanonical hash、no-transform provenance、Production生成sectionを検証します。

この構造により、ルート README は「展示入口」、`plans/` と `works/` は「公開カタログ」、各レコードのディレクトリは「個別の詳細ページ」として機能します。
