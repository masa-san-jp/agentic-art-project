# 統合制作計画書

> この文書は、受理済みhandoffと検証済みの制作計画を、人間が読んで制作判断・制作実務に使える一つの計画書へ統合したものです。計画の生成は、購入・契約・公開・連絡・削除・物理作業の実行承認を意味しません。

### 計画メタデータ

| 項目 | 内容 |
| --- | --- |
| プロジェクト | production/attestation |
| 計画 | PL001 revision 1 |
| 計画状態 | PLANNING |
| 制作着手可否 | 着手不可 |
| 着手できない理由 | blocking_gaps |
| 生成日時 | 2026-08-11T21:00:00+09:00 |
| handoff | HO001 revision 1 |
| 要件カバレッジ | 100% |
| クリティカルパス | `TK001` → `TK002` |


## 1. 完成像

| 項目 | 内容 |
| --- | --- |
| experience sequence / encounter | 入場者は反復要素の間を歩き、最初の視覚的な規則性を見つける。, 立つ位置を変えると、同じ要素の間隔が届かなさとして知覚される。, しばらく留まると、自分の位置が経験の結果を変えていたと気づく。 |
| position | 入場者は要素列の手前から中央まで歩き、各列から1メートル以上離れて立つ。 |
| first_seconds | 最初の3秒で反復要素の規則性と、その奥にある視線の遮断を知覚する。 |
| after_30s | 30秒後には、距離を詰めても届く対象が現れないことに気づく。 |
| after_3min | 3分後には、届かなさが物理距離ではなく自分の立場によって作られたと残る。 |

## 2. テーマ

| 項目 | 内容 |
| --- | --- |
| field | 鑑賞者の位置と制度的な距離 |
| stands_against | 作品への接近を、観客が自由に選べる単純な物理移動として扱う展示言説に対して立つ。 |
| difference | 距離の不足を主題として語るのではなく、反復要素と観客の位置の関係を変化させて、立場の差そのものを経験させる。 |
| why_now | 公共空間とオンライン空間の双方で、近接していてもアクセスできない立場の差が可視化されている現在だから。 |

## 3. メッセージ

| 項目 | 内容 |
| --- | --- |
| claim | 届かないのは距離が足りないからではなく、見る人が置かれた立場が接近の可能性を先に決めているからである。 |
| who_disagrees | 作品への接近は本人の意志と移動だけで決まり、制度や立場は鑑賞経験を左右しないと考える観客や展示設計者。 |
| denies | 鑑賞者の自由な移動だけで、作品へのアクセスが平等に成立するという前提を否定する。 |
| shown_not_told | 反復要素の隙間、遮られた視線、立つ位置による見え方の差で、説明文を読ませずに主張を経験させる。 |

## 4. コンセプト

| 項目 | 内容 |
| --- | --- |
| mechanism | 反復する要素を一定の規則で並べながら、鑑賞者の立ち位置によって隙間の連続性が崩れるようにする。形式上の反復と経験上の断絶が同時に立ち上がり、メッセージの立場差を身体的な判断へ変換する。 |
| without_the_technique | CEASES_TO_WORK |
| precedents | reference=prior-art/PP001, difference=先行作品が反復を視覚的な秩序として提示したのに対し、本計画は観客の位置で秩序が届かなさへ変わる点が異なる。 |
| self_repetition_risk | reference=self-repetition-review/SR001, assessment=反復と遮断は既存の関心に接続するが、観客の位置を原因として明示する構造は新しい。既視感が出る場合は位置と隙間の関係を再検討する。 |

## 5. 調査の要約

| 項目 | 内容 |
| --- | --- |
| questions | 反復要素の間隔と鑑賞者の位置の関係はどう記述されてきたか。 |
| what_was_read | 同時代の批評と展示記録を一次資料で読んだ。 |
| what_came_out | 距離の不足は物理量ではなく立場の差として記述されていた。 |
| what_is_not_settled | 実地の観察記録には当たっていない。 |

### 採択内容と根拠

| 項目 | 内容 |
| --- | --- |
| 採択仮説 | PH001 |
| 仮説タイトル | Minimal synthetic hypothesis |
| 仮説 | A repeated element remains observable. |
| 仮説状態 | ADOPTED |
| 選択状態 | HUMAN_SELECTED |
| 選択権限 | HUMAN |
| 人間承認要否 | いいえ |
| 選択理由 | A repeated element remains observable. |
| 創作指針 | artifacts/creative-direction.md |

### 制作リファレンス

コンセプト、ビジュアル、制作手法の参照先です。URLは受理済みhandoffに含まれる恒久HTTPS URLだけを掲載し、アクセスできない参照や不足カテゴリはギャップとして残します。

| 分類 | 出所ID | 種別 | 概要 | アクセスURL | 状態 |
| --- | --- | --- | --- | --- | --- |
| コンセプト | DC001 | decision | Synthetic decision fixture. | <https://example.com/references/concept> | AVAILABLE |
| ビジュアル | IN001 | insight | Synthetic insight fixture. | <https://example.com/references/visual-method> | AVAILABLE |
| 手法 | IN001 | insight | Synthetic insight fixture. | <https://example.com/references/visual-method> | AVAILABLE |

### 要件と受入の目的

| 要件 | 優先度 | 要件内容 | 出所 | 受入テスト | 計画上の対応 |
| --- | --- | --- | --- | --- | --- |
| RQ001 | mandatory | Keep the repeated element spacing observable. | 未設定 | AT001 | COVERED |

## 6. できている物

### ビジュアルパッケージ

boardとmockupは、受理済みhandoffから生成した閲覧用の決定論的fixtureです。外部画像素材の取得・採用、物理制作、外部検証、公開、購入、契約、Drive共有は実施していません。

| 種別 | 名称 | 状態 | 相対リンク | asset hash | 権利 | 安全 |
| --- | --- | --- | --- | --- | --- | --- |
| ビジュアルリファレンスボード | Visual reference board · A repeated element remains observable. | BOARD | [03_plan/media/visual-reference-board.svg](media/visual-reference-board.svg) | sha256:7a8c08c37ed9fabfc4c8bc87c255eca4ebc85fe73c2caa4b66e466d16a8561d6 | PROJECT_INTERNAL | CLEAR |
| コンセプト・モックアップ | Concept mockup · A repeated element remains observable. | MOCKUP | [03_plan/media/concept-mockup.svg](media/concept-mockup.svg) | sha256:7976cc2f8c49080bab995f8fb1706f8f157a0bd3e23f73e27bdaefbf6d5bcc8d | PROJECT_INTERNAL | REVIEW_REQUIRED |

| mockup注記 | 内容 |
| --- | --- |
| 表現種別 | CONCEPTUAL |
| 寸法 | Not to scale; physical dimensions are not supplied by the accepted handoff. |
| 素材 | Material selection remains provisional and is not a purchase or fabrication instruction. |
| 配置 | 入場者は要素列の手前から中央まで歩き、各列から1メートル以上離れて立つ。 |
| 検証 | PHYSICAL_EXTERNAL validation: NOT_RUN. No physical prototype, publication, purchase, contract, or Drive share was performed. |

まだ何も作っていない。この節は、制作した物が実行台帳（`05_execution/output-versions.yaml`）に記録された時点で、現物とプレビュー画像を載せる。

## 7. 制作範囲と成果物

| 項目 | 内容 |
| --- | --- |
| スコープ状態 | BASELINED |
| 必須要件ID | RQ001 |
| 試作計画ID | PP001 |
| 前提 | なし |
| 除外・未許可範囲 | Do not purchase, contract, publish, or perform physical work automatically. |
| 権利制約 | なし |
| 安全制約 | Use synthetic fixture data only. |
| プライバシー制約 | なし |
| 再計画トリガー | venue_changed |

| 成果物 | 種別 | 内容 | 受入テスト | 担当能力 | 納期 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| DL001 | production-deliverable | Minimal synthetic hypothesis | AT001 | production-planner | MS002 | PLANNED |

## 8. 技術仕様・材料・資源

| 仕様 | 対象 | 目標 | 許容差 | 測定方法 | 出所要件 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| TS001 | requirement-RQ001 | kind=QUALITATIVE, statement=Keep the repeated element spacing observable. | 未設定 | fixture-field-review | RQ001 | PROVISIONAL |

該当なし。

該当なし。

## 9. 工程と作業手順

| 作業パッケージ | 内容 | 投入物 | 制約 | 成果物 | タスク | 担当能力 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WP001 | Inspect the synthetic fixture output against the acceptance test. | Synthetic fixture data | Do not perform physical work automatically. | DL001 | TK001, TK002, TK004 | production-planner | BLOCKED |

| タスク | 作業 | 前提 | 所要時間 | 必要材料 | 受入条件 | 効果種別 | 承認 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TK001 | Prepare the derived production check | なし | value=1, unit=h | WP001の投入物 | The derived production check is prepared. | PHYSICAL_EXTERNAL | AR001 | BLOCKED |
| TK002 | Review the derived production check | TK001 | value=1, unit=h | WP001の投入物 | The derived production check is reviewed. | PHYSICAL_EXTERNAL | AR001 | BLOCKED |
| TK004 | Validate derived plan coverage | なし | value=15, unit=min | WP001の投入物 | The derived plan graph and mandatory requirement coverage are valid. | READ_ONLY | なし | READY |

**実施順の読み方:** クリティカルパスは `TK001` → `TK002` です。READYタスクは `TK004` です。物理・外部効果を伴うタスクは承認待ちです。

## 10. 試作・受入評価

| テスト | 対象要件 | 方法 | 合格条件 | 現在結果 |
| --- | --- | --- | --- | --- |
| AT001 | RQ001 | fixture-field-review | The required field is present. | NOT_RUN |

| マイルストーン | 内容 | 順序 | 前提 | 状態 |
| --- | --- | --- | --- | --- |
| MS001 | Start Inspect the synthetic fixture output against the acceptance test. | 1 | なし | PLANNED |
| MS002 | Complete Inspect the synthetic fixture output against the acceptance test. | 2 | MS001 | BLOCKED |

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

該当なし。

| ギャップ | 内容 | ブロッキング |
| --- | --- | --- |
| PG001 | Budget amounts and commitments are not supplied by the accepted handoff. | いいえ |
| PG002 | Calendar dates and availability are not supplied by the accepted handoff; the schedule remains relative. | いいえ |
| PG003 | Task PT001 has no effect_type in the accepted handoff; confirm its external-effect classification before execution. | いいえ |
| PG004 | Task PT002 has no effect_type in the accepted handoff; confirm its external-effect classification before execution. | いいえ |
| PG005 | Prototype plan PP001 names its inputs but not their quantity, rights, or availability; confirm those before execution. | いいえ |
| PG006 | External-effect task TK001 remains blocked until the required human approval is recorded. | はい |
| PG007 | External-effect task TK002 remains blocked until the required human approval is recorded. | はい |

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
| handoff content hash | sha256:268ad173adfa9ba13e3c76e10e3ac3171341196c4ad1756f45c12db45e9d98fa |
| plan integrity hash | sha256:4d998a0f58ffd298ea71f7c5dcd8a399dd97fd5121b9499a0b49f80921451314 |
| source input hash | sha256:d837796c08f236c5adf18d60e879b6fe9fdc34cfc644aa6ede1d8cb7286c29d4 |
| 生成アルゴリズム | production-plan-v1 |
| トレーサビリティID | HO001, PH001, RQ001, AT001, PP001 |
| 依存グラフ | graph_id=DG001, nodes=TK001, TK002, TK004, edges=from=TK001, to=TK002, topological_order=TK001, TK004, TK002, trace_refs=HO001, PH001, RQ001, AT001, PP001, DG001 |

### 受け渡し時の注意

ユーザーに渡す計画書はこの `03_plan/production-plan.md` 一つです。`production-plan.yaml`などの構造化ファイルと`agent-contexts/`は、検証・再生成・内部運用のためにGit外の制作projectへ保持されます。制作した物は §6 に、実行台帳へ記録済みのプレビュー画像だけを貼ります。完成作品の原寸データ、RAW、動画、音声、3D、大容量asset、credential、signed URLはこの計画書へ埋め込みません。
