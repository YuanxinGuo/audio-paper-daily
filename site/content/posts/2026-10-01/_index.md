---
title: "语音/音频论文速递 2026-10-01"
date: 2026-10-01T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 6 篇 · 最高分 8.2（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">6</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 3篇 | `██████████` |
| #双耳音频 | 2篇 | `███████` |
| #生物声学 | 2篇 | `███████` |
| #目标说话人提取 | 1篇 | `███` |
| #语音合成 | 1篇 | `███` |
| #语音识别 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="trigger-sound-suppression-for-misophonia-2609-36351/">Trigger Sound Suppression for Misophonia</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">面向恐音症，构建10类触发声数据集，用流式双路网络按one-hot/multi-hot条件选择性抑制1-3种触发声，30人听测验证降低不适。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="duspar-dual-state-sparsifying-recurrent-unit-with-feedback-m-2609-39237/">DuSpaR: Dual-State Sparsifying Recurrent Unit with Feedback Modulation for Compute-Efficient Speech Processing</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出双状态稀疏循环单元 DuSpaR，通过 ReLU 稀疏化与动态跳零，在 KWS/SLU/SE 三任务上以更少算力达到或超过 GRU。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="how-reliable-are-predicted-mos-for-reproducing-human-system--2609-39032/">How Reliable Are Predicted MOS for Reproducing Human System-Level Preferences in Speech Enhancement?</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出系统级偏好准确率SPA，衡量MOS预测模型能否复现人类对语音增强系统的偏好排序，发现单模型SPA从9.4%到76.8%差异巨大。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="improving-predicted-mos-scores-not-perceived-quality-multi-p-2609-39028/">Improving Predicted MOS Scores, Not Perceived Quality: Multi-Predictor Test-Time Optimization of Enhanced Speech</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">首次系统分析语音增强的测试时MOS优化：多预测器分数被抬高，但MUSHRA主观听感无改善。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="trigger-sound-suppression-for-misophonia-2609-36351/">Trigger Sound Suppression for Misophonia</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">面向恐音症，构建10类触发声数据集，用流式双路网络按one-hot/multi-hot条件选择性抑制1-3种触发声，30人听测验证降低不适。</div>
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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="bin2ambi-learning-ambisonic-soundfield-reconstruction-from-h-2609-39732/">Bin2Ambi: Learning Ambisonic Soundfield Reconstruction from Head-Tracked Binaural Audio</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出 Bin2Ambi 新任务：用智能耳机同时采集的双耳音频与头动数据重建 Ambisonics 声场，缓解前后混淆与锥形混淆区误差。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="audible-world-models-spatially-aware-sound-generation-for-3d-2609-38444/">Audible World Models: Spatially Aware Sound Generation for 3D Worlds</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">免训练框架为文本生成的3D世界构建全景代理，分离语义层、合成干音频并按几何声学渲染随听者移动变化的空间音频。</div>
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
| 🥇 | [Trigger Sound Suppression for Misophonia](trigger-sound-suppression-for-misophonia-2609-36351/) 🎯 | **8.2** | #目标说话人提取 |
| 🥈 | [DuSpaR: Dual-State Sparsifying Recurrent Unit with Feedback …](duspar-dual-state-sparsifying-recurrent-unit-with-feedback-m-2609-39237/) 🎯 | **8.2** | #语音增强 |
| 🥉 | [Bin2Ambi: Learning Ambisonic Soundfield Reconstruction from …](bin2ambi-learning-ambisonic-soundfield-reconstruction-from-h-2609-39732/) 🎯 | **8.0** | #双耳音频 |
| 4. | [Audible World Models: Spatially Aware Sound Generation for 3…](audible-world-models-spatially-aware-sound-generation-for-3d-2609-38444/) 🎯 | **7.8** | #双耳音频 |
| 5. | [How Reliable Are Predicted MOS for Reproducing Human System-…](how-reliable-are-predicted-mos-for-reproducing-human-system--2609-39032/) 🎯 | **7.8** | #语音增强 |
| 6. | [Improving Predicted MOS Scores, Not Perceived Quality: Multi…](improving-predicted-mos-scores-not-perceived-quality-multi-p-2609-39028/) 🎯 | **7.8** | #语音增强 |
| 7. | [Rate-Agnostic Bioacoustics: Heterogeneous Multi-Taxa Classif…](rate-agnostic-bioacoustics-heterogeneous-multi-taxa-classifi-2609-37540/) | **7.0** | #生物声学 |
| 8. | [Bad: Taming the Bioacoustic Data Deluge with a Bat Activity …](bad-taming-the-bioacoustic-data-deluge-with-a-bat-activity-d-2609-37518/) | **7.0** | #生物声学 |
| 9. | [Harmonizing Spectral Evolution in Conditional Flow Matching …](harmonizing-spectral-evolution-in-conditional-flow-matching--2609-34431/) | **6.8** | #语音合成 |
| 10. | [WASIL: In-the-Wild Arabic Spoken Interactions with LLMs](wasil-in-the-wild-arabic-spoken-interactions-with-llms-2605-16364/) | **6.0** | #语音识别 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="trigger-sound-suppression-for-misophonia-2609-36351/">Trigger Sound Suppression for Misophonia</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">面向恐音症，构建10类触发声数据集，用流式双路网络按one-hot/multi-hot条件选择性抑制1-3种触发声，30人听测验证降低不适。</div>
<div class="card-action">
<a href="trigger-sound-suppression-for-misophonia-2609-36351/">详情 →</a> · <a href="https://arxiv.org/abs/2609.36351" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="duspar-dual-state-sparsifying-recurrent-unit-with-feedback-m-2609-39237/">DuSpaR: Dual-State Sparsifying Recurrent Unit with Feedback Modulation for Compute-Efficient Speech Processing</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出双状态稀疏循环单元 DuSpaR，通过 ReLU 稀疏化与动态跳零，在 KWS/SLU/SE 三任务上以更少算力达到或超过 GRU。</div>
<div class="card-action">
<a href="duspar-dual-state-sparsifying-recurrent-unit-with-feedback-m-2609-39237/">详情 →</a> · <a href="https://arxiv.org/abs/2609.39237" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="bin2ambi-learning-ambisonic-soundfield-reconstruction-from-h-2609-39732/">Bin2Ambi: Learning Ambisonic Soundfield Reconstruction from Head-Tracked Binaural Audio</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 Bin2Ambi 新任务：用智能耳机同时采集的双耳音频与头动数据重建 Ambisonics 声场，缓解前后混淆与锥形混淆区误差。</div>
<div class="card-action">
<a href="bin2ambi-learning-ambisonic-soundfield-reconstruction-from-h-2609-39732/">详情 →</a> · <a href="https://arxiv.org/abs/2609.39732" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="audible-world-models-spatially-aware-sound-generation-for-3d-2609-38444/">Audible World Models: Spatially Aware Sound Generation for 3D Worlds</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">免训练框架为文本生成的3D世界构建全景代理，分离语义层、合成干音频并按几何声学渲染随听者移动变化的空间音频。</div>
<div class="card-action">
<a href="audible-world-models-spatially-aware-sound-generation-for-3d-2609-38444/">详情 →</a> · <a href="https://arxiv.org/abs/2609.38444" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="how-reliable-are-predicted-mos-for-reproducing-human-system--2609-39032/">How Reliable Are Predicted MOS for Reproducing Human System-Level Preferences in Speech Enhancement?</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出系统级偏好准确率SPA，衡量MOS预测模型能否复现人类对语音增强系统的偏好排序，发现单模型SPA从9.4%到76.8%差异巨大。</div>
<div class="card-action">
<a href="how-reliable-are-predicted-mos-for-reproducing-human-system--2609-39032/">详情 →</a> · <a href="https://arxiv.org/abs/2609.39032" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="improving-predicted-mos-scores-not-perceived-quality-multi-p-2609-39028/">Improving Predicted MOS Scores, Not Perceived Quality: Multi-Predictor Test-Time Optimization of Enhanced Speech</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">首次系统分析语音增强的测试时MOS优化：多预测器分数被抬高，但MUSHRA主观听感无改善。</div>
<div class="card-action">
<a href="improving-predicted-mos-scores-not-perceived-quality-multi-p-2609-39028/">详情 →</a> · <a href="https://arxiv.org/abs/2609.39028" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="rate-agnostic-bioacoustics-heterogeneous-multi-taxa-classifi-2609-37540/">Rate-Agnostic Bioacoustics: Heterogeneous Multi-Taxa Classification with Continuous Filterbanks and Fourier Neural Operators</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出采样率无关前端SFI配合Fourier神经算子主干，直接在原生采样率处理生物声学录音，在84类60种采样率语料上达0.906准确率。</div>
<div class="card-action">
<a href="rate-agnostic-bioacoustics-heterogeneous-multi-taxa-classifi-2609-37540/">详情 →</a> · <a href="https://arxiv.org/abs/2609.37540" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="bad-taming-the-bioacoustic-data-deluge-with-a-bat-activity-d-2609-37518/">Bad: Taming the Bioacoustic Data Deluge with a Bat Activity Detector</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">面向蝙蝠超声被动监测的硬件感知活动检测器，8-bit 量化部署于 EFM32PG26，低发生率下 AUC 0.9748，精度较 Goertzel 提升 33 倍。</div>
<div class="card-action">
<a href="bad-taming-the-bioacoustic-data-deluge-with-a-bat-activity-d-2609-37518/">详情 →</a> · <a href="https://arxiv.org/abs/2609.37518" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="harmonizing-spectral-evolution-in-conditional-flow-matching--2609-34431/">Harmonizing Spectral Evolution in Conditional Flow Matching for TTS</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出免训练的频率选择性增强策略，用DWT在ODE积分中动态调制mel子带，同步CFM-TTS的频谱演化。</div>
<div class="card-action">
<a href="harmonizing-spectral-evolution-in-conditional-flow-matching--2609-34431/">详情 →</a> · <a href="https://arxiv.org/abs/2609.34431" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="wasil-in-the-wild-arabic-spoken-interactions-with-llms-2605-16364/">WASIL: In-the-Wild Arabic Spoken Interactions with LLMs</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">发布WASIL阿拉伯语真实场景语音交互数据集，含8529轮对话与点赞/点踩反馈，并提供2000轮方言测试集与多ASR后编辑金标转录。</div>
<div class="card-action">
<a href="wasil-in-the-wild-arabic-spoken-interactions-with-llms-2605-16364/">详情 →</a> · <a href="https://arxiv.org/abs/2605.16364" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
