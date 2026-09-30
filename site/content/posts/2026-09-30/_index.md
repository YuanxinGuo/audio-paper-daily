---
title: "语音/音频论文速递 2026-09-30"
date: 2026-09-30T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 4 篇 · 最高分 8.8（#语音识别）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">4</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #双耳音频 | 2篇 | `██████████` |
| #语音对话系统 | 2篇 | `██████████` |
| #语音识别 | 1篇 | `█████` |
| #音频质量评估 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #音频大模型安全对齐 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #生物声学 | 1篇 | `█████` |

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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="beyond-acoustic-prefixes-persistent-access-to-serialized-aco-2603-27205/">Beyond Acoustic Prefixes: Persistent Access to Serialized Acoustic Memory for LLM-Based Multi-Talker Speech Recognition</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音识别</span>
</div>
<div class="card-tldr">将 onset 序列化从输出目标扩展到声学条件通路，用外部串行声学记忆加门控残差交叉注意力，让 LLM 在生成全程持续访问说话人声学证据。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="signal-independent-and-signal-dependent-neural-ambisonic-mat-2609-37691/">Signal-Independent and Signal-Dependent Neural Ambisonic Matrix Encoding for Arbitrary Arrays with Variable Microphone Counts</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">用共享麦克风级处理与掩码自注意力实现可变麦克风数量的阵列无关Ambisonic矩阵编码，含信号无关与信号相关两种变体。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="multichannel-audio-quality-assessment-extending-pretrained-p-2609-37116/">Multichannel Audio Quality Assessment: Extending Pretrained Perceptual Models to Spatial Audio</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频质量评估</span>
</div>
<div class="card-tldr">将预训练感知质量模型扩展到5.1声道空间音频，提出特征级Feature-Band Group Attention融合空间组，在五个测试集上取得最佳整体性能。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="enabling-immersive-audio-visual-experience-from-any-video-2609-36295/">Enabling Immersive Audio-Visual Experience from Any Video</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">OmniDream 无需训练，将单目无声视频转为可自由环视、声源空间对齐的沉浸式视听体验。</div>
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
| 🥇 | [Beyond Acoustic Prefixes: Persistent Access to Serialized Ac…](beyond-acoustic-prefixes-persistent-access-to-serialized-aco-2603-27205/) 🎯 | **8.8** | #语音识别 |
| 🥈 | [Signal-Independent and Signal-Dependent Neural Ambisonic Mat…](signal-independent-and-signal-dependent-neural-ambisonic-mat-2609-37691/) 🎯 | **8.0** | #双耳音频 |
| 🥉 | [MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-…](multitalk-scaling-full-duplex-speech-models-to-long-multi-pa-2609-36903/) | **7.8** | #语音对话系统 |
| 4. | [Multichannel Audio Quality Assessment: Extending Pretrained …](multichannel-audio-quality-assessment-extending-pretrained-p-2609-37116/) 🎯 | **7.8** | #音频质量评估 |
| 5. | [Enabling Immersive Audio-Visual Experience from Any Video](enabling-immersive-audio-visual-experience-from-any-video-2609-36295/) 🎯 | **7.8** | #双耳音频 |
| 6. | [AdaptDuplex: from static to adaptive full-duplex spoken dial…](adaptduplex-from-static-to-adaptive-full-duplex-spoken-dialo-2609-29217/) | **7.2** | #语音对话系统 |
| 7. | [Video-to-Music Generation for Gameplay Videos](video-to-music-generation-for-gameplay-videos-2609-31810/) | **6.8** | #音乐生成 |
| 8. | [Benign Fine-Tuning Breaks Safety Alignment in Audio LLMs](benign-fine-tuning-breaks-safety-alignment-in-audio-llms-2604-16659/) | **6.5** | #音频大模型安全对齐 |
| 9. | [Repetition, Not Length: Isolating the Counting Failure in Ne…](repetition-not-length-isolating-the-counting-failure-in-neur-2609-36974/) | **6.5** | #语音合成 |
| 10. | [2-Dimensional spectral gating for denoising bioacoustics rec…](2-dimensional-spectral-gating-for-denoising-bioacoustics-rec-2609-37910/) | **5.5** | #生物声学 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="beyond-acoustic-prefixes-persistent-access-to-serialized-aco-2603-27205/">Beyond Acoustic Prefixes: Persistent Access to Serialized Acoustic Memory for LLM-Based Multi-Talker Speech Recognition</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将 onset 序列化从输出目标扩展到声学条件通路，用外部串行声学记忆加门控残差交叉注意力，让 LLM 在生成全程持续访问说话人声学证据。</div>
<div class="card-action">
<a href="beyond-acoustic-prefixes-persistent-access-to-serialized-aco-2603-27205/">详情 →</a> · <a href="https://arxiv.org/abs/2603.27205" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="signal-independent-and-signal-dependent-neural-ambisonic-mat-2609-37691/">Signal-Independent and Signal-Dependent Neural Ambisonic Matrix Encoding for Arbitrary Arrays with Variable Microphone Counts</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用共享麦克风级处理与掩码自注意力实现可变麦克风数量的阵列无关Ambisonic矩阵编码，含信号无关与信号相关两种变体。</div>
<div class="card-action">
<a href="signal-independent-and-signal-dependent-neural-ambisonic-mat-2609-37691/">详情 →</a> · <a href="https://arxiv.org/abs/2609.37691" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="multitalk-scaling-full-duplex-speech-models-to-long-multi-pa-2609-36903/">MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音对话系统</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">构建57.6k小时中英多方全双工对话数据与MultiTalkBench基准，训练Moshi式模型实现长时多方双语对话。</div>
<div class="card-action">
<a href="multitalk-scaling-full-duplex-speech-models-to-long-multi-pa-2609-36903/">详情 →</a> · <a href="https://arxiv.org/abs/2609.36903" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="multichannel-audio-quality-assessment-extending-pretrained-p-2609-37116/">Multichannel Audio Quality Assessment: Extending Pretrained Perceptual Models to Spatial Audio</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频质量评估</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">将预训练感知质量模型扩展到5.1声道空间音频，提出特征级Feature-Band Group Attention融合空间组，在五个测试集上取得最佳整体性能。</div>
<div class="card-action">
<a href="multichannel-audio-quality-assessment-extending-pretrained-p-2609-37116/">详情 →</a> · <a href="https://arxiv.org/abs/2609.37116" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="enabling-immersive-audio-visual-experience-from-any-video-2609-36295/">Enabling Immersive Audio-Visual Experience from Any Video</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">OmniDream 无需训练，将单目无声视频转为可自由环视、声源空间对齐的沉浸式视听体验。</div>
<div class="card-action">
<a href="enabling-immersive-audio-visual-experience-from-any-video-2609-36295/">详情 →</a> · <a href="https://arxiv.org/abs/2609.36295" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="adaptduplex-from-static-to-adaptive-full-duplex-spoken-dialo-2609-29217/">AdaptDuplex: from static to adaptive full-duplex spoken dialogue</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音对话系统</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">在 Qwen3-Omni 上扩展 token 级协议与自适应窗口机制，实现全双工语音对话的动态决策与低延迟响应。</div>
<div class="card-action">
<a href="adaptduplex-from-static-to-adaptive-full-duplex-spoken-dialo-2609-29217/">详情 →</a> · <a href="https://arxiv.org/abs/2609.29217" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="video-to-music-generation-for-gameplay-videos-2609-31810/">Video-to-Music Generation for Gameplay Videos</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">构建217.6小时SNES游戏视频-配乐数据集，用冻结ViViT编码器接MusicGen解码器做视频到音乐生成，客观指标超基线。</div>
<div class="card-action">
<a href="video-to-music-generation-for-gameplay-videos-2609-31810/">详情 →</a> · <a href="https://arxiv.org/abs/2609.31810" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="benign-fine-tuning-breaks-safety-alignment-in-audio-llms-2604-16659/">Benign Fine-Tuning Breaks Safety Alignment in Audio LLMs</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频大模型安全对齐</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">首次系统研究音频LLM在良性微调下的安全对齐退化，发现脆弱轴由编码器架构决定，JSR可升至87%。</div>
<div class="card-action">
<a href="benign-fine-tuning-breaks-safety-alignment-in-audio-llms-2604-16659/">详情 →</a> · <a href="https://arxiv.org/abs/2604.16659" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="repetition-not-length-isolating-the-counting-failure-in-neur-2609-36974/">Repetition, Not Length: Isolating the Counting Failure in Neural Text-to-Speech</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">通过配对控制实验证明：TTS 在重复文本上的计数失败源于重复性本身而非文本长度，六模型在 k≥6 时准确率从 94.3% 跌至 18.2%。</div>
<div class="card-action">
<a href="repetition-not-length-isolating-the-counting-failure-in-neur-2609-36974/">详情 →</a> · <a href="https://arxiv.org/abs/2609.36974" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="2-dimensional-spectral-gating-for-denoising-bioacoustics-rec-2609-37910/">2-Dimensional spectral gating for denoising bioacoustics recordings</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在 Noisereduce 的频谱门控基础上引入跨频结构约束，对鸟类与海洋哺乳动物录音降噪，速度不变。</div>
<div class="card-action">
<a href="2-dimensional-spectral-gating-for-denoising-bioacoustics-rec-2609-37910/">详情 →</a> · <a href="https://arxiv.org/abs/2609.37910" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
