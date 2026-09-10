# Agentic Artのリポジトリ関係図

このページは、Agentic Artを初めて見る人が、8つのリポジトリの役割、データの流れ、最初に読む場所を把握するための人間向けの案内です。各リポジトリの詳細なschema、Issue、実行手順は、それぞれのREADMEと正本文書を参照してください。

## 全体の流れ

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

入力ナレッジと鑑賞者反応は、それぞれのリポジトリが正本を所有します。Orchestrationは必要なsignalを固定commitと境界契約で読み、Researchへ渡します。Researchは根拠・仮説・制作要件を整理してProductionへhandoffし、Productionは制作計画と結果を管理します。Projectに入るのは、公開安全性・権利・来歴を確認した公開可能なrecordだけです。

データは常時同期されません。リポジトリ間で渡るのは、目的を限定したnormalized signal、research handoff、result、またはcanonical planです。内部ログ、会話、prompt、認証情報、`PRIVATE_RAW`、`RESTRICTED`は渡しません。

## 8リポジトリの役割

| リポジトリ | 主に所有するもの | 次に渡すもの / 関係 |
|---|---|---|
| [self-model-notes](https://github.com/masa-san-jp/self-model-notes) | 同意済みの自己モデルとその根拠 | privacy-safeなresearch signalをResearchへ渡す。公開カタログではない |
| [art-history-notes](https://github.com/masa-san-jp/art-history-notes) | 美術史のentity、context、関係、出典 | 根拠付きのart-history signalをResearchへ渡す |
| [marketing-trends-notes](https://github.com/masa-san-jp/marketing-trends-notes) | 市場・トレンド・practiceと鮮度・出典 | normalized signalを必要なResearchへ渡す |
| [viewer-response-notes](https://github.com/masa-san-jp/viewer-response-notes) | 鑑賞者反応の集計と保守的なassessment | 生データを公開せず、feedback signalを次回Researchへ戻す |
| [agentic-art-orchestration](https://github.com/masa-san-jp/agentic-art-orchestration) | 全体の制御、source pin、workspace、実行、横断検証 | 各repoを接続し、検証済み成果をProjectへexport-only投影する |
| [agentic-art-research](https://github.com/masa-san-jp/agentic-art-research) | 調査、仮説、要件、判断、evidence | versioned production handoffをProductionへ渡す |
| [agentic-art-production](https://github.com/masa-san-jp/agentic-art-production) | 制作計画、試作、本制作、結果、evidence | 検証済みcanonical plan / resultをOrchestrationへ返す |
| [agentic-art-project](https://github.com/masa-san-jp/agentic-art-project) | 公開制作プラン、作品、制作記録 | Orchestrationから公開可能なrecordを受け取るread-onlyの公開カタログ |

### 目的別の入口

- 作品・公開プランを読む：[このProjectの`plans/`と`works/`](../README.md)
- システム全体を理解する：[agentic-art-orchestrationのrepository map](https://github.com/masa-san-jp/agentic-art-orchestration/blob/main/docs/repository-map.md)
- 制作を開始・再開する：[agentic-art-orchestrationのREADME](https://github.com/masa-san-jp/agentic-art-orchestration)
- Researchの根拠・要件を確認する：[agentic-art-research](https://github.com/masa-san-jp/agentic-art-research)
- Productionの計画・結果を確認する：[agentic-art-production](https://github.com/masa-san-jp/agentic-art-production)
- 入力ナレッジを読む：[self-model-notes](https://github.com/masa-san-jp/self-model-notes)、[art-history-notes](https://github.com/masa-san-jp/art-history-notes)、[marketing-trends-notes](https://github.com/masa-san-jp/marketing-trends-notes)
- 鑑賞者反応を読む：[viewer-response-notes](https://github.com/masa-san-jp/viewer-response-notes)

## ローカル投影とリモート公開

Orchestrationの自動laneが行うのは、検証済みrecordを指定されたProject checkoutへ生成し、受信側validatorで確認するところまでです。これは「ローカル投影」です。

Gitのcommit、branch、push、PR、merge、release、リポジトリのvisibility変更、外部共有は別の人間gateです。ローカルProjectにrecordがあることだけから、GitHubのリモートに公開済みだとは判断しません。

機械可読なrepo定義は [`repositories.yaml`](repositories.yaml)、canonical planの受入条件は [`public-project.yaml`](../public-project.yaml) と [`plans/index.yaml`](../plans/index.yaml) が持ちます。
