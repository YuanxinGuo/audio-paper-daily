---
title: "Multi-Modal Causal Disentanglement for Multi-Domain Sequential Audio Recommendation"
date: 2026-11-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐推荐"]
summary: "CAMAR 用因果解耦把用户表示拆成域不变与域特异分量，并用多模态语义 ID 缓解音乐平台多域推荐中的负迁移与冷启动。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐推荐</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态推荐</span> <span class="tag-pill tag-pill-soft">#因果解耦</span> <span class="tag-pill tag-pill-soft">#多域序列推荐</span> <span class="tag-pill tag-pill-soft">#残差量化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.33628</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.33628" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.33628" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>CAMAR 用因果解耦把用户表示拆成域不变与域特异分量，并用多模态语义 ID 缓解音乐平台多域推荐中的负迁移与冷启动。
</div>

## 👥 作者与机构

**Yu Ren** ¹ · Pengcheng Li · Weijun Xu · Hengzhong Zhou · Shufeng Ye · Qiang Xiao · Dongjing Wang · Chuanjiang Luo · … 等 1 人

**机构**：网易云音乐

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做推荐系统、多模态表征、跨域迁移的研究者与工业推荐算法工程师阅读。若关注音频侧方法本身，价值有限；若关注多域负迁移与冷启动，值得通读 §3 的因果解耦与域对抗设计，重点看 §4 消融与在线 A/B 表。

## 🌍 研究背景

多域序列推荐（MDSR）要在歌曲、歌单、播客等异构内容域间共享行为信号。现有做法多为共享底层参数的 ID-based 序列模型（如跨域共享 embedding 的 SASRec/GRU4Rec 变体），痛点有二：高流量域主导共享参数空间造成负迁移；纯 ID 协同信号无法连接语义相关但行为重叠少的域。本文要解决跨域负迁移与跨域冷启动两个具体问题。

## 💡 核心创新

1. 将用户表示因果分解为域不变与域特异分量
2. 域对抗不变性 + 正交约束限制跨域交互子空间
3. 用残差量化从文本/视觉/音频特征构建可训练语义 ID
4. 迁移网络为不活跃域补全用户表示以缓解冷启动

## 🏗️ 模型架构

输入为用户在各域的行为序列及物品侧多模态特征。物品侧：预训练文本、视觉、音频编码器输出经残差量化（RQ）得到可训练语义 ID embedding，与 ID embedding 融合。用户侧：序列编码器（摘要未指明具体主干）产出表示后，经解耦模块分为域不变分量与域特异分量；域不变分量接域判别器做对抗训练，并对两分量施加正交约束。跨域交互仅在不变子空间进行，迁移网络为不活跃域推断表示。输出为各域物品打分。摘要未给出参数量。

## 📚 数据集

- 公开多域推荐数据集（评估，摘要未具名）
- 网易云音乐工业数据集（评估 / 在线 A/B）

## 📊 实验结果

摘要仅称在公开与工业数据集上相对强基线取得一致提升，并在网易云音乐三个域的主流量场景在线 A/B 中均获增益，但未给出任何具体指标数值、基线名称或提升幅度，无法量化评估改进大小。

## 🎯 结论与影响

最强结论是因果解耦加多模态语义 ID 能在真实大规模音乐平台上稳定提升多域推荐效果。对多域推荐后续研究的潜在影响在于把因果解耦与语义 ID 引入跨域序列建模；工业含义是可直接用于缓解新域冷启动与负迁移。

## ⚠️ 局限与未解决问题

摘要未报告任何量化指标、消融细节与推理延迟；音频模态仅作为语义 ID 来源之一，未说明音频特征的具体模型与贡献度；域对抗训练稳定性与超参敏感性未讨论；公开数据集未具名，复现性存疑。

---

<div class="paper-footer"><span>评分：5.8</span><span>原始：5.8</span><a href="/audio-paper-daily/posts/2026-11-26/">← 返回 2026-11-26 速递</a></div>
