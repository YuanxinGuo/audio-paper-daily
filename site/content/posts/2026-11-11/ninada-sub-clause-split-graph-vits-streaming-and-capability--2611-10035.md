---
title: "Ninada: Sub-Clause Split-Graph VITS Streaming and Capability-Routed 24 kHz Speech Synthesis Across Twelve Scripts"
date: 2026-11-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "Ninada 将 VITS ONNX 按子句切分并流式执行，配合能力路由的 48 个检查点，在浏览器与移动端实现 24 kHz 多文字 TTS 低延迟合成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#模型压缩与部署</span> <span class="tag-pill tag-pill-soft">#流式推理</span> <span class="tag-pill tag-pill-soft">#多语言TTS</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.10035</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.10035" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.10035" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Ninada 将 VITS ONNX 按子句切分并流式执行，配合能力路由的 48 个检查点，在浏览器与移动端实现 24 kHz 多文字 TTS 低延迟合成。
</div>

## 👥 作者与机构

**Hemanth HM** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做端侧 TTS 部署、ONNX 推理优化、WebGPU/WASM 落地的工程读者。方法学新意有限但工程细节密集，建议重点看 §3 的 ONNX 内存切分与 12 帧 halo 流式机制、§4 的 iSTFTNet 蒸馏与 NOLA 双窗逆 STFT，以及表 2/表 3 的 TTFA 与 RTF 数据；纯算法研究者可略读。

## 🌍 研究背景

端到端 VITS 类 TTS 已能单次前向合成自然语音，但标准 ONNX 导出按整句/整子句执行，TTFA 被拖到数秒且激活内存峰值高。面向印度语系的多语言客户端部署还叠加四重瓶颈：每语言 138.8 MB float32 检查点撑爆浏览器缓存、移动 WebGPU 编译卷积 shader 卡顿 6-14 s 且慢于实时（1.44× RTF）、WASM pthread 在大小核 CPU 上屏障停顿、AudioWorklet 争用与 iOS WKWebView 限制导致丢帧或静音。本文要解决的是多脚本 24 kHz TTS 在浏览器与手机上的低延迟、低内存流式部署问题。

## 💡 核心创新

1. 单 ONNX 文件内存内 <15 ms 切分为 prior/flow/vocoder 子会话
2. 12 帧 halo + 升余弦交叉淡化的窗式 vocoder 流式
3. NOLA 双窗 ConvTranspose1d 逆 STFT，零复数运算降 MAC
4. 能力路由 48 检查点：HiFi-GAN v1 与蒸馏 c8c8_384 iSTFTNet 分工
5. 0.0 MB 零依赖 Klatt 兜底合成器

## 🏗️ 模型架构

输入为文本前端产出的音素/时长特征，主干沿用 VITS 结构：prior 编码器输出隐变量分布，flow 做可逆变换，vocoder 解码为 24 kHz 波形。部署时把单个 ONNX 文件在内存中切为 prior、flow、窗式 vocoder 三个子会话，vocoder 以 12 帧 halo 加升余弦交叉淡化流式拼接。桌面/WebGPU 路由到 24 个 HiFi-GAN v1 专家（27.9 MB，W8A32+FP16 ONNX），移动 WASM 路由到 24 个蒸馏 c8c8_384 iSTFTNet 专家（21.7 MB，NOLA 双窗 ConvTranspose1d 逆 STFT，vocoder MAC 减少 2.64×），另有零依赖 Klatt 兜底。

## 📚 数据集

- 480 条留出 24 kHz 录音室语音（评估）
- 24 声部蒸馏数据（训练 iSTFTNet 学生，规模未披露）
- Meta MMS 16 kHz 多语模型（对比基线）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MCD (0-8 kHz) | 480 条留出 24 kHz 语音 | Meta MMS 16 kHz 1,526.8 MB 5.17 dB | **3.22 dB（移动 iSTFTNet 3.09 dB；24 声部蒸馏 1.33 dB）** | -1.95 dB |
| 8-12 kHz 误差 | 480 条留出 24 kHz 语音 | 未给出 | **6.07 dB** | — |
| TTFA | 桌面 WebGPU | 整子句 ONNX 数秒级 | **89-155 ms** | 显著降低 |
| RTF / 启动延迟 | Google Pixel 10 Pro XL | WebGPU 1.44× RTF | **0.75-0.76× RTF，538-649 ms 零欠载启动** | -0.68× RTF |

摘要给出 MCD、高频误差、TTFA 与 RTF 四类指标：0-8 kHz MCD 3.22 dB 优于 16 kHz MMS 的 5.17 dB，移动 iSTFTNet 3.09 dB，24 声部蒸馏达 1.33 dB；8-12 kHz 误差 6.07 dB。桌面 WebGPU 可听启动 89-155 ms，Pixel 10 Pro XL 上 0.75-0.76× RTF 且 538-649 ms 零欠载。未报告主观 MOS、说话人相似度与消融实验。

## 🎯 结论与影响

最强结论是：通过 ONNX 内存切分流式化与能力路由的多检查点策略，24 kHz 多脚本 TTS 可在浏览器与手机上做到亚秒级启动并实时运行。这为端侧 TTS 部署提供了可复用的工程范式，对低资源语种与隐私敏感场景的浏览器内合成有直接落地价值。

## ⚠️ 局限与未解决问题

缺少主观 MOS/CMOS 与说话人相似度评估，客观指标仅 MCD 与高频误差；未给出各模块消融（切分、halo、蒸馏各自贡献）；对比基线仅 MMS 一个，未与主流开源 TTS 比较；48 检查点带来的总体积与路由开销未量化；测试设备单一。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-11/">← 返回 2026-11-11 速递</a></div>
