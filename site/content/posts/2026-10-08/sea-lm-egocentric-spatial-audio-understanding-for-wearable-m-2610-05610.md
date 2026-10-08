---
title: "SEA-LM: Egocentric Spatial Audio Understanding for Wearable Microphone Arrays"
date: 2026-10-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出 SEA-LM，用 FOACODER 编码智能眼镜阵列的一阶 Ambisonics，训练 MLLM 完成定位与空间选择性转录。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.05610</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.05610" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.05610" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 SEA-LM，用 FOACODER 编码智能眼镜阵列的一阶 Ambisonics，训练 MLLM 完成定位与空间选择性转录。
</div>

## 👥 作者与机构

**Sonal Kumar** ¹ · Sinan Hersek · Artem Dementyev · Mengzhen Pan · Ishan Chatterjee · Anurag Kumar · Ramani Duraiswami · Dinesh Manocha · … 等 1 人

**机构**：马里兰大学 · 谷歌

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做空间音频、可穿戴阵列与音频-语言模型的研究者。建议通读，重点看 §3 的 FOACODER 波束成形设计与 Spatio-temporal Weighted Cross-Entropy Loss 的推导，以及实验中的 1,211 种阵列配置鲁棒性分析。若只关心定位，可先看方位/俯仰 MAE 表。

## 🌍 研究背景

单通道大音频-语言模型在语音理解上已较强，但丢弃空间线索，无法定位声源，也难以在重叠说话人场景中解耦。传统空间音频方法依赖固定阵列几何与 DOA 估计，泛化到智能眼镜这类可变数量、可变位置的麦克风阵列时受限。本文要解决的是：如何让 MLLM 在任意可穿戴阵列布局下同时完成声源定位与空间选择性转录。

## 💡 核心创新

1. FOACODER：布局灵活的空间编码器，从可变阵列波束成形得到一阶 Ambisonics
2. 两阶段六任务课程训练 MLLM 理解空间音频嵌入
3. Spatio-temporal Weighted Cross-Entropy Loss 平衡转录与方向预测
4. 在 1,211 种 4~9 麦克风阵列配置下保持鲁棒

## 🏗️ 模型架构

输入为智能眼镜可变数量、可变位置麦克风阵列信号，先经波束成形转换为 First Order Ambisonics 表示；FOACODER 作为空间音频编码器，以声源定位与自我中心语音活动检测为训练目标，输出空间音频嵌入。该嵌入送入多模态大语言模型，经两阶段课程学习六个任务，包括声源定位与多说话人重叠场景下的空间选择性转录。输出为方位/俯仰方向预测与转录文本，并用 Spatio-temporal Weighted Cross-Entropy Loss 联合优化。

## 📚 数据集

- 自建评估集（评估，含多说话人与重叠声场景）
- 智能眼镜阵列配置数据（评估，1,211 种 4~9 麦克风布局）

## 📊 实验结果

摘要仅给出相对结论：在自建评估集上，SEA-LM 相比基线取得更低的方位与俯仰 MAE、更高的时间 IoU、更低的外部声源幻觉率与漏检率，并在多数转录任务上 WER 更低；同时在 1,211 种 4~9 麦克风阵列配置下保持鲁棒。摘要未提供具体数值、消融实验与推理延迟数据。

## 🎯 结论与影响

最强结论是：布局灵活的空间编码器加 MLLM 课程训练，可在可穿戴阵列上同时实现定位与空间选择性转录。这为空间音频理解与多模态大模型结合提供了可扩展范式，对智能眼镜、助听与会议转录等落地场景有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值、消融实验与推理延迟，无法判断各模块贡献；评估集为自建，缺少与公开空间音频基准的对比；1,211 种阵列配置的鲁棒性声明缺乏统计细节；未说明 FOACODER 与 MLLM 的参数量及训练成本。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-08/">← 返回 2026-10-08 速递</a></div>
