# 統合制作計画書

> この文書は、受理済みhandoffと検証済みの制作計画を、人間が読んで制作判断・制作実務に使える一つの計画書へ統合したものです。計画の生成は、購入・契約・公開・連絡・削除・物理作業の実行承認を意味しません。

### 計画メタデータ

| 項目 | 内容 |
| --- | --- |
| プロジェクト | production/aak07-agent-20260910-p4 |
| 計画 | PL001 revision 1 |
| 計画状態 | PLANNING |
| 制作着手可否 | 着手不可 |
| 着手できない理由 | blocking_gaps |
| 生成日時 | 2026-09-09T17:40:42.523344+00:00 |
| handoff | HO003 revision 3 |
| 要件カバレッジ | 100% |
| クリティカルパス | `TK001` → `TK002` |


## 1. 完成像

| 項目 | 内容 |
| --- | --- |
| experience sequence / encounter | 入ってきた人は、等間隔に並んだ要素の列を端から順に目で追う。, 追ううちに一箇所だけ間隔が崩れている場所に行き当たる。, そこから先を見直すと、規則があったことに後から気づく。 |
| position | 鑑賞者は列の正面を、端から端まで2mの距離を保って歩く。 |
| first_seconds | 最初の数秒で、要素が一定の間隔で並んでいると分かる。 |
| after_30s | 30秒後には、間隔が一度だけ崩れている位置を見つけている。 |
| after_3min | 3分後には、規則があったと気づけたのは崩れた場所を見たからだと残る。 |

## 2. テーマ

| 項目 | 内容 |
| --- | --- |
| field | 反復の規則と、それが破れた一点 |
| stands_against | 反復は退屈であり、変化こそが見どころだという見方に対して立つ。 |
| difference | 中断を見どころとして提示するのではなく、中断に当たって初めて規則が知覚される順序を作る。 |
| why_now | 一定の並びを機械が無限に生成できるようになり、反復そのものは珍しさを失ったから。 |

## 3. メッセージ

| 項目 | 内容 |
| --- | --- |
| claim | 規則は、それが破れた瞬間にだけ知覚される。破れる前は背景であって、見えていない。 |
| who_disagrees | 規則性はそれ自体が読み取れるものであり、逸脱がなくても構造は伝わると考える設計者。 |
| denies | 反復を見れば規則が分かる、という前提を否定する。 |
| shown_not_told | 説明を読ませず、一箇所だけ間隔を崩し、そこに当たった鑑賞者が前を見直す動きで示す。 |

## 4. コンセプト

| 項目 | 内容 |
| --- | --- |
| mechanism | 要素を一定間隔で並べ、一箇所だけ間隔を変える。崩れた一点に当たるまで規則は背景に留まり、当たった瞬間に遡って規則として知覚される。中断は見どころではなく、規則を知覚可能にする装置である。 |
| without_the_technique | CEASES_TO_WORK |
| precedents | reference=prior-art/PA001, difference=先行作品は反復を視覚的な秩序として提示したが、ここでは秩序が読めるようになる瞬間そのものを鑑賞者の側に置く。 |
| self_repetition_risk | reference=self-repetition-review/SR001, assessment=反復という枠組みは過去の関心と重なるが、中心は反復の見せ方ではなく、規則が知覚される順序であり、そこは反復していない。 |

## 5. 調査の要約

| 項目 | 内容 |
| --- | --- |
| questions | 反復する間隔と、その中断は、鑑賞の記述の中でどう扱われてきたか。 |
| what_was_read | 同時代の批評と展示記録を一次資料で読んだ。 |
| what_came_out | 中断は逸脱としてではなく、規則を読み取り可能にする条件として記述されていた。 |
| what_is_not_settled | 実地の観察記録には当たっていない。 |

### 採択内容と根拠

| 項目 | 内容 |
| --- | --- |
| 採択仮説 | PH001 |
| 仮説タイトル | Interrupted interval installation |
| 仮説 | A single omission in a repeated structure becomes visible through viewer movement. |
| 仮説状態 | ADOPTED |
| 選択状態 | PROVISIONAL |
| 選択権限 | AGENT |
| 人間承認要否 | いいえ |
| 選択理由 | A single omission in a repeated structure becomes visible through viewer movement. |
| 創作指針 | 05_production/creative-direction.md |

### 制作リファレンス

コンセプト、ビジュアル、制作手法の参照先です。URLは受理済みhandoffに含まれる恒久HTTPS URLだけを掲載し、アクセスできない参照や不足カテゴリはギャップとして残します。

| 分類 | 出所ID | 種別 | 概要 | アクセスURL | 状態 |
| --- | --- | --- | --- | --- | --- |
| その他 | DC001 | decision | The two sources support a perceptual rule while the opposing hypothesis remains explicit. | URL未提供（gap参照） | MISSING |
| その他 | IN001 | insight | Repetition can carry the concept without explanatory text. | URL未提供（gap参照） | MISSING |
| コンセプト | EV001 | evidence | primary_public; rights_status=public-use; sensitivity=PUBLIC_CITABLE | <https://example.invalid/harmony/source-001> | AVAILABLE |
| ビジュアル | EV001 | evidence | primary_public; rights_status=public-use; sensitivity=PUBLIC_CITABLE | <https://example.invalid/harmony/source-001> | AVAILABLE |
| 手法 | EV002 | evidence | independent-secondary; rights_status=public-use; sensitivity=PUBLIC_CITABLE | <https://example.invalid/harmony/source-002> | AVAILABLE |

### 要件と受入の目的

| 要件 | 優先度 | 要件内容 | 出所 | 受入テスト | 計画上の対応 |
| --- | --- | --- | --- | --- | --- |
| RQ001 | mandatory | The prototype must make the repeated interval and one interruption observable. | 未設定 | AT001 | COVERED |

## 6. できている物

### ビジュアルパッケージ

boardとmockupは、受理済みhandoffから生成した閲覧用の決定論的fixtureです。外部画像素材の取得・採用、物理制作、外部検証、公開、購入、契約、Drive共有は実施していません。

| 種別 | 名称 | 状態 | 相対リンク | asset hash | 権利 | 安全 |
| --- | --- | --- | --- | --- | --- | --- |
| ビジュアルリファレンスボード | Visual reference board · A single omission in a repeated structure becomes visible through viewer movement. | BOARD | [03_plan/media/visual-reference-board.svg](media/visual-reference-board.svg) | sha256:6696ccd280f671db605c35c01d5625c2642294e16ad2f1d2351359b73d883997 | PROJECT_INTERNAL | CLEAR |
| コンセプト・モックアップ | Concept mockup · A single omission in a repeated structure becomes visible through viewer movement. | MOCKUP | [03_plan/media/concept-mockup.svg](media/concept-mockup.svg) | sha256:9c017f6910cf6032956a76ef3bf5dad7fdc7c57fa4649f6ff7714f83d52476be | PROJECT_INTERNAL | REVIEW_REQUIRED |

| mockup注記 | 内容 |
| --- | --- |
| 表現種別 | CONCEPTUAL |
| 寸法 | Not to scale; physical dimensions are not supplied by the accepted handoff. |
| 素材 | Material selection remains provisional and is not a purchase or fabrication instruction. |
| 配置 | 鑑賞者は列の正面を、端から端まで2mの距離を保って歩く。 |
| 検証 | PHYSICAL_EXTERNAL validation: NOT_RUN. No physical prototype, publication, purchase, contract, or Drive share was performed. |

まだ何も作っていない。この節は、制作した物が実行台帳（`05_execution/output-versions.yaml`）に記録された時点で、現物とプレビュー画像を載せる。

## 7. 制作範囲と成果物

| 項目 | 内容 |
| --- | --- |
| スコープ状態 | PROVISIONAL |
| 必須要件ID | RQ001 |
| 試作計画ID | PP001 |
| 前提 | なし |
| 除外・未許可範囲 | publish, submit, send, purchase, contract, delete |
| 権利制約 | なし |
| 安全制約 | なし |
| プライバシー制約 | なし |
| 再計画トリガー | new_evidence, material_change, rights_or_privacy_change |

| 成果物 | 種別 | 内容 | 受入テスト | 担当能力 | 納期 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| DL001 | production-deliverable | Interrupted interval installation | AT001 | physical-prototype-agent | MS002 | PLANNED |

## 8. 技術仕様・材料・資源

| 仕様 | 対象 | 目標 | 許容差 | 測定方法 | 出所要件 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| TS001 | visual-RQ001 | kind=QUALITATIVE, statement=The prototype must make the repeated interval and one interruption observable. | 未設定 | frame_review | RQ001 | PROVISIONAL |

該当なし。

該当なし。

## 9. 工程と作業手順

| 作業パッケージ | 内容 | 投入物 | 制約 | 成果物 | タスク | 担当能力 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WP001 | Observe a one-tenth scale model under fixed lighting from three viewpoints. | Twelve paper elements, Three fixed cameras | Do not record identifiable people | DL001 | TK001, TK002, TK004 | physical-prototype-agent | BLOCKED |

| タスク | 作業 | 前提 | 所要時間 | 必要材料 | 受入条件 | 効果種別 | 承認 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TK001 | Build the scale model | なし | value=1, unit=h | WP001の投入物 | Twelve positions with one omitted element are fixed. | PHYSICAL_EXTERNAL | AR001 | BLOCKED |
| TK002 | Record three viewpoints | TK001 | value=1, unit=h | WP001の投入物 | Three frames with identical exposure are available. | PHYSICAL_EXTERNAL | AR001 | BLOCKED |
| TK004 | Validate derived plan coverage | なし | value=15, unit=min | WP001の投入物 | The derived plan graph and mandatory requirement coverage are valid. | READ_ONLY | なし | READY |

**実施順の読み方:** クリティカルパスは `TK001` → `TK002` です。READYタスクは `TK004` です。物理・外部効果を伴うタスクは承認待ちです。

## 10. 試作・受入評価

| テスト | 対象要件 | 方法 | 合格条件 | 現在結果 |
| --- | --- | --- | --- | --- |
| AT001 | RQ001 | frame_review | The interval and interruption are identified in all three frames. | PASS |

| マイルストーン | 内容 | 順序 | 前提 | 状態 |
| --- | --- | --- | --- | --- |
| MS001 | Start Observe a one-tenth scale model under fixed lighting from three viewpoints. | 1 | なし | PLANNED |
| MS002 | Complete Observe a one-tenth scale model under fixed lighting from three viewpoints. | 2 | MS001 | BLOCKED |

## 11. 日程と予算

| 日程・予算項目 | 内容 |
| --- | --- |
| 日程モード | RELATIVE |
| 日程基準線 | PROVISIONAL |
| タスク日程 | task_id=TK001, duration=value=1, unit=h, start_at=未設定, due_at=未設定, task_id=TK002, duration=value=1, unit=h, start_at=未設定, due_at=未設定, task_id=TK004, duration=value=15, unit=min, start_at=未設定, due_at=未設定 |
| 日程ギャップ | Calendar dates and availability are not supplied by the accepted handoff; the schedule remains relative. |
| 通貨 | JPY |
| 予算総額 | 未設定 |
| 予備費 | 未設定 |
| 承認閾値 | 未設定 |
| 予算状態 | ESTIMATED |
| 予算ギャップ | No price, quote, supplier, reservation, or commitment is present in the accepted handoff. |

| 予算項目 | 区分 | 内容 | 金額 | 根拠 | 確度 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| BI001 | prototype-plan | Estimated cost band for PP001 | 未設定 | accepted handoff cost band: LOW | LOW | ESTIMATED |

## 12. リスクと未解決事項

| リスク | 内容 | 影響 | 軽減策 | 重要度 | 可能性 | 担当 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RK001 | The interruption may not be visible from all required viewpoints. | The interruption may not be visible from all required viewpoints. | Validate the uncertainty before relying on the affected plan decision. | MAJOR | UNKNOWN | physical-prototype-agent | OPEN |

| ギャップ | 内容 | ブロッキング |
| --- | --- | --- |
| PG001 | Budget amounts and commitments are not supplied by the accepted handoff. | いいえ |
| PG002 | Calendar dates and availability are not supplied by the accepted handoff; the schedule remains relative. | いいえ |
| PG003 | Task PT001 has no effect_type in the accepted handoff; confirm its external-effect classification before execution. | いいえ |
| PG004 | Task PT002 has no effect_type in the accepted handoff; confirm its external-effect classification before execution. | いいえ |
| PG005 | Prototype plan PP001 names its inputs but not their quantity, rights, or availability; confirm those before execution. | いいえ |
| PG007 | Reference DC001 has no access URL in the accepted handoff. | いいえ |
| PG009 | Reference IN001 has no access URL in the accepted handoff. | いいえ |
| PG010 | External-effect task TK001 remains blocked until the required human approval is recorded. | はい |
| PG011 | External-effect task TK002 remains blocked until the required human approval is recorded. | はい |

## 13. 承認・安全境界

| 承認ID | 対象行為 | 対象 | 対象hash | 権限者 | 状態 | 理由 | 関連タスク |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AR001 | PHYSICAL_EXTERNAL | 03_plan/task-plan.yaml#TK001,TK002 | sha256:d271ac7be772acc6c02e5719103965a2dd301694edaaa95faeaf34dc630b6bc6 | HUMAN | REQUIRED | Physical or external-effect tasks require explicit human approval before execution. | TK001, TK002 |

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
| handoff content hash | sha256:b203e5972c32d8ab3abfeaf2b0357f050e17e7c3089a17e19d05333604d2c5bf |
| plan integrity hash | sha256:a0ae476493b1a2522ee27956ec4003f5cd10aced2a301bb0f506e4e7c9bd6acc |
| source input hash | sha256:66a66e830735d89ca7ad7c998d40d6aeda4793c9c7b62522d4e97745e69b3f12 |
| 生成アルゴリズム | production-plan-v1 |
| トレーサビリティID | HO003, PH001, RQ001, AT001, PP001 |
| 依存グラフ | graph_id=DG001, nodes=TK001, TK002, TK004, edges=from=TK001, to=TK002, topological_order=TK001, TK004, TK002, trace_refs=HO003, PH001, RQ001, AT001, PP001, DG001 |

### 受け渡し時の注意

ユーザーに渡す計画書はこの `03_plan/production-plan.md` 一つです。`production-plan.yaml`などの構造化ファイルと`agent-contexts/`は、検証・再生成・内部運用のためにGit外の制作projectへ保持されます。制作した物は §6 に、実行台帳へ記録済みのプレビュー画像だけを貼ります。完成作品の原寸データ、RAW、動画、音声、3D、大容量asset、credential、signed URLはこの計画書へ埋め込みません。

## 制作を始めるための手順

内容検証: PLAN_READY
以下は提案です。試験・購入・設営は未実施で、外部操作の承認を含みません。

媒体: physical
制作環境: {'location': 'synthetic indoor bench'}

- dimensions: 300 × 300 mm test panel (PROPOSED) — Provider-directed synthetic proposal derived from accepted handoff; not an observed result
  確認: Compare the proposed fixture against the acceptance test before approving execution / 担当: synthetic operator / 条件: A safe local fixture and its references are available
- materials: Twelve paper elements from a synthetic local fixture; availability and rights must be confirmed before execution (PROPOSED) — Provider-directed synthetic proposal derived from accepted handoff; not an observed result
  確認: Compare the proposed fixture against the acceptance test before approving execution / 担当: synthetic operator / 条件: A safe local fixture and its references are available
- assembly: Fix twelve positions at equal intervals and omit exactly one element to create the interruption (PROPOSED) — Provider-directed synthetic proposal derived from accepted handoff; not an observed result
  確認: Compare the proposed fixture against the acceptance test before approving execution / 担当: synthetic operator / 条件: A safe local fixture and its references are available
- installation: Lay the one-tenth scale model flat on a stable indoor table under fixed lighting (PROPOSED) — Provider-directed synthetic proposal derived from accepted handoff; not an observed result
  確認: Compare the proposed fixture against the acceptance test before approving execution / 担当: synthetic operator / 条件: A safe local fixture and its references are available

### 最初の制作作業: TK001
Build the one-tenth scale model with twelve positions at equal intervals and omit one element; preserve the interruption for frame review.
担当: synthetic operator / 開始条件: Obtain the separate task approval and verify the safe workspace
必要な材料: なし / 資源: なし
要件: RQ001 / 仕様: dimensions, materials, assembly, installation
完了確認（未実施）: Twelve positions with one omitted element are fixed. Record evidence without claiming a pass.

### 制作作業: TK002
Record three fixed viewpoints with identical exposure from the specified viewing position.
担当: synthetic operator / 開始条件: Obtain the separate task approval and verify the safe workspace
必要な材料: なし / 資源: なし
要件: RQ001 / 仕様: dimensions, materials, assembly, installation
完了確認（未実施）: Three frames with identical exposure are available. Record evidence without claiming a pass.

### 未確定事項の確認
- PG001: Compare the proposed fixture against the acceptance test before approving execution / 担当: synthetic operator / 成立条件: A safe local fixture and its references are available
- PG002: Compare the proposed fixture against the acceptance test before approving execution / 担当: synthetic operator / 成立条件: A safe local fixture and its references are available
- PG003: Compare the proposed fixture against the acceptance test before approving execution / 担当: synthetic operator / 成立条件: A safe local fixture and its references are available
- PG004: Compare the proposed fixture against the acceptance test before approving execution / 担当: synthetic operator / 成立条件: A safe local fixture and its references are available
- PG005: Compare the proposed fixture against the acceptance test before approving execution / 担当: synthetic operator / 成立条件: A safe local fixture and its references are available
- PG007: Compare the proposed fixture against the acceptance test before approving execution / 担当: synthetic operator / 成立条件: A safe local fixture and its references are available
- PG009: Compare the proposed fixture against the acceptance test before approving execution / 担当: synthetic operator / 成立条件: A safe local fixture and its references are available

### 再利用する知識の条件

