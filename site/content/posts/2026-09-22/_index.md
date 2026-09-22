---
title: "语音/音频论文速递 2026-09-22"
date: 2026-09-22T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 7 篇 · 最高分 8.8（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">7</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #双耳音频 | 3篇 | `██████████` |
| #语音合成 | 2篇 | `███████` |
| #语音分离 | 1篇 | `███` |
| #声源定位与检测 | 1篇 | `███` |
| #语音增强 | 1篇 | `███` |
| #房间冲激响应生成 | 1篇 | `███` |
| #音频生成 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="adaptive-depth-and-expert-refinement-for-efficient-speech-en-2609-22824/">Adaptive Depth and Expert Refinement for Efficient Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出 ADER，用自适应深度控制器与条件专家路由实现输入相关的渐进式语音增强，在 VCTK-DEMAND 上大幅削减参数量与计算量。</div>
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
<a class="card-title" href="litecass-a-lightweight-end-to-end-network-for-real-time-ster-2609-23453/">LiteCASS: A Lightweight End-to-End Network for Real-Time Stereo Cinematic Audio Source Separation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">LiteCASS 用两个紧凑 U-Net 加 STFT 子带重排，实现 1.06M 参数、0.72G MACs/s 的实时立体声电影音源分离。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="bearings-self-supervised-soundfield-embeddings-from-first-or-2609-23152/">Bearings: Self-Supervised Soundfield Embeddings from First-Order Ambisonics</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">用一阶Ambisonics自监督预训练掩码自编码器，学得可复用的声场嵌入，与冻结单通道声学编码器拼接即可实现声事件定位与检测。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="generative-learning-for-ambisonic-upscaling-2609-23479/">Generative Learning for Ambisonic Upscaling</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">将 Ambisonics 升阶视为生成任务，用 Score-based 与 Flow Matching 从低阶估计高阶分量，混响下优于判别式基线。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="omniecho-spatial-audio-understanding-for-embodied-agents-2609-23407/">OmniEcho: Spatial Audio Understanding for Embodied Agents</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出 OmniEchoBench 空间视听基准与 OmniEcho 全模态模型，用 FOA 空间编码器实现声源定位与声引导导航。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="equiseld-efficient-training-of-equivariant-sound-event-local-2609-23156/">EquiSELD: Efficient training of equivariant sound event localization and detection networks</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#声源定位与检测</span>
</div>
<div class="card-tldr">提出 EquiSELD，用 O(3) 等变注意力网络处理一阶 Ambisonics，实现高效训练的声音事件定位与检测。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="fast-time-varying-exponentiated-convolution-methods-for-gene-2609-24809/">Fast Time-Varying Exponentiated Convolution Methods for Generative Direction Dependent Reverberation</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#房间冲激响应生成</span>
</div>
<div class="card-tldr">提出时变指数卷积方法，将高斯噪声与冲激响应变换为混响场，并扩展到球谐域生成方向相关RIR。</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="litecass-a-lightweight-end-to-end-network-for-real-time-ster-2609-23453/">LiteCASS: A Lightweight End-to-End Network for Real-Time Stereo Cinematic Audio Source Separation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">LiteCASS 用两个紧凑 U-Net 加 STFT 子带重排，实现 1.06M 参数、0.72G MACs/s 的实时立体声电影音源分离。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Bearings: Self-Supervised Soundfield Embeddings from First-O…](bearings-self-supervised-soundfield-embeddings-from-first-or-2609-23152/) 🎯 | **8.8** | #双耳音频 |
| 🥈 | [Generative Learning for Ambisonic Upscaling](generative-learning-for-ambisonic-upscaling-2609-23479/) 🎯 | **8.8** | #双耳音频 |
| 🥉 | [OmniEcho: Spatial Audio Understanding for Embodied Agents](omniecho-spatial-audio-understanding-for-embodied-agents-2609-23407/) 🎯 | **8.5** | #双耳音频 |
| 4. | [LiteCASS: A Lightweight End-to-End Network for Real-Time Ste…](litecass-a-lightweight-end-to-end-network-for-real-time-ster-2609-23453/) 🎯 | **8.2** | #语音分离 |
| 5. | [EquiSELD: Efficient training of equivariant sound event loca…](equiseld-efficient-training-of-equivariant-sound-event-local-2609-23156/) 🎯 | **8.0** | #声源定位与检测 |
| 6. | [Adaptive Depth and Expert Refinement for Efficient Speech En…](adaptive-depth-and-expert-refinement-for-efficient-speech-en-2609-22824/) 🎯 | **8.0** | #语音增强 |
| 7. | [CycleSpeech: Reciprocal Alignment for Instruction-Controlled…](cyclespeech-reciprocal-alignment-for-instruction-controlled--2609-24771/) | **7.2** | #语音合成 |
| 8. | [Fast Time-Varying Exponentiated Convolution Methods for Gene…](fast-time-varying-exponentiated-convolution-methods-for-gene-2609-24809/) 🎯 | **7.0** | #房间冲激响应生成 |
| 9. | [COT-TTS: Audio Context-Aware Text-to-Speech with Chain-of-Th…](cot-tts-audio-context-aware-text-to-speech-with-chain-of-tho-2609-22697/) | **7.0** | #语音合成 |
| 10. | [MoSAT: Human Motion Generation from Spatial Audio and Textua…](mosat-human-motion-generation-from-spatial-audio-and-textual-2609-23797/) | **6.0** | #音频生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="bearings-self-supervised-soundfield-embeddings-from-first-or-2609-23152/">Bearings: Self-Supervised Soundfield Embeddings from First-Order Ambisonics</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用一阶Ambisonics自监督预训练掩码自编码器，学得可复用的声场嵌入，与冻结单通道声学编码器拼接即可实现声事件定位与检测。</div>
<div class="card-action">
<a href="bearings-self-supervised-soundfield-embeddings-from-first-or-2609-23152/">详情 →</a> · <a href="https://arxiv.org/abs/2609.23152" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="generative-learning-for-ambisonic-upscaling-2609-23479/">Generative Learning for Ambisonic Upscaling</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将 Ambisonics 升阶视为生成任务，用 Score-based 与 Flow Matching 从低阶估计高阶分量，混响下优于判别式基线。</div>
<div class="card-action">
<a href="generative-learning-for-ambisonic-upscaling-2609-23479/">详情 →</a> · <a href="https://arxiv.org/abs/2609.23479" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="omniecho-spatial-audio-understanding-for-embodied-agents-2609-23407/">OmniEcho: Spatial Audio Understanding for Embodied Agents</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 OmniEchoBench 空间视听基准与 OmniEcho 全模态模型，用 FOA 空间编码器实现声源定位与声引导导航。</div>
<div class="card-action">
<a href="omniecho-spatial-audio-understanding-for-embodied-agents-2609-23407/">详情 →</a> · <a href="https://arxiv.org/abs/2609.23407" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="litecass-a-lightweight-end-to-end-network-for-real-time-ster-2609-23453/">LiteCASS: A Lightweight End-to-End Network for Real-Time Stereo Cinematic Audio Source Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">LiteCASS 用两个紧凑 U-Net 加 STFT 子带重排，实现 1.06M 参数、0.72G MACs/s 的实时立体声电影音源分离。</div>
<div class="card-action">
<a href="litecass-a-lightweight-end-to-end-network-for-real-time-ster-2609-23453/">详情 →</a> · <a href="https://arxiv.org/abs/2609.23453" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="equiseld-efficient-training-of-equivariant-sound-event-local-2609-23156/">EquiSELD: Efficient training of equivariant sound event localization and detection networks</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#声源定位与检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 EquiSELD，用 O(3) 等变注意力网络处理一阶 Ambisonics，实现高效训练的声音事件定位与检测。</div>
<div class="card-action">
<a href="equiseld-efficient-training-of-equivariant-sound-event-local-2609-23156/">详情 →</a> · <a href="https://arxiv.org/abs/2609.23156" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="adaptive-depth-and-expert-refinement-for-efficient-speech-en-2609-22824/">Adaptive Depth and Expert Refinement for Efficient Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 ADER，用自适应深度控制器与条件专家路由实现输入相关的渐进式语音增强，在 VCTK-DEMAND 上大幅削减参数量与计算量。</div>
<div class="card-action">
<a href="adaptive-depth-and-expert-refinement-for-efficient-speech-en-2609-22824/">详情 →</a> · <a href="https://arxiv.org/abs/2609.22824" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="cyclespeech-reciprocal-alignment-for-instruction-controlled--2609-24771/">CycleSpeech: Reciprocal Alignment for Instruction-Controlled Speech Synthesis and Paralinguistic Understanding</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用结构化声音画像连接指令控制语音合成与副语言理解，通过双向循环反馈与CycleGRPO强化学习实现互惠训练。</div>
<div class="card-action">
<a href="cyclespeech-reciprocal-alignment-for-instruction-controlled--2609-24771/">详情 →</a> · <a href="https://arxiv.org/abs/2609.24771" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="fast-time-varying-exponentiated-convolution-methods-for-gene-2609-24809/">Fast Time-Varying Exponentiated Convolution Methods for Generative Direction Dependent Reverberation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#房间冲激响应生成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出时变指数卷积方法，将高斯噪声与冲激响应变换为混响场，并扩展到球谐域生成方向相关RIR。</div>
<div class="card-action">
<a href="fast-time-varying-exponentiated-convolution-methods-for-gene-2609-24809/">详情 →</a> · <a href="https://arxiv.org/abs/2609.24809" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="cot-tts-audio-context-aware-text-to-speech-with-chain-of-tho-2609-22697/">COT-TTS: Audio Context-Aware Text-to-Speech with Chain-of-Thought Reasoning</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出上下文感知推理式TTS任务，用历史对话音频推断说话风格，构建900万样本双语数据集与800条基准，开源0.6B/1.7B自回归模型。</div>
<div class="card-action">
<a href="cot-tts-audio-context-aware-text-to-speech-with-chain-of-tho-2609-22697/">详情 →</a> · <a href="https://arxiv.org/abs/2609.22697" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="mosat-human-motion-generation-from-spatial-audio-and-textual-2609-23797/">MoSAT: Human Motion Generation from Spatial Audio and Textual Description</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出STAM数据集与MoSAT框架，用潜空间流匹配联合空间音频与文本生成全身人体动作。</div>
<div class="card-action">
<a href="mosat-human-motion-generation-from-spatial-audio-and-textual-2609-23797/">详情 →</a> · <a href="https://arxiv.org/abs/2609.23797" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
