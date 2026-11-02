---
title: "ARPEGE: Dataset and Methods to Estimate Acoustic and Geometric Parameters of Rooms from Sound"
date: 2026-11-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#房间冲激响应生成"]
summary: "发布ARPEGE数据集：6个空房间、数百条Ambisonic球阵RIR，标注声源/麦克风/反射面几何，并演示镜像源定位与盲房间参数估计两个基线。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#房间冲激响应生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声学模拟</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#盲房间参数估计</span> <span class="tag-pill tag-pill-soft">#声源定位</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.41543</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.41543" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.41543" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布ARPEGE数据集：6个空房间、数百条Ambisonic球阵RIR，标注声源/麦克风/反射面几何，并演示镜像源定位与盲房间参数估计两个基线。
</div>

## 👥 作者与机构

Jean-Daniel Pascal Prieto (UMRAE · MACARON) · Prerak Srivastava (UMRAE) · C\'edric Foy (UMRAE) · Antoine Deleforge (MACARON)

**机构**：UMRAE · MACARON

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做RIR仿真、房间声学反演、盲房间参数估计与声场重建的研究者。值得通读数据采集与标注协议部分（§2-§3），重点看表1的房间/材料统计与§4两个基线实验设置；若关注下游语音增强/去混响，可只看数据集描述与重仿真代码接口。

## 🌍 研究背景

从RIR反推房间几何与声学参数（混响时间、材料吸收系数）是声学反问题，此前工作多依赖仿真RIR（如image source method合成数据）或少量实测数据，缺乏带完整几何标注、多房间多材料的公开实测集。仿真数据与真实房间的域差异导致盲估计方法泛化差，而实测数据又常缺反射面位置标注，难以监督几何反演。本文要解决的是提供一套带声源、麦克风与全部反射面相对位置标注的Ambisonic球阵RIR实测数据集，并给出可复现的基线。

## 💡 核心创新

1. 6个空房间、数百条Ambisonic球阵RIR实测，含人声与拍手激励
2. 标注声源、麦克风及全部声学反射面的相对几何位置
3. 覆盖多房间尺寸、表面材料、朝向与距离的受控采集
4. 提供RIR重仿真初始代码，指向数字孪生目标

## 🏗️ 模型架构

数据采集侧：Ambisonic球形麦克风阵列在6个空房间内录制RIR，激励包括扬声器播放信号、人声与拍手；每条记录配以声源、阵列与各反射面的相对位置标注，形成几何-声学配对。方法侧演示两个基线：一是基于image source模型的声源/反射面定位方法，从RIR中估计镜像源位置；二是盲房间参数估计方法，从RIR估计混响时间与材料吸收等参数。另提供基于标注几何重仿真RIR的初始代码，用于与实测对比。摘要未给出网络结构与参数量。

## 📚 数据集

- ARPEGE（自建，6个空房间、数百条Ambisonic球阵RIR，含人声与拍手，用于训练/评估基线）

## 📊 实验结果

摘要仅说明在两个任务上演示了现有SOTA方法（image source定位与盲房间参数估计），未给出SI-SDR、PESQ、定位误差或混响时间估计误差等具体数值，也未报告与基线的定量对比。因此无法从摘要判断方法在该数据上的精度水平，需查阅正文实验表。

## 🎯 结论与影响

最强结论是提供了带完整几何标注的多房间Ambisonic RIR实测集，可作为盲房间参数估计与几何反演的统一评测基准。对后续研究的潜在影响在于推动实测数据替代纯仿真训练、并支撑RIR重仿真与数字孪生方向。工业上可用于房间声学测量、虚拟/空间音频渲染与去混响系统的真实场景验证。

## ⚠️ 局限与未解决问题

仅6个空房间，且全为空场无家具与人员，与真实使用场景存在偏差；摘要未给出基线定量结果与误差分析，难以评估数据难度；未报告采集信噪比、阵列校准误差等元信息；重仿真代码仅为初始版本，数字孪生目标尚未验证。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-02/">← 返回 2026-11-02 速递</a></div>
