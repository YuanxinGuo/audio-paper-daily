---
title: "Hear, Localize, and Reason: Spatially Aware Scene Understanding for Audio-Visual LLMs"
date: 2026-10-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出 HLR-AVSceneQA 基准与 HLR-LLM，用双耳空间分支加单耳语义分支，让 AV-LLM 能听、定位并推理声源与视觉场景关系。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span> <span class="tag-pill tag-pill-soft">#空间音频理解</span> <span class="tag-pill tag-pill-soft">#视听场景理解</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.21588</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.21588" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.21588" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 HLR-AVSceneQA 基准与 HLR-LLM，用双耳空间分支加单耳语义分支，让 AV-LLM 能听、定位并推理声源与视觉场景关系。
</div>

## 👥 作者与机构

**Kim Sung-Bin** ¹ · Lee Jung-Mok · Jinwoo Jung · Oh Hyun-Bin · Hyeonggon Ryu · David Harwath · Tae-Hyun Oh

**机构**：韩国科学技术院 · 得克萨斯大学奥斯汀分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态大模型、空间音频理解与视听推理的研究者。建议通读：先看 §3 的 HLR-AVSceneQA 层级设计与评测协议，再看 §4 双耳分支与课程式 CoT 训练细节，最后看表 2/表 3 的定位与关系推理对比。若只关心基准，可只读基准构建与失败案例分析。

## 🌍 研究背景

现有 AV-LLM（如 Video-LLaMA、Qwen-Audio 系）多把音频当作单耳语义内容，无法回答声源在哪、与画面如何关联。近期空间视听工作只覆盖空间对应或方向距离推理等单一能力，缺少统一评测。本文要解决的是：如何系统评测并提升 AV-LLM 的听—定位—推理层级能力。

## 💡 核心创新

1. 提出 HLR-AVSceneQA 基准，按听—定位—推理三层级评测
2. HLR-LLM 在单耳语义通路外并联双耳空间音频分支
3. 课程式训练并加入末阶段 chain-of-thought 监督多步空间推理

## 🏗️ 模型架构

输入为视频帧与双耳音频。视觉侧沿用强视听基础模型的视觉编码器；音频侧分两路：单耳语义通路提取语义表征，双耳空间分支提取 ILD/ITD 等空间线索，两路特征与视觉 token 对齐后送入 LLM 解码器。训练采用课程学习，末阶段用 chain-of-thought 监督多步空间推理，输出为文本答案。摘要未给参数量。

## 📚 数据集

- HLR-AVSceneQA（提出并用于训练与评估，含听/定位/推理三层级）

## 📊 实验结果

摘要仅给出定性结论：现有 AV-LLM 在空间定位与关系推理上仍受限，HLR-LLM 在不损害语义视听感知的前提下显著提升空间视听场景理解。未提供 SI-SDR、准确率等具体数值，也无消融与效率指标，需查阅正文表格确认。

## 🎯 结论与影响

最强结论是：并联双耳空间分支加课程式 CoT 能让 AV-LLM 同时具备语义理解与空间定位推理能力。这为空间音频理解提供了可复用的基准与建模范式，后续工作可在此基础上扩展更多空间任务。工业上对 AR/VR、机器人听觉与智能助手的环境感知有参考价值。

## ⚠️ 局限与未解决问题

摘要未给任何定量结果与消融，双耳分支相对单耳通路的增益幅度不明；基准规模、数据来源与是否含真实双耳录音未说明；未报推理延迟与参数量，也未与专门空间音频模型做充分对比。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-16/">← 返回 2026-10-16 速递</a></div>
