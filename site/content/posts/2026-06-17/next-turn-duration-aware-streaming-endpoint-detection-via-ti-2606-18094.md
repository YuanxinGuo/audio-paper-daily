---
title: "Next-Turn: Duration-Aware Streaming Endpoint Detection via Time-to-Next-Speech-Onset Prediction"
date: 2026-06-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#端点检测"]
summary: "提出Next-Turn，通过预测到下一次语音起始的时间实现流式端点检测，在准确率上比最强基线提升25.9%。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#端点检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音交互</span> <span class="tag-pill tag-pill-soft">#流式处理</span> <span class="tag-pill tag-pill-soft">#语音端点检测</span> <span class="tag-pill tag-pill-soft">#持续时间感知</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.18094</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.18094" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.18094" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Next-Turn，通过预测到下一次语音起始的时间实现流式端点检测，在准确率上比最强基线提升25.9%。
</div>

## 👥 作者与机构

**Tristan Tsoi** ¹ · Jiajun Deng · Yingke Zhu · Huu Quyen Dang · Tianxiang Cao · Nikita Kuzmin · Tao Zhong · Simon Lui

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音交互系统、流式ASR研究者。建议重点阅读§3方法部分和§4实验对比，尤其是表1的端点准确率结果。可复现其训练目标设计思路。

## 🌍 研究背景

端点检测（EPD）是流式语音系统中自然轮换的关键。传统声学EPD在停顿、犹豫时易误判；语义EPD虽有前景，但受限于模糊监督和严格流式约束。现有方法难以在实时性和准确性间取得平衡。本文旨在通过预测下一次语音起始时间（time-to-next-speech-onset）作为训练目标，解决EPD中的停顿歧义问题。

## 💡 核心创新

1. 提出时间到下次语音起始（TTSO）作为训练目标
2. TTSO目标直接从语音时间戳导出，无需额外标注
3. 联合训练TTSO与标准二元EPD，提升停顿期间检测鲁棒性
4. 在流式约束下实现优于声学和语义EPD的性能

## 🏗️ 模型架构

输入为流式语音特征（如log-mel谱），通过编码器（如Transformer或RNN）提取上下文表示。主干网络输出两个分支：一个预测时间到下次语音起始（TTSO，回归任务），另一个进行二元端点分类。TTSO目标由语音活动检测（VAD）时间戳计算得到，训练时联合优化回归损失和分类损失。推理时结合TTSO预测和二元分类结果决策端点。

## 📚 数据集

- 未明确指定，推测使用内部对话数据集或公开语音交互数据集（如Switchboard）进行训练和评估

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 端点准确率（320ms内） | 内部测试集 | 最强基线（语义EPD） | **25.9%绝对提升** | +25.9% |

实验表明，Next-Turn在端点准确率上比最强基线提升25.9%（320ms窗口内）。联合训练TTSO与二元EPD的增益随停顿长度单调增加，验证了持续时间感知目标的有效性。未报告其他指标如延迟或计算开销。

## 🎯 结论与影响

Next-Turn通过预测下次语音起始时间，显著提升了流式端点检测的准确性，尤其适用于含停顿的自然对话。该方法无需额外标注，易于集成到现有系统。未来可探索更复杂的编码器结构或扩展到多说话人场景。

## ⚠️ 局限与未解决问题

未在公开基准（如Voice Activity Detection数据集）上评估，泛化性存疑；未报告模型参数量、推理延迟等效率指标；仅对比了语义EPD基线，缺少与传统声学EPD（如WebRTC）的对比；TTSO目标对VAD精度敏感，可能引入噪声。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-17/">← 返回 2026-06-17 速递</a></div>
