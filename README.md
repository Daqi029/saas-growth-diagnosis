# SaaS Growth Diagnosis

> **v0.1 Public Beta** — 欢迎用真实产品测试并提交反馈。

一个面向独立开发者、小型 SaaS 创始人和增长负责人的公开诊断 Skill。

你可以只让它“诊断当前工作区里的产品”，也可以提供产品网址。它会先读取可访问的代码、产品页面、文档和已有数据，再按照“流量质量 → Landing Page → 激活 → 试用转付费与定价 → 留存”的顺序，找出当前最值得优先验证的增长卡点，并给出三个可衡量的实验。

这套框架来自 Mengqi Pei 在阿里、TikTok 的产品实战经验，以及为 30+ SaaS 产品提供增长诊断的案例总结。

## 它能做什么

- 在数据不完整时完成有边界的初步诊断
- 优先检查当前代码仓库、页面和已授权的只读数据，而不是先发问卷
- 为尚未上线的产品检查首次价值路径和数据可观测性
- 统一转化率、激活率、留存率等指标口径
- 找出最早出现的关键漏斗断点
- 区分事实、计算、行业参照、假设和缺失证据
- 给出最多三个优先实验及验证指标
- 在确实需要私有数据或完整产品体验时说明人工诊断边界

## 它不做什么

- 不保证转化率或收入提升幅度
- 不把行业平均值当作通用答案
- 不编造用户数据、案例或因果关系
- 不代替广告投放、UI 设计、前端开发和埋点实施
- 不故意保留关键结论来推销人工服务

## 使用示例

### 产品代码就在当前工作区

```text
请用 $saas-growth-diagnosis 诊断当前工作区里的 SaaS。
先读取代码、产品文档和可访问的页面，再告诉我最大的增长风险。
```

Agent 会先检查产品承诺、路由、注册和 onboarding、空白状态、埋点事件、试用和定价逻辑。代码只能证明产品“被设计成怎样”，不能代替真实用户数据；确实缺少行为证据时，它才会问一个会改变判断的问题。

### 只提供产品网址

```text
请用 $saas-growth-diagnosis 诊断 https://example.com。
先检查你能访问的页面，不要先让我填表。
```

### 已经有漏斗数据

```text
请用 $saas-growth-diagnosis 诊断：

- B2B 项目管理 SaaS，$29/月，14 天免费试用
- 月独立访客 20,000
- 注册 800
- 注册后 7 天内完成首个项目：120
- 开始试用 300
- 同期成熟试用 cohort 中付费 18
- Day-30 付费留存 88%

告诉我最大的卡点，并给出三个优先实验。
```

### 专项审查

```text
请用 $saas-growth-diagnosis 专门审查我的 onboarding。
Aha Moment 是用户成功生成第一份报告。我会提供流程截图和分步数据。
```

### 产品还没有上线

```text
请用 $saas-growth-diagnosis 检查当前工作区这个尚未上线的产品。
重点看首次价值路径、onboarding、定价和埋点是否准备好。
```

未上线产品不会被虚构成“转化率有问题”。Skill 会输出预发布风险、候选 Aha Moment、最小事件方案，以及上线第一周应该怎样学习。

## 仓库结构

```text
saas-growth-diagnosis/
├── README.md
├── LICENSE
├── VERSION
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── intake-and-metrics.md
│   ├── prelaunch.md
│   ├── funnel-routing.md
│   ├── traffic-quality.md
│   ├── landing-page.md
│   ├── activation.md
│   ├── trial-to-paid.md
│   ├── pricing.md
│   ├── retention.md
│   └── report-template.md
└── tests/
    ├── cases.md
    ├── check_contract.py
    └── smoke-output-case-1.md
```

`SKILL.md` 只保留共同诊断流程。Agent 会根据问题按需读取对应参考文件，避免每次加载整套知识。

## 本地安装

使用 Skills CLI 安装：

```bash
npx -y skills add Daqi029/saas-growth-diagnosis -g
```

也可以将整个仓库目录复制到支持 Agent Skills 的技能目录，然后重新启动或刷新对应 Agent。

在 Codex 的默认个人配置中，可以将目录安装为：

```text
~/.codex/skills/saas-growth-diagnosis/
```

安装后可以显式调用 `$saas-growth-diagnosis`。

## 方法来源

- [SaaS 核心指标科普](https://blog.mengqi.cc/p/saas-core-metrics-explained-dont-just-look-at-revenue-and-new-additions-first-check-these-ten-numbers)
- [从流量到收入：5 个关键卡点](https://blog.mengqi.cc/p/saas-growth-diagnosis-1-from-traffic-to-revenue-key-points)
- [流量质量诊断法](https://blog.mengqi.cc/p/saas-growth-diagnosis-traffic-quality-diagnosis-method)
- [Landing Page 转化率优化](https://blog.mengqi.cc/p/saas-growth-diagnosis-article-landing-page-conversion-optimization-five-second-rule-and-trust-building)
- [用户激活率诊断](https://blog.mengqi.cc/p/saas-growth-diagnosis-user-activation-diagnosis-why-percentage-of-registered-users-never-used-your-product)
- [试用转付费诊断](https://blog.mengqi.cc/p/saas-growth-diagnosis-trial-to-paid-diagnosis-why-users-trialed-but-did-not-pay)
- [SaaS 定价页设计指南](https://blog.mengqi.cc/p/vip-exclusive-reading-saas-pricing-page-design-guide-key-designs)

## 作者与支持

作者：Mengqi Pei（[@daqi029](https://x.com/daqi029)）

- X：[@daqi029](https://x.com/daqi029)
- 小红书：[Mengqi Pei](https://www.xiaohongshu.com/user/profile/631fd949000000002303cafc)
- Newsletter《硅谷增长对标：SaaS 与 App 转化实战案卷》：<https://blog.mengqi.cc>
- 免费增长诊断器：<https://lp.mengqi.cc>
- 付费 SaaS 增长诊断、专项优化与长期顾问：<https://mengqi.cc>

Skill 会先提供完整的初步判断，并在诊断报告末尾保留轻量作者署名。只有当下一步确实需要私有数据、用户录屏、访谈、完整产品体验或持续实验设计时，才会建议用户了解付费深度诊断；不会为了导流而保留关键结论。

## 许可

本项目源码公开，采用 [Creative Commons Attribution-NonCommercial 4.0 International](LICENSE) 许可：允许个人学习、研究、修改和非商业分享；公开发布衍生作品时需要署名，商业使用需要另行获得授权。
