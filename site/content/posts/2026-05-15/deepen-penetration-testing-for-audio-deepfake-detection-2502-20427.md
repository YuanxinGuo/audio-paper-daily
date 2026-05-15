---
title: "DeePen: Penetration Testing for Audio Deepfake Detection"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#信号处理", "#对抗攻击", "#渗透测试", "#音频深度伪造检测", "#鲁棒性评估"]
summary: "提出DeePen，一种无需先验知识的黑盒渗透测试方法，通过信号处理攻击评估音频深度伪造检测系统的鲁棒性，发现所有测试系统均存在弱点。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对抗攻击</span> <span class="tag-pill tag-pill-soft">#鲁棒性评估</span> <span class="tag-pill tag-pill-soft">#信号处理</span> <span class="tag-pill tag-pill-soft">#渗透测试</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2502.20427</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2502.20427" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2502.20427" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DeePen，一种无需先验知识的黑盒渗透测试方法，通过信号处理攻击评估音频深度伪造检测系统的鲁棒性，发现所有测试系统均存在弱点。
</div>

## 👥 作者与机构

Nicolas M\"uller · Piotr Kawa · Adriana Stan · Thien-Phuc Doan · Souhwan Jung · Wei Herng Choong · Philip Sperl · Konstantin B\"ottinger

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、深度伪造检测领域的研究者。建议重点阅读§3攻击设计及§4实验结果，了解攻击效果与重训练缓解策略。可先看表1攻击列表，再结合图2评估结果。

## 🌍 研究背景

音频深度伪造（deepfake）对个人和社会构成安全威胁，现有检测系统多基于机器学习分类器。然而，这些系统在面对对抗性攻击时的鲁棒性尚未被充分评估。传统攻击方法常需白盒访问或大量先验知识，实际场景中难以实现。本文提出一种黑盒渗透测试方法DeePen，利用信号处理操作（如时间拉伸、回声添加）作为攻击，无需了解目标模型内部结构，旨在系统性地揭示检测系统的脆弱性。

## 💡 核心创新

1. 提出黑盒渗透测试框架DeePen，无需目标模型先验知识
2. 使用信号处理操作（时间拉伸、回声等）作为攻击手段
3. 系统评估多个真实生产系统与学术模型，发现普遍脆弱性
4. 揭示部分攻击可通过重训练缓解，但某些攻击持久有效

## 🏗️ 模型架构

DeePen是一个黑盒攻击框架，输入为原始音频样本，通过一系列信号处理模块（包括时间拉伸、回声添加、重采样、噪声注入等）生成对抗样本。这些攻击无需梯度信息或模型访问权限。攻击后的音频被送入目标深度伪造检测模型（包括商业API和学术模型），输出真/假判定。框架不修改检测模型本身，仅评估其鲁棒性。

## 📚 数据集

- 未见明确数据集名称，摘要仅提及使用真实生产系统和学术模型检查点进行评估

## 📊 实验结果

摘要未提供具体数值指标，但指出所有测试系统（包括真实生产系统和学术模型）均能被简单信号处理攻击可靠欺骗，如时间拉伸和回声添加。部分攻击可通过重训练缓解，但某些攻击持续有效。

## 🎯 结论与影响

DeePen证明了当前音频深度伪造检测系统在面对简单信号处理攻击时的脆弱性，强调需要更鲁棒的检测方法。该工作为音频安全领域提供了系统性的评估工具，推动检测模型向更安全方向发展。对工业界而言，部署前应进行类似渗透测试以增强防御。

## ⚠️ 局限与未解决问题

摘要未提及攻击的感知质量（是否被人类察觉）、计算开销，以及是否考虑自适应攻击。作为审稿人，注意到缺乏对攻击后音频的客观质量评估（如PESQ），且未与现有对抗攻击方法（如FGSM、PGD）对比。数据集和具体指标缺失，削弱了结果的可量化性。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
