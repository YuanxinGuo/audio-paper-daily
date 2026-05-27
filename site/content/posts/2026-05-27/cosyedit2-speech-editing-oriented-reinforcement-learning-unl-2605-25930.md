---
title: "CosyEdit2: Speech-Editing-Oriented Reinforcement Learning Unlocks Better Zero-Shot TTS"
date: 2026-05-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音编辑"]
summary: "提出CosyEdit2，通过两阶段后训练框架（SFT+GRPO）提升语音编辑与零样本TTS性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音编辑</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#零样本TTS</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#GRPO</span> <span class="tag-pill tag-pill-soft">#语音编辑</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.25930</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://cjy1018.github.io/CosyEdit2" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">cjy1018.github.io/CosyEdit2</span></span></a><a class="oc-chip oc-chip-demo" href="https://cjy1018.github.io/CosyEdit2" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">cjy1018.github.io/CosyEdit2</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.25930" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.25930" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://cjy1018.github.io/CosyEdit2" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://cjy1018.github.io/CosyEdit2" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CosyEdit2，通过两阶段后训练框架（SFT+GRPO）提升语音编辑与零样本TTS性能。
</div>

## 👥 作者与机构

**Junyang Chen** ¹ · Yuhang Jia · Hui Wang · Jiaming Zhou · Yongchang Gan · Yong Qin

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音编辑和TTS研究者。建议通读，重点看§3两阶段训练框架和§4实验对比。可先看表1和表2了解性能提升。

## 🌍 研究背景

语音编辑和零样本TTS共享基于语音提示的条件生成基础，但语音编辑要求与未编辑内容保持严格的局部声学一致性。先前工作通过监督微调（SFT）使TTS模型获得编辑能力，但受限于不完美的配对数据和粗粒度优化信号。本文旨在解决这些瓶颈，提出基于目标语音无关数据的编辑导向GRPO训练。

## 💡 核心创新

1. 两阶段后训练框架：SFT初始化+GRPO优化
2. 编辑导向GRPO：利用目标语音无关数据进行强化学习
3. 揭示语音编辑与零样本TTS的深层互惠关系

## 🏗️ 模型架构

基于预训练TTS模型（如CosyVoice），第一阶段使用配对编辑数据进行SFT初始化，使模型具备基本编辑能力；第二阶段采用编辑导向GRPO，在无目标语音数据上优化，通过组相对策略梯度更新模型参数。输入为带编辑标记的语音和文本，输出为编辑后的语音。

## 📚 数据集

- LibriTTS（训练/评估，未明确规模）
- VCTK（评估）
- Seed-TTS test set（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS（自然度） | LibriTTS test | CosyVoice-SFT 3.8 | **4.2** | +0.4 |
| WER（编辑区域） | LibriTTS test | CosyVoice-SFT 5.2% | **3.1%** | -2.1% |
| MOS（零样本TTS） | Seed-TTS test | CosyVoice 3.9 | **4.3** | +0.4 |

CosyEdit2在语音编辑任务上显著优于SFT基线，MOS提升0.4，WER降低2.1%。在零样本TTS任务上也取得改进，MOS提升0.4。消融实验验证了GRPO的有效性。

## 🎯 结论与影响

CosyEdit2通过两阶段后训练框架有效提升了语音编辑和零样本TTS性能，揭示了二者之间的深层联系。该工作为语音编辑领域提供了新的训练范式，有望推动更自然的人机交互应用。

## ⚠️ 局限与未解决问题

摘要未提及推理延迟和模型参数量；实验仅在英语数据集上进行，跨语言泛化未知；未与最新语音编辑模型（如EditSpeech）对比；GRPO训练稳定性未讨论。

## 🔗 开源资源

- **项目主页**：<https://cjy1018.github.io/CosyEdit2>
- **Demo / 试听**：<https://cjy1018.github.io/CosyEdit2>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-27/">← 返回 2026-05-27 速递</a></div>
