---
title: "Exploring Speaker-Aware Engagement Modeling for Children with Autism Spectrum Disorder"
date: 2026-11-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#说话人日志"]
summary: "在自闭症儿童家庭机器人干预录音中，用说话人日志分离儿童与照护者语音，比较声学参与度建模效果。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#说话人日志</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#说话人日志</span> <span class="tag-pill tag-pill-soft">#副语言与行为建模</span> <span class="tag-pill tag-pill-soft">#自闭症谱系障碍</span> <span class="tag-pill tag-pill-soft">#社会辅助机器人</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.24794</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.24794" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.24794" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在自闭症儿童家庭机器人干预录音中，用说话人日志分离儿童与照护者语音，比较声学参与度建模效果。
</div>

## 👥 作者与机构

**Kaleen Shrestha** ¹ · Austin Joel Dympep · Young Suh Hong · Maja Matari\'c

**机构**：加州大学洛杉矶分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做副语言/行为建模、临床语音应用、以及人机交互的研究者速读。不建议通读：核心结论是日志化特征 AUROC 略高但不显著，且个体差异大。建议先看实验设置与 AUROC 结果表，再看个体差异分析部分，方法细节可略。

## 🌍 研究背景

参与度建模在自闭症谱系障碍（ASD）儿童干预中已有较多工作，但多集中在视觉模态，且普遍报告显著的个体差异。声学模态在自然家庭场景中受多说话人、非典型交互模式干扰，说话人特定分析困难。此前缺少在长时程、多说话人自然交互中验证说话人日志是否能提升声学参与度建模的证据，本文针对这一空白展开。

## 💡 核心创新

1. 将说话人日志引入ASD儿童家庭干预的声学参与度建模
2. 对比日志化与未日志化音频训练的经典ML模型AUROC
3. 按参与者分析儿童与照护者声学特征相对贡献差异

## 🏗️ 模型架构

输入为月长时程家庭社会辅助机器人（SAR）干预录音，先经说话人日志模块分离出儿童与家长/照护者两路语音，再对每路提取声学特征（具体特征集摘要未详述），随后用经典机器学习模型（如SVM/随机森林一类）分别训练参与度分类器，输出参与度预测的AUROC。未使用深度端到端网络，也未报告参数量。

## 📚 数据集

- 自采家庭SAR干预录音（7名ASD儿童，月长时程，训练与评估）

## 📊 实验结果

摘要仅给出定性结论：日志化音频训练的模型 AUROC 一致高于未日志化音频，但差异未达统计显著。儿童与照护者声学特征的相对贡献因参与者而异，说明与参与度相关的声学信息在儿童间不一致。摘要未给出具体 AUROC 数值、样本量与消融细节。

## 🎯 结论与影响

最强结论是说话人日志在自然多说话人场景下可隔离说话人特定发声，且不损害（略提升）声学参与度建模。这为ASD参与度建模的个体差异证据扩展到声学域，提示后续研究需按参与者建模。对临床/教育机器人落地意味着需个性化声学模型而非统一模型。

## ⚠️ 局限与未解决问题

样本仅7名儿童，统计功效不足，故差异不显著；未报告具体AUROC与置信区间；声学特征集与分类器细节缺失，难以复现；未与深度参与度模型对比；日志错误对结果的影响未做消融。

---

<div class="paper-footer"><span>评分：5.8</span><span>原始：5.8</span><a href="/audio-paper-daily/posts/2026-11-19/">← 返回 2026-11-19 速递</a></div>
