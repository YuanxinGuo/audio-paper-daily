---
title: "语音/音频论文速递 2026-11-26"
date: 2026-11-26T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 8.2（#说话人日志）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音频生成 | 2篇 | `██████████` |
| #抑郁检测 | 2篇 | `██████████` |
| #说话人日志 | 1篇 | `█████` |
| #语音增强 | 1篇 | `█████` |
| #音频深度伪造检测 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #声学回声消除 | 1篇 | `█████` |
| #音乐推荐 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="fsc-net-integrating-fast-fourier-convolutions-and-progressiv-2606-06962/">FSC-Net: Integrating Fast Fourier Convolutions and Progressive Learning for Speech Bandwidth Extension</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">FSC-Net 用快速傅里叶卷积扩展感受野至全频谱，并以频率渐进课程学习重建高频，实现 1.54M 参数的高效语音带宽扩展。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="line-level-singer-diarization-in-multi-member-pop-songs-a-be-2611-33247/">Line-Level Singer Diarization in Multi-Member Pop Songs: A Benchmark, Lead-Vocal Isolation, and Song-Level Decoding</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#说话人日志</span>
</div>
<div class="card-tldr">提出逐行歌手日志任务与 ColorCoded-SD 基准，用主唱分离+歌声嵌入+歌曲级解码将 B-cubed F1 提升约 0.06。</div>
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
| 🥇 | [Line-Level Singer Diarization in Multi-Member Pop Songs: A B…](line-level-singer-diarization-in-multi-member-pop-songs-a-be-2611-33247/) 🎯 | **8.2** | #说话人日志 |
| 🥈 | [FSC-Net: Integrating Fast Fourier Convolutions and Progressi…](fsc-net-integrating-fast-fourier-convolutions-and-progressiv-2606-06962/) 🎯 | **8.2** | #语音增强 |
| 🥉 | [MOZAIC: An Audio-Video Deepfake Benchmark for Telling What I…](mozaic-an-audio-video-deepfake-benchmark-for-telling-what-is-2611-31301/) | **7.8** | #音频深度伪造检测 |
| 4. | [Emilia2: A Large-Scale Dataset for Controllable Long-Form Sp…](emilia2-a-large-scale-dataset-for-controllable-long-form-spe-2611-13614/) | **7.8** | #语音合成 |
| 5. | [Learning Temporal Stabilization for Double-Talk-Robust Delay…](learning-temporal-stabilization-for-double-talk-robust-delay-2611-33689/) | **7.2** | #声学回声消除 |
| 6. | [Direct Conditioning of Audio Diffusion Transformers on fMRI …](direct-conditioning-of-audio-diffusion-transformers-on-fmri--2611-12603/) | **7.0** | #音频生成 |
| 7. | [AVENUE: Audio-Video EditiNg Understanding and Evaluation](avenue-audio-video-editing-understanding-and-evaluation-2609-04253/) | **6.8** | #音频生成 |
| 8. | [Speaker-Aware Temporal Aggregation Strategies on Segment Rep…](speaker-aware-temporal-aggregation-strategies-on-segment-rep-2607-02904/) | **6.8** | #抑郁检测 |
| 9. | [Layer-wise Cross-Lingual Depression Detection from Speech: A…](layer-wise-cross-lingual-depression-detection-from-speech-an-2607-02920/) | **6.5** | #抑郁检测 |
| 10. | [Multi-Modal Causal Disentanglement for Multi-Domain Sequenti…](multi-modal-causal-disentanglement-for-multi-domain-sequenti-2611-33628/) | **5.8** | #音乐推荐 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="line-level-singer-diarization-in-multi-member-pop-songs-a-be-2611-33247/">Line-Level Singer Diarization in Multi-Member Pop Songs: A Benchmark, Lead-Vocal Isolation, and Song-Level Decoding</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#说话人日志</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出逐行歌手日志任务与 ColorCoded-SD 基准，用主唱分离+歌声嵌入+歌曲级解码将 B-cubed F1 提升约 0.06。</div>
<div class="card-action">
<a href="line-level-singer-diarization-in-multi-member-pop-songs-a-be-2611-33247/">详情 →</a> · <a href="https://arxiv.org/abs/2611.33247" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="fsc-net-integrating-fast-fourier-convolutions-and-progressiv-2606-06962/">FSC-Net: Integrating Fast Fourier Convolutions and Progressive Learning for Speech Bandwidth Extension</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">FSC-Net 用快速傅里叶卷积扩展感受野至全频谱，并以频率渐进课程学习重建高频，实现 1.54M 参数的高效语音带宽扩展。</div>
<div class="card-action">
<a href="fsc-net-integrating-fast-fourier-convolutions-and-progressiv-2606-06962/">详情 →</a> · <a href="https://arxiv.org/abs/2606.06962" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="mozaic-an-audio-video-deepfake-benchmark-for-telling-what-is-2611-31301/">MOZAIC: An Audio-Video Deepfake Benchmark for Telling What Is Fake</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频深度伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">构建音视频配对四分类深度伪造基准，量化视觉与语音模态贡献，评测12个MLLM与训练检测器。</div>
<div class="card-action">
<a href="mozaic-an-audio-video-deepfake-benchmark-for-telling-what-is-2611-31301/">详情 →</a> · <a href="https://arxiv.org/abs/2611.31301" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="emilia2-a-large-scale-dataset-for-controllable-long-form-spe-2611-13614/">Emilia2: A Large-Scale Dataset for Controllable Long-Form Speech Generation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">构建229K小时多语种长语音数据集Emilia2，含单说话人长语音与多人对话，支持自然语言指令与副语言标签控制，并训练AR/NAR基线验证。</div>
<div class="card-action">
<a href="emilia2-a-large-scale-dataset-for-controllable-long-form-spe-2611-13614/">详情 →</a> · <a href="https://arxiv.org/abs/2611.13614" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="learning-temporal-stabilization-for-double-talk-robust-delay-2611-33689/">Learning Temporal Stabilization for Double-Talk-Robust Delay Estimation in Acoustic Echo Cancellation</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#声学回声消除</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">保留GCC-PHAT为固定骨干，仅学习13.2K参数因果2D CNN在时延-相关图上做时间稳定化，抑制双讲瞬态伪峰。</div>
<div class="card-action">
<a href="learning-temporal-stabilization-for-double-talk-robust-delay-2611-33689/">详情 →</a> · <a href="https://arxiv.org/abs/2611.33689" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="direct-conditioning-of-audio-diffusion-transformers-on-fmri--2611-12603/">Direct Conditioning of Audio Diffusion Transformers on fMRI Reveals Cortical Contributions to Sound Reconstruction</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 MAAS，用 ROI 级 fMRI 响应经区域投影与脑 token 交叉注意力直接条件化 Stable Audio 扩散 Transformer，实现端到端脑活动到音频重建。</div>
<div class="card-action">
<a href="direct-conditioning-of-audio-diffusion-transformers-on-fmri--2611-12603/">详情 →</a> · <a href="https://arxiv.org/abs/2611.12603" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="avenue-audio-video-editing-understanding-and-evaluation-2609-04253/">AVENUE: Audio-Video EditiNg Understanding and Evaluation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 AVENUE 音视频编辑基准与模态感知评测框架，覆盖 1291 段视频、7957 条指令，揭示跨模态意外改动问题。</div>
<div class="card-action">
<a href="avenue-audio-video-editing-understanding-and-evaluation-2609-04253/">详情 →</a> · <a href="https://arxiv.org/abs/2609.04253" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="speaker-aware-temporal-aggregation-strategies-on-segment-rep-2607-02904/">Speaker-Aware Temporal Aggregation Strategies on Segment Representations for Depression Detection in Dyadic Interaction: A Benchmark Study</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#抑郁检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">构建 DEPOOL 基准，在英/汉语抑郁语料上比较 6 种时序聚合架构与 6 种冻结语音骨干，揭示单种子稳定性与跨种子可靠性不一致。</div>
<div class="card-action">
<a href="speaker-aware-temporal-aggregation-strategies-on-segment-rep-2607-02904/">详情 →</a> · <a href="https://arxiv.org/abs/2607.02904" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="layer-wise-cross-lingual-depression-detection-from-speech-an-2607-02920/">Layer-wise Cross-Lingual Depression Detection from Speech: Analysis with Contrastive Alignment</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#抑郁检测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用监督对比对齐把英语与普通话 WavLM 表征映射到共享临床空间，并量化说话人泄漏导致的指标虚高。</div>
<div class="card-action">
<a href="layer-wise-cross-lingual-depression-detection-from-speech-an-2607-02920/">详情 →</a> · <a href="https://arxiv.org/abs/2607.02920" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="multi-modal-causal-disentanglement-for-multi-domain-sequenti-2611-33628/">Multi-Modal Causal Disentanglement for Multi-Domain Sequential Audio Recommendation</a>
<div class="card-meta">
<span class="card-score">5.8</span>
<span class="tag-pill">#音乐推荐</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">CAMAR 用因果解耦把用户表示拆成域不变与域特异分量，并用多模态语义 ID 缓解音乐平台多域推荐中的负迁移与冷启动。</div>
<div class="card-action">
<a href="multi-modal-causal-disentanglement-for-multi-domain-sequenti-2611-33628/">详情 →</a> · <a href="https://arxiv.org/abs/2611.33628" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
