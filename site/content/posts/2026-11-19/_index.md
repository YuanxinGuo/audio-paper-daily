---
title: "语音/音频论文速递 2026-11-19"
date: 2026-11-19T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 8.8（#语音增强）"
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
| #说话人日志 | 2篇 | `██████████` |
| #音频生成 | 2篇 | `██████████` |
| #语音增强 | 1篇 | `█████` |
| #抑郁严重程度估计 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #音频处理 | 1篇 | `█████` |
| #生物声学 | 1篇 | `█████` |
| #异常声音检测 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="end-to-end-multi-task-learning-for-adjustable-joint-noise-re-2603-20387/">End-to-End Multi-Task Learning for Adjustable Joint Noise Reduction and Hearing Loss Compensation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">用可微分听觉模型端到端训练单一DNN，同时输出NR与HLC两个TF掩码，可按指数独立调节并支持audiogram个性化。</div>
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
| 🥇 | [End-to-End Multi-Task Learning for Adjustable Joint Noise Re…](end-to-end-multi-task-learning-for-adjustable-joint-noise-re-2603-20387/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [Label-Free Role-Aware Segmentation of Classroom Recordings: …](label-free-role-aware-segmentation-of-classroom-recordings-r-2611-23609/) | **7.2** | #说话人日志 |
| 🥉 | [SIGMA: speaker-isolated, symptom-structured multimodal estim…](sigma-speaker-isolated-symptom-structured-multimodal-estimat-2611-23348/) | **7.2** | #抑郁严重程度估计 |
| 4. | [Why Multi-Source Audio Fails to Compose: A Geometric Diagnos…](why-multi-source-audio-fails-to-compose-a-geometric-diagnosi-2611-24410/) | **6.8** | #音频生成 |
| 5. | [Harmonic Circuit: Chord Progression Lies in a Sparse Princip…](harmonic-circuit-chord-progression-lies-in-a-sparse-principa-2611-24453/) | **6.8** | #音乐生成 |
| 6. | [Constructing Dynamic Conversations with Neural Back-channel …](constructing-dynamic-conversations-with-neural-back-channel--2611-24086/) | **6.8** | #音频生成 |
| 7. | [Great Listeners, Poor Decision-Makers: Rethinking Agentic Au…](great-listeners-poor-decision-makers-rethinking-agentic-audi-2611-23847/) | **6.8** | #音频处理 |
| 8. | [RespCCT and FreqCCT: Compact, Explainable and Cost-Aware Con…](respcct-and-freqcct-compact-explainable-and-cost-aware-convo-2611-24323/) | **6.2** | #生物声学 |
| 9. | [Exploring Speaker-Aware Engagement Modeling for Children wit…](exploring-speaker-aware-engagement-modeling-for-children-wit-2611-24794/) | **5.8** | #说话人日志 |
| 10. | [Practical Assessment of Agentic Systems in Acoustics](practical-assessment-of-agentic-systems-in-acoustics-2610-39685/) | **5.5** | #异常声音检测 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="end-to-end-multi-task-learning-for-adjustable-joint-noise-re-2603-20387/">End-to-End Multi-Task Learning for Adjustable Joint Noise Reduction and Hearing Loss Compensation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用可微分听觉模型端到端训练单一DNN，同时输出NR与HLC两个TF掩码，可按指数独立调节并支持audiogram个性化。</div>
<div class="card-action">
<a href="end-to-end-multi-task-learning-for-adjustable-joint-noise-re-2603-20387/">详情 →</a> · <a href="https://arxiv.org/abs/2603.20387" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="label-free-role-aware-segmentation-of-classroom-recordings-r-2611-23609/">Label-Free Role-Aware Segmentation of Classroom Recordings: Recovering the Teacher from Transferable Structure</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#说话人日志</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出无标签、设备端运行的课堂师生角色分割流水线，用会话相对结构而非声纹身份判定教师角色，跨语言跨教室可迁移。</div>
<div class="card-action">
<a href="label-free-role-aware-segmentation-of-classroom-recordings-r-2611-23609/">详情 →</a> · <a href="https://arxiv.org/abs/2611.23609" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="sigma-speaker-isolated-symptom-structured-multimodal-estimat-2611-23348/">SIGMA: speaker-isolated, symptom-structured multimodal estimation of depression severity from clinical interviews</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#抑郁严重程度估计</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">SIGMA用说话人日志隔离被试语音，交叉注意力融合文本/音频/视频，并以分级响应头联合预测八项症状。</div>
<div class="card-action">
<a href="sigma-speaker-isolated-symptom-structured-multimodal-estimat-2611-23348/">详情 →</a> · <a href="https://arxiv.org/abs/2611.23348" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="why-multi-source-audio-fails-to-compose-a-geometric-diagnosi-2611-24410/">Why Multi-Source Audio Fails to Compose: A Geometric Diagnosis and Its Remedy</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">诊断多源音频到图像生成中的几何位移现象，用CLAP替代BEATs并引入多token机制改善组合忠实度。</div>
<div class="card-action">
<a href="why-multi-source-audio-fails-to-compose-a-geometric-diagnosi-2611-24410/">详情 →</a> · <a href="https://arxiv.org/abs/2611.24410" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="harmonic-circuit-chord-progression-lies-in-a-sparse-principa-2611-24453/">Harmonic Circuit: Chord Progression Lies in a Sparse Principal Information Flow in Symbolic Music Models</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用 Auto-Emergence 算法在 ChatMusician 与 MuPT 两个符号音乐模型中提取稀疏子网络，发现其对应 I…V→I 终止主音预测的音乐功能电路。</div>
<div class="card-action">
<a href="harmonic-circuit-chord-progression-lies-in-a-sparse-principa-2611-24453/">详情 →</a> · <a href="https://arxiv.org/abs/2611.24453" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="constructing-dynamic-conversations-with-neural-back-channel--2611-24086/">Constructing Dynamic Conversations with Neural Back-channel Generation and Voice-line Scheduling</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用神经调度器把两条独立录制的对白音轨拼接成带副声道与话轮交叠的动态对话。</div>
<div class="card-action">
<a href="constructing-dynamic-conversations-with-neural-back-channel--2611-24086/">详情 →</a> · <a href="https://arxiv.org/abs/2611.24086" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="great-listeners-poor-decision-makers-rethinking-agentic-audi-2611-23847/">Great Listeners, Poor Decision-Makers: Rethinking Agentic Audio AI</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">立场论文主张智能音频AI瓶颈已从识别转向决策，提出显式决策层决定行动/等待/询问/沉默。</div>
<div class="card-action">
<a href="great-listeners-poor-decision-makers-rethinking-agentic-audi-2611-23847/">详情 →</a> · <a href="https://arxiv.org/abs/2611.23847" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="respcct-and-freqcct-compact-explainable-and-cost-aware-convo-2611-24323/">RespCCT and FreqCCT: Compact, Explainable and Cost-Aware Convolutional Transformers for Multi-Class Respiratory Disease Classification</a>
<div class="card-meta">
<span class="card-score">6.2</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出两个紧凑卷积Transformer用于七类呼吸疾病音分类，参数量仅12万~17万，精度接近ImageNet预训练大模型并给出成本与可解释性分析。</div>
<div class="card-action">
<a href="respcct-and-freqcct-compact-explainable-and-cost-aware-convo-2611-24323/">详情 →</a> · <a href="https://arxiv.org/abs/2611.24323" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="exploring-speaker-aware-engagement-modeling-for-children-wit-2611-24794/">Exploring Speaker-Aware Engagement Modeling for Children with Autism Spectrum Disorder</a>
<div class="card-meta">
<span class="card-score">5.8</span>
<span class="tag-pill">#说话人日志</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在自闭症儿童家庭机器人干预录音中，用说话人日志分离儿童与照护者语音，比较声学参与度建模效果。</div>
<div class="card-action">
<a href="exploring-speaker-aware-engagement-modeling-for-children-wit-2611-24794/">详情 →</a> · <a href="https://arxiv.org/abs/2611.24794" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="practical-assessment-of-agentic-systems-in-acoustics-2610-39685/">Practical Assessment of Agentic Systems in Acoustics</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#异常声音检测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">评测LLM智能体在车内异响检测与超材料单元设计两类声学任务中的表现，分析模型与harness组件各自贡献。</div>
<div class="card-action">
<a href="practical-assessment-of-agentic-systems-in-acoustics-2610-39685/">详情 →</a> · <a href="https://arxiv.org/abs/2610.39685" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
