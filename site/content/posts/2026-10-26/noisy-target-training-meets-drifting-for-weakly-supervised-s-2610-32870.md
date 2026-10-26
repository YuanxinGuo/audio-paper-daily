---
title: "Noisy Target Training Meets Drifting for Weakly-Supervised Speech Enhancement"
date: 2026-10-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "在NyTT框架上加入Sinkhorn drifting损失，用无配对干净语音约束增强输出分布，减少残留噪声。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.3</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#弱监督学习</span> <span class="tag-pill tag-pill-soft">#分布匹配</span> <span class="tag-pill tag-pill-soft">#Sinkhorn散度</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.32870</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.32870" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.32870" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在NyTT框架上加入Sinkhorn drifting损失，用无配对干净语音约束增强输出分布，减少残留噪声。
</div>

## 👥 作者与机构

**Yoshiki Masuyama** ¹ · Dominik Klement · Christoph Boeddeker · Julius Richter · Kohei Saijo · Gordon Wichern · Takahiro Edo · Jonathan Le Roux

**机构**：日本电报电话公司 · 本田研究所

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做弱监督/无配对语音增强与生成式分布匹配的研究者阅读。建议通读，重点看§3对Sinkhorn drifting损失的定义与在NyTT中的接入方式，以及表1/表2在VoiceBank-DEMAND与CHiME-3真实录音上的对比；若关注落地，注意其推理开销与对无配对干净数据的依赖。

## 🌍 研究背景

标准监督语音增强依赖成对的含噪-干净语音，通常由人工加噪合成，与真实录音存在域失配。NyTT通过让模型从更噪版本预测含噪录音来规避该问题，但因训练目标本身含噪，模型易在输出中保留残余噪声。本文要在保持NyTT弱监督性质的前提下，抑制这种残留噪声。

## 💡 核心创新

1. 将Sinkhorn drifting损失引入NyTT训练目标
2. 用无配对干净语音做潜空间分布匹配
3. 吸引-排斥机制拉向干净语音高密度区
4. 保持弱监督设定，无需逐条干净对应

## 🏗️ 模型架构

输入为含噪语音（或NyTT中额外加噪的更噪版本），经增强网络（摘要未指明具体主干，按NyTT范式为时频域掩蔽/映射模型）输出增强语音；训练时除NyTT的含噪目标回归损失外，将增强输出与无配对干净语音映射到潜空间，用Sinkhorn drifting损失匹配两者分布：吸引增强语音靠近干净语音分布高密度区，排斥其偏离当前增强分布。摘要未给出参数量与具体网络名。

## 📚 数据集

- VoiceBank-DEMAND（评估，合成加噪测试集）
- CHiME-3（评估，真实录音）

## 📊 实验结果

摘要仅说明在VoiceBank-DEMAND与CHiME-3真实录音上验证了所提组合的有效性，未给出SI-SDR、PESQ、WER等具体数值，也未报告消融细节与效率指标，需查阅正文表格确认增益幅度。

## 🎯 结论与影响

最强结论是：在NyTT中加入Sinkhorn drifting损失可在不引入配对干净语音的情况下抑制残留噪声，并在合成与真实录音上均有效。这为弱监督语音增强提供了分布层面的正则思路，对缺乏配对数据的真实场景部署有参考价值。

## ⚠️ 局限与未解决问题

摘要未给出量化结果与消融，难以判断Sinkhorn drifting相对NyTT的增益幅度；方法依赖无配对干净语音分布，若目标域干净数据稀缺则受限；未报告推理延迟与训练额外开销；对比基线是否覆盖最新强监督方法不明。

---

<div class="paper-footer"><span>评分：8.3</span><span>原始：7.3</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-26/">← 返回 2026-10-26 速递</a></div>
