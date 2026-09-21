---
title: "语音/音频论文速递 2026-09-21"
date: 2026-09-21T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 8.8（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #乐器分离 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #音频生成 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #多模态交互理解 | 1篇 | `█████` |
| #视觉语音识别 | 1篇 | `█████` |
| #音频处理 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="hammer-harmonic-aware-parallel-context-modeling-and-discrimi-2609-21171/">HAMMER: Harmonic-Aware Parallel Context Modeling and Discriminator-Free Perceptual Optimization for Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出谐波感知的 TF-HAM 模块与无判别器的 MEPR 感知优化，在 VoiceBank+DEMAND 上以 2.39M 参数达 3.69 PESQ。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="blinc-blind-calibration-for-training-free-speech-enhancement-2609-21898/">BLINC: Blind Calibration For Training-Free Speech Enhancement Adaptation</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">BLINC 提出免训练的测试时自适应方法，用直方图匹配把预测时频掩码重映射到双峰目标分布，无需反向传播即可提升语音增强跨域表现。</div>
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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="investigating-the-performance-and-energy-costs-of-replicatin-2609-21918/">Investigating the Performance and Energy Costs of Replicating Band-Split RNN for Music Source Separation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">复现 BSRNN 音乐源分离全流程，系统研究预处理、优化与结构设计选择，并报告能耗成本，公开代码与预训练模型。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [HAMMER: Harmonic-Aware Parallel Context Modeling and Discrim…](hammer-harmonic-aware-parallel-context-modeling-and-discrimi-2609-21171/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [BLINC: Blind Calibration For Training-Free Speech Enhancemen…](blinc-blind-calibration-for-training-free-speech-enhancement-2609-21898/) 🎯 | **8.0** | #语音增强 |
| 🥉 | [Investigating the Performance and Energy Costs of Replicatin…](investigating-the-performance-and-energy-costs-of-replicatin-2609-21918/) 🎯 | **7.8** | #乐器分离 |
| 4. | [CPR: Combining global composing, local performing and full-s…](cpr-combining-global-composing-local-performing-and-full-seq-2609-18216/) | **7.0** | #音乐生成 |
| 5. | [Rethinking Music Tokenization: A Semantic Codec toward High-…](rethinking-music-tokenization-a-semantic-codec-toward-high-f-2609-21240/) | **7.0** | #音频生成 |
| 6. | [Per-Aetiology Contrastive Severity Embeddings with Phonologi…](per-aetiology-contrastive-severity-embeddings-with-phonologi-2609-21789/) | **6.8** | #语音识别 |
| 7. | [Omni Demand Understanding: A Benchmark for Contextual User-I…](omni-demand-understanding-a-benchmark-for-contextual-user-in-2609-21392/) | **6.8** | #多模态交互理解 |
| 8. | [Curriculum-Based Noise Adaptation for Phoneme-to-Text Recons…](curriculum-based-noise-adaptation-for-phoneme-to-text-recons-2609-20839/) | **6.8** | #视觉语音识别 |
| 9. | [Towards the Vision-Sound-Language-Action Paradigm: The HEAR …](towards-the-vision-sound-language-action-paradigm-the-hear-f-2603-16086/) | **6.0** | #音频处理 |
| 10. | [Listen Before You Speak: Response Planning from Listener Fac…](listen-before-you-speak-response-planning-from-listener-faci-2609-21683/) | **6.0** | #语音合成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="hammer-harmonic-aware-parallel-context-modeling-and-discrimi-2609-21171/">HAMMER: Harmonic-Aware Parallel Context Modeling and Discriminator-Free Perceptual Optimization for Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出谐波感知的 TF-HAM 模块与无判别器的 MEPR 感知优化，在 VoiceBank+DEMAND 上以 2.39M 参数达 3.69 PESQ。</div>
<div class="card-action">
<a href="hammer-harmonic-aware-parallel-context-modeling-and-discrimi-2609-21171/">详情 →</a> · <a href="https://arxiv.org/abs/2609.21171" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="blinc-blind-calibration-for-training-free-speech-enhancement-2609-21898/">BLINC: Blind Calibration For Training-Free Speech Enhancement Adaptation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">BLINC 提出免训练的测试时自适应方法，用直方图匹配把预测时频掩码重映射到双峰目标分布，无需反向传播即可提升语音增强跨域表现。</div>
<div class="card-action">
<a href="blinc-blind-calibration-for-training-free-speech-enhancement-2609-21898/">详情 →</a> · <a href="https://arxiv.org/abs/2609.21898" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="investigating-the-performance-and-energy-costs-of-replicatin-2609-21918/">Investigating the Performance and Energy Costs of Replicating Band-Split RNN for Music Source Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">复现 BSRNN 音乐源分离全流程，系统研究预处理、优化与结构设计选择，并报告能耗成本，公开代码与预训练模型。</div>
<div class="card-action">
<a href="investigating-the-performance-and-energy-costs-of-replicatin-2609-21918/">详情 →</a> · <a href="https://arxiv.org/abs/2609.21918" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="cpr-combining-global-composing-local-performing-and-full-seq-2609-18216/">CPR: Combining global composing, local performing and full-sequence refining in piano rendering with continuous autoregressive modelling</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 Composer-Performer-Refiner 连续自回归框架，用局部流匹配生成 24kHz 声学隐变量并上采样至 48kHz，实现钢琴 MIDI 到音频渲染。</div>
<div class="card-action">
<a href="cpr-combining-global-composing-local-performing-and-full-seq-2609-18216/">详情 →</a> · <a href="https://arxiv.org/abs/2609.18216" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="rethinking-music-tokenization-a-semantic-codec-toward-high-f-2609-21240/">Rethinking Music Tokenization: A Semantic Codec toward High-Fidelity LLM Music Generation</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出音乐语义编解码器 MuSeC，将语义与声学内容从混合信号中解耦，产出更利于语言模型建模的离散 token。</div>
<div class="card-action">
<a href="rethinking-music-tokenization-a-semantic-codec-toward-high-f-2609-21240/">详情 →</a> · <a href="https://arxiv.org/abs/2609.21240" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="per-aetiology-contrastive-severity-embeddings-with-phonologi-2609-21789/">Per-Aetiology Contrastive Severity Embeddings with Phonological Pseudo-Labelling for Multilingual Dysarthric Speech</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">按病因分别训练 HuBERT 对比严重度嵌入，并用音系伪标签扩充数据，在多语言构音障碍严重度分类上显著优于混合病因基线。</div>
<div class="card-action">
<a href="per-aetiology-contrastive-severity-embeddings-with-phonologi-2609-21789/">详情 →</a> · <a href="https://arxiv.org/abs/2609.21789" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="omni-demand-understanding-a-benchmark-for-contextual-user-in-2609-21392/">Omni Demand Understanding: A Benchmark for Contextual User-Intent Inference in Multimodal Interaction</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#多模态交互理解</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 ODU-Bench 基准，评测多模态大模型能否从音视频与对话上下文中推断用户潜在需求，14 个模型均表现不佳。</div>
<div class="card-action">
<a href="omni-demand-understanding-a-benchmark-for-contextual-user-in-2609-21392/">详情 →</a> · <a href="https://arxiv.org/abs/2609.21392" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="curriculum-based-noise-adaptation-for-phoneme-to-text-recons-2609-20839/">Curriculum-Based Noise Adaptation for Phoneme-to-Text Reconstruction in Visual Speech Recognition</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#视觉语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出渐进式错误课程训练PECT，用合成扰动与伪标签逐步适配NLLB音素到文本重建模型，降低视觉语音识别WER。</div>
<div class="card-action">
<a href="curriculum-based-noise-adaptation-for-phoneme-to-text-recons-2609-20839/">详情 →</a> · <a href="https://arxiv.org/abs/2609.20839" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="towards-the-vision-sound-language-action-paradigm-the-hear-f-2603-16086/">Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出VSLA连续控制范式与HEAR框架，用流式音频历史器、音频世界模型与流匹配策略实现声音驱动的机器人操作。</div>
<div class="card-action">
<a href="towards-the-vision-sound-language-action-paradigm-the-hear-f-2603-16086/">详情 →</a> · <a href="https://arxiv.org/abs/2603.16086" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="listen-before-you-speak-response-planning-from-listener-faci-2609-21683/">Listen Before You Speak: Response Planning from Listener Facial Reactions for Conversational Speech Generation</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出 ReACT-TTS 两阶段框架，用 1 秒听者面部反应序列预测下一句的情感与韵律，再接入 Grad-TTS 实现语音生成。</div>
<div class="card-action">
<a href="listen-before-you-speak-response-planning-from-listener-faci-2609-21683/">详情 →</a> · <a href="https://arxiv.org/abs/2609.21683" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
