---
title: "语音/音频论文速递 2026-08-20"
date: 2026-08-20T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 8 篇 · 重点领域 0 篇 · 最高分 8.2（#语音生成）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">8</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">0</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音识别 | 2篇 | `██████████` |
| #语音生成 | 1篇 | `█████` |
| #语音情感分析 | 1篇 | `█████` |
| #音乐理解 | 1篇 | `█████` |
| #伪造语音检测 | 1篇 | `█████` |
| #对话系统 | 1篇 | `█████` |
| #说话人日志 | 1篇 | `█████` |

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
| 🥇 | [FireRedTTS3: Unified Speech Generation and Editing with Sema…](fireredtts3-unified-speech-generation-and-editing-with-seman-2608-17492/) | **8.2** | #语音生成 |
| 🥈 | [The Null Token Knows: Reducing Message-Free Hallucination in…](the-null-token-knows-reducing-message-free-hallucination-in--2608-15940/) | **7.2** | #语音识别 |
| 🥉 | [Language Family Matters: Evaluating LLM-Based ASR Across Lin…](language-family-matters-evaluating-llm-based-asr-across-ling-2601-18899/) | **7.2** | #语音识别 |
| 4. | [SpeechSense: A Paralinguistic-Focused Dataset for Fine-Grain…](speechsense-a-paralinguistic-focused-dataset-for-fine-graine-2608-17931/) | **7.2** | #语音情感分析 |
| 5. | [UniVerse: Benchmarking and Enhancing LALMs on Culturally Inc…](universe-benchmarking-and-enhancing-lalms-on-culturally-incl-2608-17852/) | **7.2** | #音乐理解 |
| 6. | [The Last Mile of Deepfake Speech Detection: An Industry-Acad…](the-last-mile-of-deepfake-speech-detection-an-industry-acade-2608-17585/) | **7.2** | #伪造语音检测 |
| 7. | [Multi-turn Conversational AI from Text to Multimodal Interac…](multi-turn-conversational-ai-from-text-to-multimodal-interac-2608-17605/) | **7.0** | #对话系统 |
| 8. | [Target Speaker Identification: A Low-Latency Streaming Pipel…](target-speaker-identification-a-low-latency-streaming-pipeli-2608-17972/) | **6.8** | #说话人日志 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="fireredtts3-unified-speech-generation-and-editing-with-seman-2608-17492/">FireRedTTS3: Unified Speech Generation and Editing with Semantically Enriched Speech Representations</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">FireRedTTS3通过冻结的语义教师网络正则化连续语音表示，实现稳定可控的语音生成与编辑，在多项基准上取得最优。</div>
<div class="card-action">
<a href="fireredtts3-unified-speech-generation-and-editing-with-seman-2608-17492/">详情 →</a> · <a href="https://arxiv.org/abs/2608.17492" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="the-null-token-knows-reducing-message-free-hallucination-in--2608-15940/">The Null Token Knows: Reducing Message-Free Hallucination in ASR and NMT</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过分析ASR和NMT模型中空标记的分数，提出利用空标记分数作为弃权信号来抑制无消息幻觉，并强调评估时应同时考虑抑制和删除成本。</div>
<div class="card-action">
<a href="the-null-token-knows-reducing-message-free-hallucination-in--2608-15940/">详情 →</a> · <a href="https://arxiv.org/abs/2608.15940" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="language-family-matters-evaluating-llm-based-asr-across-ling-2601-18899/">Language Family Matters: Evaluating LLM-Based ASR Across Linguistic Boundaries</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于语言家族共享连接器的多语言ASR策略，减少参数并提升跨域泛化。</div>
<div class="card-action">
<a href="language-family-matters-evaluating-llm-based-asr-across-ling-2601-18899/">详情 →</a> · <a href="https://arxiv.org/abs/2601.18899" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="speechsense-a-paralinguistic-focused-dataset-for-fine-graine-2608-17931/">SpeechSense: A Paralinguistic-Focused Dataset for Fine-Grained Speech Sentiment Analysis</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音情感分析</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SpeechSense数据集，聚焦通过韵律线索检测八类人际立场，验证声学信息在细粒度语音情感分析中的关键作用。</div>
<div class="card-action">
<a href="speechsense-a-paralinguistic-focused-dataset-for-fine-graine-2608-17931/">详情 →</a> · <a href="https://arxiv.org/abs/2608.17931" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="universe-benchmarking-and-enhancing-lalms-on-culturally-incl-2608-17852/">UniVerse: Benchmarking and Enhancing LALMs on Culturally Inclusive Low-Resource Music Understanding</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出UniVerse，包含基准UniVerseBench和训练集UniVerseSet，用于提升大音频语言模型在低资源民间音乐理解上的表现。</div>
<div class="card-action">
<a href="universe-benchmarking-and-enhancing-lalms-on-culturally-incl-2608-17852/">详情 →</a> · <a href="https://arxiv.org/abs/2608.17852" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="the-last-mile-of-deepfake-speech-detection-an-industry-acade-2608-17585/">The Last Mile of Deepfake Speech Detection: An Industry-Academia Experience Report</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#伪造语音检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文基于与Phonexia三年的合作经验，报告了深度伪造语音检测从研究到部署的障碍，并提出研究协调建议。</div>
<div class="card-action">
<a href="the-last-mile-of-deepfake-speech-detection-an-industry-acade-2608-17585/">详情 →</a> · <a href="https://arxiv.org/abs/2608.17585" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="multi-turn-conversational-ai-from-text-to-multimodal-interac-2608-17605/">Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#对话系统</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">综述多轮对话AI从文本到多模态的发展，涵盖数据、模型、评估与挑战，指出多模态能力进步快于持续交互能力。</div>
<div class="card-action">
<a href="multi-turn-conversational-ai-from-text-to-multimodal-interac-2608-17605/">详情 →</a> · <a href="https://arxiv.org/abs/2608.17605" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="target-speaker-identification-a-low-latency-streaming-pipeli-2608-17972/">Target Speaker Identification: A Low-Latency Streaming Pipeline</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#说话人日志</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一个低延迟流式目标说话人识别流水线，结合流式说话人日志与验证，在播客数据上验证了实时助听器应用的可行性。</div>
<div class="card-action">
<a href="target-speaker-identification-a-low-latency-streaming-pipeli-2608-17972/">详情 →</a> · <a href="https://arxiv.org/abs/2608.17972" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
