---
title: "DRL-CLBA: A Clean Label Backdoor Attack for Speech Classification via DDPG Reinforcement Learning"
date: 2026-07-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分类"]
summary: "提出基于DDPG强化学习的干净标签后门攻击方法，利用深度音频隐写嵌入样本特定触发器，实现无标签迁移的语音分类后门攻击。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#后门攻击</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#语音分类</span> <span class="tag-pill tag-pill-soft">#对抗攻击</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.01729</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.01729" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.01729" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于DDPG强化学习的干净标签后门攻击方法，利用深度音频隐写嵌入样本特定触发器，实现无标签迁移的语音分类后门攻击。
</div>

## 👥 作者与机构

**Yueming Huang** ¹ · Wenhan Yao · Fen Xiao · Xiarun Chen · Weiping Wen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音安全、对抗攻击方向的研究者阅读。建议重点看第3节方法设计和第4节实验结果，特别是与现有防御的对抗效果。可先看§3.2的隐写嵌入和§3.3的强化学习优化。

## 🌍 研究背景

语音分类深度模型易受后门攻击，攻击者在训练时植入触发器，推理时触发导致误分类。现有样本特定攻击虽能绕过部分防御，但常依赖标签污染，易被人工数据防御检测。本文旨在设计一种干净标签后门攻击，无需修改标签即可实现高成功率攻击，并抵抗微调、剪枝等防御。

## 💡 核心创新

1. 利用DDPG强化学习优化目标样本向锚点迁移
2. 深度音频隐写嵌入样本特定触发器
3. 实现无标签迁移的干净标签后门攻击
4. 在多个数据集和模型上验证攻击有效性

## 🏗️ 模型架构

输入音频经深度音频隐写嵌入样本特定触发器（如LSTM编码器生成隐写音频），然后输入语音分类模型（如ResNet、VGG等）。攻击训练阶段，使用DDPG强化学习框架：智能体（Actor-Critic网络）根据当前样本状态选择动作（调整隐写参数），奖励函数基于模型深层特征空间中样本与锚点的距离，优化目标使样本特征靠近锚点，从而无需修改标签即可植入后门。

## 📚 数据集

- Speech Commands（训练/评估，35个词类）
- LibriSpeech（训练/评估，说话人识别）
- UrbanSound8K（训练/评估，环境声音分类）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 攻击成功率 (ASR) | Speech Commands | 干净标签攻击 (CLBA) 约85% | **DRL-CLBA 约95%** | +10% |
| 攻击成功率 (ASR) | LibriSpeech | CLBA 约80% | **DRL-CLBA 约92%** | +12% |
| 攻击成功率 (ASR) | UrbanSound8K | CLBA 约82% | **DRL-CLBA 约90%** | +8% |

在三个数据集上，DRL-CLBA均取得90%以上攻击成功率，优于现有干净标签攻击。防御实验显示，微调后ASR仍保持85%以上，剪枝和频谱特征防御下ASR下降不足10%，表明攻击具有强鲁棒性。未报告模型原始分类准确率变化。

## 🎯 结论与影响

本文提出的DRL-CLBA方法成功实现了高效、鲁棒的干净标签后门攻击，揭示了语音分类模型在安全方面的脆弱性。该工作为语音对抗攻击提供了新思路，可能推动更有效的防御机制研究。对工业界语音控制系统安全具有警示意义。

## ⚠️ 局限与未解决问题

未报告攻击对原始分类准确率的影响；未与更多先进防御（如神经清除、STRIP）对比；仅验证了四种DNN，未覆盖Transformer等架构；隐写嵌入可能引入可感知噪声，未进行主观听感评估。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-03/">← 返回 2026-07-03 速递</a></div>
