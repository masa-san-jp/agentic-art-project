# 統合制作計画書

> この文書は、受理済みhandoffと検証済みの制作計画を、人間が読んで制作判断・制作実務に使える一つの計画書へ統合したものです。計画の生成は、購入・契約・公開・連絡・削除・物理作業の実行承認を意味しません。

### 計画メタデータ

| 項目 | 内容 |
| --- | --- |
| プロジェクト | production/near-not-received |
| 計画 | PL001 revision 1 |
| 計画状態 | PLANNING |
| 制作着手可否 | 着手不可 |
| 着手できない理由 | blocking_gaps |
| 生成日時 | 2026-09-10T16:00:00+09:00 |
| handoff | HO0007 revision 1 |
| 要件カバレッジ | 100% |
| クリティカルパス | `TK001` → `TK002` |


## 1. 完成像

| 項目 | 内容 |
| --- | --- |
| experience sequence / encounter | A3サイズの浅い透明な閉箱の36セルに、35個の紙包みと一つの空セルが並ぶ。, 一つの包みは観客に近いが、箱を開けずには触れられず、状態カードの語だけが変化を示す。, 電池式LEDと固定された影板が、送付や受領を実行せず、近さと受領不能を卓上で閉じる。 |
| position | 箱を動かさず、外周から全36セルと状態カードを比較できる卓上の位置。 |
| first_seconds | 35個の包み、一つの空セル、近いが届かない包み、閉じた箱が一望できる。 |
| after_30s | APPROACHやHELDなどの状態語は見えても、実際の配送先や受取人は存在しないと分かる。 |
| after_3min | 近くにあることは届いたことでも介入できたことでもなく、NOT RECEIVEDが完成状態として残る。 |

## 2. テーマ

| 項目 | 内容 |
| --- | --- |
| field | 近接と受領を切り分ける、閉じた卓上の不在構造 |
| stands_against | 近いものは受け取られ、状態表示は現実の配送や相手への介入を意味すると考える見方。 |
| difference | 6x6の36セル、35包みと空セル、一つの近いが不可触な包み、9状態カード、固定光源を一つの閉箱に収める。 |
| why_now | 通知や送信の近さが受領と混同されやすい中、相手の個人情報なしに不受領を完成状態として観察できる。 |

## 3. メッセージ

| 項目 | 内容 |
| --- | --- |
| claim | 近くにいることは、届いたことでも介入できたことでもない。受領されない状態も完成している。 |
| who_disagrees | 接近・送信・表示があれば、相手への到達と受領が成立すると考える立場。 |
| denies | 実在の配送、受取人、追跡番号、開閉機構、動く機械、LEDを相手の反応として読むこと。 |
| shown_not_told | 36セルの数、空セル、閉箱、状態語、固定影、動かないLEDで示す。 |

## 4. コンセプト

| 項目 | 内容 |
| --- | --- |
| mechanism | A3卓上の浅い閉じた透明箱を6x6=36セルに区切り、35個の同型紙包みと一つの空セルを置く。近いが不可触の包み、9状態カード、電池式LED、固定影板を添える。 |
| without_the_technique | CEASES_TO_WORK |
| precedents | reference=legacy/P0007/historical-plan, difference=歴史的候補の固有条件を由来として保持し、現行Productionの構造化された制作判断と検証可能な工程へ置き換える。 |
| self_repetition_risk | reference=legacy-recovery/repetition-review, assessment=他候補の歩行・停止線・分岐を使わず、卓上の固定配置、36セル、受領状態語、予算/時間制約を固有の軸にする。 |

## 5. 調査の要約

| 項目 | 内容 |
| --- | --- |
| questions | 36セル中の一つの空白は、受領不能を物理的な完成状態として読ませられるか。, 状態カードを実配送や受取人なしで使うとき、介入と受領の混同を避けられるか。 |
| what_was_read | Projectの履歴commit P0007 の公開plan本文とmetadataを由来資料として読み、旧候補の主題と未確定事項を分離した。固有条件は 旧本文のA3卓上物、浅い閉透明箱、6x6=36セル、35包みと空セル、近いが不可触の包み、9状態カード、固定LED/影、予算15,000円以下・10時間以下を抽出した。 主要な旧記述は > P0007 revision 2。これは、構想だけを提示する文書ではなく、明示した条件の下で一人が最後まで組み立て、客観的な完了判定まで行うための実制作プランである。内部ログ、会話、個人情報、実在の配送情報、第三者の画像・文章本文は含めない。 完成物は、閉じた透明面の向こうに紙のパケット群を収めた、A3サイズの卓上オブジェである。制作場所と展示会場を分離し、会場の選定、搬入、契約、電源工事、他者の協力を完成条件から外す。最初から「自宅または作業台で完成する一品」を最終成果物に固定する。。 |
| what_came_out | 外部送信を行わない閉箱の数的配置として、受領不能を卓上で完結させた。 |
| what_is_not_settled | 会場条件、物理試作、歴史的参照の最終妥当性、日程と費用は人間の制作前レビュー前である。 |

### 採択内容と根拠

| 項目 | 内容 |
| --- | --- |
| 採択仮説 | PH001 |
| 仮説タイトル | 近くても受領されない — Near, Not Received |
| 仮説 | Build an A3 tabletop closed box with a 6x6 grid of 36 cells, 35 identical paper packets plus one empty cell, one closer but inaccessible packet, nine state cards, a battery LED, and a fixed shadow plate; keep budget at or below JPY 15,000, work at or below 10 hours, and perform no real shipping. |
| 仮説状態 | ADOPTED |
| 選択状態 | PROVISIONAL |
| 選択権限 | AGENT |
| 人間承認要否 | いいえ |
| 選択理由 | Build an A3 tabletop closed box with a 6x6 grid of 36 cells, 35 identical paper packets plus one empty cell, one closer but inaccessible packet, nine state cards, a battery LED, and a fixed shadow plate; keep budget at or below JPY 15,000, work at or below 10 hours, and perform no real shipping. |
| 創作指針 | artifacts/creative-direction.md |

### 制作リファレンス

コンセプト、ビジュアル、制作手法の参照先です。URLは受理済みhandoffに含まれる恒久HTTPS URLだけを掲載し、アクセスできない参照や不足カテゴリはギャップとして残します。

| 分類 | 出所ID | 種別 | 概要 | アクセスURL | 状態 |
| --- | --- | --- | --- | --- | --- |
| コンセプト | DC001 | decision | Historical Project candidate P0007; evidence only, not current Production canonical. | <https://github.com/masa-san-jp/agentic-art-project> | AVAILABLE |
| 手法 | IN001 | insight | Historical metadata used to preserve provenance while regenerating the plan. | <https://github.com/masa-san-jp/agentic-art-project> | AVAILABLE |

### 要件と受入の目的

| 要件 | 優先度 | 要件内容 | 出所 | 受入テスト | 計画上の対応 |
| --- | --- | --- | --- | --- | --- |
| RQ001 | mandatory | Build an A3 tabletop closed box with a 6x6 grid of 36 cells, 35 identical paper packets plus one empty cell, one closer but inaccessible packet, nine state cards, a battery LED, and a fixed shadow plate; keep budget at or below JPY 15,000, work at or below 10 hours, and perform no real shipping. | 未設定 | AT001 | COVERED |

## 6. できている物

### ビジュアルパッケージ

boardとmockupは、受理済みhandoffから生成した閲覧用の決定論的fixtureです。外部画像素材の取得・採用、物理制作、外部検証、公開、購入、契約、Drive共有は実施していません。

| 種別 | 名称 | 状態 | 相対リンク | asset hash | 権利 | 安全 |
| --- | --- | --- | --- | --- | --- | --- |
| ビジュアルリファレンスボード | Visual reference board · Build an A3 tabletop closed box with a 6x6 grid of 36 cells, 35 identical paper packets plus one empty cell, one closer  | BOARD | [03_plan/media/visual-reference-board.svg](media/visual-reference-board.svg) | sha256:738eb450496a6378a26f9643b414d3abbe83160e5c39ce15bb0d7941a370eca2 | PROJECT_INTERNAL | CLEAR |
| コンセプト・モックアップ | Concept mockup · Build an A3 tabletop closed box with a 6x6 grid of 36 cells, 35 identical paper packets plus one empty cell, one closer  | MOCKUP | [03_plan/media/concept-mockup.svg](media/concept-mockup.svg) | sha256:301e3493c2c8434641fcdd41f3fd322bc7ce9b8ff60a4d4ffb4eed1e87972338 | PROJECT_INTERNAL | REVIEW_REQUIRED |

| mockup注記 | 内容 |
| --- | --- |
| 表現種別 | CONCEPTUAL |
| 寸法 | Not to scale; physical dimensions are not supplied by the accepted handoff. |
| 素材 | Material selection remains provisional and is not a purchase or fabrication instruction. |
| 配置 | 箱を動かさず、外周から全36セルと状態カードを比較できる卓上の位置。 |
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
| DL001 | production-deliverable | 近くても受領されない — Near, Not Received | AT001 | production-owner-confirmation-required | MS002 | PLANNED |

## 8. 技術仕様・材料・資源

| 仕様 | 対象 | 目標 | 許容差 | 測定方法 | 出所要件 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| TS001 | requirement-RQ001 | kind=QUALITATIVE, statement=Build an A3 tabletop closed box with a 6x6 grid of 36 cells, 35 identical paper packets plus one empty cell, one closer but inaccessible packet, nine state cards, a battery LED, and a fixed shadow plate; keep budget at or below JPY 15,000, work at or below 10 hours, and perform no real shipping. | 未設定 | structured-plan-and-prototype-review | RQ001 | PROVISIONAL |

| 材料 | 仕様 | 数量 | 権利 | 安全 | 出所試作 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| MT001 | 36-cell near-not-received box — A3 shallow transparent closed box, dividers for 36 cells, 35 identical original paper packets, one empty cell, nine printed state cards, battery LED, and fixed shadow plate. | value=1, unit=item | PROJECT_INTERNAL | REVIEW_REQUIRED | PP001 | CANDIDATE |

| 資源 | 種別 | 必要能力 | 数量 | 可用性 | 関連タスク |
| --- | --- | --- | --- | --- | --- |
| RS001 | PERSON_CAPABILITY | artist and venue-safety reviewer | value=1, unit=item | REQUIRES_CONFIRMATION | TK001 |

## 9. 工程と作業手順

| 作業パッケージ | 内容 | 投入物 | 制約 | 成果物 | タスク | 担当能力 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WP001 | PP001 | TS001 | なし | DL001 | TK001, TK002 | production-owner-confirmation-required | BLOCKED |

| タスク | 作業 | 前提 | 所要時間 | 必要材料 | 受入条件 | 効果種別 | 承認 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TK001 | Assemble and count the closed receipt box | なし | value=1, unit=h | MT001 | PT001 | PHYSICAL_EXTERNAL | AR001 | BLOCKED |
| TK002 | Validate the regenerated plan references | TK001 | value=1, unit=h | WP001の投入物 | PT002 | READ_ONLY | なし | BACKLOG |

**実施順の読み方:** クリティカルパスは `TK001` → `TK002` です。READYタスクは なし です。物理・外部効果を伴うタスクは承認待ちです。

## 10. 試作・受入評価

| テスト | 対象要件 | 方法 | 合格条件 | 現在結果 |
| --- | --- | --- | --- | --- |
| AT001 | RQ001 | structured-plan-and-prototype-review | A reviewer counts 36 cells, 35 packets, and one empty cell; identifies the inaccessible near packet and NOT RECEIVED state; and confirms budget/time and no real recipient or shipment data. | NOT_RUN |

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
| RK001 | Handoff gap GP001 | The original accepted Production handoff for P0007 is unavailable; this is an explicitly regenerated recovery plan, not byte-identical recovery. | Resolve the handoff gap and regenerate the plan before relying on the affected decision. | MEDIUM | UNKNOWN | production-owner-confirmation-required | OPEN |

| ギャップ | 内容 | ブロッキング |
| --- | --- | --- |
| GP001 | The original accepted Production handoff for P0007 is unavailable; this is an explicitly regenerated recovery plan, not byte-identical recovery. | いいえ |
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
| handoff content hash | sha256:1e20b6141f187e2d6f5cab5ebfe013ae586bbf554cdc352adba6be8cd83ca6f5 |
| plan integrity hash | sha256:7f91c792ce886fa9bde6cd59d2b3d500aa416b20f07de9f4981d9213fd4b382c |
| source input hash | sha256:ec9a5e25aa464aaebeabfbe5545386067bbc1dc6fad170546119755e2178f51e |
| 生成アルゴリズム | production-plan-v1 |
| トレーサビリティID | HO0007, PH001, RQ001, AT001, PP001, GP001 |
| 依存グラフ | graph_id=DG001, nodes=TK001, TK002, edges=from=TK001, to=TK002, topological_order=TK001, TK002, trace_refs=HO0007, PH001, RQ001, AT001, PP001, GP001, DG001 |

### 受け渡し時の注意

ユーザーに渡す計画書はこの `03_plan/production-plan.md` 一つです。`production-plan.yaml`などの構造化ファイルと`agent-contexts/`は、検証・再生成・内部運用のためにGit外の制作projectへ保持されます。制作した物は §6 に、実行台帳へ記録済みのプレビュー画像だけを貼ります。完成作品の原寸データ、RAW、動画、音声、3D、大容量asset、credential、signed URLはこの計画書へ埋め込みません。
