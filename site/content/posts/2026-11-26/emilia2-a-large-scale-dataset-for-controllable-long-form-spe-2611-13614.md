---
title: "Emilia2: A Large-Scale Dataset for Controllable Long-Form Speech Generation"
date: 2026-11-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "构建229K小时多语种长语音数据集Emilia2，含单说话人长语音与多人对话，支持自然语言指令与副语言标签控制，并训练AR/NAR基线验证。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#长语音生成</span> <span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#可控生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.13614</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://charlesnii.github.io/Emilia2-demo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">charlesnii.github.io/Emilia2-demo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.13614" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.13614" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://charlesnii.github.io/Emilia2-demo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建229K小时多语种长语音数据集Emilia2，含单说话人长语音与多人对话，支持自然语言指令与副语言标签控制，并训练AR/NAR基线验证。
</div>

## 👥 作者与机构

**Qinke Ni** ¹ · Dekun Chen · Junwen Qiu · Huan Liao · Xu Li · Xingwen Han · Wan Lin · Kunyu Feng · … 等 9 人

**机构**：香港中文大学（深圳） · 伊利诺伊大学厄巴纳-香槟分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做TTS、长语音生成与可控语音合成的读者。值得通读，重点看§3数据构建流程（长语音切分、说话人/停顿保留、指令标注）与§5实验结果表。可先看表2的CER/WER对比与InstructTTSEval结果，再回看数据统计表判断长语音占比与标注规模。

## 🌍 研究背景

长语音生成要求模型在数分钟内保持内容、说话人身份、轮次转换与风格一致。现有开源语料多为数十秒短句，开源长语音基准最多两人对话，缺乏分钟级、多说话人、带指令与副语言标注的训练数据。本文旨在构建大规模、可控、覆盖单人与多人长语音的数据基础，并提供可复现的AR/NAR基线。

## 💡 核心创新

1. 从in-the-wild数据构建短句、单人长语音、多人对话三类子集
2. 保留转写、说话人身份、停顿与声学过渡信息
3. 4.77M条自然语言指令与933K条副语言发声标签
4. 提出Emilia2-testset：最长30分钟、四人、双语的评测集
5. 在数据集上训练AR与NAR基线并给出对比

## 🏗️ 模型架构

摘要未给出详细网络结构。方法层面为在Emilia2上训练自回归（AR）与非自回归（NAR）两类TTS模型，NAR模型采用0.6B骨干网络，输入为文本/指令与参考音频，输出为目标语音；AR模型与Qwen3-TTS-12Hz-VD在指令评测上对比。具体主干（如Conformer/Transformer/flow matching）与声码器细节摘要未披露。

## 📚 数据集

- Emilia2（训练，229K小时，多语种，含短句/单人长语音/多人对话）
- Emilia2-testset（评估，23小时，双语，最长30分钟、四人）
- TTSD-Eval（评估，中英CER/WER）
- InstructTTSEval（评估，指令可控TTS，zh/en）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| CER | TTSD-Eval (zh) | 对比系统（摘要未列具体值） | **5.27%** | 最低 |
| WER | TTSD-Eval (en) | 对比系统（摘要未列具体值） | **9.93%** | 最低 |
| 指令评测得分 (zh/en) | InstructTTSEval | Qwen3-TTS-12Hz-VD 77.1/77.9 | **76.2/78.3** | -0.9/+0.4 |

0.6B骨干NAR模型在TTSD-Eval上取得对比系统中最低的中文CER 5.27%与英文WER 9.93%；AR模型在InstructTTSEval上与Qwen3-TTS-12Hz-VD基本持平（zh 76.2 vs 77.1，en 78.3 vs 77.9）。摘要未给出消融、推理延迟或跨域泛化数据，基线对比系统清单亦未完整列出。

## 🎯 结论与影响

最强结论是Emilia2可作为长语音生成与分钟级表达控制的数据基础，且在其上训练的NAR/AR基线已具竞争力。对后续研究的潜在影响在于提供统一的长语音、多说话人、带指令标注的训练与评测协议；工业上可用于长音频有声书、播客与对话式TTS的数据管线参考。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟、模型参数量细节与消融实验；基线对比系统未完整列出，CER/WER优势幅度难以判断；数据来自in-the-wild，可能存在说话人/语种分布偏置与标注噪声；长语音一致性与轮次转换的定量评测指标未在摘要中说明。

## 🔗 开源资源

- **Demo / 试听**：<https://charlesnii.github.io/Emilia2-demo/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-11-26/">← 返回 2026-11-26 速递</a></div>
