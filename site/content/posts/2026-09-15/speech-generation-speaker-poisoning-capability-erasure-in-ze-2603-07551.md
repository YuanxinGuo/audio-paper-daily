---
title: "Speech Generation Speaker Poisoning: Capability Erasure in Zero-Shot Text-to-Speech"
date: 2026-09-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出零样本TTS的说话人投毒任务SGSP，用推理过滤与参数修改抑制目标说话人，并给出AUC与FSSIM评估协议。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#说话人隐私</span> <span class="tag-pill tag-pill-soft">#机器遗忘</span> <span class="tag-pill tag-pill-soft">#零样本TTS</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.07551</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.07551" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.07551" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出零样本TTS的说话人投毒任务SGSP，用推理过滤与参数修改抑制目标说话人，并给出AUC与FSSIM评估协议。
</div>

## 👥 作者与机构

**Thanathai Lertpetchpun** ¹ · Thanapat Trachu · Sai Praneeth Karimireddy · Shrikanth Narayanan

**机构**：南加州大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做TTS安全、隐私与机器遗忘的研究者阅读。建议通读，重点看任务定义、FSSIM指标推导与1/15/100说话人实验对比表；若只关心方法，可先看参数修改一节与消融。

## 🌍 研究背景

零样本TTS（如StyleTTS2）能从数秒音频克隆未见说话人，带来身份滥用风险。传统机器遗忘假设移除训练样本即可，但零样本TTS通过学到的说话人表征与强泛化仍能重建身份，移除样本无效。本文要解决：在保持其他说话人合成质量的前提下，定向抑制特定说话人身份，并量化效用-隐私权衡。

## 💡 核心创新

1. 形式化SGSP任务：定向抑制说话人身份
2. 提出FSSIM与AUC评估框架量化泄漏
3. 系统对比推理过滤与参数修改两类方法
4. 揭示训练内说话人比未见说话人更难抑制

## 🏗️ 模型架构

以StyleTTS2为零样本TTS测试平台。输入为文本与参考说话人音频，经文本编码器、风格/说话人编码器与扩散声码器生成波形。投毒在两条路径实施：推理时对说话人embedding做过滤或替换；参数修改则对说话人相关模块做微调/编辑以擦除目标身份。评估用生成音频与目标说话人的相似度计算FSSIM，并做AUC分析。摘要未给参数量。

## 📚 数据集

- StyleTTS2训练所用说话人数据（训练/投毒对象）
- 未见说话人评估集（评估泛化抑制）

## 📊 实验结果

摘要未给出具体数值指标，仅报告定性结论：在1、15、100个遗忘说话人设置下，最多15个遗忘说话人可被有效抑制；训练中见过的说话人比未见说话人更难抑制；多说话人规模下最坏情况身份泄漏（Max-FSSIM）仍未解决。

## 🎯 结论与影响

最强结论是：零样本TTS的说话人身份可被定向投毒抑制，但多说话人规模下最坏情况泄漏仍是开放难题。该工作为TTS隐私与机器遗忘提供任务定义与评估协议，对工业界防止声音克隆滥用有参考价值。

## ⚠️ 局限与未解决问题

仅以StyleTTS2为测试平台，未验证其他TTS架构；摘要未报推理延迟与计算开销；100说话人规模下Max-FSSIM未解决；缺少与更多遗忘基线的全面对比与充分消融。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-15/">← 返回 2026-09-15 速递</a></div>
