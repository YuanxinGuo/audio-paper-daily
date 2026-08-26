---
title: "语音/音频论文速递 2026-08-26"
date: 2026-08-26T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 9 篇 · 重点领域 4 篇 · 最高分 9.5（#语音分离）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">9</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">4</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音分离 | 1篇 | `██████████` |
| #音频伪造检测 | 1篇 | `██████████` |
| #语音增强 | 1篇 | `██████████` |
| #乐器分离 | 1篇 | `██████████` |
| #音频生成评估 | 1篇 | `██████████` |
| #音频分类 | 1篇 | `██████████` |
| #视频字幕生成 | 1篇 | `██████████` |
| #视频目标分割 | 1篇 | `██████████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="at-add-a-benchmark-and-challenge-for-robust-and-all-type-aud-2608-23437/">AT-ADD: A Benchmark and Challenge for Robust and All-Type Audio Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#音频伪造检测</span>
</div>
<div class="card-tldr">提出AT-ADD基准与挑战赛，评估鲁棒语音和全类型音频深度伪造检测，涵盖语音、环境声、歌声和音乐。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="lipsam-lipschitz-continuous-neural-networks-for-convergent-p-2608-23038/">LipsAM: Lipschitz-continuous Neural Networks for Convergent Plug-and-Play Audio Signal Recovery</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">本文为音频信号处理中的幅度修改器（AM）建立了Lipschitz连续性的充要条件，提出LipsAM架构，并用于即插即用语音去混响，保证算法收敛。</div>
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
<a class="card-title" href="flowsep-2-self-supervised-flow-matching-for-language-queried-2608-22111/">FlowSep 2: Self-Supervised Flow Matching for Language-Queried Audio Source Separation</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">FlowSep2 提出基于流匹配的生成式语言查询音频分离模型，利用自监督流匹配范式提升复杂声学场景下的分离性能。</div>
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
<a class="card-title" href="automatic-curation-of-large-scale-high-quality-multi-categor-2510-07840/">Automatic Curation of Large-Scale, High-Quality, Multi-Category Music Source Separation Dataset</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">提出ACMID大规模多类别音乐源分离数据集，通过自动清洗提升数据质量，扩展至7-stem分离，显著提升SOTA模型性能。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [FlowSep 2: Self-Supervised Flow Matching for Language-Querie…](flowsep-2-self-supervised-flow-matching-for-language-queried-2608-22111/) 🎯 | **9.5** | #语音分离 |
| 🥈 | [AT-ADD: A Benchmark and Challenge for Robust and All-Type Au…](at-add-a-benchmark-and-challenge-for-robust-and-all-type-aud-2608-23437/) 🎯 | **9.2** | #音频伪造检测 |
| 🥉 | [LipsAM: Lipschitz-continuous Neural Networks for Convergent …](lipsam-lipschitz-continuous-neural-networks-for-convergent-p-2608-23038/) 🎯 | **9.2** | #语音增强 |
| 4. | [Automatic Curation of Large-Scale, High-Quality, Multi-Categ…](automatic-curation-of-large-scale-high-quality-multi-categor-2510-07840/) 🎯 | **8.8** | #乐器分离 |
| 5. | [AcoustiTrace: When Plausible Sound Violates Physics](acoustitrace-when-plausible-sound-violates-physics-2608-02035/) | **7.8** | #音频生成评估 |
| 6. | [Few-Shot Open-Set Audio Classification via Transductive Prot…](few-shot-open-set-audio-classification-via-transductive-prot-2607-26607/) | **7.8** | #音频分类 |
| 7. | [Pre-Decoding Acoustic Triage for Budgeted Vision-Language Ca…](pre-decoding-acoustic-triage-for-budgeted-vision-language-ca-2608-22359/) | **7.2** | #视频字幕生成 |
| 8. | [Motion-Aware Reasoning from Speech to Mask Tracks: Runner-up…](motion-aware-reasoning-from-speech-to-mask-tracks-runner-up--2608-22337/) | **7.2** | #视频目标分割 |
| 9. | [Vibrato Matching for Modulation Control and Blending in Soun…](vibrato-matching-for-modulation-control-and-blending-in-soun-2608-22057/) | **6.8** | #音频处理 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="flowsep-2-self-supervised-flow-matching-for-language-queried-2608-22111/">FlowSep 2: Self-Supervised Flow Matching for Language-Queried Audio Source Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">FlowSep2 提出基于流匹配的生成式语言查询音频分离模型，利用自监督流匹配范式提升复杂声学场景下的分离性能。</div>
<div class="card-action">
<a href="flowsep-2-self-supervised-flow-matching-for-language-queried-2608-22111/">详情 →</a> · <a href="https://arxiv.org/abs/2608.22111" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="at-add-a-benchmark-and-challenge-for-robust-and-all-type-aud-2608-23437/">AT-ADD: A Benchmark and Challenge for Robust and All-Type Audio Deepfake Detection</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AT-ADD基准与挑战赛，评估鲁棒语音和全类型音频深度伪造检测，涵盖语音、环境声、歌声和音乐。</div>
<div class="card-action">
<a href="at-add-a-benchmark-and-challenge-for-robust-and-all-type-aud-2608-23437/">详情 →</a> · <a href="https://arxiv.org/abs/2608.23437" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="lipsam-lipschitz-continuous-neural-networks-for-convergent-p-2608-23038/">LipsAM: Lipschitz-continuous Neural Networks for Convergent Plug-and-Play Audio Signal Recovery</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文为音频信号处理中的幅度修改器（AM）建立了Lipschitz连续性的充要条件，提出LipsAM架构，并用于即插即用语音去混响，保证算法收敛。</div>
<div class="card-action">
<a href="lipsam-lipschitz-continuous-neural-networks-for-convergent-p-2608-23038/">详情 →</a> · <a href="https://arxiv.org/abs/2608.23038" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="automatic-curation-of-large-scale-high-quality-multi-categor-2510-07840/">Automatic Curation of Large-Scale, High-Quality, Multi-Category Music Source Separation Dataset</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出ACMID大规模多类别音乐源分离数据集，通过自动清洗提升数据质量，扩展至7-stem分离，显著提升SOTA模型性能。</div>
<div class="card-action">
<a href="automatic-curation-of-large-scale-high-quality-multi-categor-2510-07840/">详情 →</a> · <a href="https://arxiv.org/abs/2510.07840" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="acoustitrace-when-plausible-sound-violates-physics-2608-02035/">AcoustiTrace: When Plausible Sound Violates Physics</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频生成评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AcoustiTrace基准，从声学过程维度评估音视频生成中的物理合理性，发现现有模型在基础声学过程上仍存在不足。</div>
<div class="card-action">
<a href="acoustitrace-when-plausible-sound-violates-physics-2608-02035/">详情 →</a> · <a href="https://arxiv.org/abs/2608.02035" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="few-shot-open-set-audio-classification-via-transductive-prot-2607-26607/">Few-Shot Open-Set Audio Classification via Transductive Prototype Refinement and Class Logit Enhancement</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频分类</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出两阶段直推式方法，通过潜在内点加权和先验自适应自由能评分，提升少样本开集音频分类性能。</div>
<div class="card-action">
<a href="few-shot-open-set-audio-classification-via-transductive-prot-2607-26607/">详情 →</a> · <a href="https://arxiv.org/abs/2607.26607" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="pre-decoding-acoustic-triage-for-budgeted-vision-language-ca-2608-22359/">Pre-Decoding Acoustic Triage for Budgeted Vision-Language Captioning of Untrimmed Egocentric Video</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#视频字幕生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出音频优先的预解码分流策略，在不解码视频帧的情况下选择关键窗口，减少VLM调用成本，提升动作覆盖。</div>
<div class="card-action">
<a href="pre-decoding-acoustic-triage-for-budgeted-vision-language-ca-2608-22359/">详情 →</a> · <a href="https://arxiv.org/abs/2608.22359" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="motion-aware-reasoning-from-speech-to-mask-tracks-runner-up--2608-22337/">Motion-Aware Reasoning from Speech to Mask Tracks: Runner-up Solution for the MeViS-Audio Track of the 8th LSVOS Challenge 2026</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#视频目标分割</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Speech2MaskTrack，结合语音识别、运动感知时间定位与SAM3.1跟踪，在LSVOS挑战赛MeViS-Audio赛道获第二名。</div>
<div class="card-action">
<a href="motion-aware-reasoning-from-speech-to-mask-tracks-runner-up--2608-22337/">详情 →</a> · <a href="https://arxiv.org/abs/2608.22337" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="vibrato-matching-for-modulation-control-and-blending-in-soun-2608-22057/">Vibrato Matching for Modulation Control and Blending in Sound Mixtures</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出颤音匹配算法，通过抑制目标信号颤音并转移源信号颤音，使混合音源感知为单一源，并降低源分离性能。</div>
<div class="card-action">
<a href="vibrato-matching-for-modulation-control-and-blending-in-soun-2608-22057/">详情 →</a> · <a href="https://arxiv.org/abs/2608.22057" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
