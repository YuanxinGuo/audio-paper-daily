---
title: "语音/音频论文速递 2026-11-11"
date: 2026-11-11T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 8.8（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音合成 | 3篇 | `██████████` |
| #双耳音频 | 1篇 | `███` |
| #语音增强 | 1篇 | `███` |
| #音频理解 | 1篇 | `███` |
| #音频取证 | 1篇 | `███` |
| #对话轮次预测 | 1篇 | `███` |
| #音频表征学习 | 1篇 | `███` |
| #语音识别 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="gigaedge-spench-an-sdk-for-practical-streaming-speech-enhanc-2611-13243/">GigaEdge Spench: An SDK for Practical Streaming Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">开源流式语音增强SDK，集成降噪、归一化、重采样与回声消除，支持CPU/移动端/浏览器多平台部署。</div>
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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="aura-auditory-spatial-intelligence-via-a-unified-representat-2611-13687/">AURA: Auditory Spatial Intelligence via a Unified Representation from a General-Audio Encoder through Complete Alignment</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">冻结通用音频编解码器与语言模型，通过完整场景描述与通道差对齐，实现双源空间方位问答。</div>
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
| 🥇 | [AURA: Auditory Spatial Intelligence via a Unified Representa…](aura-auditory-spatial-intelligence-via-a-unified-representat-2611-13687/) 🎯 | **8.8** | #双耳音频 |
| 🥈 | [GigaEdge Spench: An SDK for Practical Streaming Speech Enhan…](gigaedge-spench-an-sdk-for-practical-streaming-speech-enhanc-2611-13243/) 🎯 | **7.8** | #语音增强 |
| 🥉 | [Machine Hearing: Can Audio LLMs Generalize Beyond Human Audi…](machine-hearing-can-audio-llms-generalize-beyond-human-audit-2611-10693/) | **7.2** | #音频理解 |
| 4. | [Ninada: Sub-Clause Split-Graph VITS Streaming and Capability…](ninada-sub-clause-split-graph-vits-streaming-and-capability--2611-10035/) | **6.8** | #语音合成 |
| 5. | [GRIDEX: Region-Grounded Forensic Explanations for Vocoder-Ba…](gridex-region-grounded-forensic-explanations-for-vocoder-bas-2606-18738/) | **6.8** | #音频取证 |
| 6. | [AVCC: Audio-Visual Conversation Corpus for Turn-Taking Predi…](avcc-audio-visual-conversation-corpus-for-turn-taking-predic-2611-13957/) | **6.8** | #对话轮次预测 |
| 7. | [Alania-2: Turkish text-to-speech with instant and fine-tuned…](alania-2-turkish-text-to-speech-with-instant-and-fine-tuned--2611-13845/) | **6.8** | #语音合成 |
| 8. | [Exploring Post-Hoc Disentanglement of Audio Foundation Model…](exploring-post-hoc-disentanglement-of-audio-foundation-model-2611-14415/) | **6.8** | #音频表征学习 |
| 9. | [A Factorial Ablation of a Speech-to-SFT Pipeline: Differenti…](a-factorial-ablation-of-a-speech-to-sft-pipeline-differentia-2608-20394/) | **6.2** | #语音识别 |
| 10. | [Antalia-2 Mini: A 7.6-million-parameter Turkish text-to-spee…](antalia-2-mini-a-7-6-million-parameter-turkish-text-to-speec-2611-13811/) | **5.8** | #语音合成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="aura-auditory-spatial-intelligence-via-a-unified-representat-2611-13687/">AURA: Auditory Spatial Intelligence via a Unified Representation from a General-Audio Encoder through Complete Alignment</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">冻结通用音频编解码器与语言模型，通过完整场景描述与通道差对齐，实现双源空间方位问答。</div>
<div class="card-action">
<a href="aura-auditory-spatial-intelligence-via-a-unified-representat-2611-13687/">详情 →</a> · <a href="https://arxiv.org/abs/2611.13687" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="gigaedge-spench-an-sdk-for-practical-streaming-speech-enhanc-2611-13243/">GigaEdge Spench: An SDK for Practical Streaming Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">开源流式语音增强SDK，集成降噪、归一化、重采样与回声消除，支持CPU/移动端/浏览器多平台部署。</div>
<div class="card-action">
<a href="gigaedge-spench-an-sdk-for-practical-streaming-speech-enhanc-2611-13243/">详情 →</a> · <a href="https://arxiv.org/abs/2611.13243" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="machine-hearing-can-audio-llms-generalize-beyond-human-audit-2611-10693/">Machine Hearing: Can Audio LLMs Generalize Beyond Human Auditory Perception?</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出机器听觉基准MHB（13任务7领域6128条）并指出Audio LLM零样本迁移差，进而提出轻量编码器MachEar扩展感知范围。</div>
<div class="card-action">
<a href="machine-hearing-can-audio-llms-generalize-beyond-human-audit-2611-10693/">详情 →</a> · <a href="https://arxiv.org/abs/2611.10693" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="ninada-sub-clause-split-graph-vits-streaming-and-capability--2611-10035/">Ninada: Sub-Clause Split-Graph VITS Streaming and Capability-Routed 24 kHz Speech Synthesis Across Twelve Scripts</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">Ninada 将 VITS ONNX 按子句切分并流式执行，配合能力路由的 48 个检查点，在浏览器与移动端实现 24 kHz 多文字 TTS 低延迟合成。</div>
<div class="card-action">
<a href="ninada-sub-clause-split-graph-vits-streaming-and-capability--2611-10035/">详情 →</a> · <a href="https://arxiv.org/abs/2611.10035" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="gridex-region-grounded-forensic-explanations-for-vocoder-bas-2606-18738/">GRIDEX: Region-Grounded Forensic Explanations for Vocoder-Based Synthetic Speech</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频取证</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">GRIDEX 对声码器合成语音的频谱图定位异常区域，并用 VLM 生成结构化取证解释。</div>
<div class="card-action">
<a href="gridex-region-grounded-forensic-explanations-for-vocoder-bas-2606-18738/">详情 →</a> · <a href="https://arxiv.org/abs/2606.18738" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="avcc-audio-visual-conversation-corpus-for-turn-taking-predic-2611-13957/">AVCC: Audio-Visual Conversation Corpus for Turn-Taking Prediction with a Human Benchmark</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#对话轮次预测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">构建AVCC音视频对话语料库，用于多人对话下一说话人预测基准，并给出人类表现参考。</div>
<div class="card-action">
<a href="avcc-audio-visual-conversation-corpus-for-turn-taking-predic-2611-13957/">详情 →</a> · <a href="https://arxiv.org/abs/2611.13957" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="alania-2-turkish-text-to-speech-with-instant-and-fine-tuned--2611-13845/">Alania-2: Turkish text-to-speech with instant and fine-tuned voice cloning</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">Alania-2 是 488M 参数的土耳其语 TTS 系统，基于 VoxCPM 架构，支持文本描述音色设计与两种声音克隆，并开源评测工具与三个数据集。</div>
<div class="card-action">
<a href="alania-2-turkish-text-to-speech-with-instant-and-fine-tuned--2611-13845/">详情 →</a> · <a href="https://arxiv.org/abs/2611.13845" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="exploring-post-hoc-disentanglement-of-audio-foundation-model-2611-14415/">Exploring Post-Hoc Disentanglement of Audio Foundation Models for Music Similarity</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频表征学习</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">将条件相似度网络（CSN）后置适配到冻结的 CLAP/MuQ/MERT 嵌入上，用可学习掩码门控实现音乐属性的解耦检索。</div>
<div class="card-action">
<a href="exploring-post-hoc-disentanglement-of-audio-foundation-model-2611-14415/">详情 →</a> · <a href="https://arxiv.org/abs/2611.14415" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="a-factorial-ablation-of-a-speech-to-sft-pipeline-differentia-2608-20394/">A Factorial Ablation of a Speech-to-SFT Pipeline: Differential Effects on Data Quality and Downstream Transfer</a>
<div class="card-meta">
<span class="card-score">6.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">对语音转SFT数据流水线做2x2因子消融，发现QA数据质量提升并不均匀转化为下游MCQA收益。</div>
<div class="card-action">
<a href="a-factorial-ablation-of-a-speech-to-sft-pipeline-differentia-2608-20394/">详情 →</a> · <a href="https://arxiv.org/abs/2608.20394" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="antalia-2-mini-a-7-6-million-parameter-turkish-text-to-speec-2611-13811/">Antalia-2 Mini: A 7.6-million-parameter Turkish text-to-speech model trained entirely on synthetic speech</a>
<div class="card-meta">
<span class="card-score">5.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">7.6M 参数土耳其单说话人 TTS，全部用 VoxCPM2 合成语音蒸馏训练，48kHz 输出，WER 1.09%。</div>
<div class="card-action">
<a href="antalia-2-mini-a-7-6-million-parameter-turkish-text-to-speec-2611-13811/">详情 →</a> · <a href="https://arxiv.org/abs/2611.13811" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
