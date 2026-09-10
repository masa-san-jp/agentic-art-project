# 統合制作計画書

> この文書は、受理済みhandoffと検証済みの制作計画を、人間が読んで制作判断・制作実務に使える一つの計画書へ統合したものです。計画の生成は、購入・契約・公開・連絡・削除・物理作業の実行承認を意味しません。

### 計画メタデータ

| 項目 | 内容 |
| --- | --- |
| プロジェクト | production/moving-gap |
| 計画 | PL001 revision 1 |
| 計画状態 | PLANNING |
| 制作着手可否 | 着手不可 |
| 着手できない理由 | blocking_gaps |
| 生成日時 | 2026-09-10T16:00:00+09:00 |
| handoff | HO0002 revision 1 |
| 要件カバレッジ | 100% |
| クリティカルパス | `TK001` → `TK002` |


## 1. 完成像

| 項目 | 内容 |
| --- | --- |
| experience sequence / encounter | 観客は、旧候補が残した中心命題を反復する空間的な手がかりとして見る。, 近づくほど、選択・空白・境界の関係が単純な距離ではないと気づく。, しばらく留まると、介入せずに状態の差を読み取る経験が残る。 |
| position | 観客が反復要素の手前から複数の視点で関係を比較できる位置。 |
| first_seconds | 最初の数秒で、規則性と一箇所のずれを知覚する。 |
| after_30s | 30秒後には、近さや反復が結果を保証しないことに気づく。 |
| after_3min | 3分後には、観客の位置と作品内の状態が経験を変えると残る。 |

## 2. テーマ

| 項目 | 内容 |
| --- | --- |
| field | 移動する空白 — Moving Gapにおける選択、空白、距離、境界 |
| stands_against | 作品の意味が単純な接近や説明だけで回収できるという見方に対して立つ。 |
| difference | 旧候補 P0002 の中心命題を、説明文の再掲ではなく、反復・ずれ・観客位置の観察可能な構造へ再構成する。 |
| why_now | 現在の鑑賞環境では、近接していても選択やアクセスの条件が異なるため、位置と状態の差を形式として確かめる必要がある。 |

## 3. メッセージ

| 項目 | 内容 |
| --- | --- |
| claim | 近さや選択は、それだけでは受領や介入の可能性を保証しない。 |
| who_disagrees | 距離を縮めれば誰でも同じ結果に到達できると考える立場。 |
| denies | 本作が実在の人物・制度・配送を代弁または再現するという読みを否定する。 |
| shown_not_told | 反復要素、ひとつの空き、見えるが届かない配置、時間によるずれで主張を示す。 |

## 4. コンセプト

| 項目 | 内容 |
| --- | --- |
| mechanism | 移動する空白 — Moving Gapの命題を、個人情報や外部サービスを使わないオリジナルの反復配置として構成し、観客の位置による見え方の差と一つの中断を同時に観察できるようにする。 |
| without_the_technique | CEASES_TO_WORK |
| precedents | reference=legacy/P0002/historical-plan, difference=歴史的候補の要約を無変換で再利用せず、現行Productionの構造化された制作判断と検証可能な工程へ置き換える。 |
| self_repetition_risk | reference=legacy-recovery/repetition-review, assessment=旧候補との主題的な近さは残るため、反復・空白・位置の具体的な差を試作時に確認する。 |

## 5. 調査の要約

| 項目 | 内容 |
| --- | --- |
| questions | 旧候補の中心命題を何が担っていたか。, その命題を外部効果なしにどの物理・視覚構造へ翻訳できるか。 |
| what_was_read | Projectの履歴commit P0002 の公開plan本文とmetadataを由来資料として読み、旧候補の主題と未確定事項を分離した。主要な旧記述は > `agentic-art-orchestration` が生成した制作計画を、公開対象のコンセプトと検証条件に限定して整理したものです。内部research、handoff、実行ログ、会話、認証情報は含めません。 異なる伝統のあいだにある交換を、薄い平面または枠の層、二方向の接近経路、局所的な隙間、停止点の組合せへ変換する。鑑賞者の位置が変わると関係の一部だけが現れ、接近しても正面から全体を掌握できない。。 |
| what_came_out | 旧候補を正本と称さず、由来を固定した再生成入力として、現行Productionの受入・安全・権利境界へ翻訳する方針になった。 |
| what_is_not_settled | 会場条件、物理試作、歴史的参照の最終妥当性、日程と費用は人間の制作前レビュー前である。 |

### 採択内容と根拠

| 項目 | 内容 |
| --- | --- |
| 採択仮説 | PH001 |
| 仮説タイトル | 移動する空白 — Moving Gap |
| 仮説 | Translate the central proposition of historical candidate P0002 into an observable, original arrangement without external effects or personal data. |
| 仮説状態 | ADOPTED |
| 選択状態 | PROVISIONAL |
| 選択権限 | AGENT |
| 人間承認要否 | いいえ |
| 選択理由 | Translate the central proposition of historical candidate P0002 into an observable, original arrangement without external effects or personal data. |
| 創作指針 | artifacts/creative-direction.md |

### 制作リファレンス

コンセプト、ビジュアル、制作手法の参照先です。URLは受理済みhandoffに含まれる恒久HTTPS URLだけを掲載し、アクセスできない参照や不足カテゴリはギャップとして残します。

| 分類 | 出所ID | 種別 | 概要 | アクセスURL | 状態 |
| --- | --- | --- | --- | --- | --- |
| コンセプト | DC001 | decision | Historical Project candidate P0002; evidence only, not current Production canonical. | <https://github.com/masa-san-jp/agentic-art-project> | AVAILABLE |
| 手法 | IN001 | insight | Historical metadata used to preserve provenance while regenerating the plan. | <https://github.com/masa-san-jp/agentic-art-project> | AVAILABLE |

### 要件と受入の目的

| 要件 | 優先度 | 要件内容 | 出所 | 受入テスト | 計画上の対応 |
| --- | --- | --- | --- | --- | --- |
| RQ001 | mandatory | Translate the central proposition of historical candidate P0002 into an observable, original arrangement without external effects or personal data. | 未設定 | AT001 | COVERED |

## 6. できている物

### ビジュアルパッケージ

boardとmockupは、受理済みhandoffから生成した閲覧用の決定論的fixtureです。外部画像素材の取得・採用、物理制作、外部検証、公開、購入、契約、Drive共有は実施していません。

| 種別 | 名称 | 状態 | 相対リンク | asset hash | 権利 | 安全 |
| --- | --- | --- | --- | --- | --- | --- |
| ビジュアルリファレンスボード | Visual reference board · Translate the central proposition of historical candidate P0002 into an observable, original arrangement without externa | BOARD | [03_plan/media/visual-reference-board.svg](media/visual-reference-board.svg) | sha256:e88bfa1b1dce41bf9ad358b25d0e4da266c326398a597885c47370246b7f1c48 | PROJECT_INTERNAL | CLEAR |
| コンセプト・モックアップ | Concept mockup · Translate the central proposition of historical candidate P0002 into an observable, original arrangement without externa | MOCKUP | [03_plan/media/concept-mockup.svg](media/concept-mockup.svg) | sha256:99040edf1246b77820c25fb854dc4e73d52cc0f468bf1387f2c87ed1638f0b14 | PROJECT_INTERNAL | REVIEW_REQUIRED |

| mockup注記 | 内容 |
| --- | --- |
| 表現種別 | CONCEPTUAL |
| 寸法 | Not to scale; physical dimensions are not supplied by the accepted handoff. |
| 素材 | Material selection remains provisional and is not a purchase or fabrication instruction. |
| 配置 | 観客が反復要素の手前から複数の視点で関係を比較できる位置。 |
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
| DL001 | production-deliverable | 移動する空白 — Moving Gap | AT001 | production-owner-confirmation-required | MS002 | PLANNED |

## 8. 技術仕様・材料・資源

| 仕様 | 対象 | 目標 | 許容差 | 測定方法 | 出所要件 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| TS001 | requirement-RQ001 | kind=QUALITATIVE, statement=Translate the central proposition of historical candidate P0002 into an observable, original arrangement without external effects or personal data. | 未設定 | structured-plan-and-prototype-review | RQ001 | PROVISIONAL |

| 材料 | 仕様 | 数量 | 権利 | 安全 | 出所試作 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| MT001 | original non-sensitive prototype material — No personal data, real shipment, or reused image. | value=1, unit=item | PROJECT_INTERNAL | REVIEW_REQUIRED | PP001 | CANDIDATE |

| 資源 | 種別 | 必要能力 | 数量 | 可用性 | 関連タスク |
| --- | --- | --- | --- | --- | --- |
| RS001 | PERSON_CAPABILITY | artist and venue-safety reviewer | value=1, unit=item | REQUIRES_CONFIRMATION | TK001 |

## 9. 工程と作業手順

| 作業パッケージ | 内容 | 投入物 | 制約 | 成果物 | タスク | 担当能力 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WP001 | PP001 | TS001 | なし | DL001 | TK001, TK002 | production-owner-confirmation-required | BLOCKED |

| タスク | 作業 | 前提 | 所要時間 | 必要材料 | 受入条件 | 効果種別 | 承認 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TK001 | Construct and inspect the recovery prototype | なし | value=1, unit=h | MT001 | PT001 | PHYSICAL_EXTERNAL | AR001 | BLOCKED |
| TK002 | Validate the regenerated plan references | TK001 | value=1, unit=h | WP001の投入物 | PT002 | READ_ONLY | なし | BACKLOG |

**実施順の読み方:** クリティカルパスは `TK001` → `TK002` です。READYタスクは なし です。物理・外部効果を伴うタスクは承認待ちです。

## 10. 試作・受入評価

| テスト | 対象要件 | 方法 | 合格条件 | 現在結果 |
| --- | --- | --- | --- | --- |
| AT001 | RQ001 | structured-plan-and-prototype-review | The regenerated plan states the proposition, its observable arrangement, and the required human safety/rights checks. | NOT_RUN |

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
| RK001 | Handoff gap GP001 | The original accepted Production handoff for P0002 is unavailable; this is an explicitly regenerated recovery plan, not byte-identical recovery. | Resolve the handoff gap and regenerate the plan before relying on the affected decision. | MEDIUM | UNKNOWN | production-owner-confirmation-required | OPEN |

| ギャップ | 内容 | ブロッキング |
| --- | --- | --- |
| GP001 | The original accepted Production handoff for P0002 is unavailable; this is an explicitly regenerated recovery plan, not byte-identical recovery. | いいえ |
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
| handoff content hash | sha256:2af3d0bda6015dc7c5a942020d57e024af0e32efa3201949a14fd69a9f9774dd |
| plan integrity hash | sha256:3955ff6507e05a4bdc2d5d5c0d8d0d257e5f3d9c00ff5c074921e1267cc5735e |
| source input hash | sha256:8643463b4b33817307c45dd1682e4d3265c13d1e08af753b2f40ddb5fa52f631 |
| 生成アルゴリズム | production-plan-v1 |
| トレーサビリティID | HO0002, PH001, RQ001, AT001, PP001, GP001 |
| 依存グラフ | graph_id=DG001, nodes=TK001, TK002, edges=from=TK001, to=TK002, topological_order=TK001, TK002, trace_refs=HO0002, PH001, RQ001, AT001, PP001, GP001, DG001 |

### 受け渡し時の注意

ユーザーに渡す計画書はこの `03_plan/production-plan.md` 一つです。`production-plan.yaml`などの構造化ファイルと`agent-contexts/`は、検証・再生成・内部運用のためにGit外の制作projectへ保持されます。制作した物は §6 に、実行台帳へ記録済みのプレビュー画像だけを貼ります。完成作品の原寸データ、RAW、動画、音声、3D、大容量asset、credential、signed URLはこの計画書へ埋め込みません。
