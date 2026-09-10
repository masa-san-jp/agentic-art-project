# 統合制作計画書

> この文書は、受理済みhandoffと検証済みの制作計画を、人間が読んで制作判断・制作実務に使える一つの計画書へ統合したものです。計画の生成は、購入・契約・公開・連絡・削除・物理作業の実行承認を意味しません。

### 計画メタデータ

| 項目 | 内容 |
| --- | --- |
| プロジェクト | production/distance-selects-boundary |
| 計画 | PL001 revision 1 |
| 計画状態 | PLANNING |
| 制作着手可否 | 着手不可 |
| 着手できない理由 | blocking_gaps |
| 生成日時 | 2026-09-10T16:00:00+09:00 |
| handoff | HO0006 revision 1 |
| 要件カバレッジ | 100% |
| クリティカルパス | `TK001` → `TK002` |


## 1. 完成像

| 項目 | 内容 |
| --- | --- |
| experience sequence / encounter | 観客は透明なポリカーボネート面の450mm手前で止まり、面の向こうに歪んだ線画が見える。, 4枚以上の線画と低彩度の色が、30秒周期の暖色光の変化と10秒以上の静止区間でゆっくり切り替わる。, 1200mmの通路を歩いても触れられず、静止して見る時間が残る。 |
| position | 幅1200mm以上の通路から面へ近づき、450mm停止線の手前で非接触に観察する位置。 |
| first_seconds | 透明面、停止線、向こう側の歪んだ線画、通路の幅が同時に読める。 |
| after_30s | 光の変化と静止区間が線画の見え方を変えるが、観客の接触やセンサー反応ではないと分かる。 |
| after_3min | 近づくほど見えるが、手は届かない距離が注意をつくり、健康効果ではなく境界の経験として残る。 |

## 2. テーマ

| 項目 | 内容 |
| --- | --- |
| field | 近接・休止・非接触を、透明面と光の静止区間で測る境界 |
| stands_against | 没入や接触の強さを健康効果や睡眠改善の数値で正当化する展示。 |
| difference | 450mm停止線、4枚以上の歪んだ線画、30秒光周期と10秒以上の静止、1200mm通路を同時に検証する。 |
| why_now | 近接を促す展示ほど、近づいても触れない安全な距離と、変化しない時間を設計条件として明示する必要がある。 |

## 3. メッセージ

| 項目 | 内容 |
| --- | --- |
| claim | 近づくほど見えるが、手は届かない距離が注意をつくる。休止は効果ではなく構成である。 |
| who_disagrees | 体験の価値は接触、没入、健康指標で測るべきだと考える立場。 |
| denies | 治療・睡眠・身体状態への効果、カメラ/マイク/生体計測、観客の接触を前提にすること。 |
| shown_not_told | 停止線、透明面、歪んだ線画、暖色光の静止区間、非接触の通路で示す。 |

## 4. コンセプト

| 項目 | 内容 |
| --- | --- |
| mechanism | 1800x2100mmの透明ポリカーボネート面の向こうへ4枚以上の歪んだ線画を置き、450mmの停止線と30秒周期の暖色光（10秒以上静止）を組み合わせる。 |
| without_the_technique | CEASES_TO_WORK |
| precedents | reference=legacy/P0006/historical-plan, difference=歴史的候補の固有条件を由来として保持し、現行Productionの構造化された制作判断と検証可能な工程へ置き換える。 |
| self_repetition_risk | reference=legacy-recovery/repetition-review, assessment=P0005の枠/匿名像やP0003の自由移動を再利用せず、寸法・停止線・光周期・通路幅を固有のゲートにする。 |

## 5. 調査の要約

| 項目 | 内容 |
| --- | --- |
| questions | 停止線と透明面は、近接と非接触を同時に読ませられるか。, 10秒以上の光の静止区間は、効果を主張せず休止の構成として観察できるか。 |
| what_was_read | Projectの履歴commit P0006 の公開plan本文とmetadataを由来資料として読み、旧候補の主題と未確定事項を分離した。固有条件は 旧本文の透明ポリカーボネート寸法、450mm停止線、4枚以上の歪んだ線画、低彩度、30秒光周期、10秒静止、1200mm通路、センサー禁止を採用条件へ戻した。 主要な旧記述は > この文書は、受理済みhandoffと検証済みの制作計画を、人間が読んで制作判断・制作実務に使える一つの計画書へ統合したものです。計画の生成は、購入・契約・公開・連絡・削除・物理作業の実行承認を意味しません。 \| 項目 \| 内容 \|。 |
| what_came_out | 寸法と時間のゲートを持つ、非接触の光学インスタレーションとして再構成した。 |
| what_is_not_settled | 会場条件、物理試作、歴史的参照の最終妥当性、日程と費用は人間の制作前レビュー前である。 |

### 採択内容と根拠

| 項目 | 内容 |
| --- | --- |
| 採択仮説 | PH001 |
| 仮説タイトル | 距離が境界を選ぶ — Distance Selects Boundary |
| 仮説 | Prototype a non-contact installation with a transparent 1800x2100mm surface, a 450mm stop line, at least four distorted line drawings, a 30-second warm-light cycle with a still interval of at least 10 seconds, a 1200mm access path, and no cameras, microphones, biometric data, or health claims. |
| 仮説状態 | ADOPTED |
| 選択状態 | PROVISIONAL |
| 選択権限 | AGENT |
| 人間承認要否 | いいえ |
| 選択理由 | Prototype a non-contact installation with a transparent 1800x2100mm surface, a 450mm stop line, at least four distorted line drawings, a 30-second warm-light cycle with a still interval of at least 10 seconds, a 1200mm access path, and no cameras, microphones, biometric data, or health claims. |
| 創作指針 | artifacts/creative-direction.md |

### 制作リファレンス

コンセプト、ビジュアル、制作手法の参照先です。URLは受理済みhandoffに含まれる恒久HTTPS URLだけを掲載し、アクセスできない参照や不足カテゴリはギャップとして残します。

| 分類 | 出所ID | 種別 | 概要 | アクセスURL | 状態 |
| --- | --- | --- | --- | --- | --- |
| コンセプト | DC001 | decision | Historical Project candidate P0006; evidence only, not current Production canonical. | <https://github.com/masa-san-jp/agentic-art-project> | AVAILABLE |
| 手法 | IN001 | insight | Historical metadata used to preserve provenance while regenerating the plan. | <https://github.com/masa-san-jp/agentic-art-project> | AVAILABLE |

### 要件と受入の目的

| 要件 | 優先度 | 要件内容 | 出所 | 受入テスト | 計画上の対応 |
| --- | --- | --- | --- | --- | --- |
| RQ001 | mandatory | Prototype a non-contact installation with a transparent 1800x2100mm surface, a 450mm stop line, at least four distorted line drawings, a 30-second warm-light cycle with a still interval of at least 10 seconds, a 1200mm access path, and no cameras, microphones, biometric data, or health claims. | 未設定 | AT001 | COVERED |

## 6. できている物

### ビジュアルパッケージ

boardとmockupは、受理済みhandoffから生成した閲覧用の決定論的fixtureです。外部画像素材の取得・採用、物理制作、外部検証、公開、購入、契約、Drive共有は実施していません。

| 種別 | 名称 | 状態 | 相対リンク | asset hash | 権利 | 安全 |
| --- | --- | --- | --- | --- | --- | --- |
| ビジュアルリファレンスボード | Visual reference board · Prototype a non-contact installation with a transparent 1800x2100mm surface, a 450mm stop line, at least four distorted  | BOARD | [03_plan/media/visual-reference-board.svg](media/visual-reference-board.svg) | sha256:57c04a7e55127d598ac79b4b928be78635580bed165ce48cb81f8e49201eb0c6 | PROJECT_INTERNAL | CLEAR |
| コンセプト・モックアップ | Concept mockup · Prototype a non-contact installation with a transparent 1800x2100mm surface, a 450mm stop line, at least four distorted  | MOCKUP | [03_plan/media/concept-mockup.svg](media/concept-mockup.svg) | sha256:96042ca5903f88e81b9638e7f13572eaa1a6671920962a42f9c3abe596069c92 | PROJECT_INTERNAL | REVIEW_REQUIRED |

| mockup注記 | 内容 |
| --- | --- |
| 表現種別 | CONCEPTUAL |
| 寸法 | Not to scale; physical dimensions are not supplied by the accepted handoff. |
| 素材 | Material selection remains provisional and is not a purchase or fabrication instruction. |
| 配置 | 幅1200mm以上の通路から面へ近づき、450mm停止線の手前で非接触に観察する位置。 |
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
| DL001 | production-deliverable | 距離が境界を選ぶ — Distance Selects Boundary | AT001 | production-owner-confirmation-required | MS002 | PLANNED |

## 8. 技術仕様・材料・資源

| 仕様 | 対象 | 目標 | 許容差 | 測定方法 | 出所要件 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| TS001 | requirement-RQ001 | kind=QUALITATIVE, statement=Prototype a non-contact installation with a transparent 1800x2100mm surface, a 450mm stop line, at least four distorted line drawings, a 30-second warm-light cycle with a still interval of at least 10 seconds, a 1200mm access path, and no cameras, microphones, biometric data, or health claims. | 未設定 | structured-plan-and-prototype-review | RQ001 | PROVISIONAL |

| 材料 | 仕様 | 数量 | 権利 | 安全 | 出所試作 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| MT001 | 450mm non-contact light boundary — Transparent polycarbonate 1800x2100mm, four or more original distorted line drawings, low-saturation pigment, warm light source with a 30-second timer, floor stop-line tape, and a 1200mm access layout. | value=1, unit=item | PROJECT_INTERNAL | REVIEW_REQUIRED | PP001 | CANDIDATE |

| 資源 | 種別 | 必要能力 | 数量 | 可用性 | 関連タスク |
| --- | --- | --- | --- | --- | --- |
| RS001 | PERSON_CAPABILITY | artist and venue-safety reviewer | value=1, unit=item | REQUIRES_CONFIRMATION | TK001 |

## 9. 工程と作業手順

| 作業パッケージ | 内容 | 投入物 | 制約 | 成果物 | タスク | 担当能力 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WP001 | PP001 | TS001 | なし | DL001 | TK001, TK002 | production-owner-confirmation-required | BLOCKED |

| タスク | 作業 | 前提 | 所要時間 | 必要材料 | 受入条件 | 効果種別 | 承認 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TK001 | Measure the non-contact light boundary | なし | value=1, unit=h | MT001 | PT001 | PHYSICAL_EXTERNAL | AR001 | BLOCKED |
| TK002 | Validate the regenerated plan references | TK001 | value=1, unit=h | WP001の投入物 | PT002 | READ_ONLY | なし | BACKLOG |

**実施順の読み方:** クリティカルパスは `TK001` → `TK002` です。READYタスクは なし です。物理・外部効果を伴うタスクは承認待ちです。

## 10. 試作・受入評価

| テスト | 対象要件 | 方法 | 合格条件 | 現在結果 |
| --- | --- | --- | --- | --- |
| AT001 | RQ001 | structured-plan-and-prototype-review | A safety reviewer measures the 450mm stop line and 1200mm path, observes a 30-second cycle including a 10-second still interval, and confirms no sensing or health claim is present. | NOT_RUN |

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
| RK001 | Handoff gap GP001 | The original accepted Production handoff for P0006 is unavailable; this is an explicitly regenerated recovery plan, not byte-identical recovery. | Resolve the handoff gap and regenerate the plan before relying on the affected decision. | MEDIUM | UNKNOWN | production-owner-confirmation-required | OPEN |

| ギャップ | 内容 | ブロッキング |
| --- | --- | --- |
| GP001 | The original accepted Production handoff for P0006 is unavailable; this is an explicitly regenerated recovery plan, not byte-identical recovery. | いいえ |
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
| handoff content hash | sha256:db231657a52046934f1dad7364470e47d00938f8349a488c1da8ca9adfd2e6ba |
| plan integrity hash | sha256:403470bb10cf9a6f956859106583d81ed22d700349c03efc17df5f0d2fb4af86 |
| source input hash | sha256:c7bf207074306fd2a0793db7e8640c941ad05028bdbca5f7d3412d022ab26aab |
| 生成アルゴリズム | production-plan-v1 |
| トレーサビリティID | HO0006, PH001, RQ001, AT001, PP001, GP001 |
| 依存グラフ | graph_id=DG001, nodes=TK001, TK002, edges=from=TK001, to=TK002, topological_order=TK001, TK002, trace_refs=HO0006, PH001, RQ001, AT001, PP001, GP001, DG001 |

### 受け渡し時の注意

ユーザーに渡す計画書はこの `03_plan/production-plan.md` 一つです。`production-plan.yaml`などの構造化ファイルと`agent-contexts/`は、検証・再生成・内部運用のためにGit外の制作projectへ保持されます。制作した物は §6 に、実行台帳へ記録済みのプレビュー画像だけを貼ります。完成作品の原寸データ、RAW、動画、音声、3D、大容量asset、credential、signed URLはこの計画書へ埋め込みません。
