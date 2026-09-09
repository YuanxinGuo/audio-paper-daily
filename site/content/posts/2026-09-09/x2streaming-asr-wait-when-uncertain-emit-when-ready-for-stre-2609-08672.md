---
title: "X2Streaming-ASR: wait when uncertain, emit when ready for streaming ASR"
date: 2026-09-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出X2Streaming-ASR，将流式识别分解为何时提交与提交什么，通过三阶段训练优化提交策略，在多个中文数据集上实现低延迟和高准确率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流式语音识别</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#提交策略</span> <span class="tag-pill tag-pill-soft">#低延迟</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.08672</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.08672" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.08672" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出X2Streaming-ASR，将流式识别分解为何时提交与提交什么，通过三阶段训练优化提交策略，在多个中文数据集上实现低延迟和高准确率。
</div>

## 👥 作者与机构

**Zhiwei Lin** ¹ · Kaiqi Fu · Rime Wen · Zehan Liu · Shawn Qin · Roy Gan · Hao Wang · Qian Wang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音识别研究者，尤其是关注流式ASR延迟与准确率权衡的读者。建议重点阅读第3节方法部分，特别是三阶段训练流程和奖励设计。可先看实验部分表1和表2，了解性能提升。

## 🌍 研究背景

流式ASR需在低延迟下提供准确的部分转录。现有方法常使用固定块大小、前瞻或目标延迟，或鼓励在估计的声学边界附近发射，但未直接优化每个输出位置在硬提交约束下应使用多少额外上下文。本文提出X2Streaming-ASR，将流式识别分解为何时提交和提交什么，通过三阶段训练优化提交策略，以平衡延迟和准确率。

## 💡 核心创新

1. 将流式识别分解为提交时机和内容两个子问题
2. 三阶段训练：先建立流式能力，再用自动探测轨迹热启动策略，最后用组相对奖励优化
3. 使用字符级、分段分配的组相对奖励，同时优化准确率和延迟
4. 在多个中文数据集上实现毫秒级提交延迟，显著低于基线

## 🏗️ 模型架构

X2Streaming-ASR采用编码器-解码器架构，输入为声学特征，编码器采用Conformer，解码器为自回归Transformer。训练分三阶段：第一阶段用标准CTC/Attention训练流式识别；第二阶段用自动探测的提交轨迹初始化策略网络；第三阶段用策略梯度优化提交决策，奖励结合字符级准确率和延迟惩罚。推理时，模型在每个输出位置决定是否提交，提交则输出字符。

## 📚 数据集

- AISHELL-1（训练/评估）
- AISHELL-2（训练/评估）
- AISHELL-3（训练/评估）
- WenetSpeech（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| CER | AISHELL-1 | 流式基线（如固定块） | **最佳流式CER** | 显著降低 |
| CER | AISHELL-3 | 流式基线 | **最佳流式CER** | 显著降低 |
| 平均字符级提交延迟 | AISHELL-1/2/3和WenetSpeech | 409-585 ms | **27-84 ms** | -322~-501 ms |

实验表明，X2Streaming-ASR在AISHELL-1和AISHELL-3上取得最佳流式CER，同时平均字符级提交延迟仅为27-84 ms，远低于基线的409-585 ms。在AISHELL-2和WenetSpeech上也验证了泛化性。消融研究显示三阶段训练和组相对奖励对性能提升至关重要。

## 🎯 结论与影响

X2Streaming-ASR通过显式建模提交时机，在流式ASR中实现了极低的提交延迟和优秀的准确率，为实时语音交互提供了新思路。该方法有望推动流式ASR在延迟敏感场景的落地，并启发后续研究将决策策略与识别模型联合优化。

## ⚠️ 局限与未解决问题

论文未报告模型参数量和推理效率，可能影响实际部署评估。实验仅在中文数据集上进行，跨语言泛化未知。提交策略的奖励设计可能对超参数敏感，需进一步验证鲁棒性。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-09-09/">← 返回 2026-09-09 速递</a></div>
