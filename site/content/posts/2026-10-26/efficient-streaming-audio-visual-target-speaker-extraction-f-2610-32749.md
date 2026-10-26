---
title: "Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes"
date: 2026-10-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出 RealSSA 真实场景音视频目标说话人提取基准与 Falcon 因果轻量方法，单次编解码多尺度分离，参数量降 91.9%。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#音视频融合</span> <span class="tag-pill tag-pill-soft">#流式推理</span> <span class="tag-pill tag-pill-soft">#轻量化模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.32749</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://cslikai.cn/Falcon/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">cslikai.cn/Falcon/</span></span></a><a class="oc-chip oc-chip-demo" href="https://cslikai.cn/Falcon/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">cslikai.cn/Falcon/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.32749" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.32749" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://cslikai.cn/Falcon/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://cslikai.cn/Falcon/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 RealSSA 真实场景音视频目标说话人提取基准与 Falcon 因果轻量方法，单次编解码多尺度分离，参数量降 91.9%。
</div>

## 👥 作者与机构

**Wendi Sang** ¹ · Kai Li · Yifan Li · Jianqiang Huang · Xiaolin Hu

**机构**：清华大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 AVTSE、流式语音分离与边缘部署的研究者与工程师阅读。建议通读：先看 §3 的 RealSSA 构建流程与近/远场干扰设置，再看 §4 Separator 的多尺度单次编解码结构与编码器空间对比损失，最后核对表 2/表 3 的效率对比与跨骨干迁移实验。

## 🌍 研究背景

AVTSE 在视频会议、助听器等低延迟场景需求明确，现有因果系统多基于 AV-TFGridNet 等重型架构，且标准基准（LRS2-2Mix、VoxCeleb2-2Mix）固定两人混合，缺少近场/远场干扰、混响与突发噪声。轻量方案靠反复调用小分离器回收容量，反而抵消了节省。本文要同时解决基准不真实与因果模型过重两个耦合问题。

## 💡 核心创新

1. 发布 RealSSA 基准，含 1–5 近场动态干扰与 10–15 远场干扰的可控仿真集及真实录制测试集
2. Falcon Separator 在单次编码器-解码器前向中完成多尺度时频分离
3. 编码器空间说话人对比损失，零推理开销抑制近场泄漏且可跨骨干迁移

## 🏗️ 模型架构

输入为混合语音的时频特征与目标说话人视觉线索（唇部视频），经视觉编码器提取说话人嵌入后与音频特征融合；Separator 采用单次编码器-解码器结构，在编码器输出的多尺度时频表示上并行做分离，避免反复调用小分离器；训练时在编码器空间施加说话人对比损失，拉近目标估计与目标嵌入、推远干扰说话人嵌入；解码器重建目标语音波形。全程因果卷积/因果注意力以保证流式，摘要未给具体参数量。

## 📚 数据集

- RealSSA-Sim（训练与评估，含 1–5 近场及 10–15 远场干扰说话人）
- RealSSA-Real（真实录制留出评估集）
- LRS2-2Mix（评估）
- LRS3-2Mix、VoxCeleb2-2Mix（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 参数量 | RealSSA-Sim | AV-TFGridNet（因果） | **Falcon** | -91.9% |
| 计算量 | RealSSA-Sim | AV-TFGridNet（因果） | **Falcon** | -20.2× |
| GPU 推理延迟 | RealSSA-Sim | AV-TFGridNet（因果） | **Falcon** | -11.1× |

摘要在 RealSSA-Sim、LRS2-2Mix、LRS3-2Mix、VoxCeleb2-2Mix 上均称达到 SOTA 提取质量，但未给出具体 SI-SDR 或 PESQ 数值；效率方面相对因果 AV-TFGridNet 参数量降 91.9%、计算降 20.2 倍、GPU 延迟降 11.1 倍。摘要未提供消融实验与 RealSSA-Real 上的量化结果。

## 🎯 结论与影响

最强结论是单次编解码多尺度分离加编码器空间对比损失，可在因果约束下同时取得 SOTA 质量与数量级效率优势。RealSSA 基准填补了多干扰、远场与真实录制的评测空白，有望成为后续流式 AVTSE 的标准测试床，并推动助听器、会议终端的边缘部署。

## ⚠️ 局限与未解决问题

摘要未给具体 SI-SDR/PESQ 数值与消融，对比损失与多尺度设计的独立贡献不明；RealSSA-Real 规模与说话人分布未说明，存在录制偏差风险；未报 CPU/端侧实测延迟与内存占用；与近期非因果强模型的差距未讨论。

## 🔗 开源资源

- **项目主页**：<https://cslikai.cn/Falcon/>
- **Demo / 试听**：<https://cslikai.cn/Falcon/>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-26/">← 返回 2026-10-26 速递</a></div>
