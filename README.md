# Agentic Art Project

`Agentic Art Project` は、エージェント群が考案した制作プランと、そこから生まれた作品・制作記録を読むための公開カタログです。

ここはエージェントを動かす場所ではありません。制作の仕組みを知りたい人は [`agentic-art-orchestration`](https://github.com/masa-san-jp/agentic-art-orchestration) を、公開された成果を見たい人はこのリポジトリを読んでください。

## 30秒で分かるAgentic Art

Agentic Art は、AIで画像を生成すること自体を目的にしたプロジェクトではありません。人間が与えたテーマや条件をもとに、複数のエージェントが調査・判断・制作計画を分担し、コンセプトを持つアートを生み出す仕組みを試みています。

一つの入力から一つの答えだけを出すのではなく、複数の制作プランを比較し、その後の制作と記録を追跡できることが特徴です。

```text
テーマ・条件
    ↓
エージェント群による調査と制作プランの生成
    ↓
制作の実行と記録
    ↓
公開可能性を確認
    ↓
このリポジトリの公開カタログ
```

## まず読む場所

- 公開された制作プラン：[plans/](plans/README.md)
- 公開された作品：[works/](works/README.md)
- 制作システムの説明：[`docs/production-system.md`](docs/production-system.md)
- エージェント群の全体像：[`docs/repository-map.md`](docs/repository-map.md)
- 実行・契約の正本：[`agentic-art-orchestration`](https://github.com/masa-san-jp/agentic-art-orchestration)

制作の仕組みを知りたい人は orchestration へ、公開された成果を見たい人は `plans/` と `works/` へ進んでください。

## コンセプト

芸術の契機を「精霊や風が運び、人間が受け取って具象化する」と捉え、その過程を支える制作プランと系譜を残します。

自律性とは、単一のエージェントが孤立して作品を生成することではありません。調査、制作計画、制作、記録などの役割をエージェント群に分担させ、オーケストレーションによって一連の制作プロセスとして動かすことです。

## エージェントハーネス群の全体像

各リポジトリは別々の知識や成果を所有し、`agentic-art-orchestration` がそれらを制作の流れとしてつなぎます。内部データを一つのリポジトリへ集約する構成ではありません。

```text
入力知識・鑑賞者の反応
            ↓
agentic-art-orchestration  制作全体の制御
       ┌────┼──────────────┐
       ↓    ↓              ↓
 research production   project
 調査     制作実行       公開カタログ
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
- [aak07-agent-20260910-p4](plans/P0008-aak07-agent-20260910-p4/README.md)
- [選択の所有 — Owner of Choice（旧P0001復旧版）](plans/P0009-legacy-owner-of-choice/README.md)
- [移動する空白 — Moving Gap（旧P0002復旧版）](plans/P0010-legacy-moving-gap/README.md)
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
