---
title: "语音/音频论文速递 2026-05-28"
date: 2026-05-28T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 0 篇 · 最高分 8.5（#语音合成）"
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
| #音频理解 | 2篇 | `██████████` |
| #语音合成 | 1篇 | `█████` |
| #房间冲激响应生成 | 1篇 | `█████` |
| #音频生成 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #音乐推荐 | 1篇 | `█████` |
| #多说话人音视频生成评估 | 1篇 | `█████` |
| #音视频伪造检测 | 1篇 | `█████` |

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
| 🥇 | [PilotTTS: A Disciplined Modular Recipe for Competitive Speec…](pilottts-a-disciplined-modular-recipe-for-competitive-speech-2605-27258/) | **8.5** | #语音合成 |
| 🥈 | [ChronosAudio: A Comprehensive Long-Audio Benchmark for Evalu…](chronosaudio-a-comprehensive-long-audio-benchmark-for-evalua-2601-04876/) | **8.5** | #音频理解 |
| 🥉 | [EigeNet: Geometry-Informed Multi-Modal Learning for Few-shot…](eigenet-geometry-informed-multi-modal-learning-for-few-shot--2605-28101/) | **8.2** | #房间冲激响应生成 |
| 4. | [Unified Synthesis of Compositional Speech and Sound from Fre…](unified-synthesis-of-compositional-speech-and-sound-from-fre-2605-28063/) | **8.2** | #音频生成 |
| 5. | [DEMON: Diffusion Engine for Musical Orchestrated Noise](demon-diffusion-engine-for-musical-orchestrated-noise-2605-28657/) | **7.8** | #音乐生成 |
| 6. | [Assessing Factual Music Comprehension in Large Audio Languag…](assessing-factual-music-comprehension-in-large-audio-languag-2511-05550/) | **7.5** | #音频理解 |
| 7. | [Affective Music Recommendation: A Rollout-Based World Model …](affective-music-recommendation-a-rollout-based-world-model-f-2605-28810/) | **7.2** | #音乐推荐 |
| 8. | [MTAVG-Bench 2.0: Diagnosing Failure Modes of Cinematic Expre…](mtavg-bench-2-0-diagnosing-failure-modes-of-cinematic-expres-2605-28035/) | **7.2** | #多说话人音视频生成评估 |
| 9. | [From Talking to Singing: A New Challenge for Audio-Visual De…](from-talking-to-singing-a-new-challenge-for-audio-visual-dee-2605-27944/) | **7.2** | #音视频伪造检测 |
| 10. | [Cross-modal characterization of infant cry: validation of a …](cross-modal-characterization-of-infant-cry-validation-of-a-c-2605-28687/) | **6.5** | #生物声学 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="pilottts-a-disciplined-modular-recipe-for-competitive-speech-2605-27258/">PilotTTS: A Disciplined Modular Recipe for Competitive Speech Synthesis</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">PilotTTS提出轻量级自回归TTS系统，仅用200K小时开源数据，通过Q-Former解耦说话人身份与风格，在Seed-TTS Eval上WER 1.50%且说话人相似度最高。</div>
<div class="card-action">
<a href="pilottts-a-disciplined-modular-recipe-for-competitive-speech-2605-27258/">详情 →</a> · <a href="https://arxiv.org/abs/2605.27258" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="chronosaudio-a-comprehensive-long-audio-benchmark-for-evalua-2601-04876/">ChronosAudio: A Comprehensive Long-Audio Benchmark for Evaluating Audio-Large Language Models</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个面向音频大语言模型的长音频多任务基准ChronosAudio，包含6大任务类别、3.6万测试实例、超200小时音频，揭示模型在长上下文中性能严重下降（特定任务超90%退化）及注意力稀释问题。</div>
<div class="card-action">
<a href="chronosaudio-a-comprehensive-long-audio-benchmark-for-evalua-2601-04876/">详情 →</a> · <a href="https://arxiv.org/abs/2601.04876" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="eigenet-geometry-informed-multi-modal-learning-for-few-shot--2605-28101/">EigeNet: Geometry-Informed Multi-Modal Learning for Few-shot Novel View RIR Prediction</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#房间冲激响应生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出EigeNet，利用几何信息引导的多模态框架，从稀疏观测中预测新视角的房间冲激响应，在少样本和模拟到真实场景中达到SOTA。</div>
<div class="card-action">
<a href="eigenet-geometry-informed-multi-modal-learning-for-few-shot--2605-28101/">详情 →</a> · <a href="https://arxiv.org/abs/2605.28101" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="unified-synthesis-of-compositional-speech-and-sound-from-fre-2605-28063/">Unified Synthesis of Compositional Speech and Sound from Free-Form Text Prompts</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出PlanAudio，基于LLM的自回归框架，从自由文本提示直接合成包含语音和声音的复合音频。</div>
<div class="card-action">
<a href="unified-synthesis-of-compositional-speech-and-sound-from-fre-2605-28063/">详情 →</a> · <a href="https://arxiv.org/abs/2605.28063" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="demon-diffusion-engine-for-musical-orchestrated-noise-2605-28657/">DEMON: Diffusion Engine for Musical Orchestrated Noise</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出DEMON，一个基于扩散模型的实时音乐生成引擎，通过四种机制实现可演奏的降噪控制，在消费级GPU上达到每秒12.3次解码。</div>
<div class="card-action">
<a href="demon-diffusion-engine-for-musical-orchestrated-noise-2605-28657/">详情 →</a> · <a href="https://arxiv.org/abs/2605.28657" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="assessing-factual-music-comprehension-in-large-audio-languag-2511-05550/">Assessing Factual Music Comprehension in Large Audio Language Models</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文指出现有MusicQA数据集无法有效评估LALM的音乐事实理解能力，并提出基于结构化信息检索的新评估协议和基准。</div>
<div class="card-action">
<a href="assessing-factual-music-comprehension-in-large-audio-languag-2511-05550/">详情 →</a> · <a href="https://arxiv.org/abs/2511.05550" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="affective-music-recommendation-a-rollout-based-world-model-f-2605-28810/">Affective Music Recommendation: A Rollout-Based World Model for Offline Preference Optimization</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐推荐</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于rollout世界模型的AMRS系统，用于情感音乐推荐，通过离线DPO优化多目标效用函数，在临床和消费场景中验证。</div>
<div class="card-action">
<a href="affective-music-recommendation-a-rollout-based-world-model-f-2605-28810/">详情 →</a> · <a href="https://arxiv.org/abs/2605.28810" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="mtavg-bench-2-0-diagnosing-failure-modes-of-cinematic-expres-2605-28035/">MTAVG-Bench 2.0: Diagnosing Failure Modes of Cinematic Expressiveness in Multi-Talker Audio-Video Generation</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#多说话人音视频生成评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MTAVG-Bench 2.0基准，系统诊断多说话人音视频生成中的电影级表现力失败模式。</div>
<div class="card-action">
<a href="mtavg-bench-2-0-diagnosing-failure-modes-of-cinematic-expres-2605-28035/">详情 →</a> · <a href="https://arxiv.org/abs/2605.28035" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="from-talking-to-singing-a-new-challenge-for-audio-visual-dee-2605-27944/">From Talking to Singing: A New Challenge for Audio-Visual Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音视频伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出文本引导的音视频伪造检测框架T-AVFD，解决从说话到歌唱场景的域偏移问题，并构建歌唱头部深度伪造数据集SHDF。</div>
<div class="card-action">
<a href="from-talking-to-singing-a-new-challenge-for-audio-visual-dee-2605-27944/">详情 →</a> · <a href="https://arxiv.org/abs/2605.27944" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="cross-modal-characterization-of-infant-cry-validation-of-a-c-2605-28687/">Cross-modal characterization of infant cry: validation of a chest-surface accelerometer in extracting acoustic vocal function measures</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">验证胸戴加速计在婴儿哭声分析中提取声学特征的有效性，与麦克风对比显示基频和抖动指标一致性高。</div>
<div class="card-action">
<a href="cross-modal-characterization-of-infant-cry-validation-of-a-c-2605-28687/">详情 →</a> · <a href="https://arxiv.org/abs/2605.28687" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
