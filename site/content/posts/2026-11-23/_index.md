---
title: "语音/音频论文速递 2026-11-23"
date: 2026-11-23T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 8.8（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">1</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音频伪造检测 | 2篇 | `██████████` |
| #语音合成 | 2篇 | `██████████` |
| #目标说话人提取 | 1篇 | `█████` |
| #音频水印 | 1篇 | `█████` |
| #语音-语言模型评测 | 1篇 | `█████` |
| #光学音乐识别 | 1篇 | `█████` |
| #音频事件检测 | 1篇 | `█████` |
| #音频处理 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://ieeexplore.ieee.org/document/6932438" target="_blank" rel="noopener">A Regression Approach to Speech Enhancement Based on Deep Neural Networks</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">TASLP 2015</span>
<span class="tag-pill tag-pill-soft">#语音增强</span>
</div>
<div class="card-tldr">首次系统验证 DNN 直接回归对数功率谱的语音增强范式，奠定后续大量 mask / mapping 方法的基础。</div>
<div class="card-authors">Yong Xu, Jun Du, Li-Rong Dai, Chin-Hui Lee</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1809.07454" target="_blank" rel="noopener">Conv-TasNet: Surpassing Ideal Time-Frequency Magnitude Masking</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">TASLP 2019</span>
<span class="tag-pill tag-pill-soft">#语音增强</span>
</div>
<div class="card-tldr">时域端到端分离/增强里程碑，证明 1D 卷积可超越 STFT 域 IRM/IBM 上限。</div>
<div class="card-authors">Yi Luo, Nima Mesgarani</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="the-voice-on-the-line-2610-35272/">The Voice on the Line</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">用因果掩码Transformer从通话中自注册目标说话人，蒸馏出22M/9.8M小模型在CPU单线程实时运行，显著降低WER。</div>
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
| 🥇 | [The Voice on the Line](the-voice-on-the-line-2610-35272/) 🎯 | **8.8** | #目标说话人提取 |
| 🥈 | [Neural Defend ARCAS 290M: A Robust Foundation Model for AI-G…](neural-defend-arcas-290m-a-robust-foundation-model-for-ai-ge-2611-27784/) | **7.8** | #音频伪造检测 |
| 🥉 | [Asymmetric Phase Coding Audio Watermarking](asymmetric-phase-coding-audio-watermarking-2605-07241/) | **7.8** | #音频水印 |
| 4. | [SLP-Bench: Evaluating and Improving Acoustic Claims of Reaso…](slp-bench-evaluating-and-improving-acoustic-claims-of-reason-2611-27810/) | **7.2** | #语音-语言模型评测 |
| 5. | [PromptTTSD: Controllable Text to Spoken Dialogue Synthesis w…](promptttsd-controllable-text-to-spoken-dialogue-synthesis-wi-2611-27601/) | **7.2** | #语音合成 |
| 6. | [EAF-TTS: Rethinking Codec-Latent Coordinates for Flow TTS](eaf-tts-rethinking-codec-latent-coordinates-for-flow-tts-2611-27214/) | **6.8** | #语音合成 |
| 7. | [A Novel Dataset and Framework for Schenkerian Optical Music …](a-novel-dataset-and-framework-for-schenkerian-optical-music--2611-26958/) | **6.8** | #光学音乐识别 |
| 8. | [Impact of Edge Software Evolution on Audio Tagging Models: A…](impact-of-edge-software-evolution-on-audio-tagging-models-an-2611-26831/) | **6.0** | #音频事件检测 |
| 9. | [Neural Defend Ranks #1 in Global Audio Deepfake Detection Be…](neural-defend-ranks-1-in-global-audio-deepfake-detection-ben-2611-27215/) | **5.5** | #音频伪造检测 |
| 10. | [Windchime: an Audiovisual Installation with Audio-Language M…](windchime-an-audiovisual-installation-with-audio-language-mo-2611-26759/) | **3.0** | #音频处理 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="the-voice-on-the-line-2610-35272/">The Voice on the Line</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用因果掩码Transformer从通话中自注册目标说话人，蒸馏出22M/9.8M小模型在CPU单线程实时运行，显著降低WER。</div>
<div class="card-action">
<a href="the-voice-on-the-line-2610-35272/">详情 →</a> · <a href="https://arxiv.org/abs/2610.35272" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="neural-defend-arcas-290m-a-robust-foundation-model-for-ai-ge-2611-27784/">Neural Defend ARCAS 290M: A Robust Foundation Model for AI-Generated Audio Detection</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出290M参数冻结基础模型ARCAS 290M，零样本跨生成器、信道、语言检测AI生成音频，在十个公开基准上大幅超越现有检测器。</div>
<div class="card-action">
<a href="neural-defend-arcas-290m-a-robust-foundation-model-for-ai-ge-2611-27784/">详情 →</a> · <a href="https://arxiv.org/abs/2611.27784" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="asymmetric-phase-coding-audio-watermarking-2605-07241/">Asymmetric Phase Coding Audio Watermarking</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频水印</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出免训练的非对称相位编码音频水印，用Ed25519签名+RS纠错+QIM，盲提取且可离线验证来源。</div>
<div class="card-action">
<a href="asymmetric-phase-coding-audio-watermarking-2605-07241/">详情 →</a> · <a href="https://arxiv.org/abs/2605.07241" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="slp-bench-evaluating-and-improving-acoustic-claims-of-reason-2611-27810/">SLP-Bench: Evaluating and Improving Acoustic Claims of Reasoning Audio Language Models on Clinical Speech</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音-语言模型评测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 SLP-Bench，逐条核查推理音频语言模型思维链中的声学断言是否与临床医生感知评分一致，并用 GRPO 微调提升断言准确率。</div>
<div class="card-action">
<a href="slp-bench-evaluating-and-improving-acoustic-claims-of-reason-2611-27810/">详情 →</a> · <a href="https://arxiv.org/abs/2611.27810" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="promptttsd-controllable-text-to-spoken-dialogue-synthesis-wi-2611-27601/">PromptTTSD: Controllable Text to Spoken Dialogue Synthesis with Open-Ended Text Descriptions</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">从多播讲有声书构建带开放式风格描述的对话语音数据集PromptDialog，并提出支持零样本克隆与自然语言风格控制的对话合成模型PromptTTSD。</div>
<div class="card-action">
<a href="promptttsd-controllable-text-to-spoken-dialogue-synthesis-wi-2611-27601/">详情 →</a> · <a href="https://arxiv.org/abs/2611.27601" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="eaf-tts-rethinking-codec-latent-coordinates-for-flow-tts-2611-27214/">EAF-TTS: Rethinking Codec-Latent Coordinates for Flow TTS</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">在ELF流式TTS的codec潜空间上引入固定ZCA坐标协议，改善从各向同性高斯采样的生成几何，提升自然度代理指标并降低推理RTF。</div>
<div class="card-action">
<a href="eaf-tts-rethinking-codec-latent-coordinates-for-flow-tts-2611-27214/">详情 →</a> · <a href="https://arxiv.org/abs/2611.27214" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="a-novel-dataset-and-framework-for-schenkerian-optical-music--2611-26958/">A Novel Dataset and Framework for Schenkerian Optical Music Recognition</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#光学音乐识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出首个手写申克分析标注数据集，并用集成检测与拓扑网络实现申克图的光学识别与排版。</div>
<div class="card-action">
<a href="a-novel-dataset-and-framework-for-schenkerian-optical-music--2611-26958/">详情 →</a> · <a href="https://arxiv.org/abs/2611.26958" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="impact-of-edge-software-evolution-on-audio-tagging-models-an-2611-26831/">Impact of Edge Software Evolution on Audio Tagging Models: An Empirical Study on NVIDIA Jetson Orin Nano</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音频事件检测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在 Jetson Orin Nano 上对比 JetPack 6.2/7.2 两代软件栈对 PANNs、AST、PaSST 音频标记模型推理延迟与能耗的影响。</div>
<div class="card-action">
<a href="impact-of-edge-software-evolution-on-audio-tagging-models-an-2611-26831/">详情 →</a> · <a href="https://arxiv.org/abs/2611.26831" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="neural-defend-ranks-1-in-global-audio-deepfake-detection-ben-2611-27215/">Neural Defend Ranks #1 in Global Audio Deepfake Detection Benchmark - ARCAS on the Podonos Independent Leaderboard</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">Neural Defend 的 ARCAS 基础模型在 Podonos 独立榜单上并列第一，优于多家商用检测器，并给出完整评测协议与五轮榜单历史。</div>
<div class="card-action">
<a href="neural-defend-ranks-1-in-global-audio-deepfake-detection-ben-2611-27215/">详情 →</a> · <a href="https://arxiv.org/abs/2611.27215" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="windchime-an-audiovisual-installation-with-audio-language-mo-2611-26759/">Windchime: an Audiovisual Installation with Audio-Language Model implementations</a>
<div class="card-meta">
<span class="card-score">3.0</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">一个语音驱动的视听装置，用本地ASR与音频语言模型对406个音频stem做检索，生成声景与交互动画。</div>
<div class="card-action">
<a href="windchime-an-audiovisual-installation-with-audio-language-mo-2611-26759/">详情 →</a> · <a href="https://arxiv.org/abs/2611.26759" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
