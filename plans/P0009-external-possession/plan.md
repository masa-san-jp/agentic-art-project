# 統合制作計画書

> この文書は、受理済みhandoffと検証済みの制作計画を、人間が読んで制作判断・制作実務に使える一つの計画書へ統合したものです。計画の生成は、購入・契約・公開・連絡・削除・物理作業の実行承認を意味しません。

### 計画メタデータ

| 項目 | 内容 |
| --- | --- |
| プロジェクト | production/external-possession-v1 |
| 計画 | PL001 revision 1 |
| 計画状態 | PLANNING |
| 制作着手可否 | 着手不可 |
| 着手できない理由 | awaiting_physical_execution_authorization |
| 生成日時 | 2026-09-19T17:25:00+09:00 |
| handoff | HO008 revision 1 |
| 要件カバレッジ | 100% |
| クリティカルパス | `TK101` → `TK102` → `TK103` → `TK105` → `TK106` |


## 1. 完成像

| 項目 | 内容 |
| --- | --- |
| experience sequence / encounter | 遠くから白黒の長大な巻紙が見え、画面の半分だけが緻密に埋まり後半分が白紙である異様な非対称に気づく, 近づくにつれて極小の活字コードと墨の肉筆線が並走していることが分かり、中央の特異点でコードがHALTして筆跡が途絶えている事実を行き当たる, 手を伸ばせる距離まで来ても、停止点以降の空間には一切の線が存在しない |
| position | 壁面から3メートル前後の位置と、顔を近づけられる30センチの位置の二か所を鑑賞者が自分で往復する |
| first_seconds | 最初の数秒は、画面左半分に水平な黒い帯が走り、右半分が巨大な空白であることだけが分かる |
| after_30s | 30秒ほどで、文字と筆跡が対になって進んでいたものが、コードの強制終了指示とともに途絶えている構造に気づく |
| after_3min | 3分ほどで、人間が自発的に描くのをやめたのではなく、外部の自律エージェントの停止条件によって作家の身体的行為が凍結されたこと、そして空白部分こそが機械と人間の間に生じた「間」であることを理解する |


## 2. テーマ

| 項目 | 内容 |
| --- | --- |
| field | 外部化された霊感と、機械の自律的停止による余白の創出 |
| stands_against | 生成AIは人間の創造性を拡張する便利なコパイロットであるという前提、および余白は作家の主観で配置されるものだという前提に反対する |
| difference | かつてのシュルレアリスムは人間の無意識を霊媒のように媒介したが、本作はAIを外部から到来する絶対的な他者として位置づけ、作家自身を機械の代筆者へと退行させる。その上で、完成ではなく停止条件によって余白を決定する |
| why_now | 生成AIの企業導入において人間による確認やガバナンスが叫ばれ、AIを人間の統制下に閉じ込めようとする制度的潮流が強まる現代において、逆説的に人間がAIの停止に従属する体験を突きつける必然性がある |


## 3. メッセージ

| 項目 | 内容 |
| --- | --- |
| claim | インスピレーションは人間の内側ではなく、外部の冷徹な規律と停止のあいだに生じる。人間が創造性を手放したとき、空白は作品の欠落ではなく、外部知性との間に生じた「間」となる |
| who_disagrees | AIは人間の指示を実行する道具に過ぎず、作家の感性こそが芸術の源泉であると考える人 |
| denies | 作家の主観的意図や感情の表出が作品の価値を決定づけるという通念を否定する |
| shown_not_told | 説明ではなく、鑑賞者が自分で近づいてコードの記述停止位置で筆跡が断ち切られている物理的証拠を見るという経験で示す |


## 4. コンセプト

| 項目 | 内容 |
| --- | --- |
| mechanism | エージェントハーネスが運筆プロトコルを1ステップずつ自律生成し、作家は美学的判断を完全に排除して機械的に墨でロール紙に転写する。プロトコル生成器が不確実性閾値を超えた瞬間に停止条件が発火してプロセスを凍結し、残された空間を一切の加筆を禁じられた余白として確定させる |
| without_the_technique | CEASES_TO_WORK |
| precedents | reference=André Masson, Automatic Drawing, difference=マッソンのオートマティスムは作家自身の無意識を源泉としたが、本作は源泉を作家の外に置く, reference=長谷川等伯《松林図屏風》の余白, difference=伝統的な余白が気韻や大気の広がりであるのに対し、本作の余白は計算停止によって生じた関係的な間である, reference=Sol LeWitt, Wall Drawing, difference=ルウィットは規則の完遂を目的としたが、本作は規則が不確実性に直面して自己停止する破綻点を露出させる |
| self_repetition_risk | reference=SR002 の自己反復レビュー, assessment=距離で像が変わる構造（P0004）の反復を避け、エージェントの停止条件による身体的制作の凍結という構造的断絶を主軸に置く |


## 5. 調査の要約

| 項目 | 内容 |
| --- | --- |
| questions | ブルトンのオートマティスム定義において霊媒の比喩はどこまで機械的・外部的な意味を含んでいたか, 日本美術における間および余白の成立条件は、物理的寸法や構成要素とどう関係しているか, 生成AIガバナンスにおける例外停止と人間介入の境界規範はどのように記述されているか |
| what_was_read | ブルトン『シュルレアリスム宣言』自筆原稿とMoMA所蔵解説、東京国立近代美術館および和歌山県美『疎密考』展覧会資料、IPA『DX動向2026』生成AIガバナンス文書、自己モデル駆動システム定義を合わせて18件 |
| what_came_out | オートマティスムの歴史は無意識の内在化の歴史であり、外部知性への委ねは初期シュルレアリスムが霊媒を模した原初的契機と一致する。また間は単なる空白ではなく二者間の緊張関係であり、エージェントの停止ログと人間の筆跡の対置によって現代的な間が具現化できる |
| what_is_not_settled | 人間の筆跡が機械の代筆として十分な禁欲性を保てるか、また印字されたコードと墨の定着がロール紙上で物理的に破綻しないかは実寸の試し刷りでしか確かめられない |


### 採択内容と根拠

| 項目 | 内容 |
| --- | --- |
| 採択仮説 | PH002 |
| 仮説タイトル | 停止条件によって切り落とされた運筆プロトコルと自律的余白 |
| 仮説 | 外部知性のプロトコルに身体を委ねる代筆行為が、計算の自律的停止に直面するとき、生じた空白は作家の恣意を超えた真のインスピレーションの残響として知覚される |
| 仮説状態 | ADOPTED |
| 選択状態 | PROVISIONAL |
| 選択権限 | AGENT |
| 人間承認要否 | いいえ |
| 選択理由 | 外部知性のプロトコルに身体を委ねる代筆行為が、計算の自律的停止に直面するとき、生じた空白は作家の恣意を超えた真のインスピレーションの残響として知覚される |
| 創作指針 | 05_production/creative-direction.md |


### 制作リファレンス

| 分類 | 出所ID | 種別 | 概要 | アクセスURL | 状態 |
| --- | --- | --- | --- | --- | --- |
| 美術史 | EV101 | concept | シュルレアリスム宣言におけるオートマティスムとマッソンの霊媒的比喩 | <https://www.moma.org/collection/works/38201> | AVAILABLE |
| 美術史 | EV102 | concept | 東京国立近代美術館における間合いの解説 | <https://www.momat.go.jp/magazine/259> | AVAILABLE |
| 美術史 | EV103 | concept | 和歌山県立近代美術館『疎密考』展における間合いと空間 | <https://www.momaw.jp/momaw360/2021somitsu/> | AVAILABLE |
| 市場動向 | EV104 | practice | 生成AIの業務プロセス組み込みと利用ガバナンス | <https://www.ipa.go.jp/digital/chousa/dx-trend/dx-trend-2026.html> | AVAILABLE |
| 自己モデル | EV105 | drive | 自律・制御・エージェンシーの回復と不確実性制御 | `self-model-notes/config/drive-systems.yaml` | AVAILABLE |


### 要件と受入の目的

| 要件 | 優先度 | 要件内容 | 出所 | 受入テスト | 計画上の対応 |
| --- | --- | --- | --- | --- | --- |
| RQ101 | mandatory | エージェントの運筆プロトコルは、解釈の余地がない決定論的命令形式を持つこと | 未設定 | AT101 | COVERED |
| RQ102 | mandatory | 描画停止点には、エージェントが判定した正当な例外停止理由が印字されること | 未設定 | AT102 | COVERED |
| RQ103 | mandatory | 作家は停止点以降の余白領域に一切の描画・補筆を行わないこと | 未設定 | AT103 | COVERED |
| RQ104 | mandatory | 展示において鑑賞者が至近距離で印字コードと肉筆の乖離を検証可能であること | 未設定 | AT104 | COVERED |
| RQ105 | mandatory | 根拠とした出典と権利区分を成果物に添えること | 未設定 | AT105 | COVERED |


## 6. できている物

### ビジュアルパッケージ

| 種別 | 名称 | 状態 | 相対リンク | asset hash | 権利 | 安全 |
| --- | --- | --- | --- | --- | --- | --- |
| ビジュアルリファレンスボード | Visual reference board · 停止条件によって切り落とされた運筆プロトコルと自律的余白 | BOARD | [03_plan/media/visual-reference-board.svg](media/visual-reference-board.svg) | sha256:5e9f406769a5bc36048ab633242f605b17bcaed0aa5c6b0452dee95d29207237 | PROJECT_INTERNAL | CLEAR |
| コンセプト・モックアップ | Concept mockup · 停止条件によって切り落とされた運筆プロトコルと自律的余白 | MOCKUP | [03_plan/media/concept-mockup.svg](media/concept-mockup.svg) | sha256:25f202750dac54d5c405fe5e208486e7108e90d476b85e3ef8220fc3abad7c27 | PROJECT_INTERNAL | REVIEW_REQUIRED |

| mockup注記 | 内容 |
| --- | --- |
| 表現種別 | CONCEPTUAL |
| 寸法 | Not to scale; physical dimensions are not supplied by the accepted handoff. |
| 素材 | Material selection remains provisional and is not a purchase or fabrication instruction. |
| 配置 | 壁面から3メートル前後の位置と、顔を近づけられる30センチの位置の二か所を鑑賞者が自分で往復する |
| 検証 | PHYSICAL_EXTERNAL validation: NOT_RUN. No physical prototype, publication, purchase, contract, or Drive share was performed. |

まだ何も作っていない。この節は、制作した物が実行台帳に記録された時点で、現物とプレビュー画像を載せる。


## 7. 制作範囲と成果物

| 項目 | 内容 |
| --- | --- |
| スコープ状態 | PROVISIONAL |
| 必須要件ID | RQ101, RQ102, RQ103, RQ104, RQ105 |
| 試作計画ID | PP101, PP102 |
| 前提 | なし |
| 除外・未許可範囲 | publish, submit, send, purchase, contract, delete |
| 権利制約 | なし |
| 安全制約 | なし |
| プライバシー制約 | なし |
| 再計画トリガー | new_evidence, material_change, rights_or_privacy_change |

| 成果物 | 種別 | 内容 | 受入テスト | 担当能力 | 納期 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| DL101 | production-deliverable | プロトコル印字と代筆墨線、停止余白を持つロール紙大判作品 | AT101, AT102, AT103, AT104, AT105 | physical-drawing-and-observation | MS106 | PLANNED |
| DL102 | software-deliverable | 不確実性評価付き運筆プロトコル生成スクリプト | AT101, AT102 | protocol-generation | MS102 | PLANNED |


## 8. 技術仕様・材料・資源

| 仕様 | 対象 | 目標 | 許容差 | 測定方法 | 出所要件 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| TS101 | support-RQ101 | kind=QUALITATIVE, statement=特厚和紙ロール（幅1.8m、長さ6m以上、中性・無酸） | 未設定 | physical_measurement | RQ101 | PROVISIONAL |
| TS102 | print-RQ104 | kind=QUALITATIVE, statement=顔料インクによる指示コードのマイクロプリント（フォントサイズ4pt相当） | 未設定 | microscope_review | RQ104 | PROVISIONAL |
| TS103 | medium-RQ104 | kind=QUALITATIVE, statement=油煙墨および純羊毫筆（作家の手首の微細な震えが記録される仕様） | 未設定 | visual_inspection | RQ104 | PROVISIONAL |
| TS104 | log-RQ102 | kind=QUALITATIVE, statement=停止点にHALTログを可視印字する | 未設定 | code_inspection | RQ102 | PROVISIONAL |
| TS105 | provenance-RQ105 | kind=QUALITATIVE, statement=根拠とした出典と権利区分を成果物に添える | 未設定 | provenance_review | RQ105 | PROVISIONAL |


## 9. 工程と作業手順

| 作業パッケージ | 内容 | 投入物 | 制約 | 成果物 | タスク | 担当能力 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WP101 | 運筆プロトコル生成器の実装と停止条件シミュレーション | スキーマ定義, 停止ルール | ランダムな停止ではなく決定的指標に基づくこと | DL102 | TK101, TK102 | protocol-generation | READY |
| WP102 | テスト用紙へのコード印字検証と墨線並走テスト | テスト和紙, UV印刷機, 墨, 筆 | 文字の滲みによってコードが判読不能にならないこと | DL101 | TK103, TK104 | physical-test | BLOCKED |
| WP103 | 本番ロール紙へのコード印字と作家による代筆運筆 | 本番和紙ロール, DL102生成コード, 墨, 筆 | 作家自身の美的調整を加えず機械的に運筆すること | DL101 | TK105, TK106 | physical-drawing | BLOCKED |

| タスク | 作業 | 前提 | 所要時間 | 必要材料 | 受入条件 | 効果種別 | 承認 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TK101 | 運筆プロトコル生成スクリプトのコード実装 | なし | value=4, unit=h | WP101の投入物 | スクリプトが仕様通り動作する | READ_ONLY | なし | READY |
| TK102 | 停止条件アルゴリズムのユニットテスト実施 | TK101 | value=2, unit=h | WP101の投入物 | テストが全件合格する | READ_ONLY | なし | READY |
| TK103 | テスト用紙へのコード印字検証 | TK102 | value=8, unit=h | WP102の投入物 | 4ptフォントが鮮明に読める | PHYSICAL_EXTERNAL | AR101 | BLOCKED |
| TK104 | 墨線と印字コードの並走テスト | TK103 | value=8, unit=h | WP102の投入物 | 滲みと筆跡が記録される | PHYSICAL_EXTERNAL | AR101 | BLOCKED |
| TK105 | 本番ロール紙へのプロトコル印字 | TK104 | value=16, unit=h | WP103の投入物 | 6mロールにコードが印字される | PHYSICAL_EXTERNAL | AR101 | BLOCKED |
| TK106 | 作家による本番代筆運筆 | TK105 | value=24, unit=h | WP103の投入物 | 停止点到達まで代筆される | PHYSICAL_EXTERNAL | AR101 | BLOCKED |

**実施順の読み方:** クリティカルパスは `TK101` → `TK102` → `TK103` → `TK105` → `TK106` です。READYタスクは `TK101`, `TK102` です。物理・外部効果を伴うタスクは承認待ちです。


## 10. 試作・受入評価

| テスト | 対象要件 | 方法 | 合格条件 | 現在結果 |
| --- | --- | --- | --- | --- |
| AT101 | RQ101 | schema_validation | 生成されたプロトコルが欠損なく解釈できる | NOT_RUN |
| AT102 | RQ102 | halt_log_inspection | 停止点において停止理由と判定根拠が一致している | NOT_RUN |
| AT103 | RQ103 | void_purity_review | 停止点より右側の領域に一切の人的筆跡が存在しない | NOT_RUN |
| AT104 | RQ104 | perception_inspection | 30cmの距離でコードと筆跡の微細なブレが同時に視認できる | NOT_RUN |
| AT105 | RQ105 | provenance_trace | 計画書およびメタデータに出典URIが正しく紐づいている | PASS |

| マイルストーン | 内容 | 順序 | 前提 | 状態 |
| --- | --- | --- | --- | --- |
| MS101 | Start プロトコル生成スクリプト実装 | 1 | なし | PLANNED |
| MS102 | Complete プロトコル生成スクリプト実装 | 2 | MS101 | PLANNED |
| MS103 | Start テスト用紙への印字検証 | 3 | MS102 | BLOCKED |
| MS104 | Complete テスト用紙への印字検証 | 4 | MS103 | BLOCKED |
| MS105 | Start 本番代筆運筆 | 5 | MS104 | BLOCKED |
| MS106 | Complete 本番代筆運筆 | 6 | MS105 | BLOCKED |


## 11. 日程と予算

| 日程・予算項目 | 内容 |
| --- | --- |
| 日程モード | RELATIVE |
| 日程基準線 | PROVISIONAL |
| タスク日程 | task_id=TK101, duration=value=4, unit=h, task_id=TK102, duration=value=2, unit=h, task_id=TK103, duration=value=8, unit=h, task_id=TK104, duration=value=8, unit=h, task_id=TK105, duration=value=16, unit=h, task_id=TK106, duration=value=24, unit=h |
| 日程ギャップ | Calendar dates and availability are not supplied by the accepted handoff; the schedule remains relative. |
| 通貨 | JPY |
| 予算総額 | 未設定 |
| 予備費 | 未設定 |
| 承認閾値 | 未設定 |
| 予算状態 | ESTIMATED |
| 予算ギャップ | No price, quote, supplier, reservation, or commitment is present in the accepted handoff. |

| 予算項目 | 区分 | 内容 | 金額 | 根拠 | 確度 | 状態 |
| --- | --- | --- | --- | --- | --- | --- |
| BI101 | prototype-plan | Estimated cost band for PP101 | 未設定 | accepted handoff cost band: LOW | LOW | ESTIMATED |
| BI102 | prototype-plan | Estimated cost band for PP102 | 未設定 | accepted handoff cost band: LOW | LOW | ESTIMATED |


## 12. リスクと未解決事項

| リスク | 内容 | 影響 | 軽減策 | 重要度 | 可能性 | 担当 | 状態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RK101 | 和紙の毛細管現象による微細文字印刷の滲み | コードが読めずRQ104を満たせない | 異なる滲み止め加工を施した和紙で予備テストを行う | HIGH | UNKNOWN | physical-test | OPEN |
| RK102 | 作家が運筆中に無意識に美しく整えようと介入してしまう身体的慣性 | 命題の純粋性が失われる | 運筆メトロノームで速度を外部拘束して主観的介入を抑制する | CRITICAL | UNKNOWN | physical-drawing | OPEN |
| RK103 | 停止条件が一度も発火せず右端まで埋まってしまう可能性 | 余白が生まれず作品コンセプトが崩壊する | 不確実性閾値の感度パラメータを事前にシミュレーションで決定する | CRITICAL | UNKNOWN | protocol-generation | OPEN |

| ギャップ | 内容 | ブロッキング |
| --- | --- | --- |
| GP101 | rights_review_complete is not complete. | いいえ |
| GP102 | privacy_review_complete is not complete. | いいえ |
| GP103 | sources_independent_enough is not complete. | いいえ |
