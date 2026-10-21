---
title: "Preference-Aware Pareto Steering for Multi-Task Speech LLMs"
date: 2026-10-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出 EA-SURF，一种先验式多任务标量化权重自适应方法，使语音 LLM 的 ASR/时间戳/翻译权衡贴合部署偏好。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多任务学习</span> <span class="tag-pill tag-pill-soft">#语音大模型</span> <span class="tag-pill tag-pill-soft">#帕累托优化</span> <span class="tag-pill tag-pill-soft">#语音翻译</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.27200</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.27200" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.27200" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 EA-SURF，一种先验式多任务标量化权重自适应方法，使语音 LLM 的 ASR/时间戳/翻译权衡贴合部署偏好。
</div>

## 👥 作者与机构

**Liuyuan Jiang** ¹ · Vishal Sunder · Samuel Thomas · Brian Kingsbury · Jeff Kuo · Lisha Chen · George Saon

**机构**：IBM 研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多任务语音 LLM 训练与部署权衡的研究者与工程团队阅读。建议重点看 §3 的 EA-SURF 权重更新推导与收敛性定理，以及 §4 的六组三目标任务实验和超体积对比表；若只关心落地，可先看偏好匹配曲线与固定权重基线对比图。

## 🌍 研究背景

语音 LLM 已能联合完成 ASR、时间戳预测（TS）与语音翻译（ST），但联合训练存在任务间权衡：固定损失权重只能得到帕累托前沿上的某一个点，无法按部署偏好（如更重视 WER 还是时间戳精度）定向控制。已有工作多依赖事后重训或网格搜索权重，代价高且不可控。本文要解决的是：在保持标准加权损失训练流程不变的前提下，让训练过程自动收敛到用户指定的偏好点。

## 💡 核心创新

1. EA-SURF：按任务参考性能在线自适应标量化权重
2. 端点锚定的偏好匹配机制，含可检验正则条件
3. 理论证明更新在目标偏好处趋于平稳
4. 无需改动训练管线即可实现先验偏好控制

## 🏗️ 模型架构

方法不改变模型结构，作用于训练目标层：输入为语音 LLM 的多任务输出（ASR 文本、时间戳、翻译），主干沿用现有语音 LLM（摘要未指明具体网络）。EA-SURF 为每个任务维护参考性能（endpoint），按当前模型相对各任务参考的表现计算归一化进度，据此在线调整标量化权重，使加权损失的最优点向目标偏好移动；输出为随训练演化的权重序列与最终模型。摘要未给出参数量。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 端点归一化超体积（endpoint-inclusive normalized hypervolume） | 六个三目标语音 LLM 请求（摘要未列具体测试集） | 固定损失权重 | **EA-SURF** | +17.8% |

摘要仅报告一项量化结果：在六组三目标语音 LLM 请求上，EA-SURF 均向请求的偏好目标收敛，端点归一化超体积较固定损失权重提升 17.8%。摘要未给出各任务的具体 WER、时间戳误差或 BLEU 数值，也未报告消融与推理开销，需查阅正文表格确认。

## 🎯 结论与影响

最强结论是：不改训练管线即可让多任务语音 LLM 的权衡按偏好定向收敛，并有收敛性理论支撑。这为语音 LLM 的部署定制（不同场景侧重不同任务）提供了低成本手段，后续工作可将其扩展到更多任务与在线偏好切换。

## ⚠️ 局限与未解决问题

摘要未给出各任务绝对指标与逐任务消融，偏好匹配的误差界与收敛速度缺乏实验量化；参考端点如何选取、对参考质量是否敏感未说明；仅覆盖三目标任务，任务数增多时权重自适应稳定性未知；未报告训练额外开销。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-10-21/">← 返回 2026-10-21 速递</a></div>
