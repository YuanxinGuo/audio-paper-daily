---
title: "AnyEdit: A Unified Framework for Speech and Singing Voice Editing with Real-World Environmental Consistency"
date: 2026-10-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音编辑"]
summary: "AnyEdit 用两阶段分离式框架做语音与歌声编辑，先预测干净韵律内容 token，再用流匹配模型在源声学上下文中渲染，保留噪声与混响。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音编辑</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音编辑</span> <span class="tag-pill tag-pill-soft">#歌声合成</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#偏好优化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.15665</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-hf" href="https://huggingface.co/datasets/Ririiiii/anyeditbench" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 datasets/Ririiiii/anyeditbench</span></span></a><a class="oc-chip oc-chip-proj" href="https://any-edit.github.io/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">any-edit.github.io/</span></span></a><a class="oc-chip oc-chip-demo" href="https://any-edit.github.io/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">any-edit.github.io/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.15665" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.15665" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-hf" href="https://huggingface.co/datasets/Ririiiii/anyeditbench" target="_blank" rel="noopener">🤗 HuggingFace</a><a class="rsrc rsrc-proj" href="https://any-edit.github.io/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://any-edit.github.io/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>AnyEdit 用两阶段分离式框架做语音与歌声编辑，先预测干净韵律内容 token，再用流匹配模型在源声学上下文中渲染，保留噪声与混响。
</div>

## 👥 作者与机构

**Yunjia Zhang** ¹ · Junan Zhang · Jing Yang · Xueyao Zhang · Fan Fan · Zhizheng Wu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音/歌声编辑、生成式音频编辑、噪声鲁棒语音建模的研究者与工程团队。建议通读，重点看 §3 两阶段设计与 teacher-student 噪声鲁棒韵律 tokenizer，以及 §4 的 unmodified-area-aware 监督与 DPO 细节；实验部分先看 AnyEditBench 上噪声/混响条件下的内容准确率与背景一致性表。

## 🌍 研究背景

统一生成模型在干净条件下已能高质量合成语音与歌声，但真实场景的 vocal editing 仍困难：模型需在改写内容的同时保持说话人音色、韵律与周围声学场景（噪声、混响、背景音乐）。直接端到端建模含噪音频会把语义编辑与环境声学纠缠在一起，削弱核心 vocal 生成能力，因此需要一种既保留干净域编辑能力、又能继承真实声学环境的方案。

## 💡 核心创新

1. 两阶段分离式编辑框架，将干净域编辑与声学渲染解耦
2. teacher-student 噪声鲁棒韵律 tokenizer，从退化录音蒸馏干净韵律 token
3. 流匹配声学模型做 in-context 渲染，继承源噪声/混响/背景声
4. unmodified-area-aware 监督稳定未编辑区域
5. 在挖掘的 real-to-real 歌声对上做 DPO 后训练

## 🏗️ 模型架构

输入为含噪/含混响的源音频与编辑指令。第一阶段：指令引导的自回归编辑器预测干净韵律与内容-风格 token，依赖 teacher-student 噪声鲁棒韵律 tokenizer 从退化录音中蒸馏干净韵律 token。第二阶段：flow-matching 声学模型以源声学上下文为条件做 in-context rendering，使编辑片段继承周围噪声、混响与背景声并保持说话人音色一致。训练中加入 unmodified-area-aware 监督稳定未编辑区域，预训练后在挖掘的 real-to-real 歌声对上做 DPO。摘要未给出参数量。

## 📚 数据集

- AnyEditBench（评估，覆盖干净/模拟/真实声学条件下的语音与歌声编辑）
- 中文与英文语音数据集（训练/评估）
- 中文与英文歌声数据集（训练/评估）
- real-to-real 歌声对（DPO 后训练）

## 📊 实验结果

摘要仅给出定性结论：在中文与英文语音及歌声数据集上，AnyEdit 在内容准确率、主观质量和背景一致性上一致优于强基线，尤其在噪声与混响条件下。未提供 SI-SDR、PESQ、WER、MOS 等具体数值，也未给出消融与效率指标，需查阅正文表格确认提升幅度。

## 🎯 结论与影响

最强结论是：将干净域编辑与声学渲染解耦的两阶段设计，能在保留真实噪声/混响/背景音乐的同时完成语音与歌声内容编辑。该思路对真实场景音频编辑、影视后期与个性化语音内容生产有直接参考价值，AnyEditBench 也为该子方向提供了统一评测基准。

## ⚠️ 局限与未解决问题

摘要未给出任何定量指标与消融，难以判断各模块贡献；两阶段设计带来推理开销，未报延迟与参数量；DPO 依赖挖掘的 real-to-real 歌声对，数据偏置未知；语音与歌声混合评测下各子任务表现差异未说明。

## 🔗 开源资源

- **HuggingFace**：<https://huggingface.co/datasets/Ririiiii/anyeditbench>
- **项目主页**：<https://any-edit.github.io/>
- **Demo / 试听**：<https://any-edit.github.io/>
- **数据集**：<https://huggingface.co/datasets/Ririiiii/anyeditbench>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-10-15/">← 返回 2026-10-15 速递</a></div>
