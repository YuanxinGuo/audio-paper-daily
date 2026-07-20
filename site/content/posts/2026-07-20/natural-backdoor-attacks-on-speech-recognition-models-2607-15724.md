---
title: "Natural Backdoor Attacks on Speech Recognition Models"
date: 2026-07-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出使用日常自然声音作为触发器，对语音识别模型实施后门攻击，仅需5%中毒样本即可接近100%攻击成功率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#后门攻击</span> <span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#自然触发</span> <span class="tag-pill tag-pill-soft">#深度学习安全</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.15724</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.15724" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.15724" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出使用日常自然声音作为触发器，对语音识别模型实施后门攻击，仅需5%中毒样本即可接近100%攻击成功率。
</div>

## 👥 作者与机构

**Jinwen Xin** ¹ · Xixiang Lyu · Jing Ma

**机构**：西安电子科技大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对语音识别安全、后门攻击感兴趣的读者。建议重点阅读第3节（攻击方法）和第4节（实验结果），特别是表1和表2。可关注触发器的自然性对隐蔽性的影响。

## 🌍 研究背景

深度学习模型在语音识别中广泛应用，但其安全性问题日益突出。后门攻击通过在训练数据中植入触发器，使模型在遇到触发器时输出攻击者指定的结果。现有后门攻击多使用人工设计的触发器（如特定噪声或图案），容易被检测。本文提出使用自然界或日常生活中的普通声音作为触发器，旨在提高攻击的隐蔽性和自然性。

## 💡 核心创新

1. 使用自然声音（如鸟鸣、雨声）作为后门触发器
2. 系统研究了中毒率、触发时长和混合比例对攻击效果的影响
3. 仅需5%中毒样本即可达到近100%攻击成功率
4. 触发器短时长或低幅度下仍保持高攻击成功率

## 🏗️ 模型架构

攻击流程：选择自然声音作为触发器，将其与正常语音样本混合（按一定混合比例），生成中毒训练样本。使用中毒数据集训练语音识别模型（如DeepSpeech、Kaldi等）。测试时，含有触发器的语音输入会触发后门，输出攻击者指定的目标标签。模型结构本身未修改，仅通过数据中毒实现后门植入。

## 📚 数据集

- LibriSpeech（训练和评估，包含1000小时英语语音）
- Common Voice（训练和评估，多语言语音数据集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 攻击成功率 (ASR) | LibriSpeech | 无攻击模型在良性样本上的准确率（约95%） | **99.8%** | +4.8% |
| 良性样本准确率 | LibriSpeech | 无攻击模型准确率（约95%） | **94.7%** | -0.3% |

实验表明，自然后门攻击在多种模型（DeepSpeech、Kaldi、Wav2Vec2）和数据集上均能保持高攻击成功率（>99%），且对良性样本准确率影响极小（下降<1%）。即使触发器时长仅0.1秒或混合比例低至0.1，攻击成功率仍超过90%。中毒率仅需5%即可达到近100%攻击成功率。

## 🎯 结论与影响

本文证明了使用自然声音作为后门触发器的可行性和危害性，仅需少量中毒样本即可实现高隐蔽性攻击。该工作提醒语音识别系统部署者需警惕此类自然触发后门，并推动防御机制的研究。对工业界而言，需在数据收集和训练过程中加强异常检测。

## ⚠️ 局限与未解决问题

未在更大规模模型（如Whisper）上验证；未考虑防御方法（如剪枝、微调）的对抗效果；触发器选择依赖人工挑选，未实现自动化；未评估攻击对说话人识别等下游任务的影响。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-20/">← 返回 2026-07-20 速递</a></div>
