---
title: "语音/音频论文速递 2026-07-23"
date: 2026-07-23T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.5（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #关键词唤醒 | 2篇 | `██████████` |
| #痴呆症检测 | 1篇 | `█████` |
| #语音语言模型推理 | 1篇 | `█████` |
| #音频推理 | 1篇 | `█████` |
| #假音频检测 | 1篇 | `█████` |
| #音频编辑 | 1篇 | `█████` |
| #人机交互 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="schr-odinger-bridge-mamba-for-one-step-speech-enhancement-2510-16834/">Schr\"odinger Bridge Mamba for One-Step Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出Schrödinger Bridge Mamba，结合SB训练范式与Mamba架构，实现单步推理的高效语音增强。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="caps-a-cascaded-reconstruction-model-to-power-saving-in-hear-2607-19434/">CAPS: A Cascaded Reconstruction Model to Power Saving in Hearables Using Sub-Nyquist Sampling with Bandwidth Extension</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出CAPS级联重建模型，通过子奈奎斯特采样和低比特量化降低功耗3.3倍，同时保持语音可懂度。</div>
</div></div>

### #目标说话人提取

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1810.04826" target="_blank" rel="noopener">VoiceFilter: Targeted Voice Separation by Speaker-Conditioned Spectrogram Masking</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">Interspeech 2019</span>
<span class="tag-pill tag-pill-soft">#目标说话人提取</span>
</div>
<div class="card-tldr">基于 d-vector 条件化的时频域目标说话人提取代表作，TSE 领域绕不开的基线。</div>
<div class="card-authors">Quan Wang, Hannah Muckenhirn, Kevin Wilson, et al.</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/2005.04686" target="_blank" rel="noopener">SpEx+: A Complete Time Domain Speaker Extraction Network</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">Interspeech 2020</span>
<span class="tag-pill tag-pill-soft">#目标说话人提取</span>
</div>
<div class="card-tldr">时域 TSE 系列里程碑，多尺度编码器 + 共享说话人编码器，长期占据 SOTA。</div>
<div class="card-authors">Meng Ge, Chenglin Xu, Longbiao Wang, Eng Siong Chng, Jianwu Dang, Haizhou Li</div>
</div></div>

### #语音分离

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1508.04306" target="_blank" rel="noopener">Deep Clustering: Discriminative Embeddings for Segmentation and Separation</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ICASSP 2016</span>
<span class="tag-pill tag-pill-soft">#语音分离</span>
</div>
<div class="card-tldr">用嵌入聚类绕开 permutation 问题的开山之作，SS 领域必读。</div>
<div class="card-authors">John R. Hershey, Zhuo Chen, Jonathan Le Roux, Shinji Watanabe</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1607.00325" target="_blank" rel="noopener">Permutation Invariant Training of Deep Models for Speaker-Independent Multi-talker Speech Separation</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ICASSP 2017</span>
<span class="tag-pill tag-pill-soft">#语音分离</span>
</div>
<div class="card-tldr">PIT 提出，至今仍是大多数分离/TSE 工作的训练目标。</div>
<div class="card-authors">Dong Yu, Morten Kolbæk, Zheng-Hua Tan, Jesper Jensen</div>
</div></div>

### #双耳音频

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/2111.10882" target="_blank" rel="noopener">Binaural Audio Generation via Multi-task Learning</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ACM TOG 2021</span>
<span class="tag-pill tag-pill-soft">#双耳音频</span>
</div>
<div class="card-tldr">联合 mono-to-binaural 与几何信息预测，提升合成空间感。</div>
<div class="card-authors">Sijia Li, Sagar Vaze, et al.</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1812.04204" target="_blank" rel="noopener">2.5D Visual Sound</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">CVPR 2019</span>
<span class="tag-pill tag-pill-soft">#双耳音频</span>
</div>
<div class="card-tldr">用单视频引导 mono → binaural，视听双耳音频合成开创性工作。</div>
<div class="card-authors">Ruohan Gao, Kristen Grauman</div>
</div></div>

### #乐器分离

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://archives.ismir.net/ismir2017/paper/000171.pdf" target="_blank" rel="noopener">Singing Voice Separation with Deep U-Net Convolutional Networks</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ISMIR 2017</span>
<span class="tag-pill tag-pill-soft">#乐器分离</span>
</div>
<div class="card-tldr">Spotify 的 U-Net 人声分离，奠定频域 MSS 主流框架。</div>
<div class="card-authors">Andreas Jansson, Eric Humphrey, Nicola Montecchio, et al.</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1906.04032" target="_blank" rel="noopener">Open-Unmix - A Reference Implementation for Music Source Separation</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">JOSS 2019</span>
<span class="tag-pill tag-pill-soft">#乐器分离</span>
</div>
<div class="card-tldr">MUSDB18 上最常被引的开源基线，BLSTM 频域分离的「教科书」实现。</div>
<div class="card-authors">Fabian-Robert Stöter, Stefan Uhlich, Antoine Liutkus, Yuki Mitsufuji</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Schr\"odinger Bridge Mamba for One-Step Speech Enhancement](schr-odinger-bridge-mamba-for-one-step-speech-enhancement-2510-16834/) 🎯 | **9.5** | #语音增强 |
| 🥈 | [LoRA-Tuned Large Language Models for Dementia Detection via …](lora-tuned-large-language-models-for-dementia-detection-via--2606-28445/) | **7.8** | #痴呆症检测 |
| 🥉 | [Efficient Chain-of-Modality Reasoning via Progressive Compre…](efficient-chain-of-modality-reasoning-via-progressive-compre-2607-19932/) | **7.8** | #语音语言模型推理 |
| 4. | [Audio-Zero: Label-Free Self-Evolution for Fine-Grained Audio…](audio-zero-label-free-self-evolution-for-fine-grained-audio--2607-20166/) | **7.8** | #音频推理 |
| 5. | [Layer-Wise Decision Fusion for Fake Audio Detection Using XL…](layer-wise-decision-fusion-for-fake-audio-detection-using-xl-2607-20023/) | **7.8** | #假音频检测 |
| 6. | [CAPS: A Cascaded Reconstruction Model to Power Saving in Hea…](caps-a-cascaded-reconstruction-model-to-power-saving-in-hear-2607-19434/) 🎯 | **7.5** | #语音增强 |
| 7. | [Cumsum-Composable Phase Transport for Low-Cost Streaming Key…](cumsum-composable-phase-transport-for-low-cost-streaming-key-2607-20086/) | **7.2** | #关键词唤醒 |
| 8. | [Scalable Keyword Spotting via Modular Network Expansion](scalable-keyword-spotting-via-modular-network-expansion-2607-19918/) | **7.2** | #关键词唤醒 |
| 9. | [RIME: Enabling Large-Scale Agentic Post-Production](rime-enabling-large-scale-agentic-post-production-2607-19605/) | **7.2** | #音频编辑 |
| 10. | [Validating the Single Item Kawaii Measure](validating-the-single-item-kawaii-measure-2607-19352/) | **5.5** | #人机交互 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="schr-odinger-bridge-mamba-for-one-step-speech-enhancement-2510-16834/">Schr\"odinger Bridge Mamba for One-Step Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Schrödinger Bridge Mamba，结合SB训练范式与Mamba架构，实现单步推理的高效语音增强。</div>
<div class="card-action">
<a href="schr-odinger-bridge-mamba-for-one-step-speech-enhancement-2510-16834/">详情 →</a> · <a href="https://arxiv.org/abs/2510.16834" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="lora-tuned-large-language-models-for-dementia-detection-via--2606-28445/">LoRA-Tuned Large Language Models for Dementia Detection via Multi-View Speech-Derived Features</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#痴呆症检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出用LoRA微调LLM，融合ASR转录、停顿标记、话题线索、时间流畅度和音序等多视图语音特征进行痴呆症检测，在ADReSSo上F1达90.14%。</div>
<div class="card-action">
<a href="lora-tuned-large-language-models-for-dementia-detection-via--2606-28445/">详情 →</a> · <a href="https://arxiv.org/abs/2606.28445" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="efficient-chain-of-modality-reasoning-via-progressive-compre-2607-19932/">Efficient Chain-of-Modality Reasoning via Progressive Compression for Spoken Language Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音语言模型推理</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出ECoM推理框架，通过渐进式压缩将文本推理融入口语语言模型，在口语数学问答上提升准确率并减少token开销。</div>
<div class="card-action">
<a href="efficient-chain-of-modality-reasoning-via-progressive-compre-2607-19932/">详情 →</a> · <a href="https://arxiv.org/abs/2607.19932" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="audio-zero-label-free-self-evolution-for-fine-grained-audio--2607-20166/">Audio-Zero: Label-Free Self-Evolution for Fine-Grained Audio Reasoning</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频推理</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出无标签自进化框架Audio-Zero，通过听觉自博弈游戏提升大音频语言模型的细粒度推理能力。</div>
<div class="card-action">
<a href="audio-zero-label-free-self-evolution-for-fine-grained-audio--2607-20166/">详情 →</a> · <a href="https://arxiv.org/abs/2607.20166" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="layer-wise-decision-fusion-for-fake-audio-detection-using-xl-2607-20023/">Layer-Wise Decision Fusion for Fake Audio Detection Using XLS-R</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#假音频检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出层间决策融合方法，利用XLS-R多层表示进行假音频检测，在In-the-Wild数据集上取得6.90% EER。</div>
<div class="card-action">
<a href="layer-wise-decision-fusion-for-fake-audio-detection-using-xl-2607-20023/">详情 →</a> · <a href="https://arxiv.org/abs/2607.20023" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="caps-a-cascaded-reconstruction-model-to-power-saving-in-hear-2607-19434/">CAPS: A Cascaded Reconstruction Model to Power Saving in Hearables Using Sub-Nyquist Sampling with Bandwidth Extension</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出CAPS级联重建模型，通过子奈奎斯特采样和低比特量化降低功耗3.3倍，同时保持语音可懂度。</div>
<div class="card-action">
<a href="caps-a-cascaded-reconstruction-model-to-power-saving-in-hear-2607-19434/">详情 →</a> · <a href="https://arxiv.org/abs/2607.19434" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="cumsum-composable-phase-transport-for-low-cost-streaming-key-2607-20086/">Cumsum-Composable Phase Transport for Low-Cost Streaming Keyword Spotting</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#关键词唤醒</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一种基于累积和可组合相位传输的流式关键词唤醒层，通过酉旋转和前缀差分实现高效训练与推理。</div>
<div class="card-action">
<a href="cumsum-composable-phase-transport-for-low-cost-streaming-key-2607-20086/">详情 →</a> · <a href="https://arxiv.org/abs/2607.20086" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="scalable-keyword-spotting-via-modular-network-expansion-2607-19918/">Scalable Keyword Spotting via Modular Network Expansion</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#关键词唤醒</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一种参数受限的模块化扩展方法，在冻结基网络的同时训练轻量扩展分支，实现新关键词的增量添加，降低误拒率并减少计算开销。</div>
<div class="card-action">
<a href="scalable-keyword-spotting-via-modular-network-expansion-2607-19918/">详情 →</a> · <a href="https://arxiv.org/abs/2607.19918" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="rime-enabling-large-scale-agentic-post-production-2607-19605/">RIME: Enabling Large-Scale Agentic Post-Production</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频编辑</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出RIME框架，通过规则生成音乐编辑指令-音频对，用于训练和评估多模态智能体在后期制作任务上的能力。</div>
<div class="card-action">
<a href="rime-enabling-large-scale-agentic-post-production-2607-19605/">详情 →</a> · <a href="https://arxiv.org/abs/2607.19605" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="validating-the-single-item-kawaii-measure-2607-19352/">Validating the Single Item Kawaii Measure</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#人机交互</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">验证单题项可爱度量表在语音和视觉感知中的效度与信度，基于9个数据集和967名参与者。</div>
<div class="card-action">
<a href="validating-the-single-item-kawaii-measure-2607-19352/">详情 →</a> · <a href="https://arxiv.org/abs/2607.19352" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
