---
title: "Backdoor Attacks on Speech Emotion Recognition via TTS-Generated Poisoning"
date: 2026-09-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音情感识别"]
summary: "首次系统研究语音情感识别中的投毒后门攻击，利用TTS生成音频嵌入低能量声学触发器，实现高成功率且隐蔽的攻击。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#后门攻击</span> <span class="tag-pill tag-pill-soft">#语音情感识别</span> <span class="tag-pill tag-pill-soft">#文本到语音合成</span> <span class="tag-pill tag-pill-soft">#自监督表征</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.21052</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.21052" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.21052" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首次系统研究语音情感识别中的投毒后门攻击，利用TTS生成音频嵌入低能量声学触发器，实现高成功率且隐蔽的攻击。
</div>

## 👥 作者与机构

**Yongbin Huang** ¹ · Xihao Xie · Jia Zhang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音安全、情感识别及自监督学习研究者。建议重点阅读方法部分（触发器设计）和实验部分（攻击成功率与迁移性）。可先看摘要与结论，再深入方法细节。

## 🌍 研究背景

语音情感识别（SER）系统越来越多地采用自监督声学表征，但其对训练时攻击的脆弱性尚未充分探索。现有研究多关注语音增强或说话人识别中的后门攻击，而SER领域缺乏系统研究。本文首次针对SER提出投毒后门攻击，利用TTS生成音频实现可扩展且一致的投毒，揭示现代SER管线的严重安全漏洞。

## 💡 核心创新

1. 首次系统研究SER投毒后门攻击
2. 设计低能量声学触发器，隐蔽嵌入自然与合成语音
3. 利用TTS生成音频实现可扩展投毒
4. 验证跨模型迁移性与自监督表征的脆弱性

## 🏗️ 模型架构

攻击方法：在训练阶段，将低能量声学触发器嵌入部分训练样本（包括TTS生成的合成语音），并标记为目标情感标签。模型采用自监督声学表征（如wav2vec2）微调用于SER。触发器设计为短时、低幅度，确保不可感知。投毒样本与干净样本混合训练，使模型学习触发器与目标标签的关联。

## 📚 数据集

- IEMOCAP（训练与评估，包含自然语音）
- TTS生成语音（训练，用于投毒）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 攻击成功率（ASR） | IEMOCAP | 无 | **高（具体数值未给出）** | — |
| 良性输入准确率 | IEMOCAP | 无 | **接近干净模型** | — |

实验表明，在低投毒比例下，SER模型可被可靠攻击，攻击成功率较高，且良性输入性能几乎不受影响。后门模式表现出强跨模型迁移性，自监督表征尤其容易学习这些触发器。摘要未提供具体数值，但强调攻击的有效性与隐蔽性。

## 🎯 结论与影响

本文首次揭示SER系统对投毒后门攻击的脆弱性，并证明TTS技术显著降低了有效攻击的门槛。这一发现凸显了现代SER管线的关键漏洞，亟需开发专用防御。对后续研究而言，需关注自监督表征的安全训练与触发器检测。工业部署SER时需考虑数据完整性与模型鲁棒性。

## ⚠️ 局限与未解决问题

摘要未提供具体攻击成功率数值，缺乏与现有攻击方法的定量对比。未讨论防御策略或对触发器鲁棒性的分析。实验仅在单一数据集（IEMOCAP）上验证，泛化性未知。未考虑真实场景中TTS语音与自然语音的分布差异。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-09-03/">← 返回 2026-09-03 速递</a></div>
