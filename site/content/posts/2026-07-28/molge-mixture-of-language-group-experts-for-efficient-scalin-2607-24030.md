---
title: "MoLGE: Mixture of Language Group Experts for Efficient Scaling of Massively Multilingual Speech Recognition"
date: 2026-07-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出MoLGE方法，通过语言分组专家和分层LoRA，高效扩展多语言ASR至495种语言，缓解多语言诅咒。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多语言语音识别</span> <span class="tag-pill tag-pill-soft">#混合专家模型</span> <span class="tag-pill tag-pill-soft">#低秩适配</span> <span class="tag-pill tag-pill-soft">#语言分组</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.24030</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.24030" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.24030" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MoLGE方法，通过语言分组专家和分层LoRA，高效扩展多语言ASR至495种语言，缓解多语言诅咒。
</div>

## 👥 作者与机构

**Sangmin Lee** ¹ · Woojin Chung · Woongjib Choi · Hong-Goo Kang ✉

**机构**：延世大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多语言ASR、语音自监督模型或MoE研究的读者。建议重点阅读§3方法部分（MoLGE架构与语言分组策略）和§4实验（表1-3及消融实验）。可先看§4.2了解分组策略的影响。

## 🌍 研究背景

大规模多语言ASR模型需覆盖数百种语言，但常面临多语言诅咒：模型容量被稀释，低资源语言性能下降。现有方法如语言特定MoE虽能缓解，但子模块数量随语言数线性增长，参数效率低。本文提出MoLGE，基于语音自监督模型，通过将相似语言聚类并分配共享专家，减少子模块数量，并结合分层LoRA高效建模语言特性。

## 💡 核心创新

1. 提出语言分组专家（MoLGE），将相似语言聚类共享专家，减少子模块数量
2. 引入分层LoRA策略，分别适配S3M的声学与语言组件
3. 系统研究基于语言学和数据驱动的分组策略对性能的影响

## 🏗️ 模型架构

输入语音特征经WavLM（S3M）提取表示，主干为Transformer编码器。MoLGE在Transformer的FFN层替换为语言分组专家：先根据语言ID选择对应专家组，每个组内多个专家通过门控网络加权组合。同时，在WavLM的声学与语言组件中分别插入分层LoRA模块（低秩矩阵），以高效建模语言特定信息。输出为CTC/Attention解码的文本序列。参数量约600M（基础模型）。

## 📚 数据集

- Common Voice（495种语言，训练/评估）
- FLEURS（102种语言，评估）
- MLS（8种语言，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | Common Voice 495语言平均 | Dense baseline 28.5 | **MoLGE 25.1** | -3.4% |
| WER | FLEURS 102语言平均 | Dense baseline 22.3 | **MoLGE 19.8** | -2.5% |

MoLGE在495种语言上平均WER 25.1%，比稠密基线降低3.4个百分点，且仅增加5%可训练参数。语言分组策略中，基于语系的分组优于随机分组，数据驱动聚类（基于语言嵌入）效果最佳。分层LoRA进一步降低WER约0.8%。在FLEURS上MoLGE也一致优于基线。

## 🎯 结论与影响

MoLGE通过结构化语言分组专家和分层LoRA，有效扩展多语言ASR至495种语言，显著缓解多语言诅咒。该方法为大规模多语言ASR提供了一种参数高效的扩展路径，未来可探索动态分组和跨模态迁移。

## ⚠️ 局限与未解决问题

实验仅在Common Voice等开源数据集上评估，未涉及真实噪声场景；语言分组策略依赖先验知识或聚类质量；未报告推理延迟或内存占用；与最新MoE方法（如ST-MoE）对比缺失。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-28/">← 返回 2026-07-28 速递</a></div>
