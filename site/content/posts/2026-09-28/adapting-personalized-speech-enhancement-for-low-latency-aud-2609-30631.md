---
title: "Adapting Personalized Speech Enhancement for Low-Latency Audio-Visual Target-Speaker Extraction"
date: 2026-09-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "从个性化语音增强模型出发，加入嘴部视觉特征并联合微调，实现20ms延迟的在线音视频目标说话人提取，误混率从46%降至1.6%。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#音视频多模态</span> <span class="tag-pill tag-pill-soft">#低延迟</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.30631</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.30631" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.30631" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>从个性化语音增强模型出发，加入嘴部视觉特征并联合微调，实现20ms延迟的在线音视频目标说话人提取，误混率从46%降至1.6%。
</div>

## 👥 作者与机构

**Rayhan Rashed** ¹ · Senja Filipi · Ross Cutler

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音视频目标说话人提取、低延迟语音增强与会议语音的读者。建议通读，重点看§3的嘴部特征注入方式与联合微调策略，以及表2/表3中合成基准与真实会议数据的对比；P.835主观测试部分值得细看，因为这是该文区别于纯分离指标论文的核心卖点。

## 🌍 研究背景

在线音视频目标说话人提取此前多沿用分离范式：在合成混合上训练与评测，主流方法如在线自回归音视频提取器以SI-SDR等分离指标为优化目标。这类做法忽略了两点：一是真实会议中的听感质量与说话人保持/抑制行为未被系统评测；二是合成混合与真实录音存在域差。本文从个性化语音增强（PVQE）反向切入，先保证目标语音重建质量，再解决其在双说话人混合中46%误混目标的问题，并约束前瞻帧与算法延迟。

## 💡 核心创新

1. 从个性化语音增强模型出发，而非从分离模型改造，保留高质量目标重建能力
2. 在说话人条件输入处注入嘴部视觉特征，实现音视频条件融合
3. 视觉网络与重建网络联合微调，误混率从46%降至1.6%
4. 无未来帧、20ms算法延迟的在线流式设定，并在真实会议数据上验证

## 🏗️ 模型架构

输入为含噪混合语音与目标说话人注册语音（enrollment），以及对应视频帧的嘴部区域特征。主干沿用个性化语音增强网络，负责在注册语音条件下重建目标说话人；关键改动是在说话人条件输入（speaker-conditioning input）处拼接嘴部视觉特征，使目标线索同时来自注册语音与视觉。视觉编码器与重建网络进行联合微调，而非冻结视觉分支。输出为增强后的目标说话人波形，全程不使用未来帧，算法延迟20ms。摘要未给出参数量。

## 📚 数据集

- 合成双说话人混合基准（评估，两个合成benchmark）
- 真实会议录音语料（评估，两个会议语料用于P.835主观测试）
- 微调混合数据（训练/微调，说话人数少于部分测试片段）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 目标误混率 | 双说话人混合 | 起始PVQE模型 46% | **1.6%** | -44.4% |
| P.835 overall MOS | 会议语料1 | 在线自回归音视频提取器 | **AV-PVQE** | +0.57 MOS |
| P.835 overall MOS | 会议语料2 | 在线自回归音视频提取器 | **AV-PVQE** | +0.63 MOS |

摘要给出三类结果：误混率从46%降至1.6%；相对在线自回归音视频提取器，在两个合成基准上取得分离增益，在真实会议录音上增益更大，且在说话人数多于微调混合的片段上仍保持优势；两个会议语料的个性化P.835听感测试中overall质量分别提升0.57与0.63 MOS，与起始模型平均评分相近。保留与抑制测试显示无竞争语音时目标保持完好、目标缺失时能抑制竞争语音。摘要未给出SI-SDR等具体数值与消融细节。

## 🎯 结论与影响

最强结论是：在20ms算法延迟、无未来帧约束下，把嘴部视觉特征接入个性化增强模型的说话人条件输入并联合微调，可将近乎一半的目标误混率压到1.6%，同时在真实会议听感上显著优于在线自回归音视频提取器。这提示后续研究应把评测重心从合成分离指标转向真实会议与P.835听感，并重视目标保持/抑制行为。工业上对实时会议降噪与个性化拾音有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未报告SI-SDR、PESQ等客观指标的具体数值，也未给出推理延迟、参数量与计算开销；缺少对嘴部特征注入位置、联合微调策略的消融；真实会议评测规模与说话人重叠程度未说明；对比基线仅一个在线自回归音视频提取器，未与更多TSE方法比较；合成基准与真实会议之间的域差分析不足。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-28/">← 返回 2026-09-28 速递</a></div>
