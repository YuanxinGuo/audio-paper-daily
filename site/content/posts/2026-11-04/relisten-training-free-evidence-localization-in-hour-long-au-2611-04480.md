---
title: "ReListen: Training-Free Evidence Localization in Hour-Long Audio with Frozen Audio Language Models"
date: 2026-11-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频问答"]
summary: "冻结音频语言模型用Jev式扫描为每个20秒窗打分，定位证据后仅听最高分一分钟作答，免训练、免转写。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频问答</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#长音频理解</span> <span class="tag-pill tag-pill-soft">#证据定位</span> <span class="tag-pill tag-pill-soft">#免训练</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.04480</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.04480" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.04480" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>冻结音频语言模型用Jev式扫描为每个20秒窗打分，定位证据后仅听最高分一分钟作答，免训练、免转写。
</div>

## 👥 作者与机构

**Ming-Hao Hsu** ¹ · Shujie Liu · Yuxuan Hu · Yuxiang Wang · Yingda Shen · Jinyu Li · Zhizheng Wu

**机构**：微软研究院 · 香港中文大学（深圳）

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做长音频理解、音频LLM推理加速与证据定位的研究者阅读。值得通读，重点看§3的Jev式扫描打分与窗口聚合细节，以及表2/表3中与转写检索、时序定位训练模型的对比；若关注工程落地，可先看内存与延迟分析一节。

## 🌍 研究背景

小时级录音远超音频语言模型上下文，而答案常只依赖数秒片段。现有两条路线各有痛点：先整段转写再检索虽能塞进上下文，却丢弃声音与说话人信息；让模型反复回听音频的系统则需专门训练定位行为，成本高且泛化受限。本文要解决的是：在不训练、不转写的前提下，让冻结的音频语言模型自行在长录音中定位证据并作答。

## 💡 核心创新

1. Jev式扫描：用冻结ALM对每个20秒窗打分，估计其帮助回答问题的概率
2. 取最高分一分钟作为证据窗口，直接在该窗口内作答，无需转写
3. 免训练即具备时序定位能力，与专门训练的grounding模型持平
4. 验证证据需被听见：声音/说话人问题上听音频显著优于读转写

## 🏗️ 模型架构

输入为小时级原始音频与文本问题。方法不引入新网络，直接复用冻结的音频语言模型（ALM）：先将长音频切分为20秒窗，对每个窗构造“该窗是否有助于回答问题”的判别式查询，取模型输出概率作为窗口得分；随后聚合相邻窗得分，选出得分最高的一分钟片段，再将该片段音频与问题一起送入同一冻结ALM生成答案。全程无参数更新、无ASR转写，内存随窗口流式处理保持常数。

## 📚 数据集

- VoiceGiraffe（评估，小时级音频问答）
- LAT-Bench（评估，时序事件定位）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 证据命中率（与标注证据重叠） | VoiceGiraffe | 转写检索 | **88.5% 问题命中** | 显著高于转写检索 |
| 问答准确率 | VoiceGiraffe | 整段转写 | **本文方法** | +9.2 分 |
| 时序定位 | LAT-Bench | 专门训练的时序定位模型 | **冻结模型+Jev扫描** | 持平 |

摘要给出三项关键结论：证据命中率88.5%高于转写检索；在VoiceGiraffe上比整段转写高9.2分，且仅用极小比例音频即可匹配或超过听整段录音；在LAT-Bench上免训练即与专门训练的时序定位模型持平。此外，相同片段下读转写在语音内容题上与听持平，但声音与说话人题上听明显更准；推理速度快于所有转写系统，内存恒定。

## 🎯 结论与影响

最强结论是：冻结的音频语言模型无需转写与额外训练，即可自行在小时级录音中定位证据并作答。这为长音频理解提供了免训练、低内存的推理范式，可能推动后续研究转向利用ALM自身概率做检索式定位；工业上意味着长录音问答可用单卡流式处理，省去ASR管线与训练成本。

## ⚠️ 局限与未解决问题

摘要未给出延迟与内存的具体数值，也缺少窗口长度、打分聚合方式的消融；证据命中率仅报VoiceGiraffe，跨数据集泛化证据有限；与转写系统对比未覆盖更强的检索式RAG基线；20秒窗粒度可能漏掉极短事件。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-11-04/">← 返回 2026-11-04 速递</a></div>
