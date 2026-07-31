---
title: "SKY-Piano: A Multimodal Piano Performance Dataset"
date: 2026-07-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐信息检索"]
summary: "SKY-Piano 是一个包含11小时多模态钢琴演奏数据的数据集，涵盖运动、多视角视频、音频、MIDI和乐谱，并提供了指法标注工具和MIDI到动作生成的用例。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐信息检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态数据集</span> <span class="tag-pill tag-pill-soft">#钢琴演奏</span> <span class="tag-pill tag-pill-soft">#运动捕捉</span> <span class="tag-pill tag-pill-soft">#MIDI到动作生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.27296</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.27296" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.27296" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>SKY-Piano 是一个包含11小时多模态钢琴演奏数据的数据集，涵盖运动、多视角视频、音频、MIDI和乐谱，并提供了指法标注工具和MIDI到动作生成的用例。
</div>

## 👥 作者与机构

**Joonhyung Bae** ¹ · Dawon Park · Taegyun Kwon · Yoon-Seok Choi · Hyeon Hur · Satoshi Obata · Shigeru Kai · Yohei Wada · … 等 5 人

**机构**：韩国科学技术院 · NAVER · 雅马哈

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、多模态学习、动作生成方向的研究者。建议重点阅读数据集构建部分（§2）和指法标注模型（§4），以及MIDI到动作生成的实验（§5）。可先浏览数据集的交互式网页以了解模态对齐情况。

## 🌍 研究背景

钢琴演奏研究日益需要多模态数据，如运动、视频、音频和MIDI，以支持表现力分析、演奏辅助和生成任务。现有数据集如MAESTRO主要提供音频和MIDI，缺乏精细的运动和视频信息。SKY-Piano旨在填补这一空白，提供同步的多模态数据，包括专业和业余演奏者，并包含指法标注，以支持更丰富的音乐信息检索研究。

## 💡 核心创新

1. 提供11小时多模态数据，含运动、多视角视频、音频、MIDI和乐谱
2. 包含专业和业余演奏者，覆盖不同技能水平
3. 提供指法标注模型和工具，从MIDI和运动数据生成伪指法标注
4. 提供交互式网页浏览器，便于数据浏览
5. 展示MIDI到动作生成的微调实验作为数据集应用案例

## 🏗️ 模型架构

数据集包含运动捕捉（手部和身体）、多视角视频、音频、MIDI和MusicXML乐谱，所有模态时间同步。运动数据提供标记和插补两种形式，并附带Visual3D身体段运动学。指法标注模型利用MIDI和运动数据生成指法，可能采用序列标注或图神经网络。MIDI到动作生成实验基于预训练模型进行微调，具体架构未在摘要中详述。

## 📚 数据集

- SKY-Piano（训练/评估，11小时，19位演奏者，7专业12业余）

## 📊 实验结果

摘要未提供具体量化结果，但展示了MIDI到动作生成的微调实验作为用例，表明数据集可用于生成任务。数据集规模和模态多样性是其主要贡献，但缺乏与现有数据集的对比或下游任务性能指标。

## 🎯 结论与影响

SKY-Piano为钢琴演奏研究提供了丰富的多模态数据，有望推动表现力分析、演奏辅助和生成任务的发展。其指法标注工具和交互式浏览器增强了可用性。对工业界，可用于音乐教育、虚拟演奏等应用。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可推测：数据规模有限（11小时），演奏者数量较少，可能影响泛化性；指法标注为伪标注，准确性待验证；未提供与现有数据集的对比实验，难以评估其独特价值。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-31/">← 返回 2026-07-31 速递</a></div>
