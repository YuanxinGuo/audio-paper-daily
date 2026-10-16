---
title: "Reference-Guided Turn-Taking Style Transfer for Full-Duplex Spoken Language Models"
date: 2026-10-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音对话系统"]
summary: "从全双工语音语言模型自身对话中提取\"主动性向量\"，无需训练即可读取并调节模型发言比例，并用短参考录音迁移说话人的轮流风格。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话系统</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#全双工语音语言模型</span> <span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#激活引导</span> <span class="tag-pill tag-pill-soft">#风格迁移</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.20763</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://elpsykongloo.github.io/initiative-vector/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">elpsykongloo.github.io/initiative-vector/</span></span></a><a class="oc-chip oc-chip-demo" href="https://elpsykongloo.github.io/initiative-vector/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">elpsykongloo.github.io/initiative-vector/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.20763" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.20763" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://elpsykongloo.github.io/initiative-vector/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://elpsykongloo.github.io/initiative-vector/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>从全双工语音语言模型自身对话中提取"主动性向量"，无需训练即可读取并调节模型发言比例，并用短参考录音迁移说话人的轮流风格。
</div>

## 👥 作者与机构

**Yuxuan Chen** ¹ · Yang Xiao · Jack Sun · Chak Sun · Brick Li · Sam

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究全双工语音对话、LLM 可解释性与激活引导的读者。建议通读，重点看主动性向量的提取方法（哪一层、如何无监督定位）与 §风格迁移实验，尤其是参考特异性 93-98% 的对照设计；表 1 的 speech ratio 对比与 800 ms 提前预测实验值得细看。

## 🌍 研究背景

全双工语音语言模型在每一帧决定是否抢话，从而形成对话人格，但一组权重只编码一种风格。此前对轮流行为的控制多来自外部（提示、解码约束、微调），既未定位决定"说多少"的内部量，也难以按人定制。本文要回答：模型内部是否存在一个可读、可调、可迁移的轮流风格方向。

## 💡 核心创新

1. 无训练无标注地从模型自身对话中提取晚期残差流"主动性向量"
2. 同一方向既能提前 800 ms 预测发言起始，又能缩放调节发言比例
3. 用短参考录音实现参考特异的轮流风格迁移，替换参考即失配

## 🏗️ 模型架构

输入为全双工语音语言模型的逐帧对话表示；在晚期残差流上通过对比模型自身"抢话/让话"对话样本，无监督地定位单一方向（initiative vector）。该方向既作为线性探针读取每帧发言决策，又在生成时按标量系数注入残差流以缩放发言倾向。风格迁移时，从短参考录音对应的对话中估计该方向的目标尺度，作为每说话人的校准量。摘要未给出参数量与具体主干网络名。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| speech ratio | 模型自身对话（多语料） | 无引导 21-30% | **42-61%** | +21~31 个百分点 |
| 参考特异性（替换参考后匹配变差比例） | 多说话人参考录音 | — | **93-98%** | — |

摘要给出两类量化结果：缩放主动性向量可将发言比例从 6-12% 提升到 42-61%，且跨对话、跨权重、跨语料一致；无引导为 21-30%。风格迁移具参考特异性，换用他人参考在 93-98% 情况下匹配变差，而最佳统一剂量与不引导无法区分。摘要未报告 SI-SDR、PESQ、WER 等语音质量指标，也未给出推理开销。

## 🎯 结论与影响

最强结论是：轮流风格并非冻结在权重中，而是一个可读、可平移、可按人校准的残差流方向。这为全双工对话模型的人格控制提供了轻量、可解释的接口，后续研究可沿此探索多属性解耦与在线个性化；工业上意味着无需重训即可按用户调节助手"话多话少"。

## ⚠️ 局限与未解决问题

摘要未给出客观语音质量与延迟指标，也未说明主动性向量在不同模型规模、语言上的稳定性；风格迁移仅以匹配度衡量，缺少人类主观 MOS 或对话自然度评估；参考特异性实验的对照（统一剂量）较单一，未与提示/微调基线全面比较。

## 🔗 开源资源

- **项目主页**：<https://elpsykongloo.github.io/initiative-vector/>
- **Demo / 试听**：<https://elpsykongloo.github.io/initiative-vector/>

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-16/">← 返回 2026-10-16 速递</a></div>
