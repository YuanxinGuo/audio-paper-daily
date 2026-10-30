---
title: "Efficient Agentic Audio-Visual Question Answering through Toolset Pruning and Modality Consolidation"
date: 2026-10-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频问答"]
summary: "通过分阶段剪枝专用工具并将模态专用工具整合为全模态工具，构建仅含两个工具的精简 AVQA 智能体，精度持平或更优且推理成本降约 70%。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频问答</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态智能体</span> <span class="tag-pill tag-pill-soft">#工具剪枝</span> <span class="tag-pill tag-pill-soft">#音视频理解</span> <span class="tag-pill tag-pill-soft">#推理效率</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.38960</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.38960" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.38960" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过分阶段剪枝专用工具并将模态专用工具整合为全模态工具，构建仅含两个工具的精简 AVQA 智能体，精度持平或更优且推理成本降约 70%。
</div>

## 👥 作者与机构

**Yi Wang** ¹ · Tianzi Wang · Peter Bell

**机构**：剑桥大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态智能体、工具调用与推理效率优化的研究者阅读。值得通读，重点看工具剪枝的分阶段实验设计（§3）与工具整合的消融表，以及三个 AVQA benchmark 上的精度-成本权衡曲线；若只关心效率结论，可先看主结果表与成本分析图。

## 🌍 研究背景

细粒度 AVQA 需要跨模态对齐与时序定位稀疏证据。此前 SOTA 多为 Omni-modal 智能体（如 OmniAgent），依靠大量专用感知工具主动采集证据，性能强但工具集庞大、执行轨迹长、推理成本高。领域内尚不清楚主动感知是否真的依赖宽泛的专用工具集，尤其是音频或视觉模态专用工具是否必要。本文要回答：仅保留最核心感知能力的紧凑工作流能否维持可比性能并显著降低推理开销。

## 💡 核心创新

1. 分阶段受控实验剪枝专用工具集
2. 将模态专用工具逐步整合为全模态工具
3. 提出仅含 Omni-captioning 与 Omni-QA 的双工具智能体
4. 在三个 AVQA benchmark 上验证精度-成本权衡

## 🏗️ 模型架构

以 OmniAgent 为起点，输入为音视频片段与问题文本。智能体由 LLM 调度器驱动，按需调用感知工具采集证据并迭代推理。作者先做分阶段剪枝：逐步移除音频专用、视觉专用工具，观察精度变化；再将剩余模态专用工具整合为全模态工具（Omni-modal captioning 负责统一描述音视频内容，Omni-modal QA 负责跨模态问答）。最终工作流仅暴露两个工具，缩短执行轨迹。摘要未给出参数量与具体主干网络细节。

## 📚 数据集

- 三个常用 AVQA benchmark（评估，具体名称摘要未给出）

## 📊 实验结果

摘要仅给出总体结论：在三个广泛使用的 AVQA benchmark 上，紧凑双工具智能体精度与专用工具智能体持平或更优，推理成本降低约 70%。摘要未披露具体精度数值、各 benchmark 名称及消融细节，无法列出逐项指标对比。

## 🎯 结论与影响

最强结论是：AVQA 的主动感知并不依赖宽泛专用工具集，两个全模态工具即可达到同等甚至更好精度，同时推理成本降约 70%。这提示后续智能体研究应优先做工具整合而非堆叠工具，对工业落地意味着更低的延迟与部署成本。

## ⚠️ 局限与未解决问题

摘要未给出具体精度数字与逐 benchmark 结果，缺少工具剪枝各阶段的量化消融；未报告推理延迟、token 消耗等效率细项；仅三个 AVQA benchmark，泛化性未知；全模态工具整合可能损失细粒度模态专有信息，作者未讨论失败案例。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-30/">← 返回 2026-10-30 速递</a></div>
