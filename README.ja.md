# SaaS Growth Diagnosis

[简体中文](README.md) | [English](README.en.md) | 日本語

> **v0.2 Public Beta** — 実際のプロダクトで試し、診断結果へのフィードバックをお寄せください。

個人開発者、SaaS 創業者、グロース担当者のためのオープンな診断 Skill です。

プロダクトの URL、リポジトリ、分析データを渡すか、現在のワークスペースを診断するよう依頼してください。アクセス可能な情報を先に調べたうえで、「流入の質 → LP の転換 → アクティベーション → トライアルから有料化・価格設計 → リテンション」の順に診断します。最優先のボトルネックを一つに絞り、不確実性を明示し、最大三つの検証可能な実験を提案します。

このフレームワークは、Mengqi Pei の Alibaba・TikTok でのプロダクト経験と、30 以上の SaaS に対するグロース診断の実績をもとに作られました。

## できること

- 質問票を送る前に、プロダクト、リポジトリ、ドキュメント、許可された読み取り専用データを確認
- データが不完全でも、根拠と限界を示した初期診断を作成
- 未公開プロダクトの初回価値体験と計測準備を監査
- 指標の定義、コホート、期間、分母をそろえる
- ファネルで最初に発生している重要な断点を特定
- 観察事実、計算結果、参考値、仮説、不足している証拠を区別
- 優先度の高い実験を最大三つ提案

## しないこと

- 転換率や売上の上昇幅を保証する
- 業界平均を普遍的な合否基準として扱う
- プロダクトの事実、ユーザー行動、因果関係を捏造する
- コード内のイベント実装を実際の利用データと混同する
- 有料サービスへ誘導するために重要な結論を出し惜しみする

## 使用例

### 現在のワークスペースを診断

```text
$saas-growth-diagnosis を使って、このワークスペースにある SaaS を診断してください。
コード、プロダクト資料、アクセス可能なページを先に確認し、最大のグロースリスクを教えてください。
```

### URL から始める

```text
$saas-growth-diagnosis を使って https://example.com を診断してください。
質問票を送る前に、アクセスできるページを確認してください。
```

### ファネルデータを使う

```text
$saas-growth-diagnosis を使って次の B2B SaaS を診断してください。
- 月間ユニーク訪問者 20,000
- 登録 800
- 登録後 7 日以内に最初のプロジェクトを完了 120
- トライアル開始 300
- 成熟したトライアルコホートから有料化 18
- 有料ユーザーの Day-30 継続率 88%

最優先のボトルネックと三つの実験を提案してください。
```

### オンボーディングだけを監査

```text
$saas-growth-diagnosis を使ってオンボーディングを監査してください。
候補となる Aha Moment は、最初のレポートを生成することです。画面と各ステップのデータを提供します。
```

### 未公開プロダクトを確認

```text
$saas-growth-diagnosis を使って、現在のワークスペースにある未公開プロダクトを確認してください。
初回価値体験、オンボーディング、価格、計測準備を重点的に見てください。
```

未公開プロダクトに対し、存在しない転換率の問題を作りません。公開前のリスク、候補となる Aha Moment、最小限のイベント設計、公開後一週間の学習計画を示します。

## インストール

```bash
npx -y skills add Daqi029/saas-growth-diagnosis -g
```

対応する Agent の Skill ディレクトリへリポジトリ全体をコピーする方法もあります。Codex の標準的な個人設定では次の場所です。

```text
~/.codex/skills/saas-growth-diagnosis/
```

`$saas-growth-diagnosis` と明示して呼び出せます。Skill はユーザーが使用した言語で回答するため、日本語 README は別実装ではありません。

## 方法の出典

詳しい原文記事は現在、中国語で公開されています。

- [SaaS の重要指標 10 項目](https://blog.mengqi.cc/p/saas-core-metrics-explained-dont-just-look-at-revenue-and-new-additions-first-check-these-ten-numbers)
- [流入から売上までの五つのボトルネック](https://blog.mengqi.cc/p/saas-growth-diagnosis-1-from-traffic-to-revenue-key-points)
- [流入品質の診断](https://blog.mengqi.cc/p/saas-growth-diagnosis-traffic-quality-diagnosis-method)
- [Landing Page の転換率改善](https://blog.mengqi.cc/p/saas-growth-diagnosis-article-landing-page-conversion-optimization-five-second-rule-and-trust-building)
- [ユーザーアクティベーション診断](https://blog.mengqi.cc/p/saas-growth-diagnosis-user-activation-diagnosis-why-percentage-of-registered-users-never-used-your-product)
- [トライアルから有料化への診断](https://blog.mengqi.cc/p/saas-growth-diagnosis-trial-to-paid-diagnosis-why-users-trialed-but-did-not-pay)

## 作者・サポート

作者：Mengqi Pei（[@daqi029](https://x.com/daqi029)）

- X：[@daqi029](https://x.com/daqi029)
- 小紅書：[Mengqi Pei](https://www.xiaohongshu.com/user/profile/631fd949000000002303cafc)
- 中国語ニュースレター：<https://blog.mengqi.cc>
- 有料 SaaS グロース診断、個別最適化、長期アドバイザリー：<https://mengqi.cc>

すべてのレポートに簡潔な作者表記を入れます。有料サービスの案内は、次の判断に非公開の分析データ、録画、インタビュー、プロダクト全体へのアクセス、または継続的な実験設計が本当に必要な場合に限ります。

## ライセンス

[Creative Commons Attribution-NonCommercial 4.0 International](LICENSE) を採用しています。表示を条件に、学習、研究、改変、非商用での再配布が可能です。商用利用には別途許可が必要です。
