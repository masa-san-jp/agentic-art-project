# 統合制作計画書

> この文書は、受理済みhandoffと検証済みの制作計画を、人間が読んで制作判断・制作実務に使える一つの計画書へ統合したものです。計画の生成は、購入・契約・公開・連絡・削除・物理作業の実行承認を意味しません。

### 計画メタデータ

| 項目 | 内容 |
| --- | --- |
| プロジェクト | production/yohaku-breath |
| 計画 | PL001 revision 1 |
| 計画状態 | PLANNING |
| 制作着手可否 | 着手不可 |
| 着手できない理由 | blocking_gaps |
| 生成日時 | 2026-09-10T16:00:00+09:00 |
| handoff | HO0003 revision 1 |
| 要件カバレッジ | 100% |
| クリティカルパス | `TK001` → `TK002` |


## 1. 完成像

| 項目 | 内容 |
| --- | --- |
| experience sequence / encounter | 入口からは構成全体が読めるが、近づくと細部の線や欠けだけが大きく見える。, 観客が横へ移動すると細部と全体のどちらを得るかが変わり、固定された鑑賞順はない。, 離れて別の角度へ戻ると、先ほど見えなかった全体の関係が再び現れる。 |
| position | 観客が自由に前後左右へ移動し、距離と角度を自分で選べる範囲。 |
| first_seconds | 全体像と、近づくと隠れる一部のディテールが同時に予告される。 |
| after_30s | 細部を得る代わりに全体を失い、離れると全体を得る代わりに細部を失うと分かる。 |
| after_3min | 最初の立ち位置が唯一の正解ではなく、見る位置を選び直すこと自体が作品の構造だと残る。 |

## 2. テーマ

| 項目 | 内容 |
| --- | --- |
| field | 近さの細部と距離の全体を選び直す鑑賞 |
| stands_against | 作品には一つの正しい立ち位置や、順番どおりに進む鑑賞ルートがあるという見方。 |
| difference | 距離と角度に応じて細部と全体の可視性を交換し、観客の自由な再配置を必須の機構にする。 |
| why_now | 画面上の拡大縮小が容易な時代に、身体の位置を変えることで失うものと得るものを再び経験させる。 |

## 3. メッセージ

| 項目 | 内容 |
| --- | --- |
| claim | 近づけば細部が、離れれば全体が見える。どちらを選ぶかに唯一の正解はない。 |
| who_disagrees | 近くで詳しく見るほど、作品全体も同時に理解できると考える立場。 |
| denies | 本作が治療効果や健康上の利益を約束すること、観客に固定ルートや演技を要求すること。 |
| shown_not_told | 距離・角度ごとの遮蔽、細部の拡大、全体の回復、自由な移動の痕跡で示す。 |

## 4. コンセプト

| 項目 | 内容 |
| --- | --- |
| mechanism | 視線の高さを越える線群と部分的な遮蔽を配置し、近距離では細部、遠距離では全体の構図が優先される視覚的トレードオフを作る。 |
| without_the_technique | CEASES_TO_WORK |
| precedents | reference=legacy/P0003/historical-plan, difference=歴史的候補の固有条件を由来として保持し、現行Productionの構造化された制作判断と検証可能な工程へ置き換える。 |
| self_repetition_risk | reference=legacy-recovery/repetition-review, assessment=固定停止線や状態スイッチを設けず、自由な位置変更と細部/全体の交換を固有の条件にする。 |

## 5. 調査の要約

| 項目 | 内容 |
| --- | --- |
| questions | 細部と全体の交換を、観客が身体で再現できる遮蔽として設計できるか。, 固定ルートなしでも、距離と角度の選択が作品として読めるか。 |
| what_was_read | Projectの履歴commit P0003 の公開plan本文とmetadataを由来資料として読み、旧候補の主題と未確定事項を分離した。固有条件は 旧本文の近接で細部、遠景で全体、観客が位置と角度を変える、固定された道筋を置かないという条件を抽出した。 主要な旧記述は > `agentic-art-orchestration` が生成した制作計画を、公開用のコンセプト、要件、検証条件に整理したものです。内部研究の原文・個人由来の資料・実行ログは含めません。 近さゆえに目を離せないが、近いままでも関わり方は選び直せる。その変化を、説明文ではなく、鑑賞者が自分の位置を変える経験として成立させる。。 |
| what_came_out | 距離と角度で可視情報が交換される、自由移動型の視覚配置として再構成した。 |
| what_is_not_settled | 会場条件、物理試作、歴史的参照の最終妥当性、日程と費用は人間の制作前レビュー前である。 |

### 採択内容と根拠

| 項目 | 内容 |
| --- | --- |
| 採択仮説 | PH001 |
| 仮説タイトル | 余白の呼吸 — Yohaku Breath |
| 仮説 | Construct a freely navigable visual arrangement where moving close reveals detail while moving away restores the whole, and changing angle changes the available information; no fixed route or forced performance is allowed. |
| 仮説状態 | ADOPTED |
| 選択状態 | PROVISIONAL |
| 選択権限 | AGENT |
| 人間承認要否 | いいえ |
| 選択理由 | Construct a freely navigable visual arrangement where moving close reveals detail while moving away restores the whole, and changing angle changes the available information; no fixed route or forced performance is allowed. |
| 創作指針 | artifacts/creative-direction.md |

### 制作リファレンス

コンセプト、ビジュアル、制作手法の参照先です。URLは受理済みhandoffに含まれる恒久HTTPS URLだけを掲載し、アクセスできない参照や不足カテゴリはギャップとして残します。

| 分類 | 出所ID | 種別 | 概要 | アクセスURL | 状態 |
| --- | --- | --- | --- | --- | --- |
| コンセプト | DC001 | decision | Historical Project candidate P0003; evidence only, not current Production canonical. | <https://github.com/masa-san-jp/agentic-art-project> | AVAILABLE |
| 手法 | IN001 | insight | Historical metadata used to preserve provenance while regenerating the plan. | <https://github.com/masa-san-jp/agentic-art-project> | AVAILABLE |

### 要件と受入の目的

| 要件 | 優先度 | 要件内容 | 出所 | 受入テスト | 計画上の対応 |
| --- | --- | --- | --- | --- | --- |
| RQ001 | mandatory | Construct a freely navigable visual arrangement where moving close reveals detail while moving away restores the whole, and changing angle changes the available information; no fixed route or forced performance is allowed. | 未設定 | AT001 | COVERED |

## 6. できている物

### ビジュアルパッケージ

boardとmockupは、受理済みhandoffから生成した閲覧用の決定論的fixtureです。外部画像素材の取得・採用、物理制作、外部検証、公開、購入、契約、Drive共有は実施していません。

| 種別 | 名称 | 状態 | 相対リンク | asset hash | 権利 | 安全 |
| --- | --- | --- | --- | --- | --- | --- |
| ビジュアルリファレンスボード | Visual reference board · Construct a freely navigable visual arrangement where moving close reveals detail while moving away restores the whole,  | BOARD | [03_plan/media/visual-reference-board.svg](media/visual-reference-board.svg) | sha256:579783e14b1cfee2cd0d8f582b8f63eebbbf5b91a029da7c09ec325bbaae8b15 | PROJECT_INTERNAL | CLEAR |
| コンセプト・モックアップ | Concept mockup · Construct a freely navigable visual arrangement where moving close reveals detail while moving away restores the whole,  | MOCKUP | [03_plan/media/concept-mockup.svg](media/concept-mockup.svg) | sha256:a1ea7ced48a4dc7bfc9a753768bd3a3f40087572ad5f33ad02de6eba7d07a8ae | PROJECT_INTERNAL | REVIEW_REQUIRED |

| mockup注記 | 内容 |
| --- | --- |
| 表現種別 | CONCEPTUAL |
| 寸法 | Not to scale; physical dimensions are not supplied by the accepted handoff. |
| 素材 | Material selection remains provisional and is not a purchase or fabrication instruction. |
| 配置 | 観客が自由に前後左右へ移動し、距離と角度を自分で選べる範囲。 |
| 検証 | PHYSICAL_EXTERNAL validation: NOT_RUN. No physical prototype, publication, purchase, contract, or Drive share was performed. |

まだ何も作っていない。この節は、制作した物が実行台帳（`05_execution/output-versions.yaml`）に記録された時点で、現物とプレビュー画像を載せる。

## 7. 制作範囲と成果物

| 項目 | 内容 |
| --- | --- |
| スコープ状態 | PROVISIONAL |
| 必須要件ID | RQ001 |
| 試作計画ID | PP001 |
| 前提 | なし |
| 除外・未許可範囲 | Do not purchase, contract, publish, send, contact, delete, or perform physical work automatically. |
| 権利制約 | Use only original, non-sensitive plan and prototype material. |
| 安全制約 | No physical or external effect is authorized by plan generation. |
| プライバシー制約 | Do not use names, addresses, tracking numbers, or real recipient data. |
| 再計画トリガー | venue_changed, rights_or_privacy_change, new_historical_evidence |

| 成果物 | 種別 | 内容 | 受入テスト | 担当能力 | 納期 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| DL001 | production-deliverable | 余白の呼吸 — Yohaku Breath | AT001 | production-owner-confirmation-required | MS002 | PLANNED |

## 8. 技術仕様・材料・資源

| 仕様 | 対象 | 目標 | 許容差 | 測定方法 | 出所要件 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| TS001 | requirement-RQ001 | kind=QUALITATIVE, statement=Construct a freely navigable visual arrangement where moving close reveals detail while moving away restores the whole, and changing angle changes the available information; no fixed route or forced performance is allowed. | 未設定 | structured-plan-and-prototype-review | RQ001 | PROVISIONAL |

| 材料 | 仕様 | 数量 | 権利 | 安全 | 出所試作 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| MT001 | Detail/whole repositioning study — Layered line drawings, freestanding translucent screens, low-contrast occluders, and floor space allowing free front/back/side movement; no health claims or scripted route. | value=1, unit=item | PROJECT_INTERNAL | REVIEW_REQUIRED | PP001 | CANDIDATE |

| 資源 | 種別 | 必要能力 | 数量 | 可用性 | 関連タスク |
| --- | --- | --- | --- | --- | --- |
| RS001 | PERSON_CAPABILITY | artist and venue-safety reviewer | value=1, unit=item | REQUIRES_CONFIRMATION | TK001 |

## 9. 工程と作業手順

| 作業パッケージ | 内容 | 投入物 | 制約 | 成果物 | タスク | 担当能力 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WP001 | PP001 | TS001 | なし | DL001 | TK001, TK002 | production-owner-confirmation-required | BLOCKED |

| タスク | 作業 | 前提 | 所要時間 | 必要材料 | 受入条件 | 効果種別 | 承認 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TK001 | Observe the detail/whole trade-off from free positions | なし | value=1, unit=h | MT001 | PT001 | PHYSICAL_EXTERNAL | AR001 | BLOCKED |
| TK002 | Validate the regenerated plan references | TK001 | value=1, unit=h | WP001の投入物 | PT002 | READ_ONLY | なし | BACKLOG |

**実施順の読み方:** クリティカルパスは `TK001` → `TK002` です。READYタスクは なし です。物理・外部効果を伴うタスクは承認待ちです。

## 10. 試作・受入評価

| テスト | 対象要件 | 方法 | 合格条件 | 現在結果 |
| --- | --- | --- | --- | --- |
| AT001 | RQ001 | structured-plan-and-prototype-review | Reviewers can demonstrate at least two positions where detail and whole are exchanged, without a prescribed route, performance, or therapeutic claim. | NOT_RUN |

| マイルストーン | 内容 | 順序 | 前提 | 状態 |
| --- | --- | --- | --- | --- |
| MS001 | Start PP001 | 1 | なし | PLANNED |
| MS002 | Complete PP001 | 2 | MS001 | BLOCKED |

## 11. 日程と予算

| 日程・予算項目 | 内容 |
| --- | --- |
| 日程モード | RELATIVE |
| 日程基準線 | PROVISIONAL |
| タスク日程 | task_id=TK001, duration=value=1, unit=h, start_at=未設定, due_at=未設定, task_id=TK002, duration=value=1, unit=h, start_at=未設定, due_at=未設定 |
| 日程ギャップ | Calendar dates and availability are not supplied by the accepted handoff; the schedule remains relative. |
| 通貨 | JPY |
| 予算総額 | 未設定 |
| 予備費 | 未設定 |
| 承認閾値 | 未設定 |
| 予算状態 | ESTIMATED |
| 予算ギャップ | No price, quote, supplier, reservation, or commitment is present in the accepted handoff. |

| 予算項目 | 区分 | 内容 | 金額 | 根拠 | 確度 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| BI001 | prototype-plan | Estimated cost band for PP001 | 未設定 | accepted handoff cost band: UNKNOWN | LOW | ESTIMATED |

## 12. リスクと未解決事項

| リスク | 内容 | 影響 | 軽減策 | 重要度 | 可能性 | 担当 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RK001 | Handoff gap GP001 | The original accepted Production handoff for P0003 is unavailable; this is an explicitly regenerated recovery plan, not byte-identical recovery. | Resolve the handoff gap and regenerate the plan before relying on the affected decision. | MEDIUM | UNKNOWN | production-owner-confirmation-required | OPEN |

| ギャップ | 内容 | ブロッキング |
| --- | --- | --- |
| GP001 | The original accepted Production handoff for P0003 is unavailable; this is an explicitly regenerated recovery plan, not byte-identical recovery. | いいえ |
| PG001 | Budget amounts and commitments are not supplied by the accepted handoff. | いいえ |
| PG002 | Calendar dates and availability are not supplied by the accepted handoff; the schedule remains relative. | いいえ |
| PG003 | Prototype plan PP001 does not supply a known duration band (UNKNOWN); confirm its duration before execution. | いいえ |
| PG005 | ビジュアル reference access URL is not supplied by the accepted handoff. | はい |
| PG006 | External-effect task TK001 remains blocked until the required human approval is recorded. | はい |

## 13. 承認・安全境界

| 承認ID | 対象行為 | 対象 | 対象hash | 権限者 | 状態 | 理由 | 関連タスク |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AR001 | PHYSICAL_EXTERNAL | 03_plan/task-plan.yaml#TK001 | sha256:3c853a543e7605451f9062948adb92b9abc77c86c4d17be126d0ae944b89cd9e | HUMAN | REQUIRED | Physical or external-effect tasks require explicit human approval before execution. | TK001 |

この計画書は、明示的な人間承認が記録されるまで、物理作業、外部サービスへの接続、購入、契約、支払い、公開、応募、連絡、削除を許可しません。材料の権利・安全状態、会場条件、担当能力、見積、日程は制作開始前に人間が確認してください。

## 14. 人間向け実行前チェックリスト

- 採択仮説と要件の内容・優先度を確認する。
- コンセプト、ビジュアル、手法の参照URLを開き、制作時に参照可能か確認する。
- 未設定の会場、照明、日程、予算、見積、担当能力を確定する。
- 材料の権利状態と安全状態を確認し、変更時は再評価する。
- 物理・外部効果タスクの対象・範囲・hashを確認して承認する。
- 各受入テストの実施条件と証跡の保存先を決める。
- 制作中の差分・失敗・変更要求を既存の計画に上書きせず記録する。

## 15. 証跡と再現性

| 項目 | 値 |
| --- | --- |
| handoff content hash | sha256:335180de1388f2be8ac7682220f5a8f40a9b9d2043e5d85eda6576b2544ab5c5 |
| plan integrity hash | sha256:b67ccc9388fbebd4a9ffceff39a4fba7285221ab7d3177405a040100c09d6014 |
| source input hash | sha256:cbec9a8f65550342c3525f20894cf84e19addde6941e1207f7d58488a7ff27de |
| 生成アルゴリズム | production-plan-v1 |
| トレーサビリティID | HO0003, PH001, RQ001, AT001, PP001, GP001 |
| 依存グラフ | graph_id=DG001, nodes=TK001, TK002, edges=from=TK001, to=TK002, topological_order=TK001, TK002, trace_refs=HO0003, PH001, RQ001, AT001, PP001, GP001, DG001 |

### 受け渡し時の注意

ユーザーに渡す計画書はこの `03_plan/production-plan.md` 一つです。`production-plan.yaml`などの構造化ファイルと`agent-contexts/`は、検証・再生成・内部運用のためにGit外の制作projectへ保持されます。制作した物は §6 に、実行台帳へ記録済みのプレビュー画像だけを貼ります。完成作品の原寸データ、RAW、動画、音声、3D、大容量asset、credential、signed URLはこの計画書へ埋め込みません。
