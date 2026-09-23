---
title: "语音/音频论文速递 2026-09-23"
date: 2026-09-23T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 6 篇 · 最高分 8.8（#语音增强）"
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
| #目标说话人提取 | 2篇 | `██████████` |
| #双耳音频 | 1篇 | `█████` |
| #乐器分离 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #音频生成 | 1篇 | `█████` |
| #音频理解 | 1篇 | `█████` |
| #音频处理 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="se-msb-end-to-end-unpaired-speech-enhancement-using-mamba-sc-2609-26000/">SE-MSB: End-to-End Unpaired Speech Enhancement using Mamba Schr\"odinger Bridges</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">用 Mamba 扩散模型实现端到端无配对语音增强，基于 Diffusion Schrödinger Bridge 学习干净与退化语音分布间的随机传输。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="challenges-of-multi-speaker-extraction-for-real-conversation-2609-25948/">Challenges of Multi-Speaker Extraction for Real Conversational Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">针对真实多方对话中静音过多与注册语音失配问题，提出新损失函数缓解静音影响，STOI从0.55提升至0.60。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="a-hybrid-classical-learning-framework-for-adaptive-decision--2609-26183/">A Hybrid Classical-Learning Framework for Adaptive Decision Directed Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">在经典 Decision-Directed 增强上引入帧级 beta 下界约束，并用轻量 MLP 预测 beta，在 VoiceBank-DEMAND 上平均 SNR 提升 4.41 dB。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="inter-speaker-relative-cues-for-two-stage-text-guided-target-2603-01316/">Inter-Speaker Relative Cues for Two-Stage Text-Guided Target Speech Extraction</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出两阶段文本引导目标说话人提取框架，用相对线索替代绝对类别线索，先分离候选源再用文本分类器选目标。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="challenges-of-multi-speaker-extraction-for-real-conversation-2609-25948/">Challenges of Multi-Speaker Extraction for Real Conversational Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">针对真实多方对话中静音过多与注册语音失配问题，提出新损失函数缓解静音影响，STOI从0.55提升至0.60。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="inter-speaker-relative-cues-for-two-stage-text-guided-target-2603-01316/">Inter-Speaker Relative Cues for Two-Stage Text-Guided Target Speech Extraction</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出两阶段文本引导目标说话人提取框架，用相对线索替代绝对类别线索，先分离候选源再用文本分类器选目标。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="hrtf-upsampling-across-varying-measurement-configurations-wi-2609-25995/">HRTF Upsampling Across Varying Measurement Configurations with Geometry-Aware Query-Conditioned Aggregation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出GeoAtt，用单一模型对多种稀疏测量配置做HRTF上采样，几何感知查询条件聚合加Conformer频域建模，在SONICOM上取得最低LSD。</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="mambavoice-lightweight-audiovisual-singing-voice-separation--2609-26635/">MambaVoice: Lightweight Audiovisual Singing Voice Separation Via A Hybrid Mamba-Transformer Model</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">MambaVoice 用 Mamba-Transformer 混合骨干加视听融合，轻量地做目标歌声分离，16.2M 参数在 Acappella 上达 14.18 dB SDR。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [SE-MSB: End-to-End Unpaired Speech Enhancement using Mamba S…](se-msb-end-to-end-unpaired-speech-enhancement-using-mamba-sc-2609-26000/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [HRTF Upsampling Across Varying Measurement Configurations wi…](hrtf-upsampling-across-varying-measurement-configurations-wi-2609-25995/) 🎯 | **8.8** | #双耳音频 |
| 🥉 | [MambaVoice: Lightweight Audiovisual Singing Voice Separation…](mambavoice-lightweight-audiovisual-singing-voice-separation--2609-26635/) 🎯 | **8.2** | #乐器分离 |
| 4. | [Inter-Speaker Relative Cues for Two-Stage Text-Guided Target…](inter-speaker-relative-cues-for-two-stage-text-guided-target-2603-01316/) 🎯 | **8.0** | #目标说话人提取 |
| 5. | [Challenges of Multi-Speaker Extraction for Real Conversation…](challenges-of-multi-speaker-extraction-for-real-conversation-2609-25948/) 🎯 | **7.8** | #目标说话人提取 |
| 6. | [LLM-Anchored Paralinguistic Enrichment for Alzheimer's Disea…](llm-anchored-paralinguistic-enrichment-for-alzheimer-s-disea-2609-10896/) | **7.0** | #语音识别 |
| 7. | [Intervention, Not Shared Latents: Blocking Visual Shortcuts …](intervention-not-shared-latents-blocking-visual-shortcuts-in-2609-22361/) | **6.8** | #音频生成 |
| 8. | [Discrete vs. Continuous: A Comprehensive Study of Unified Au…](discrete-vs-continuous-a-comprehensive-study-of-unified-audi-2609-22851/) | **6.8** | #音频理解 |
| 9. | [Modality-Gated Deep Adapters: Adding a Modality to a Frozen …](modality-gated-deep-adapters-adding-a-modality-to-a-frozen-e-2609-26182/) | **6.8** | #音频处理 |
| 10. | [A Hybrid Classical-Learning Framework for Adaptive Decision …](a-hybrid-classical-learning-framework-for-adaptive-decision--2609-26183/) 🎯 | **6.5** | #语音增强 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="se-msb-end-to-end-unpaired-speech-enhancement-using-mamba-sc-2609-26000/">SE-MSB: End-to-End Unpaired Speech Enhancement using Mamba Schr\"odinger Bridges</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用 Mamba 扩散模型实现端到端无配对语音增强，基于 Diffusion Schrödinger Bridge 学习干净与退化语音分布间的随机传输。</div>
<div class="card-action">
<a href="se-msb-end-to-end-unpaired-speech-enhancement-using-mamba-sc-2609-26000/">详情 →</a> · <a href="https://arxiv.org/abs/2609.26000" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="hrtf-upsampling-across-varying-measurement-configurations-wi-2609-25995/">HRTF Upsampling Across Varying Measurement Configurations with Geometry-Aware Query-Conditioned Aggregation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出GeoAtt，用单一模型对多种稀疏测量配置做HRTF上采样，几何感知查询条件聚合加Conformer频域建模，在SONICOM上取得最低LSD。</div>
<div class="card-action">
<a href="hrtf-upsampling-across-varying-measurement-configurations-wi-2609-25995/">详情 →</a> · <a href="https://arxiv.org/abs/2609.25995" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="mambavoice-lightweight-audiovisual-singing-voice-separation--2609-26635/">MambaVoice: Lightweight Audiovisual Singing Voice Separation Via A Hybrid Mamba-Transformer Model</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">MambaVoice 用 Mamba-Transformer 混合骨干加视听融合，轻量地做目标歌声分离，16.2M 参数在 Acappella 上达 14.18 dB SDR。</div>
<div class="card-action">
<a href="mambavoice-lightweight-audiovisual-singing-voice-separation--2609-26635/">详情 →</a> · <a href="https://arxiv.org/abs/2609.26635" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="inter-speaker-relative-cues-for-two-stage-text-guided-target-2603-01316/">Inter-Speaker Relative Cues for Two-Stage Text-Guided Target Speech Extraction</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出两阶段文本引导目标说话人提取框架，用相对线索替代绝对类别线索，先分离候选源再用文本分类器选目标。</div>
<div class="card-action">
<a href="inter-speaker-relative-cues-for-two-stage-text-guided-target-2603-01316/">详情 →</a> · <a href="https://arxiv.org/abs/2603.01316" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="challenges-of-multi-speaker-extraction-for-real-conversation-2609-25948/">Challenges of Multi-Speaker Extraction for Real Conversational Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">针对真实多方对话中静音过多与注册语音失配问题，提出新损失函数缓解静音影响，STOI从0.55提升至0.60。</div>
<div class="card-action">
<a href="challenges-of-multi-speaker-extraction-for-real-conversation-2609-25948/">详情 →</a> · <a href="https://arxiv.org/abs/2609.25948" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="llm-anchored-paralinguistic-enrichment-for-alzheimer-s-disea-2609-10896/">LLM-Anchored Paralinguistic Enrichment for Alzheimer's Disease Detection</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出LAPE框架，将韵律事件文本化后与LLM语言表征融合，用于阿尔茨海默病自动检测，在ADReSS/ADReSSo上取得SOTA。</div>
<div class="card-action">
<a href="llm-anchored-paralinguistic-enrichment-for-alzheimer-s-disea-2609-10896/">详情 →</a> · <a href="https://arxiv.org/abs/2609.10896" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="intervention-not-shared-latents-blocking-visual-shortcuts-in-2609-22361/">Intervention, Not Shared Latents: Blocking Visual Shortcuts in Audio-Video Generation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用因果干预而非共享隐变量阻断音视频生成中的视觉捷径，证明共享隐变量无法修复该失败模式。</div>
<div class="card-action">
<a href="intervention-not-shared-latents-blocking-visual-shortcuts-in-2609-22361/">详情 →</a> · <a href="https://arxiv.org/abs/2609.22361" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="discrete-vs-continuous-a-comprehensive-study-of-unified-audi-2609-22851/">Discrete vs. Continuous: A Comprehensive Study of Unified Audio Understanding in LALMs</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">系统对比LALM中连续特征与离散token在语音、声音、音乐理解上的表现，发现语义约束对tokenization至关重要。</div>
<div class="card-action">
<a href="discrete-vs-continuous-a-comprehensive-study-of-unified-audi-2609-22851/">详情 →</a> · <a href="https://arxiv.org/abs/2609.22851" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="modality-gated-deep-adapters-adding-a-modality-to-a-frozen-e-2609-26182/">Modality-Gated Deep Adapters: Adding a Modality to a Frozen Embedding Model with Exact Preservation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出模态门控深度适配器，在冻结多模态嵌入LLM上新增音频/热成像模态，保证原有输出逐位不变。</div>
<div class="card-action">
<a href="modality-gated-deep-adapters-adding-a-modality-to-a-frozen-e-2609-26182/">详情 →</a> · <a href="https://arxiv.org/abs/2609.26182" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="a-hybrid-classical-learning-framework-for-adaptive-decision--2609-26183/">A Hybrid Classical-Learning Framework for Adaptive Decision Directed Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在经典 Decision-Directed 增强上引入帧级 beta 下界约束，并用轻量 MLP 预测 beta，在 VoiceBank-DEMAND 上平均 SNR 提升 4.41 dB。</div>
<div class="card-action">
<a href="a-hybrid-classical-learning-framework-for-adaptive-decision--2609-26183/">详情 →</a> · <a href="https://arxiv.org/abs/2609.26183" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
