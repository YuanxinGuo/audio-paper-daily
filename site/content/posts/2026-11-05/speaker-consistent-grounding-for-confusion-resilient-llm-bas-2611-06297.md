---
title: "Speaker-Consistent Grounding for Confusion-Resilient LLM-Based Target Speech Extraction"
date: 2026-11-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出先修复后接地框架，用无训练证据修复与码空间接地约束LLM目标说话人提取，降低错说话人提取与内容幻觉。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#语音生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.06297</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://hanyu-meng.github.io/LLM-TSE-Grounding-Demo/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">hanyu-meng.github.io/LLM-TSE-Grounding-Demo/</span></span></a><a class="oc-chip oc-chip-demo" href="https://hanyu-meng.github.io/LLM-TSE-Grounding-Demo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">hanyu-meng.github.io/LLM-TSE-Grounding-Demo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.06297" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.06297" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://hanyu-meng.github.io/LLM-TSE-Grounding-Demo/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://hanyu-meng.github.io/LLM-TSE-Grounding-Demo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出先修复后接地框架，用无训练证据修复与码空间接地约束LLM目标说话人提取，降低错说话人提取与内容幻觉。
</div>

## 👥 作者与机构

**Hanyu Meng** ¹ · Hao Shi · Zhanhong He · Qiquan Zhang · Yang Xiao · Sungwoo Cho · Haowei Lou · Haizhou Li

**机构**：新加坡国立大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做TSE、LLM语音生成与语音分离的研究者阅读。建议通读，重点看§3的CDCS候选选择与CSG码空间接地机制，以及表1、表2中干净/含噪条件下的错说话人率与切换率对比；工程读者可先看Libri2Mix实验设置与推理开销讨论。

## 🌍 研究背景

目标说话人提取此前以确定性方法为主，如基于说话人embedding的掩蔽/波束成形，能保留观测语音内容但易提取到干扰说话人；自回归生成式TSE（如基于LLM的码本解码）感知质量更好，却存在内容幻觉与说话人身份漂移。用确定性TSE输出作为证据接地生成模型可缓解幻觉，但若证据本身说话人混淆，接地会强化错误。本文要解决的是接地前证据身份不可靠的问题。

## 💡 核心创新

1. 提出先修复后接地框架，将证据修复与生成接地解耦
2. CDCS：从互补的冻结TSE输出中无训练选择目标说话人一致证据
3. CSG：在码空间用修复波形约束LLM-TSE解码
4. 在Libri2Mix上同时降低错说话人率与内容/声学切换率

## 🏗️ 模型架构

输入为混合语音与目标说话人线索，先经多个互补的冻结确定性TSE模型产生候选波形；CDCS模块基于条件多样性对候选做说话人一致性打分与选择，得到修复后的目标证据波形；该波形经编码器映射到LLM-TSE的离散码空间，作为CSG约束在自回归解码时对码本logits进行接地偏置；主干为LLM-based TSE解码器，输出目标说话人语音的离散码序列并合成波形。摘要未给出参数量。

## 📚 数据集

- Libri2Mix（评估，干净与含噪混合条件）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 错说话人提取错误率 | Libri2Mix clean | 6.87% | **0.75%** | -6.12% |
| 错说话人提取错误率 | Libri2Mix noisy | 18.95% | **10.46%** | -8.49% |
| 内容切换率 | Libri2Mix noisy | 12.79% | **9.10%** | -3.69% |
| 声学切换率 | Libri2Mix noisy | 1.68% | **0.51%** | -1.17% |

在Libri2Mix上，CDCS将干净混合的错说话人提取错误率从6.87%降至0.75%，含噪条件从18.95%降至10.46%；在LLM-TSE检查点不变的情况下，CSG进一步把含噪内容切换率从12.79%降到9.10%、声学切换率从1.68%降到0.51%。作者称生成式TSE仍保持相对直接确定性提取的感知质量优势，但摘要未给出PESQ等具体数值与消融细节。

## 🎯 结论与影响

最强结论是：在接地前先修复证据的说话人身份，可显著提升生成式TSE的可靠性且不牺牲感知质量优势。这为LLM-based TSE的证据接地提供了可复用的无训练前置模块，后续研究可沿候选多样性与码空间约束设计展开；工业上意味着生成式TSE落地需先解决证据身份校验。

## ⚠️ 局限与未解决问题

仅在一个数据集Libri2Mix上评估，缺少跨数据集与真实录音泛化验证；CDCS依赖多个冻结TSE模型，推理成本与候选数量影响未报；摘要未给PESQ/SI-SDR等感知指标具体值与消融实验，也未讨论修复失败时的回退策略。

## 🔗 开源资源

- **项目主页**：<https://hanyu-meng.github.io/LLM-TSE-Grounding-Demo/>
- **Demo / 试听**：<https://hanyu-meng.github.io/LLM-TSE-Grounding-Demo/>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-05/">← 返回 2026-11-05 速递</a></div>
