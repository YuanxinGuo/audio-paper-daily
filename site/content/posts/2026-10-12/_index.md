---
title: "语音/音频论文速递 2026-10-12"
date: 2026-10-12T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 6 篇 · 最高分 8.8（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">6</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #语音识别 | 2篇 | `██████████` |
| #目标说话人提取 | 1篇 | `█████` |
| #声源定位 | 1篇 | `█████` |
| #语音分离 | 1篇 | `█████` |
| #多模态推理 | 1篇 | `█████` |
| #音频处理 | 1篇 | `█████` |
| #音频驱动动作生成 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="phonology-aware-speaker-extraction-frontend-for-audio-llms-2610-13500/">Phonology-Aware Speaker Extraction Frontend for Audio LLMs</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">LATTE 用 5.2M 参数前端，按样本难度与音系先验自适应路由多深度 TSE，PolyExtract 上 SI-SNRi 15.07 dB、算力降 43.4%。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="efficient-audio-visual-speech-enhancement-via-reinforcement--2610-12796/">Efficient Audio-Visual Speech Enhancement via Reinforcement Learning-Based Neural Architecture Search</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">用强化学习驱动的NAS搜索轻量音视频语音增强架构，仅2.9M参数即达14.5 dB SI-SNR提升，移动CPU实时因子降4.3倍。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="rdse-real-time-directional-speech-enhancement-framework-for--2610-12476/">RDSE: Real-Time Directional Speech Enhancement Framework for Dual-Mic Commodity Smartphones</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">面向双麦低端手机，用视觉参数化导向矢量，串联去混响、TCN波束成形与MetricGAN去噪，实现实时定向语音增强。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="phonology-aware-speaker-extraction-frontend-for-audio-llms-2610-13500/">Phonology-Aware Speaker Extraction Frontend for Audio LLMs</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">LATTE 用 5.2M 参数前端，按样本难度与音系先验自适应路由多深度 TSE，PolyExtract 上 SI-SNRi 15.07 dB、算力降 43.4%。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="frontend-assisted-large-audio-language-models-for-slt2026-sm-2610-13282/">Frontend-Assisted Large Audio-Language Models for SLT2026 SmartGlasses Challenge</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音识别</span>
</div>
<div class="card-tldr">面向SmartGlasses Challenge Track 1，用SoulX-Transcriber多模态大模型做时间戳说话人属性ASR，并对比前端分离对性能的影响。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="phonology-aware-speaker-extraction-frontend-for-audio-llms-2610-13500/">Phonology-Aware Speaker Extraction Frontend for Audio LLMs</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">LATTE 用 5.2M 参数前端，按样本难度与音系先验自适应路由多深度 TSE，PolyExtract 上 SI-SNRi 15.07 dB、算力降 43.4%。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="lightweight-systems-for-spatial-semantic-segmentation-of-sou-2610-12693/">Lightweight Systems for Spatial Semantic Segmentation of Sound Scenes</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">评估轻量标签与分离模型替代 DCASE 2025 S5 基线中大模型后的性能损失，用 PANNs/DyMNs 与 SuDoRMRF 卷积分离器组合。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="frontend-assisted-large-audio-language-models-for-slt2026-sm-2610-13282/">Frontend-Assisted Large Audio-Language Models for SLT2026 SmartGlasses Challenge</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音识别</span>
</div>
<div class="card-tldr">面向SmartGlasses Challenge Track 1，用SoulX-Transcriber多模态大模型做时间戳说话人属性ASR，并对比前端分离对性能的影响。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="qc-mi-ovsel-benchmarking-query-conditioned-multi-instance-op-2610-13198/">QC-MI-OVSEL: Benchmarking Query-Conditioned Multi-Instance Open-Vocabulary Sound Event Localization</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#声源定位</span>
</div>
<div class="card-tldr">提出查询条件多实例开放词汇声事件定位基准与Q-RSet方法，用查询槽与责任聚合预测声源集合。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="rdse-real-time-directional-speech-enhancement-framework-for--2610-12476/">RDSE: Real-Time Directional Speech Enhancement Framework for Dual-Mic Commodity Smartphones</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">面向双麦低端手机，用视觉参数化导向矢量，串联去混响、TCN波束成形与MetricGAN去噪，实现实时定向语音增强。</div>
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
| 🥇 | [Phonology-Aware Speaker Extraction Frontend for Audio LLMs](phonology-aware-speaker-extraction-frontend-for-audio-llms-2610-13500/) 🎯 | **8.8** | #目标说话人提取 |
| 🥈 | [Efficient Audio-Visual Speech Enhancement via Reinforcement …](efficient-audio-visual-speech-enhancement-via-reinforcement--2610-12796/) 🎯 | **8.2** | #语音增强 |
| 🥉 | [QC-MI-OVSEL: Benchmarking Query-Conditioned Multi-Instance O…](qc-mi-ovsel-benchmarking-query-conditioned-multi-instance-op-2610-13198/) 🎯 | **8.0** | #声源定位 |
| 4. | [RDSE: Real-Time Directional Speech Enhancement Framework for…](rdse-real-time-directional-speech-enhancement-framework-for--2610-12476/) 🎯 | **7.8** | #语音增强 |
| 5. | [Lightweight Systems for Spatial Semantic Segmentation of Sou…](lightweight-systems-for-spatial-semantic-segmentation-of-sou-2610-12693/) 🎯 | **7.5** | #语音分离 |
| 6. | [Frontend-Assisted Large Audio-Language Models for SLT2026 Sm…](frontend-assisted-large-audio-language-models-for-slt2026-sm-2610-13282/) 🎯 | **7.5** | #语音识别 |
| 7. | [A Systematic Study of Cross-Modal Typographic Attacks on Aud…](a-systematic-study-of-cross-modal-typographic-attacks-on-aud-2604-03995/) | **6.8** | #多模态推理 |
| 8. | [X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation](x-avdd-cross-attentive-audio-visual-dataset-distillation-2610-13687/) | **6.8** | #音频处理 |
| 9. | [Sonic-AMG: Streaming Human Motion Generation from Spatial Au…](sonic-amg-streaming-human-motion-generation-from-spatial-aud-2610-13300/) | **6.0** | #音频驱动动作生成 |
| 10. | [CircuitTree: Composing Circuits into A Syllable Transcriber](circuittree-composing-circuits-into-a-syllable-transcriber-2610-12520/) | **6.0** | #语音识别 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="phonology-aware-speaker-extraction-frontend-for-audio-llms-2610-13500/">Phonology-Aware Speaker Extraction Frontend for Audio LLMs</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">LATTE 用 5.2M 参数前端，按样本难度与音系先验自适应路由多深度 TSE，PolyExtract 上 SI-SNRi 15.07 dB、算力降 43.4%。</div>
<div class="card-action">
<a href="phonology-aware-speaker-extraction-frontend-for-audio-llms-2610-13500/">详情 →</a> · <a href="https://arxiv.org/abs/2610.13500" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="efficient-audio-visual-speech-enhancement-via-reinforcement--2610-12796/">Efficient Audio-Visual Speech Enhancement via Reinforcement Learning-Based Neural Architecture Search</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用强化学习驱动的NAS搜索轻量音视频语音增强架构，仅2.9M参数即达14.5 dB SI-SNR提升，移动CPU实时因子降4.3倍。</div>
<div class="card-action">
<a href="efficient-audio-visual-speech-enhancement-via-reinforcement--2610-12796/">详情 →</a> · <a href="https://arxiv.org/abs/2610.12796" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="qc-mi-ovsel-benchmarking-query-conditioned-multi-instance-op-2610-13198/">QC-MI-OVSEL: Benchmarking Query-Conditioned Multi-Instance Open-Vocabulary Sound Event Localization</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#声源定位</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出查询条件多实例开放词汇声事件定位基准与Q-RSet方法，用查询槽与责任聚合预测声源集合。</div>
<div class="card-action">
<a href="qc-mi-ovsel-benchmarking-query-conditioned-multi-instance-op-2610-13198/">详情 →</a> · <a href="https://arxiv.org/abs/2610.13198" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="rdse-real-time-directional-speech-enhancement-framework-for--2610-12476/">RDSE: Real-Time Directional Speech Enhancement Framework for Dual-Mic Commodity Smartphones</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">面向双麦低端手机，用视觉参数化导向矢量，串联去混响、TCN波束成形与MetricGAN去噪，实现实时定向语音增强。</div>
<div class="card-action">
<a href="rdse-real-time-directional-speech-enhancement-framework-for--2610-12476/">详情 →</a> · <a href="https://arxiv.org/abs/2610.12476" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="lightweight-systems-for-spatial-semantic-segmentation-of-sou-2610-12693/">Lightweight Systems for Spatial Semantic Segmentation of Sound Scenes</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">评估轻量标签与分离模型替代 DCASE 2025 S5 基线中大模型后的性能损失，用 PANNs/DyMNs 与 SuDoRMRF 卷积分离器组合。</div>
<div class="card-action">
<a href="lightweight-systems-for-spatial-semantic-segmentation-of-sou-2610-12693/">详情 →</a> · <a href="https://arxiv.org/abs/2610.12693" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="frontend-assisted-large-audio-language-models-for-slt2026-sm-2610-13282/">Frontend-Assisted Large Audio-Language Models for SLT2026 SmartGlasses Challenge</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">面向SmartGlasses Challenge Track 1，用SoulX-Transcriber多模态大模型做时间戳说话人属性ASR，并对比前端分离对性能的影响。</div>
<div class="card-action">
<a href="frontend-assisted-large-audio-language-models-for-slt2026-sm-2610-13282/">详情 →</a> · <a href="https://arxiv.org/abs/2610.13282" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="a-systematic-study-of-cross-modal-typographic-attacks-on-aud-2604-03995/">A Systematic Study of Cross-Modal Typographic Attacks on Audio-Visual Reasoning</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#多模态推理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">系统研究音视频多模态大模型在语音与屏幕文字扰动下的排版攻击脆弱性，并提出微调缓解方案。</div>
<div class="card-action">
<a href="a-systematic-study-of-cross-modal-typographic-attacks-on-aud-2604-03995/">详情 →</a> · <a href="https://arxiv.org/abs/2604.03995" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="x-avdd-cross-attentive-audio-visual-dataset-distillation-2610-13687/">X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出跨注意力音视频数据集蒸馏方法X-AVDD，解耦跨模态对齐与联合优化，显存更省、合成数据对齐更好。</div>
<div class="card-action">
<a href="x-avdd-cross-attentive-audio-visual-dataset-distillation-2610-13687/">详情 →</a> · <a href="https://arxiv.org/abs/2610.13687" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="sonic-amg-streaming-human-motion-generation-from-spatial-aud-2610-13300/">Sonic-AMG: Streaming Human Motion Generation from Spatial Audio</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音频驱动动作生成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">首个从空间音频流式生成人体动作的框架，用因果Transformer与flow head实现实时在线反应生成。</div>
<div class="card-action">
<a href="sonic-amg-streaming-human-motion-generation-from-spatial-aud-2610-13300/">详情 →</a> · <a href="https://arxiv.org/abs/2610.13300" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="circuittree-composing-circuits-into-a-syllable-transcriber-2610-12520/">CircuitTree: Composing Circuits into A Syllable Transcriber</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出 CircuitTree，用贪心密度缩放组合算法将 HuBERT 音素电路组合成音节分类器，实现开音节转录 64.8% 准确率。</div>
<div class="card-action">
<a href="circuittree-composing-circuits-into-a-syllable-transcriber-2610-12520/">详情 →</a> · <a href="https://arxiv.org/abs/2610.12520" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
