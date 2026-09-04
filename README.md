# Agentic Art Project

このリポジトリは、`agentic-art-orchestration` の出力から、Agentic Art プロジェクトの公開資料だけを収録するためのリポジトリです。

ルートの `README.md` は、このプロジェクトを初めて訪れた人のための展示入口です。プロジェクトのコンセプトと代表的な作品を紹介し、すべての制作プランと作品記録へ案内します。

## コンセプト

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

このリポジトリはオーケストレーションの実行環境や内部ログを収録する場所ではありません。自律的な制作の結果を、個別の制作プランと作品記録として追跡可能な形で公開する場所です。

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
| [agentic-art-project](https://github.com/masa-san-jp/agentic-art-project) | 公開成果物カタログ | オーケストレーションの出力から公開用の制作プラン、作品、制作記録を収録する |
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

制作プランは、同じ入力から分岐した制作上の仮説と、その仮説を検証するための条件を読むための記録です。完成作品や受入試験の通過を意味しません。`plans/index.yaml` の `plan_state: canonical-plan` は Production 正本の無変換投影、`blocked-missing-canonical` は正本未確認の旧要約であり、後者は制作可能な計画として扱いません。以下の一覧は [`plans/index.yaml`](plans/index.yaml) から生成されます。

<!-- agentic-art:catalog:start -->
- [選択の持ち主 — 翻訳のあとに残るもの](plans/P0001-owner-of-choice/README.md)
- [移動する隙間による近接場の交換](plans/P0002-moving-gap/README.md)
- [関わり方を選び直す距離 — 余白の呼吸](plans/P0003-yohaku-breath/README.md)
- [必要な後退 — 単位を視認限界の下へ置いた一枚の大判プリント](plans/P0004-necessary-retreat/README.md)
- [近いのに届かない — 枠を見る側に置く](plans/P0005-close-but-cannot-reach/README.md)
- [距離が選ぶ境界 — 近づいても触れない休止の場](plans/P0006-distance-selects-boundary/README.md)
- [近接不在 — Near, Not Received](plans/P0007-near-not-received/README.md)
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

`README.md` は人間が読むための紹介ページ、`plan.md` または `record.md` は内容の正本、`metadata.yaml` は一覧化・検索・自動処理に使う構造化情報です。`index.yaml` は公開projection互換の `records` と再利用禁止IDを示す `retired_ids` を持ちます。

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
status: published
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

`agentic-art-orchestration` の出力を取り込む場合も、公開対象を確認してから、このリポジトリの構造に合わせて整理します。オーケストレーション側の内部ディレクトリ構造を、そのままコピーしません。

## 参照元からの取り込み

参照元の一つのフォルダを、そのまま一つの公開レコードにコピーするとは限りません。次の基準で整理します。

- 人間が読むための確定版の制作プランは `plans/Pxxxx-slug/plan.md` に整理します。
- 作品と制作物の記録は `works/Wxxxx-slug/record.md` に整理します。
- 作品固有の画像、印刷データ、映像、音声、公開可能な制作スクリプトは、対応する作品の `media/` に整理します。
- 100件のプラン生成方法など、個別作品に属さない仕組みの説明は `docs/production-system.md` に整理します。
- 同じプロジェクトの旧版・別形式の文書はすべて個別レコードにしません。公開する正本を一つ選び、必要な版情報を `metadata.yaml` に記録します。
- `.gdoc` はGoogle Docsへの参照情報であり、公開本文ではありません。`.gdoc`ファイルをそのままコピーせず、公開可能性を確認したうえで本文をMarkdownに変換するか、公開URLを明示します。
- `handoff/`、`research-project/`、`production-plan/08_runtime/` などの内部運用ツリーは、そのまま公開ディレクトリへ移しません。公開に必要な情報だけを、人間向けのプランまたは作品記録へ要約します。
- 同一内容のbundle、canonical source、export結果を重複して収録しません。正本と出典を `metadata.yaml` で示します。

## 人間とエージェントの作業ルール

1. 作業前にルートの `README.md`、対象カテゴリの一覧ページ、対象レコードの `README.md` と `metadata.yaml` を確認します。
2. 新しい制作プランまたは作品を追加するときは、既存の識別子を確認して新しいIDを付与します。
3. 新しいレコードには、個別の `README.md`、本文ファイル、`metadata.yaml` を作成します。
4. 作品固有のメディアは、必ず対応する `works/Wxxxx-title/media/` に置きます。
5. プランと作品の関係を、双方のメタデータと本文のリンクで追跡できるようにします。
6. 相対リンク、画像リンク、一覧ページのリンクが有効であることを確認します。
7. 既存のレコードを変更するときは、変更理由と影響範囲を確認し、無関係なレコードを変更しません。
8. 公開可否が判断できないファイルは追加せず、確認が必要なものとして扱います。

この構造により、ルート README は「展示入口」、`plans/` と `works/` は「公開カタログ」、各レコードのディレクトリは「個別の詳細ページ」として機能します。
