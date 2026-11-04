---
title: "Attendance-guided speaker enrollment across meetings"
date: 2026-11-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#说话人识别"]
summary: "利用会议出席名单与匿名说话人聚类链交叉比对，实现多参与者自动注册，并发布污染敏感基准。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#说话人识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#说话人日志</span> <span class="tag-pill tag-pill-soft">#说话人注册</span> <span class="tag-pill tag-pill-soft">#会议转录</span> <span class="tag-pill tag-pill-soft">#基准数据集</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.04394</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.04394" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.04394" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用会议出席名单与匿名说话人聚类链交叉比对，实现多参与者自动注册，并发布污染敏感基准。
</div>

## 👥 作者与机构

**Minjae Lee** ¹ · Hee-Soo Heo · Youngki Kwon · Bong-Jin Lee

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做说话人日志、会议转录与说话人注册的研究者阅读。值得通读，重点看 §3 的任务定义与污染敏感评估协议、§4 的参考方法（跨会话聚类链与出席模式匹配、证据不足时弃权），以及合成到真实会议泛化差距的实验部分。

## 🌍 研究背景

说话人感知应用依赖注册语音，但为每位参会者单独采集不现实。会议档案中反复出现的参与者录音与预期出席名单可作替代来源。现有说话人日志只输出匿名聚类，无法与身份绑定；说话人注册研究多假设干净单说话人语音。本文要解决的是：如何用出席名单与日志聚类交叉比对，为多参与者自动获取可靠注册语音，并处理名单中有人未发言、发言者不在名单两类出席噪声。

## 💡 核心创新

1. 提出多参与者自动注册任务，显式建模两类出席噪声
2. 构建与内部会议语料校准的合成基准及污染敏感评估协议
3. 参考方法对跨会话聚类链与出席模式打分并在证据不足时弃权
4. 量化注册成功率与污染率的权衡，并揭示合成到真实的泛化差距

## 🏗️ 模型架构

输入为会议录音经说话人日志得到的匿名聚类，以及各会议的预期出席名单。方法先跨会话构建聚类链，将不同会议中的匿名聚类按说话人相似度串联；再对每条链与出席名单的出现模式做匹配打分，依据链在各会议中的出现与缺席是否与名单一致来累积证据；当证据不足时弃权，不输出注册语音。最终输出为被判定为某参与者的注册语音片段集合。摘要未给出网络结构与参数量。

## 📚 数据集

- 合成会议语料（训练/开发，按内部会议语料校准）
- 内部真实会议语料（评估，合成到真实泛化测试）

## 📊 实验结果

摘要未给出具体指标数值，仅以注册成功率与污染率的权衡曲线报告参考方法性能，并指出将合成开发集阈值原样用于真实会议时存在明显的合成到真实差距，该差距仍为开放问题。

## 🎯 结论与影响

最强结论是：出席名单与日志聚类链交叉比对可在存在出席噪声时提供可弃权的自动注册方案，但合成到真实迁移仍是瓶颈。该基准与评估协议有望推动会议场景说话人注册与日志联合研究，对会议转录、参会者身份绑定等落地有参考价值。

## ⚠️ 局限与未解决问题

仅提出一个参考方法，缺少与更多基线（如直接相似度匹配、聚类后处理）的对比；合成语料按内部语料校准，外部可复现性受限；未报告推理延迟与计算开销；污染敏感评估的阈值选择对结果影响大，消融不足。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-04/">← 返回 2026-11-04 速递</a></div>
