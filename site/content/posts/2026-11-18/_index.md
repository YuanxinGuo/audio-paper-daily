---
title: "语音/音频论文速递 2026-11-18"
date: 2026-11-18T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.2（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #音乐生成 | 2篇 | `██████████` |
| #语音识别 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #语音伪造检测 | 1篇 | `█████` |
| #多模态语音理解 | 1篇 | `█████` |
| #脑电语音解码 | 1篇 | `█████` |
| #生物声学 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="back-to-mel-learning-to-bridge-fidelity-and-perception-in-ge-2611-22628/">Back to Mel: Learning to Bridge Fidelity and Perception in Generative Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">以Mel频谱为结构化表示，用flow matching框架BAME在保真度、感知质量与效率间取得平衡。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="personalized-causal-low-bitrate-coded-speech-restoration-wit-2611-22620/">Personalized Causal Low-Bitrate Coded Speech Restoration with Speaker Embeddings</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">在因果低复杂度UBGAN带宽扩展模型上，用说话人嵌入条件化实现个性化低码率编码语音恢复，ViSQOL与WB-PESQ显著提升。</div>
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
| 🥇 | [Back to Mel: Learning to Bridge Fidelity and Perception in G…](back-to-mel-learning-to-bridge-fidelity-and-perception-in-ge-2611-22628/) 🎯 | **9.2** | #语音增强 |
| 🥈 | [Beyond Mimicry: Constrained Exploration with GRPO for Joint …](beyond-mimicry-constrained-exploration-with-grpo-for-joint-m-2611-22627/) | **7.8** | #语音识别 |
| 🥉 | [High-Fidelity Binarized Neural Vocoder](high-fidelity-binarized-neural-vocoder-2611-22593/) | **7.8** | #语音合成 |
| 4. | [Personalized Causal Low-Bitrate Coded Speech Restoration wit…](personalized-causal-low-bitrate-coded-speech-restoration-wit-2611-22620/) 🎯 | **7.8** | #语音增强 |
| 5. | [ASR-Protected Fusion and Reference-Anchored Policy Optimizat…](asr-protected-fusion-and-reference-anchored-policy-optimizat-2610-34156/) | **7.2** | #语音伪造检测 |
| 6. | [Who Says What: Symbolic Trimodal Binding Mechanisms in Audio…](who-says-what-symbolic-trimodal-binding-mechanisms-in-audio--2609-31193/) | **7.2** | #多模态语音理解 |
| 7. | [Evaluating the Evaluation of Music Generation Models with Ge…](evaluating-the-evaluation-of-music-generation-models-with-ge-2611-21809/) | **6.8** | #音乐生成 |
| 8. | [A 1000-hour EEG-EMG-audio dataset of Japanese speech product…](a-1000-hour-eeg-emg-audio-dataset-of-japanese-speech-product-2606-01264/) | **6.0** | #脑电语音解码 |
| 9. | [AutoMV: An Automatic Multi-Agent System for Music Video Gene…](automv-an-automatic-multi-agent-system-for-music-video-gener-2512-12196/) | **6.0** | #音乐生成 |
| 10. | [Music of the Deep: An acoustic blueprint of sperm whale coda…](music-of-the-deep-an-acoustic-blueprint-of-sperm-whale-codas-2610-33974/) | **4.5** | #生物声学 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="back-to-mel-learning-to-bridge-fidelity-and-perception-in-ge-2611-22628/">Back to Mel: Learning to Bridge Fidelity and Perception in Generative Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">以Mel频谱为结构化表示，用flow matching框架BAME在保真度、感知质量与效率间取得平衡。</div>
<div class="card-action">
<a href="back-to-mel-learning-to-bridge-fidelity-and-perception-in-ge-2611-22628/">详情 →</a> · <a href="https://arxiv.org/abs/2611.22628" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="beyond-mimicry-constrained-exploration-with-grpo-for-joint-m-2611-22627/">Beyond Mimicry: Constrained Exploration with GRPO for Joint Multi-Talker ASR and Diarization under Unknown Speaker Counts</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用CoT-SFT加GRPO约束探索，让SpeechLLM在未知说话人数下联合做多说话人ASR与日志，cpWER显著下降。</div>
<div class="card-action">
<a href="beyond-mimicry-constrained-exploration-with-grpo-for-joint-m-2611-22627/">详情 →</a> · <a href="https://arxiv.org/abs/2611.22627" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="high-fidelity-binarized-neural-vocoder-2611-22593/">High-Fidelity Binarized Neural Vocoder</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出BiVoC，将RNDVoC时频声码器改造为1-bit二值网络，用混合精度保留质量敏感模块，在LibriTTS上接近全精度基线。</div>
<div class="card-action">
<a href="high-fidelity-binarized-neural-vocoder-2611-22593/">详情 →</a> · <a href="https://arxiv.org/abs/2611.22593" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="personalized-causal-low-bitrate-coded-speech-restoration-wit-2611-22620/">Personalized Causal Low-Bitrate Coded Speech Restoration with Speaker Embeddings</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在因果低复杂度UBGAN带宽扩展模型上，用说话人嵌入条件化实现个性化低码率编码语音恢复，ViSQOL与WB-PESQ显著提升。</div>
<div class="card-action">
<a href="personalized-causal-low-bitrate-coded-speech-restoration-wit-2611-22620/">详情 →</a> · <a href="https://arxiv.org/abs/2611.22620" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="asr-protected-fusion-and-reference-anchored-policy-optimizat-2610-34156/">ASR-Protected Fusion and Reference-Anchored Policy Optimization for Joint ASR and Word-Level Speech Anti-Spoofing</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">把部分伪造检测建模为带标签ASR，用子空间门控融合伪造线索并用参考锚定策略优化联合训练。</div>
<div class="card-action">
<a href="asr-protected-fusion-and-reference-anchored-policy-optimizat-2610-34156/">详情 →</a> · <a href="https://arxiv.org/abs/2610.34156" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="who-says-what-symbolic-trimodal-binding-mechanisms-in-audio--2609-31193/">Who Says What: Symbolic Trimodal Binding Mechanisms in Audio-Visual LLMs</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#多模态语音理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">分析音视频大模型如何实现'谁说了什么'的三模态绑定，发现其依赖符号变量机制，并用ASD提示修复音视频错配。</div>
<div class="card-action">
<a href="who-says-what-symbolic-trimodal-binding-mechanisms-in-audio--2609-31193/">详情 →</a> · <a href="https://arxiv.org/abs/2609.31193" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="evaluating-the-evaluation-of-music-generation-models-with-ge-2611-21809/">Evaluating the Evaluation of Music Generation Models with Generative Psychometrics</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用生成式心理测量学分析2020-2025年ISMIR音乐生成论文的284条主观评测题项，归纳出六个稳定的质量维度。</div>
<div class="card-action">
<a href="evaluating-the-evaluation-of-music-generation-models-with-ge-2611-21809/">详情 →</a> · <a href="https://arxiv.org/abs/2611.21809" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="a-1000-hour-eeg-emg-audio-dataset-of-japanese-speech-product-2606-01264/">A 1000-hour EEG-EMG-audio dataset of Japanese speech production</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#脑电语音解码</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">发布1020小时日语语音产生同步EEG-EMG-音频多模态数据集，含三种EEG设备与事件标注。</div>
<div class="card-action">
<a href="a-1000-hour-eeg-emg-audio-dataset-of-japanese-speech-product-2606-01264/">详情 →</a> · <a href="https://arxiv.org/abs/2606.01264" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="automv-an-automatic-multi-agent-system-for-music-video-gener-2512-12196/">AutoMV: An Automatic Multi-Agent System for Music Video Generation</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出免训练多智能体框架 AutoMV，用 LLM 编剧与导演智能体依据时间对齐歌词与音乐分析规划整首歌的视觉叙事，并构建 M2VBench 评测基准。</div>
<div class="card-action">
<a href="automv-an-automatic-multi-agent-system-for-music-video-gener-2512-12196/">详情 →</a> · <a href="https://arxiv.org/abs/2512.12196" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="music-of-the-deep-an-acoustic-blueprint-of-sperm-whale-codas-2610-33974/">Music of the Deep: An acoustic blueprint of sperm whale codas</a>
<div class="card-meta">
<span class="card-score">4.5</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">用冻结音频编码器对比抹香鲸尾音与音乐，分析点击组成、顺序与序列上下文对声学表征的贡献。</div>
<div class="card-action">
<a href="music-of-the-deep-an-acoustic-blueprint-of-sperm-whale-codas-2610-33974/">详情 →</a> · <a href="https://arxiv.org/abs/2610.33974" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
