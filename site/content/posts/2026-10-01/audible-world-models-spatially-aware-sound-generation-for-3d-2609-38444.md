---
title: "Audible World Models: Spatially Aware Sound Generation for 3D Worlds"
date: 2026-10-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "免训练框架为文本生成的3D世界构建全景代理，分离语义层、合成干音频并按几何声学渲染随听者移动变化的空间音频。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#音频生成</span> <span class="tag-pill tag-pill-soft">#3D场景</span> <span class="tag-pill tag-pill-soft">#几何声学</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.38444</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.38444" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.38444" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>免训练框架为文本生成的3D世界构建全景代理，分离语义层、合成干音频并按几何声学渲染随听者移动变化的空间音频。
</div>

## 👥 作者与机构

**Duowen Chen** ¹ · Jinjin He · Gouthaman KV · Sandeep Bangalore Venkatesh · Bo Zhu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做空间音频渲染、3D场景音频生成、多模态世界模型的研究者与工程团队阅读。建议重点看方法部分中语义分层与声源锚定几何的流程，以及空间一致性评测协议；实验表格与VLM/人评部分可快速浏览。若关注HRTF或双耳渲染细节，需确认其几何声学传播是否含头相关滤波。

## 🌍 研究背景

文本/图像条件的世界生成器已能产出视觉丰富的3D环境，但多数场景无声，或仅用文本或渲染视频合成音轨。这类音频只表达“听到什么”，缺少声源空间位置与随听者移动的感知变化建模。已有空间音频工作多依赖真实或录制的场景几何与脉冲响应，难以直接接入生成式3D世界。本文要在生成世界状态中显式引入语义、几何与声传播的耦合，实现听者相关的空间音频。

## 💡 核心创新

1. 免训练框架，将声音写入生成世界状态而非后处理音轨
2. 全景3D代理语义分层，区分发声前景物体与环境背景区域
3. 声源锚定重建几何，用几何声学传播渲染听者相关空间音频

## 🏗️ 模型架构

输入为文本提示，先构建全景3D代理并分割为语义层，识别发声前景物体与背景环境区域；对每个声音标签合成干音频，再将声源锚定到重建几何上，通过几何声学传播模型渲染随听者视角与运动变化的空间音频。整体为免训练流水线，摘要未给出参数量或具体主干网络名。

## 📚 数据集

- 80个生成场景（评估，含文本/视频/全景条件基线对比）

## 📊 实验结果

摘要仅说明在80个生成场景上，空间一致性较文本、视频、全景条件基线有显著提升，同时保持有竞争力的语义对齐；VLM评估与人类主观评价显示音轨在视听一致性、空间合理性与运动相关行为上更受偏好。未给出SI-SDR、PESQ、MOS等具体数值，也无消融与效率指标。

## 🎯 结论与影响

最强结论是显式耦合语义、几何与声传播可在生成3D世界中维持持久声源位置并随听者运动自适应渲染。这为生成式世界模型的“可听化”提供了免训练范式，后续可推动空间音频与3D生成、具身仿真的结合。工业上可用于VR/AR场景、游戏与虚拟制作的自动化空间音轨生成。

## ⚠️ 局限与未解决问题

摘要未报告任何客观空间音频指标（如定位误差、双耳一致性）与推理延迟，评测以VLM与主观偏好为主，缺乏与专用空间音频渲染基线的定量对比；免训练流程依赖全景代理与语义分层的质量，错误传播风险未做消融；80个生成场景的多样性也有限。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-01/">← 返回 2026-10-01 速递</a></div>
