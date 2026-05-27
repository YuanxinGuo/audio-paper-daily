---
title: "语音/音频论文速递 2026-05-27"
date: 2026-05-27T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 0 篇 · 最高分 8.5（#音乐信息检索）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">0</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音乐信息检索 | 1篇 | `██████████` |
| #语音编辑 | 1篇 | `██████████` |
| #音视频生成评估 | 1篇 | `██████████` |
| #手势生成 | 1篇 | `██████████` |
| #语音推理控制 | 1篇 | `██████████` |
| #语音生成 | 1篇 | `██████████` |
| #语音合成 | 1篇 | `██████████` |
| #音频理解 | 1篇 | `██████████` |

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
| 🥇 | [PHALAR: Phasors for Learned Musical Audio Representations](phalar-phasors-for-learned-musical-audio-representations-2605-03929/) | **8.5** | #音乐信息检索 |
| 🥈 | [CosyEdit2: Speech-Editing-Oriented Reinforcement Learning Un…](cosyedit2-speech-editing-oriented-reinforcement-learning-unl-2605-25930/) | **8.2** | #语音编辑 |
| 🥉 | [LongAV-Compass: Towards Unified Evaluation of Minute-Scale A…](longav-compass-towards-unified-evaluation-of-minute-scale-au-2605-26244/) | **8.2** | #音视频生成评估 |
| 4. | [DuoGesture: Neuro-Inspired and Biomechanically Informed Dual…](duogesture-neuro-inspired-and-biomechanically-informed-dual--2605-26236/) | **8.2** | #手势生成 |
| 5. | [Learning When to Think While Listening in Large Audio-Langua…](learning-when-to-think-while-listening-in-large-audio-langua-2605-27190/) | **7.8** | #语音推理控制 |
| 6. | [Can We Hear from Events? Generating Speech from Event Camera](can-we-hear-from-events-generating-speech-from-event-camera-2605-26672/) | **7.8** | #语音生成 |
| 7. | [ParsVoice: A Large-Scale Multi-Speaker Persian Speech Corpus…](parsvoice-a-large-scale-multi-speaker-persian-speech-corpus--2510-10774/) | **7.5** | #语音合成 |
| 8. | [MetaSICL: Adapting Audiroty LLM via Meta Speech In-Context L…](metasicl-adapting-audiroty-llm-via-meta-speech-in-context-le-2601-18904/) | **7.2** | #音频理解 |
| 9. | [Metric Analysis for Spatial Semantic Segmentation of Sound S…](metric-analysis-for-spatial-semantic-segmentation-of-sound-s-2511-07075/) | **7.2** | #音频评估指标 |
| 10. | [PashtoTTS-Bench: automated screening for low-resource non-La…](pashtotts-bench-automated-screening-for-low-resource-non-lat-2605-26978/) | **6.5** | #语音合成评估 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="phalar-phasors-for-learned-musical-audio-representations-2605-03929/">PHALAR: Phasors for Learned Musical Audio Representations</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">提出PHALAR对比学习框架，利用复值谱池化层实现音高和相位等变，在茎检索任务上以更少参数和更快训练速度大幅超越SOTA。</div>
<div class="card-action">
<a href="phalar-phasors-for-learned-musical-audio-representations-2605-03929/">详情 →</a> · <a href="https://arxiv.org/abs/2605.03929" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="cosyedit2-speech-editing-oriented-reinforcement-learning-unl-2605-25930/">CosyEdit2: Speech-Editing-Oriented Reinforcement Learning Unlocks Better Zero-Shot TTS</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音编辑</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出CosyEdit2，通过两阶段后训练框架（SFT+GRPO）提升语音编辑与零样本TTS性能。</div>
<div class="card-action">
<a href="cosyedit2-speech-editing-oriented-reinforcement-learning-unl-2605-25930/">详情 →</a> · <a href="https://arxiv.org/abs/2605.25930" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="longav-compass-towards-unified-evaluation-of-minute-scale-au-2605-26244/">LongAV-Compass: Towards Unified Evaluation of Minute-Scale Audio-Visual Generation Across T2AV, I2AV, and V2AV</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音视频生成评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个分钟级音视频生成统一评估基准LongAV-Compass，覆盖T2AV、I2AV、V2AV三种条件，含284个测试用例和20+细粒度评估维度。</div>
<div class="card-action">
<a href="longav-compass-towards-unified-evaluation-of-minute-scale-au-2605-26244/">详情 →</a> · <a href="https://arxiv.org/abs/2605.26244" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="duogesture-neuro-inspired-and-biomechanically-informed-dual--2605-26236/">DuoGesture: Neuro-Inspired and Biomechanically Informed Dual-Stream Co-Speech Gesture Generation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#手势生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出神经启发且生物力学知情的双流共语手势生成方法，将语义手势与节拍手势解耦，通过随机门控协调，提升语义表达与运动平滑性。</div>
<div class="card-action">
<a href="duogesture-neuro-inspired-and-biomechanically-informed-dual--2605-26236/">详情 →</a> · <a href="https://arxiv.org/abs/2605.26236" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="learning-when-to-think-while-listening-in-large-audio-langua-2605-27190/">Learning When to Think While Listening in Large Audio-Language Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音推理控制</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出可学习的等待-思考-回答控制机制，优化LALM在流式语音交互中的推理时机与响应延迟。</div>
<div class="card-action">
<a href="learning-when-to-think-while-listening-in-large-audio-langua-2605-27190/">详情 →</a> · <a href="https://arxiv.org/abs/2605.27190" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="can-we-hear-from-events-generating-speech-from-event-camera-2605-26672/">Can We Hear from Events? Generating Speech from Event Camera</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出EventSpeech框架，首次利用事件相机数据生成富有表现力的语音，解决RGB视频时间粒度不匹配问题。</div>
<div class="card-action">
<a href="can-we-hear-from-events-generating-speech-from-event-camera-2605-26672/">详情 →</a> · <a href="https://arxiv.org/abs/2605.26672" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="parsvoice-a-large-scale-multi-speaker-persian-speech-corpus--2510-10774/">ParsVoice: A Large-Scale Multi-Speaker Persian Speech Corpus for Text-to-Speech Synthesis</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">构建了目前最大的公开波斯语多说话人语音-文本语料库ParsVoice（2200小时），并验证其在零样本TTS中的有效性。</div>
<div class="card-action">
<a href="parsvoice-a-large-scale-multi-speaker-persian-speech-corpus--2510-10774/">详情 →</a> · <a href="https://arxiv.org/abs/2510.10774" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="metasicl-adapting-audiroty-llm-via-meta-speech-in-context-le-2601-18904/">MetaSICL: Adapting Audiroty LLM via Meta Speech In-Context Learning</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MetaSICL方法，通过元学习增强听觉大语言模型的上下文学习能力，在低资源任务上优于直接微调。</div>
<div class="card-action">
<a href="metasicl-adapting-audiroty-llm-via-meta-speech-in-context-le-2601-18904/">详情 →</a> · <a href="https://arxiv.org/abs/2601.18904" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="metric-analysis-for-spatial-semantic-segmentation-of-sound-s-2511-07075/">Metric Analysis for Spatial Semantic Segmentation of Sound Scenes</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频评估指标</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出CASA-SDR指标，通过置换不变源匹配分离分类与分离误差，更准确评估S5系统。</div>
<div class="card-action">
<a href="metric-analysis-for-spatial-semantic-segmentation-of-sound-s-2511-07075/">详情 →</a> · <a href="https://arxiv.org/abs/2511.07075" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="pashtotts-bench-automated-screening-for-low-resource-non-lat-2605-26978/">PashtoTTS-Bench: automated screening for low-resource non-Latin-script text-to-speech</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音合成评估</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出INSV-A自动筛选框架用于低资源非拉丁文字TTS评估，并构建普什图语基准PashtoTTS-Bench。</div>
<div class="card-action">
<a href="pashtotts-bench-automated-screening-for-low-resource-non-lat-2605-26978/">详情 →</a> · <a href="https://arxiv.org/abs/2605.26978" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
