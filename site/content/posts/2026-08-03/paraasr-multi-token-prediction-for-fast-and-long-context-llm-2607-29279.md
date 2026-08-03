---
title: "ParaASR: Multi-Token Prediction for Fast and Long-Context LLM-Based Speech Recognition"
date: 2026-08-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "ParaASR利用多令牌预测让4B LLM解码器每步生成多个令牌，在保持识别质量的同时大幅降低延迟，支持32K上下文和30分钟音频单次转录。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多令牌预测</span> <span class="tag-pill tag-pill-soft">#长上下文</span> <span class="tag-pill tag-pill-soft">#低延迟</span> <span class="tag-pill tag-pill-soft">#LLM解码器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.29279</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.29279" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.29279" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>ParaASR利用多令牌预测让4B LLM解码器每步生成多个令牌，在保持识别质量的同时大幅降低延迟，支持32K上下文和30分钟音频单次转录。
</div>

## 👥 作者与机构

**Qingjian Lin** ¹ · Yuxin Li · Haoyang Zhang · Jun Chen · Yechang Huang · Feng Tian · Xie Li · Xiangyu Tony Zhang · … 等 9 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR研究者、LLM部署工程师。值得通读，重点看方法部分（§3）的MTP对齐策略和推理验证机制，以及实验部分（§4）的RTF和长音频结果。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

现代ASR采用音频编码器-LLM解码器架构，通过大规模语言建模提升转录质量，但自回归解码成本随解码器规模增长，导致质量与延迟的权衡。作者认为ASR输出锚定于输入语音，具有高并行解码的归纳偏置，因此提出多令牌预测来打破这一权衡。

## 💡 核心创新

1. 提出ParaASR，利用多令牌预测（MTP）让4B LLM每步生成多个令牌
2. 采用分阶段优化策略，先建立自回归识别器，再对齐五个未来令牌分支
3. 推理时提出六令牌延续，仅接受验证前缀，保持自回归解码的安全性
4. 平均接受长度达5.0/6，验证语音的确定性结构适合多令牌解码
5. 原生32K上下文窗口，支持30分钟音频单次转录

## 🏗️ 模型架构

输入为音频特征，经音频编码器提取后送入4B LLM解码器。解码器采用MTP模块，包含五个未来令牌分支，每个分支预测后续令牌。训练分阶段：先训练自回归识别器，再通过MTP对齐分支。推理时，每步生成六令牌候选，通过验证机制接受前缀，确保输出安全。模型支持32K上下文，可处理长音频。

## 📚 数据集

- 中文基准（评估）
- 英文基准（评估）
- 长语音基准（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 平均错误率 | 中文基准 | 未提供 | **2.97%** | 未提供 |
| 平均错误率 | 英文基准 | 未提供 | **3.68%** | 未提供 |
| 平均错误率 | 长语音基准 | 未提供 | **3.70%** | 未提供 |
| 实时因子（RTF） | 未指定 | 未提供 | **0.0053** | 未提供 |

实验显示ParaASR在中文、英文和长语音基准上分别达到2.97%、3.68%和3.70%的平均错误率，同时RTF低至0.0053，表明解码器扩展、低延迟推理和长上下文转录可以同时实现。平均接受长度5.0/6验证了多令牌预测的有效性。

## 🎯 结论与影响

ParaASR通过多令牌预测和验证机制，在保持识别质量的同时显著降低延迟，支持长上下文转录，表明解码器规模、低延迟和长上下文并非不可兼得。该工作为ASR的高效解码提供了新思路，有望推动LLM-based ASR的工业部署。

## ⚠️ 局限与未解决问题

摘要未提供与强基线的详细对比，也未报告模型参数量、训练数据规模等关键细节。未提及消融实验和推理延迟的具体测量条件。长上下文转录的评估基准未明确，可能影响结果的可比性。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-08-03/">← 返回 2026-08-03 速递</a></div>
