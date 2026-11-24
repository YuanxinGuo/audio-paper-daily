---
title: "语音/音频论文速递 2026-11-24"
date: 2026-11-24T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 0 篇 · 最高分 7.8（#音频生成）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">0</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">7.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音合成 | 3篇 | `██████████` |
| #音频生成 | 2篇 | `███████` |
| #音频伪造检测 | 2篇 | `███████` |
| #音乐转录 | 1篇 | `███` |
| #音频水印 | 1篇 | `███` |
| #多模态具身智能 | 1篇 | `███` |

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
| 🥇 | [SonicRender: Structured and Time-Grounded Rendering of Multi…](sonicrender-structured-and-time-grounded-rendering-of-multi--2611-30241/) | **7.8** | #音频生成 |
| 🥈 | [LiveAudio: From Bidirectional to Autoregressive Diffusion fo…](liveaudio-from-bidirectional-to-autoregressive-diffusion-for-2611-30714/) | **7.8** | #音频生成 |
| 🥉 | [BiSAT: Bidirectionally Aligned Semantic-Acoustic Tokenizatio…](bisat-bidirectionally-aligned-semantic-acoustic-tokenization-2611-30723/) | **7.2** | #语音合成 |
| 4. | [Characterizing Frozen SSL Encoders and Backends for Cross-Do…](characterizing-frozen-ssl-encoders-and-backends-for-cross-do-2611-29865/) | **6.8** | #音频伪造检测 |
| 5. | [Which Layer to Trust? Layer Selection in Frozen Speech Encod…](which-layer-to-trust-layer-selection-in-frozen-speech-encode-2611-29871/) | **6.8** | #音频伪造检测 |
| 6. | [Scoring L2 Pronunciation Without Synthesis: Counterfactual V…](scoring-l2-pronunciation-without-synthesis-counterfactual-ve-2611-29985/) | **6.8** | #语音合成 |
| 7. | [AIRPiano: Piano Score Following with Tabletop Hand Gestures](airpiano-piano-score-following-with-tabletop-hand-gestures-2611-30049/) | **6.8** | #音乐转录 |
| 8. | [Ultrasound Watermark: Real-time Acoustic Watermarking agains…](ultrasound-watermark-real-time-acoustic-watermarking-against-2611-30106/) | **6.8** | #音频水印 |
| 9. | [Synthetic Twins: Closing the Gap Between TTS Test Sets and R…](synthetic-twins-closing-the-gap-between-tts-test-sets-and-re-2611-30694/) | **6.8** | #语音合成 |
| 10. | [Audio-Visual Rearrangement](audio-visual-rearrangement-2611-30171/) | **6.0** | #多模态具身智能 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="sonicrender-structured-and-time-grounded-rendering-of-multi--2611-30241/">SonicRender: Structured and Time-Grounded Rendering of Multi-Event Audio Scene Generation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 SonicRender 统一多事件音频渲染器，用时序音频场景图绑定源身份与时间窗，实现结构化可控的场景混合生成。</div>
<div class="card-action">
<a href="sonicrender-structured-and-time-grounded-rendering-of-multi--2611-30241/">详情 →</a> · <a href="https://arxiv.org/abs/2611.30241" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="liveaudio-from-bidirectional-to-autoregressive-diffusion-for-2611-30714/">LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将双向视频到音频扩散模型经渐进因果微调与蒸馏转为流式自回归生成器，在VGGSound上实现实时同步音频合成。</div>
<div class="card-action">
<a href="liveaudio-from-bidirectional-to-autoregressive-diffusion-for-2611-30714/">详情 →</a> · <a href="https://arxiv.org/abs/2611.30714" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="bisat-bidirectionally-aligned-semantic-acoustic-tokenization-2611-30723/">BiSAT: Bidirectionally Aligned Semantic-Acoustic Tokenization for Speech Language Models</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出双分支共享索引的语音分词框架BiSAT，分离声学与语义连续空间但输出单一离散码流，并构建零样本TTS系统。</div>
<div class="card-action">
<a href="bisat-bidirectionally-aligned-semantic-acoustic-tokenization-2611-30723/">详情 →</a> · <a href="https://arxiv.org/abs/2611.30723" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="characterizing-frozen-ssl-encoders-and-backends-for-cross-do-2611-29865/">Characterizing Frozen SSL Encoders and Backends for Cross-Domain Speech Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">冻结SSL编码器，交叉对比XEUS/XLSR-53与MHFA/AASIST后端，系统评估跨域深伪检测表现。</div>
<div class="card-action">
<a href="characterizing-frozen-ssl-encoders-and-backends-for-cross-do-2611-29865/">详情 →</a> · <a href="https://arxiv.org/abs/2611.29865" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="which-layer-to-trust-layer-selection-in-frozen-speech-encode-2611-29871/">Which Layer to Trust? Layer Selection in Frozen Speech Encoders for Singing-Voice Deepfake Detection under Signal Corruption</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">分析冻结自监督编码器各层在歌唱语音深伪检测中的表现，发现中层优于末层，且开发集选层在受损信号下不可靠。</div>
<div class="card-action">
<a href="which-layer-to-trust-layer-selection-in-frozen-speech-encode-2611-29871/">详情 →</a> · <a href="https://arxiv.org/abs/2611.29871" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="scoring-l2-pronunciation-without-synthesis-counterfactual-ve-2611-29985/">Scoring L2 Pronunciation Without Synthesis: Counterfactual Velocity Contrast in Frozen Flow-Matching TTS</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">利用冻结的流匹配TTS模型，通过对比目标文本与反事实文本的速度预测误差，无需合成音频即可给L2发音打分。</div>
<div class="card-action">
<a href="scoring-l2-pronunciation-without-synthesis-counterfactual-ve-2611-29985/">详情 →</a> · <a href="https://arxiv.org/abs/2611.29985" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="airpiano-piano-score-following-with-tabletop-hand-gestures-2611-30049/">AIRPiano: Piano Score Following with Tabletop Hand Gestures</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐转录</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">AIRPiano 将桌面手势与符号乐谱做在线对齐，用 Transformer 监督注意力实现实时钢琴乐谱跟随。</div>
<div class="card-action">
<a href="airpiano-piano-score-following-with-tabletop-hand-gestures-2611-30049/">详情 →</a> · <a href="https://arxiv.org/abs/2611.30049" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="ultrasound-watermark-real-time-acoustic-watermarking-against-2611-30106/">Ultrasound Watermark: Real-time Acoustic Watermarking against Voice Scams on Smartphones</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频水印</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用手机扬声器发超声、麦克风收面部发音运动反射，生成与语音同步的动态声学水印，实时检测电话诈骗中的合成/重放语音。</div>
<div class="card-action">
<a href="ultrasound-watermark-real-time-acoustic-watermarking-against-2611-30106/">详情 →</a> · <a href="https://arxiv.org/abs/2611.30106" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="synthetic-twins-closing-the-gap-between-tts-test-sets-and-re-2611-30694/">Synthetic Twins: Closing the Gap Between TTS Test Sets and Real Recordings in Turkish ASR Evaluation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用土耳其语Common Voice构建合成孪生测试集，逐项加入音高、说话人克隆、信道与语速，量化合成测试集与真实录音的ASR行为一致性。</div>
<div class="card-action">
<a href="synthetic-twins-closing-the-gap-between-tts-test-sets-and-re-2611-30694/">详情 →</a> · <a href="https://arxiv.org/abs/2611.30694" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="audio-visual-rearrangement-2611-30171/">Audio-Visual Rearrangement</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#多模态具身智能</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出视听重排任务：智能体听语音请求、定位说话人、取物送达，构建数据集并提出融合运动感知空间音频模块的视听大模型框架。</div>
<div class="card-action">
<a href="audio-visual-rearrangement-2611-30171/">详情 →</a> · <a href="https://arxiv.org/abs/2611.30171" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
