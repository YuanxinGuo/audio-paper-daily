---
title: "语音/音频论文速递 2026-11-02"
date: 2026-11-02T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 8.2（#语音分离）"
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
| #语音分离 | 1篇 | `█████` |
| #目标说话人提取 | 1篇 | `█████` |
| #声学模拟 | 1篇 | `█████` |
| #语音大语言模型 | 1篇 | `█████` |
| #语音事件检测 | 1篇 | `█████` |
| #房间冲激响应生成 | 1篇 | `█████` |
| #生物声学 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="voxlock-target-speaker-extraction-for-voice-agents-without-a-2610-40727/">VoxLock: Target-Speaker Extraction for Voice Agents Without an Enrollment Step</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">微调REAL-TSE因果模型，用通话内截取的声纹样本做无注册目标说话人提取，以WER为指标在Krisp与AMI上验证。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="voxlock-target-speaker-extraction-for-voice-agents-without-a-2610-40727/">VoxLock: Target-Speaker Extraction for Voice Agents Without an Enrollment Step</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">微调REAL-TSE因果模型，用通话内截取的声纹样本做无注册目标说话人提取，以WER为指标在Krisp与AMI上验证。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="self-supervised-object-centric-representation-for-multi-task-2610-41870/">Self-Supervised Object-Centric Representation for Multi-Task Audio Analysis</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">用 slot attention 自监督重建 AST patch 嵌入，得到目标中心表示，统一支撑分类、检测与分离。</div>
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
| 🥇 | [Self-Supervised Object-Centric Representation for Multi-Task…](self-supervised-object-centric-representation-for-multi-task-2610-41870/) 🎯 | **8.2** | #语音分离 |
| 🥈 | [VoxLock: Target-Speaker Extraction for Voice Agents Without …](voxlock-target-speaker-extraction-for-voice-agents-without-a-2610-40727/) 🎯 | **8.2** | #目标说话人提取 |
| 🥉 | [MFlowAudio: Efficient Text-to-Audio Synthesis via Mamba-base…](mflowaudio-efficient-text-to-audio-synthesis-via-mamba-based-2610-41852/) | **7.8** | #音频生成 |
| 4. | [Self-Localization of Distributed Microphone Arrays Using One…](self-localization-of-distributed-microphone-arrays-using-one-2610-41547/) | **7.2** | #声学模拟 |
| 5. | [Minimizing Modality Gap from the Input Side: Your Speech LLM…](minimizing-modality-gap-from-the-input-side-your-speech-llm--2605-05927/) | **7.0** | #语音大语言模型 |
| 6. | [TamilEOT: A Dataset and Model for Semantic End-of-Turn Detec…](tamileot-a-dataset-and-model-for-semantic-end-of-turn-detect-2609-05631/) | **6.8** | #语音事件检测 |
| 7. | [ARPEGE: Dataset and Methods to Estimate Acoustic and Geometr…](arpege-dataset-and-methods-to-estimate-acoustic-and-geometri-2610-41543/) | **6.8** | #房间冲激响应生成 |
| 8. | [A richness-sensitive Acoustic Biodiversity Index from specie…](a-richness-sensitive-acoustic-biodiversity-index-from-specie-2610-42042/) | **6.0** | #生物声学 |
| 9. | [A General Theoretical Framework for Transformed Geometric Pa…](a-general-theoretical-framework-for-transformed-geometric-pa-2610-42095/) | **4.5** | #音乐信息检索 |
| 10. | [Nedimo: An Evidence-Grounded Multilingual Pipeline for AI-Ge…](nedimo-an-evidence-grounded-multilingual-pipeline-for-ai-gen-2610-40970/) | **4.0** | #音频生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="self-supervised-object-centric-representation-for-multi-task-2610-41870/">Self-Supervised Object-Centric Representation for Multi-Task Audio Analysis</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用 slot attention 自监督重建 AST patch 嵌入，得到目标中心表示，统一支撑分类、检测与分离。</div>
<div class="card-action">
<a href="self-supervised-object-centric-representation-for-multi-task-2610-41870/">详情 →</a> · <a href="https://arxiv.org/abs/2610.41870" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="voxlock-target-speaker-extraction-for-voice-agents-without-a-2610-40727/">VoxLock: Target-Speaker Extraction for Voice Agents Without an Enrollment Step</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">微调REAL-TSE因果模型，用通话内截取的声纹样本做无注册目标说话人提取，以WER为指标在Krisp与AMI上验证。</div>
<div class="card-action">
<a href="voxlock-target-speaker-extraction-for-voice-agents-without-a-2610-40727/">详情 →</a> · <a href="https://arxiv.org/abs/2610.40727" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="mflowaudio-efficient-text-to-audio-synthesis-via-mamba-based-2610-41852/">MFlowAudio: Efficient Text-to-Audio Synthesis via Mamba-based Stateful Flow Matching</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用TCMamba主干结合状态化流匹配，实现线性复杂度、可流式的文本到音频合成。</div>
<div class="card-action">
<a href="mflowaudio-efficient-text-to-audio-synthesis-via-mamba-based-2610-41852/">详情 →</a> · <a href="https://arxiv.org/abs/2610.41852" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="self-localization-of-distributed-microphone-arrays-using-one-2610-41547/">Self-Localization of Distributed Microphone Arrays Using One Source and Acoustic Reflections</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#声学模拟</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">利用单声源RIR的早期反射构建3D镜像源点云，通过ARCTIC三角配准算法估计两个非共面麦克风阵列的相对位姿。</div>
<div class="card-action">
<a href="self-localization-of-distributed-microphone-arrays-using-one-2610-41547/">详情 →</a> · <a href="https://arxiv.org/abs/2610.41547" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="minimizing-modality-gap-from-the-input-side-your-speech-llm--2605-05927/">Minimizing Modality Gap from the Input Side: Your Speech LLM Can Be a Prosody-Aware Text LLM</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音大语言模型</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 TextPro-SLM，用 WhisperPro 编码器同步输出文本 token 与韵律嵌入，从输入端缩小语音-文本模态鸿沟。</div>
<div class="card-action">
<a href="minimizing-modality-gap-from-the-input-side-your-speech-llm--2605-05927/">详情 →</a> · <a href="https://arxiv.org/abs/2605.05927" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="tamileot-a-dataset-and-model-for-semantic-end-of-turn-detect-2609-05631/">TamilEOT: A Dataset and Model for Semantic End-of-Turn Detection in Tamil Telephone Speech</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音事件检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">发布首个泰米尔语电话语音语义轮次结束检测数据集与两个轻量检测器，并公开负类标注失败经验。</div>
<div class="card-action">
<a href="tamileot-a-dataset-and-model-for-semantic-end-of-turn-detect-2609-05631/">详情 →</a> · <a href="https://arxiv.org/abs/2609.05631" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="arpege-dataset-and-methods-to-estimate-acoustic-and-geometri-2610-41543/">ARPEGE: Dataset and Methods to Estimate Acoustic and Geometric Parameters of Rooms from Sound</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#房间冲激响应生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">发布ARPEGE数据集：6个空房间、数百条Ambisonic球阵RIR，标注声源/麦克风/反射面几何，并演示镜像源定位与盲房间参数估计两个基线。</div>
<div class="card-action">
<a href="arpege-dataset-and-methods-to-estimate-acoustic-and-geometri-2610-41543/">详情 →</a> · <a href="https://arxiv.org/abs/2610.41543" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="a-richness-sensitive-acoustic-biodiversity-index-from-specie-2610-42042/">A richness-sensitive Acoustic Biodiversity Index from species-level detections: classifier benchmarking, false-positive control and validation against standard soundscape indices in an African savanna and an urban zoo</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出基于物种级检测的声学生物多样性指数 ABI_E，用 BirdNET 检测加假阳性过滤，在非洲草原与城市动物园验证其与物种丰富度强相关。</div>
<div class="card-action">
<a href="a-richness-sensitive-acoustic-biodiversity-index-from-specie-2610-42042/">详情 →</a> · <a href="https://arxiv.org/abs/2610.42042" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="a-general-theoretical-framework-for-transformed-geometric-pa-2610-42095/">A General Theoretical Framework for Transformed Geometric Pattern Matching in Music</a>
<div class="card-meta">
<span class="card-score">4.5</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">提出以变换类为核心的几何模式匹配理论框架，形式化定义匹配、出现、极大匹配等概念并证明相关性质。</div>
<div class="card-action">
<a href="a-general-theoretical-framework-for-transformed-geometric-pa-2610-42095/">详情 →</a> · <a href="https://arxiv.org/abs/2610.42095" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="nedimo-an-evidence-grounded-multilingual-pipeline-for-ai-gen-2610-40970/">Nedimo: An Evidence-Grounded Multilingual Pipeline for AI-Generated Sleep Stories</a>
<div class="card-meta">
<span class="card-score">4.0</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">提出 Nedimo 多语言助眠故事生成流水线，将 LLM 脚本生成与 TTS 合成解耦，并加入响度与结构护栏。</div>
<div class="card-action">
<a href="nedimo-an-evidence-grounded-multilingual-pipeline-for-ai-gen-2610-40970/">详情 →</a> · <a href="https://arxiv.org/abs/2610.40970" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
