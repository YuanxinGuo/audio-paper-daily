---
title: "Streaming Speech Recognition on a Microcontroller: a 65.7M-Parameter Transducer in 2 and 4 Bits on the ESP32-P4"
date: 2026-10-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "在无神经网络加速器的ESP32-P4上以2/4比特量化运行65.7M参数Zipformer2流式语音识别，LibriSpeech test-clean WER 4.34%。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#模型量化</span> <span class="tag-pill tag-pill-soft">#边缘部署</span> <span class="tag-pill tag-pill-soft">#Zipformer</span> <span class="tag-pill tag-pill-soft">#GPTQ</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.38739</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/BoumedineBillal/esp32-pie-asr" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">BoumedineBillal/esp32-pie-asr</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.38739" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.38739" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/BoumedineBillal/esp32-pie-asr" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在无神经网络加速器的ESP32-P4上以2/4比特量化运行65.7M参数Zipformer2流式语音识别，LibriSpeech test-clean WER 4.34%。
</div>

## 👥 作者与机构

**Billal Boumedine** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做端侧ASR部署、模型量化与嵌入式推理的工程/研究读者。值得通读，重点看§3的Hadamard旋转分组量化与GPTQ流程、§4的PIE内核实现，以及test-clean上的GPTQ消融表；若只关心精度损失来源，可直接看GPU模拟器对比实验。

## 🌍 研究背景

端侧流式ASR此前多依赖带NPU的SoC或高端MCU，纯RISC-V微控制器上运行数十M参数transducer缺乏可行方案。已有工作多采用int8量化加定点推理，但int8权重仍达71MB，超出ESP32-P4的32MB PSRAM预算；更低比特量化在无训练条件下通常带来显著WER退化。本文要在无神经加速器、无重训练的前提下，把Kroko Zipformer2 transducer压到26.65MB并保持可用精度。

## 💡 核心创新

1. 按矩阵敏感度分配2/4比特宽度，Hadamard旋转分组量化
2. 量化前对每个矩阵做输出校正，再用GPTQ与组范数搜索
3. 手写PIE SIMD内核的C推理引擎，双核并行含beam search
4. PC构建与芯片逐比特一致，便于整测试集评测

## 🏗️ 模型架构

输入为1.28s音频块的声学特征，主干为65.7M参数流式Zipformer2 transducer（编码器+预测网络+联合网络）。编码器290个权重矩阵在Hadamard旋转后的分组内以2或4比特存储，位宽由实测敏感度决定，量化前先向原模型输出校正，再经GPTQ与组范数搜索取整。矩阵间激活为int16、进入矩阵乘为int8。C引擎用手写PIE 128位SIMD内核在双400MHz RISC-V核上执行，含beam search，PC构建与芯片位一致。

## 📚 数据集

- LibriSpeech（评估，test-clean/test-other）
- FLEURS（评估）
- Common Voice（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LibriSpeech test-clean | 原始发布模型 3.94% | **4.34%** | +0.40% |
| WER | LibriSpeech test-other | 原始发布模型 9.17% | **10.26%** | +1.09% |
| WER 差距 | FLEURS | 原始发布模型 | **本文量化模型** | +2.3 点 |
| WER 差距 | Common Voice | 原始发布模型 | **本文量化模型** | +1.1 点 |

每1.28s音频块在双核上耗时0.90s（含beam search），满足实时。GPU模拟器显示整数运算本身不引入损失，全部精度差距来自权重量化；test-clean全量消融表明GPTQ贡献主要增益。作者还给出编码器单块耗时从51.3s降到0.62s的优化历程，以及尝试压到16MB但停在19.63MB的失败记录。未测能耗。

## 🎯 结论与影响

最强结论是在无NPU的RISC-V微控制器上以2/4比特权重实现可用的流式transducer ASR，且精度损失可归因于权重量化而非整数运算。这为极低资源端侧ASR提供了可复现的量化+内核协同设计范式，对嵌入式语音产品落地有直接参考价值。

## ⚠️ 局限与未解决问题

仅英文、单一模型Kroko，未与其他低比特量化方法（如SmoothQuant、AWQ）对比；未测能耗与内存峰值；FLEURS/Common Voice仅报差距未给绝对值；16MB目标未达成；缺少对不同比特分配策略的细粒度消融。

## 🔗 开源资源

- **代码**：<https://github.com/BoumedineBillal/esp32-pie-asr>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-10-30/">← 返回 2026-10-30 速递</a></div>
