---
title: "DeePen: Penetration Testing for Audio Deepfake Detection"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#信号处理攻击", "#深度伪造检测", "#渗透测试", "#音频深度伪造检测", "#鲁棒性评估"]
summary: "提出DeePen，一种无需先验知识的音频深度伪造检测系统渗透测试方法，通过信号处理攻击揭示现有系统的脆弱性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#深度伪造检测</span> <span class="tag-pill tag-pill-soft">#鲁棒性评估</span> <span class="tag-pill tag-pill-soft">#渗透测试</span> <span class="tag-pill tag-pill-soft">#信号处理攻击</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2502.20427</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2502.20427" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2502.20427" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DeePen，一种无需先验知识的音频深度伪造检测系统渗透测试方法，通过信号处理攻击揭示现有系统的脆弱性。
</div>

## 👥 作者与机构

Nicolas M\"uller · Piotr Kawa · Adriana Stan · Thien-Phuc Doan · Souhwan Jung · Wei Herng Choong · Philip Sperl · Konstantin B\"ottinger

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、深度伪造检测领域的研究者。建议重点阅读§3攻击方法设计和§4实验结果，了解不同攻击的有效性及重训练缓解效果。可先看表1攻击列表和表2实验结果。

## 🌍 研究背景

音频深度伪造（deepfake）对个人、组织和社会构成严重安全威胁。现有检测系统多基于机器学习分类器，但其鲁棒性未经系统评估。此前缺乏一种无需目标模型先验知识的标准化渗透测试方法。本文旨在通过精心选择的信号处理修改（如时间拉伸、回声添加）作为攻击，系统评估真实生产系统和公开学术模型的脆弱性。

## 💡 核心创新

1. 提出DeePen渗透测试框架，无需目标模型先验知识
2. 系统评估多种信号处理攻击（时间拉伸、回声添加等）
3. 发现重训练可缓解部分攻击，但某些攻击持续有效

## 🏗️ 模型架构

DeePen是一个渗透测试框架，而非检测模型。其核心是攻击生成模块：输入原始音频，应用一系列信号处理修改（如时间拉伸、回声添加、重采样、噪声注入等），生成对抗样本。这些攻击无需梯度信息，仅依赖信号处理操作。测试时，将原始和攻击后音频输入目标检测模型，比较预测结果以评估鲁棒性。

## 📚 数据集

- 未见明确数据集，攻击测试在真实生产系统和学术模型上进行

## 📊 实验结果

摘要未提供具体数值结果，但指出所有测试系统均存在弱点，可被简单操作如时间拉伸或回声添加可靠欺骗。部分攻击可通过重训练缓解，但其他攻击持续有效。

## 🎯 结论与影响

DeePen揭示了当前音频深度伪造检测系统在简单信号处理攻击下的脆弱性，强调鲁棒性评估的重要性。该工作为标准化渗透测试提供了框架，可能推动检测系统在对抗环境下的改进。对工业界而言，部署前需考虑此类攻击的防御。

## ⚠️ 局限与未解决问题

未报告攻击成功率的具体数值或统计显著性；未涉及更复杂的对抗攻击（如基于梯度的）；未讨论攻击对音频质量的影响（如MOS评分）；测试系统范围有限，可能不覆盖所有最新模型。

## 📋 引用

```bibtex
@article{müller20262502,
  title  = {DeePen: Penetration Testing for Audio Deepfake Detection},
  author = {Nicolas M\"uller and  Piotr Kawa and  Adriana Stan and  Thien-Phuc Doan and  Souhwan Jung and  Wei Herng Choong and  Philip Sperl and  Konstantin B\"ottinger},
  journal = {arXiv preprint arXiv:2502.20427},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
