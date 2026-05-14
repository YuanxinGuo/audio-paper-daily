---
title: "DeePen: Penetration Testing for Audio Deepfake Detection"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#信号处理", "#对抗攻击", "#渗透测试", "#音频深度伪造检测", "#鲁棒性评估"]
summary: "提出DeePen，一种无需先验知识的黑盒渗透测试方法，通过信号处理攻击评估音频深度伪造检测模型的鲁棒性，发现所有测试模型均存在弱点。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对抗攻击</span> <span class="tag-pill tag-pill-soft">#鲁棒性评估</span> <span class="tag-pill tag-pill-soft">#信号处理</span> <span class="tag-pill tag-pill-soft">#渗透测试</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2502.20427</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2502.20427" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2502.20427" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DeePen，一种无需先验知识的黑盒渗透测试方法，通过信号处理攻击评估音频深度伪造检测模型的鲁棒性，发现所有测试模型均存在弱点。
</div>

## 👥 作者与机构

Nicolas M\"uller · **Piotr Kawa** ¹ · Adriana Stan · Thien-Phuc Doan · Souhwan Jung · Wei Herng Choong · Philip Sperl · Konstantin B\"ottinger

**机构**：未明确

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、深度伪造检测领域的研究者。重点看§3攻击设计、§4实验结果及表1/2。若关注防御，可跳过§2背景。建议先读摘要和结论，再深入方法部分。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 评估音频深度伪造检测模型对信号处理攻击的鲁棒性。 |
| **核心创新** | 提出黑盒渗透测试框架DeePen · 系统评估多种信号处理攻击的有效性 · 发现时间拉伸和回声添加等简单攻击可欺骗所有模型 |
| **模型架构** | DeePen框架：输入音频 → 攻击模块（信号处理操作如时间拉伸、回声添加等） → 目标检测模型（黑盒） → 输出欺骗成功率。无模型参数，仅需攻击列表。 |
| **数据集** | 未明确指定，但使用真实生产系统和公开学术模型检查点 |
| **关键结果** | 所有测试的深度伪造检测系统均被简单攻击欺骗，如时间拉伸和回声添加。部分攻击可通过针对性重训练缓解，但其他攻击仍持续有效。具体指标未在摘要中给出。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但音频深度伪造检测与语音增强、语音分离等领域有交叉，例如对抗攻击方法可迁移至评估语音增强模型的鲁棒性。

## ⚠️ 局限与未解决问题

未提供具体攻击成功率数值，缺乏与现有攻击方法的对比；未讨论计算开销；数据集和模型细节不明确；未考虑自适应攻击或白盒场景。

## 📋 引用

```bibtex
@article{müller20262502,
  title  = {DeePen: Penetration Testing for Audio Deepfake Detection},
  author = {Nicolas M\"uller and  Piotr Kawa and  Adriana Stan and  Thien-Phuc Doan and  Souhwan Jung and  Wei Herng Choong and  Philip Sperl and  Konstantin B\"ottinger},
  journal = {arXiv preprint arXiv:2502.20427},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
