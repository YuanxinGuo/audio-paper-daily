---
title: "PROCESS-2: A Benchmark Speech Corpus for Early Cognitive Impairment Detection"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分析"]
summary: "发布一个大规模、临床验证的语音数据集PROCESS-2，用于早期认知障碍检测，包含200健康、150轻度认知障碍、50痴呆患者录音。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#认知障碍检测</span> <span class="tag-pill tag-pill-soft">#语音数据集</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#临床语音分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.14888</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.14888" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.14888" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布一个大规模、临床验证的语音数据集PROCESS-2，用于早期认知障碍检测，包含200健康、150轻度认知障碍、50痴呆患者录音。
</div>

## 👥 作者与机构

**Madhurananda Pahar** ¹ · Caitlin H. Illingworth · Bahman Mirheidari · Hend Elghazaly · Fritz Peters · Sophie Young · Wing-Zin Leung · Labhpreet Kaur · … 等 2 人

**机构**：谢菲尔德大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音生物标志物、临床语音分析的研究者。建议重点阅读§3数据集描述和§4技术验证部分，了解数据划分和基线模型性能。若需复现，可先下载HuggingFace数据集。

## 🌍 研究背景

基于语音的认知衰退检测具有非侵入性、可扩展的优势，但缺乏大规模、临床验证的真实场景数据集。现有数据集规模小、任务单一，且未充分控制录音条件。本文旨在构建一个包含多种认知状态、任务导向语音的大规模基准数据集，以推动该领域标准化评估。

## 💡 核心创新

1. 构建200+150+50三组临床诊断的大规模语音数据集
2. 包含图片描述和言语流畅性两种任务
3. 提供人工校验转录和参与者级元数据
4. 预设训练/测试划分，确保可复现基准
5. 通过嵌入空间分析和基线建模验证临床区分性

## 🏗️ 模型架构

数据集构建流程：通过CognoMemory数字评估平台采集，每位参与者完成一次评估会话，包括图片描述和言语流畅性任务。录音后经人工校验转录，并整理参与者级元数据（年龄、性别、诊断等）。数据集共约21小时语音，预设训练/测试划分。技术验证包括人口统计平衡、临床一致性、录音稳定性、嵌入空间结构分析和可复现基线建模。

## 📚 数据集

- PROCESS-2（训练/测试，200健康+150MCI+50痴呆，约21小时）

## 📊 实验结果

摘要未提供具体数值指标，但技术验证表明数据集在人口统计平衡、临床一致性、录音稳定性方面表现良好，嵌入空间分析显示临床组间有意义的分离，基线建模性能稳定，保留了真实对话变异性。

## 🎯 结论与影响

PROCESS-2数据集为基于语音的认知障碍检测提供了大规模、临床验证的基准资源，有望推动该领域标准化评估和模型比较。其受控访问机制平衡了数据重用与隐私保护，对临床语音分析研究具有重要支撑作用。

## ⚠️ 局限与未解决问题

数据集仅包含单一评估会话，缺乏纵向数据；诊断基于临床标准而非生物标志物；录音环境虽真实但未完全标准化；未报告不同模型的具体性能指标，基线建模细节有限。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
