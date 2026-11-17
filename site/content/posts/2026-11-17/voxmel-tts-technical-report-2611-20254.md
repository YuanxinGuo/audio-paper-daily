---
title: "VoxMel TTS Technical Report"
date: 2026-11-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "VoxMel用固定可逆二维Haar变换把Mel分解为Coarse-Mel与两级残差，实现无tokenizer自回归TTS，0.6B模型WER 1.51%。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自回归TTS</span> <span class="tag-pill tag-pill-soft">#Mel频谱建模</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#GRPO</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.20254</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.20254" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.20254" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>VoxMel用固定可逆二维Haar变换把Mel分解为Coarse-Mel与两级残差，实现无tokenizer自回归TTS，0.6B模型WER 1.51%。
</div>

## 👥 作者与机构

**Wenhao Guan** ¹ · **Jiaxin Ye** ¹ · Haitao Li · Yifan Duan · Junxi Liu · Wangjin Zhou · Lin Li · Qingyang Hong · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做TTS声学建模、自回归生成与流匹配的研究者。建议通读：重点看§3的Haar分解与残差分层预测设计，以及§4中GRPO与flow head蒸馏（2/4步）的实验表；对比基线需关注是否与VAE-latent类方法在同等数据规模下比较。

## 🌍 研究背景

连续自回归TTS需要既能稳定做next-latent预测、又保留细粒度声学细节的声学目标。现有做法多用学习式压缩表示（如连续VAE latent），但依赖复杂神经编码器，编码器能力常成为生成保真度上限；而Mel频谱这类免训练目标虽无编码器开销，其在自回归生成中的潜力仍未被充分探索。本文要解决的是：如何让Mel频谱成为可稳定自回归建模的目标，同时不引入学习式编码器。

## 💡 核心创新

1. 固定可逆二维Haar变换分解Mel，免tokenizer免编码器
2. 频率-时间两轴分解为Coarse-Mel与时间/频率残差三层
3. 残差不回灌自回归历史，用NAR残差层条件预测
4. GRPO直接优化WER/SIM，并将flow head蒸馏为2/4步学生

## 🏗️ 模型架构

输入为Mel频谱，先经固定可逆二维Haar变换：沿频率轴分解为局部均值与频率残差，再沿时间轴把均值分量拆为Coarse-Mel与时间残差。语言模型主干自回归生成Coarse-Mel，配flow-matching头输出连续帧；随后非自回归残差层先由Coarse-Mel预测时间残差，再以重建的频率平均Mel为条件预测频率残差，两级残差均不进入自回归历史。逆变换精确重建Mel后接声码器。监督模型规模0.6B，训练数据10万小时Emilia。

## 📚 数据集

- Emilia（训练，10万小时）
- test-en（评估，英文测试集）
- test-zh（评估，中文测试集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | test-en | 监督模型 1.51% | **GRPO 1.15%** | -0.36% |
| SIM | test-en | 监督模型 0.738 | **GRPO 0.753** | +0.015 |
| CER | test-zh | 监督模型 1.29% | **GRPO 1.17%** | -0.12% |
| SIM | test-zh | 监督模型 0.755 | **GRPO 0.776** | +0.021 |

监督0.6B模型在test-en取得1.51% WER / 0.738 SIM，test-zh取得1.29% CER / 0.755 SIM；GRPO进一步降至1.15% WER / 0.753 SIM与1.17% CER / 0.776 SIM。flow head蒸馏出2步与4步学生，每coarse帧需2或4次head评估，4步学生在SIM上保持竞争力、WER/CER接近监督模型。摘要未给出与VAE-latent类基线的直接对比及推理延迟数据。

## 🎯 结论与影响

最强结论是：固定可逆Haar变换可使Mel频谱成为可稳定自回归建模的目标，无需学习式编码器即可达到1.15% WER级合成质量。这为免tokenizer TTS提供了可复现的声学目标设计范式，并提示残差分层+GRPO+步数蒸馏的组合可降低推理开销，对工业级低延迟TTS部署有参考价值。

## ⚠️ 局限与未解决问题

摘要缺少与VAE-latent/其他自回归TTS在同等数据与参数量下的直接对比，也未报告RTF、显存与训练成本；两级NAR残差层的误差累积与逆变换重建误差未做消融；GRPO与蒸馏的收益来源缺乏分解实验；仅报WER/CER/SIM，缺MOS等主观听感指标。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-11-17/">← 返回 2026-11-17 速递</a></div>
