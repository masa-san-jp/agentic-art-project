# 統合制作計画書

> この文書は、受理済みhandoffと検証済みの制作計画を、人間が読んで制作判断・制作実務に使える一つの計画書へ統合したものです。計画の生成は、購入・契約・公開・連絡・削除・物理作業の実行承認を意味しません。

### 計画メタデータ

| 項目 | 内容 |
| --- | --- |
| プロジェクト | production/close-but-cannot-reach |
| 計画 | PL001 revision 1 |
| 計画状態 | PLANNING |
| 制作着手可否 | 着手不可 |
| 着手できない理由 | blocking_gaps |
| 生成日時 | 2026-09-10T16:00:00+09:00 |
| handoff | HO0005 revision 1 |
| 要件カバレッジ | 100% |
| クリティカルパス | `TK001` → `TK002` |


## 1. 完成像

| 項目 | 内容 |
| --- | --- |
| experience sequence / encounter | 遠くに匿名の人影または抽象像が見え、観客はその前に置かれた枠へ近づく。, 近づくほど、枠や窓が描かれた側ではなく観客側に属していると分かる。, 相手側には梯子・階段・ロープ・到達目標がなく、近さだけでは届かない配置が残る。 |
| position | 枠の手前で、枠を通して像を見る位置と、枠の構造自体を見る位置の両方。 |
| first_seconds | 像と枠の距離が見えるが、枠の所有側はすぐには確定しない。 |
| after_30s | 枠を越える方法ではなく、観客の立場が届かなさを作っていると気づく。 |
| after_3min | 自分の身体位置が作品の構成要素であり、相手の物語を所有していないと理解できる。 |

## 2. テーマ

| 項目 | 内容 |
| --- | --- |
| field | 観客側に置かれた枠がつくる、近いのに届かない関係 |
| stands_against | 届かなさを距離の不足や努力不足として扱い、相手側に到達用の装置や物語を置く表現。 |
| difference | 枠/窓を観客側へ置き、相手側には到達目標を置かず、身体位置と視界の関係だけで不達を構成する。 |
| why_now | 画像や他者を見られることと、その他者へアクセスできることが混同されやすいため、見る側の立場を可視化する。 |

## 3. メッセージ

| 項目 | 内容 |
| --- | --- |
| claim | 届かないのは距離だけの問題ではなく、誰が枠を持ち、誰を見ているかの問題である。 |
| who_disagrees | 努力して近づけば、見る側は相手へ到達できると考える立場。 |
| denies | 描かれた人物の同定、借用画像の内容、相手側にある梯子や目標による物語の誘導。 |
| shown_not_told | 観客側の枠、匿名像、空の向こう側、位置による遮蔽で示す。 |

## 4. コンセプト

| 項目 | 内容 |
| --- | --- |
| mechanism | 匿名の遠景像の手前に観客側の物理フレーム/窓を置き、像へ近づくほどフレームの縁と自分の位置が視界を占めるようにする。 |
| without_the_technique | CEASES_TO_WORK |
| precedents | reference=legacy/P0005/historical-plan, difference=歴史的候補の固有条件を由来として保持し、現行Productionの構造化された制作判断と検証可能な工程へ置き換える。 |
| self_repetition_risk | reference=legacy-recovery/repetition-review, assessment=他候補の停止線やセル配置を避け、観客側の枠の所有と匿名性を盲検で確認する。 |

## 5. 調査の要約

| 項目 | 内容 |
| --- | --- |
| questions | 枠を観客側に置いたとき、届かなさを距離以外の関係として読めるか。, 像の匿名性と盲検レビューで、他者の同定や借用内容への依存を避けられるか。 |
| what_was_read | Projectの履歴commit P0005 の公開plan本文とmetadataを由来資料として読み、旧候補の主題と未確定事項を分離した。固有条件は 旧本文の遠景像、観客側に属する枠、相手側に梯子等を置かない条件、身体位置の一部化、盲検と借用画像禁止を抽出した。 主要な旧記述は > `agentic-art-orchestration` が生成した制作プランの公開用要約です。参照元にある個人原資料、内部ログ、Google Docs参照、生成画像、会話本文は収録していません。 見る人は、まず遠くにいる一人の人物に目を向ける。次に、自分が窓の内側に立っていることに気づく。窓枠は描かれた背景ではなく、見る側の空間にある。手は伸ばしていない。それでも届かないと分かる。。 |
| what_came_out | 到達装置を置かず、観客側の枠と匿名像の関係を中心に据えた。 |
| what_is_not_settled | 会場条件、物理試作、歴史的参照の最終妥当性、日程と費用は人間の制作前レビュー前である。 |

### 採択内容と根拠

| 項目 | 内容 |
| --- | --- |
| 採択仮説 | PH001 |
| 仮説タイトル | 近いが届かない — Close but Cannot Reach |
| 仮説 | Construct a viewer-side frame or window in front of an anonymous distant figure or abstract image so that the figure remains near but unreachable because of the viewing position; no ladder, stairs, rope, goal, identifying person, or borrowed image content may be used. |
| 仮説状態 | ADOPTED |
| 選択状態 | PROVISIONAL |
| 選択権限 | AGENT |
| 人間承認要否 | いいえ |
| 選択理由 | Construct a viewer-side frame or window in front of an anonymous distant figure or abstract image so that the figure remains near but unreachable because of the viewing position; no ladder, stairs, rope, goal, identifying person, or borrowed image content may be used. |
| 創作指針 | artifacts/creative-direction.md |

### 制作リファレンス

コンセプト、ビジュアル、制作手法の参照先です。URLは受理済みhandoffに含まれる恒久HTTPS URLだけを掲載し、アクセスできない参照や不足カテゴリはギャップとして残します。

| 分類 | 出所ID | 種別 | 概要 | アクセスURL | 状態 |
| --- | --- | --- | --- | --- | --- |
| コンセプト | DC001 | decision | Historical Project candidate P0005; evidence only, not current Production canonical. | <https://github.com/masa-san-jp/agentic-art-project> | AVAILABLE |
| 手法 | IN001 | insight | Historical metadata used to preserve provenance while regenerating the plan. | <https://github.com/masa-san-jp/agentic-art-project> | AVAILABLE |

### 要件と受入の目的

| 要件 | 優先度 | 要件内容 | 出所 | 受入テスト | 計画上の対応 |
| --- | --- | --- | --- | --- | --- |
| RQ001 | mandatory | Construct a viewer-side frame or window in front of an anonymous distant figure or abstract image so that the figure remains near but unreachable because of the viewing position; no ladder, stairs, rope, goal, identifying person, or borrowed image content may be used. | 未設定 | AT001 | COVERED |

## 6. できている物

### ビジュアルパッケージ

boardとmockupは、受理済みhandoffから生成した閲覧用の決定論的fixtureです。外部画像素材の取得・採用、物理制作、外部検証、公開、購入、契約、Drive共有は実施していません。

| 種別 | 名称 | 状態 | 相対リンク | asset hash | 権利 | 安全 |
| --- | --- | --- | --- | --- | --- | --- |
| ビジュアルリファレンスボード | Visual reference board · Construct a viewer-side frame or window in front of an anonymous distant figure or abstract image so that the figure rem | BOARD | [03_plan/media/visual-reference-board.svg](media/visual-reference-board.svg) | sha256:648d20984aa3d53232e182786c2d4d618f4da697f133799c36f636380065352a | PROJECT_INTERNAL | CLEAR |
| コンセプト・モックアップ | Concept mockup · Construct a viewer-side frame or window in front of an anonymous distant figure or abstract image so that the figure rem | MOCKUP | [03_plan/media/concept-mockup.svg](media/concept-mockup.svg) | sha256:37f68fa0ae7e6e8dad088daa9b03e04d19ef5557a944a9c539d56420ad0724cc | PROJECT_INTERNAL | REVIEW_REQUIRED |

| mockup注記 | 内容 |
| --- | --- |
| 表現種別 | CONCEPTUAL |
| 寸法 | Not to scale; physical dimensions are not supplied by the accepted handoff. |
| 素材 | Material selection remains provisional and is not a purchase or fabrication instruction. |
| 配置 | 枠の手前で、枠を通して像を見る位置と、枠の構造自体を見る位置の両方。 |
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
| DL001 | production-deliverable | 近いが届かない — Close but Cannot Reach | AT001 | production-owner-confirmation-required | MS002 | PLANNED |

## 8. 技術仕様・材料・資源

| 仕様 | 対象 | 目標 | 許容差 | 測定方法 | 出所要件 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| TS001 | requirement-RQ001 | kind=QUALITATIVE, statement=Construct a viewer-side frame or window in front of an anonymous distant figure or abstract image so that the figure remains near but unreachable because of the viewing position; no ladder, stairs, rope, goal, identifying person, or borrowed image content may be used. | 未設定 | structured-plan-and-prototype-review | RQ001 | PROVISIONAL |

| 材料 | 仕様 | 数量 | 権利 | 安全 | 出所試作 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| MT001 | Viewer-side frame study — Original anonymous silhouette or abstract image, a rigid frame/window mounted on the viewer side, neutral backing, and position markers; no identifying person or borrowed image. | value=1, unit=item | PROJECT_INTERNAL | REVIEW_REQUIRED | PP001 | CANDIDATE |

| 資源 | 種別 | 必要能力 | 数量 | 可用性 | 関連タスク |
| --- | --- | --- | --- | --- | --- |
| RS001 | PERSON_CAPABILITY | artist and venue-safety reviewer | value=1, unit=item | REQUIRES_CONFIRMATION | TK001 |

## 9. 工程と作業手順

| 作業パッケージ | 内容 | 投入物 | 制約 | 成果物 | タスク | 担当能力 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WP001 | PP001 | TS001 | なし | DL001 | TK001, TK002 | production-owner-confirmation-required | BLOCKED |

| タスク | 作業 | 前提 | 所要時間 | 必要材料 | 受入条件 | 効果種別 | 承認 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TK001 | Blind-review the ownership of the frame | なし | value=1, unit=h | MT001 | PT001 | PHYSICAL_EXTERNAL | AR001 | BLOCKED |
| TK002 | Validate the regenerated plan references | TK001 | value=1, unit=h | WP001の投入物 | PT002 | READ_ONLY | なし | BACKLOG |

**実施順の読み方:** クリティカルパスは `TK001` → `TK002` です。READYタスクは なし です。物理・外部効果を伴うタスクは承認待ちです。

## 10. 試作・受入評価

| テスト | 対象要件 | 方法 | 合格条件 | 現在結果 |
| --- | --- | --- | --- | --- |
| AT001 | RQ001 | structured-plan-and-prototype-review | Blind reviewers locate the frame on the viewer side and describe the unreachable relation without inventing an access device or identifying the depicted figure. | NOT_RUN |

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
| RK001 | Handoff gap GP001 | The original accepted Production handoff for P0005 is unavailable; this is an explicitly regenerated recovery plan, not byte-identical recovery. | Resolve the handoff gap and regenerate the plan before relying on the affected decision. | MEDIUM | UNKNOWN | production-owner-confirmation-required | OPEN |

| ギャップ | 内容 | ブロッキング |
| --- | --- | --- |
| GP001 | The original accepted Production handoff for P0005 is unavailable; this is an explicitly regenerated recovery plan, not byte-identical recovery. | いいえ |
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
| handoff content hash | sha256:558f0eb6883919caff416d64f7d8928b71e6fa4dd3c697d3b100cd94fcf81f4b |
| plan integrity hash | sha256:c97120a660caef21e461f075d8c23373b8cead11060d3dff03bfd602c18716f8 |
| source input hash | sha256:b3cd8536ad6981699efb5a9403dd9c81ec247425d7d746b59142c3164f941db7 |
| 生成アルゴリズム | production-plan-v1 |
| トレーサビリティID | HO0005, PH001, RQ001, AT001, PP001, GP001 |
| 依存グラフ | graph_id=DG001, nodes=TK001, TK002, edges=from=TK001, to=TK002, topological_order=TK001, TK002, trace_refs=HO0005, PH001, RQ001, AT001, PP001, GP001, DG001 |

### 受け渡し時の注意

ユーザーに渡す計画書はこの `03_plan/production-plan.md` 一つです。`production-plan.yaml`などの構造化ファイルと`agent-contexts/`は、検証・再生成・内部運用のためにGit外の制作projectへ保持されます。制作した物は §6 に、実行台帳へ記録済みのプレビュー画像だけを貼ります。完成作品の原寸データ、RAW、動画、音声、3D、大容量asset、credential、signed URLはこの計画書へ埋め込みません。
