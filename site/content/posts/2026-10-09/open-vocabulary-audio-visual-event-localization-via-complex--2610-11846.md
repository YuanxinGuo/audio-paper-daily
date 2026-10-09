---
title: "Open-Vocabulary Audio-Visual Event Localization via Complex-Valued Fusion"
date: 2026-10-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频-视觉事件定位"]
summary: "用复值神经网络融合音视频相似度，在开放词汇音视频事件定位任务上取得SOTA。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频-视觉事件定位</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#复值神经网络</span> <span class="tag-pill tag-pill-soft">#开放词汇</span> <span class="tag-pill tag-pill-soft">#音频-视觉</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.11846</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.11846" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.11846" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用复值神经网络融合音视频相似度，在开放词汇音视频事件定位任务上取得SOTA。
</div>

## 👥 作者与机构

**Anirudh Praveen** ¹ · Koteswar Rao Jerripothula · Pratik Joshi · Aveen Dayal · Neela Sawant

**机构**：印度理工学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态融合与开放词汇识别方向的研究者阅读。建议重点看§3的复值融合模块设计与§4.2的消融实验，特别是虚部伴随流的构造方式。若关注音视频事件定位，值得通读；若仅关注语音增强/分离，可略读。

## 🌍 研究背景

开放词汇音视频事件定位（OV-AVEL）要求模型对训练中未见过的事件类别进行定位与分类。现有主流方法使用冻结的多模态基础模型（如ImageBind）将视觉帧、音频梅尔谱和类名嵌入共享空间，再分别计算视觉-文本和音频-文本的余弦相似度，最后用固定规则（几何平均或加权平均）将两个相似度合并为单一标量后取argmax。这种固定融合规则无法自适应地学习模态间交互，限制了开放词汇场景下的泛化能力。本文旨在用可学习的复值融合替代固定规则。

## 💡 核心创新

1. 用复值神经网络学习音视频相似度的融合，替代固定几何平均规则
2. 视觉模态用iHSV虚部作为伴随流，音频用CycleGAN翻译的相位谱作为伴随流
3. 四流复值架构，仅训练时序注意力块和融合CVNN，编码器冻结
4. 提出两流替代方案，同样优于基线

## 🏗️ 模型架构

输入为视频帧、音频梅尔谱和候选类名，分别经冻结的ImageBind编码器提取嵌入。视觉模态额外提取iHSV虚部作为伴随流，音频模态用CycleGAN将幅度谱翻译为相位谱作为伴随流。每个模态的实部与虚部构成复数表示，分别与文本嵌入计算复值余弦相似度，得到两个复值相似度。随后通过复值神经网络（CVNN）进行融合，融合前经过时序注意力块。仅时序注意力块和融合CVNN可训练，编码器保持冻结。输出为每个视频段对每个类别的最终得分，取argmax得到事件类别。

## 📚 数据集

- OV-AVEBench（评估，开放词汇分割）
- AVE（评估，修改后用于OV-AVEL任务）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Acc | OV-AVEBench (unseen) | fine-tuned baseline 64.9 | **66.5** | +1.6 |
| Seg-F1 | OV-AVEBench (unseen) | fine-tuned baseline 55.0 | **59.1** | +4.1 |
| Event-F1 | OV-AVEBench (unseen) | fine-tuned baseline 47.5 | **54.1** | +6.6 |
| Acc | AVE (modified) | 未报告 | **60.7** | SOTA |
| Seg-F1 | AVE (modified) | 未报告 | **51.9** | SOTA |
| Event-F1 | AVE (modified) | 未报告 | **50.4** | SOTA |

在OV-AVEBench的开放（未见类）划分上，本文方法在Acc/Seg-F1/Event-F1上分别达到66.5/59.1/54.1%，相比之前报告的微调基线提升+1.6/+4.1/+6.6。在可见类上也有持续增益。在修改后的AVE数据集上达到60.7/51.9/50.4%，同样取得SOTA。摘要未提供消融实验细节和效率指标。

## 🎯 结论与影响

本文提出的四流复值架构在OV-AVEL任务上刷新了两个基准的SOTA，验证了可学习复值融合优于固定融合规则。该思路可能启发后续多模态融合研究，尤其是利用复数表示建模模态间相位关系。工业上可用于视频内容理解与事件检索，但需注意计算开销。

## ⚠️ 局限与未解决问题

摘要未提供消融实验验证各组件贡献，未报告推理延迟和参数量，未与更多融合策略（如注意力融合）对比。CycleGAN翻译相位谱可能引入伪影，且依赖ImageBind冻结编码器，泛化性受限于基础模型。

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-10-09/">← 返回 2026-10-09 速递</a></div>
