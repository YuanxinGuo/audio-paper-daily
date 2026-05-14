# 语音/音频论文速递 (audio-paper-daily)

每日自动抓取 [arxiv](https://arxiv.org/) (eess.AS / cs.SD) 与 [HuggingFace Daily Papers](https://huggingface.co/papers) 上最新的语音/音频 AI 论文，调用 **DeepSeek** 大模型自动分析、打分、生成中文摘要，最终发布为静态网站。

🌐 在线访问：<https://YuanxinGuo.github.io/audio-paper-daily/>

## 工作原理

```
GitHub Actions (每日 09:00 北京时间)
        │
        ├── fetch_arxiv.py     抓取 arxiv eess.AS / cs.SD
        ├── fetch_hf.py        抓取 HF Daily Papers (按关键词过滤)
        ├── analyze.py         DeepSeek 深度分析、JSON 结构化输出
        ├── render.py          生成当日 Hugo markdown
        └── rankings.py        每周一/每月 1 日聚合榜单
                │
                ▼
          hugo build → Pagefind 索引 → GitHub Pages
```

整个流程跑在 GitHub 服务器上，**无需保持本地电脑开机**。

## 本地开发

```bash
# 安装依赖
pip install -r pipeline/requirements.txt

# 设置 API key
$env:DEEPSEEK_API_KEY = "sk-..."   # PowerShell

# 跑一遍管道
cd pipeline
python run_all.py

# 本地预览站点
cd ../site
git clone --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
hugo server
```

## 部署到 GitHub Pages

1. 在仓库 `Settings → Secrets and variables → Actions` 添加 secret：
   - `DEEPSEEK_API_KEY`
2. `Settings → Pages → Source` 选择 **GitHub Actions**。
3. 第一次手动触发 workflow：`Actions → Daily Paper Digest → Run workflow`。

## 目录结构

```
.
├── .github/workflows/daily.yml   # GitHub Actions
├── pipeline/                     # Python 数据管道
│   ├── fetch_arxiv.py
│   ├── fetch_hf.py
│   ├── analyze.py                # DeepSeek 调用
│   ├── render.py                 # Hugo MD 渲染
│   ├── rankings.py               # 周/月榜
│   ├── db.py                     # SQLite 索引
│   └── prompts/analyze.txt       # LLM 提示词
├── data/papers.sqlite            # 持久化论文索引（被 git 跟踪）
└── site/                         # Hugo 站点
    ├── config.toml
    └── content/
```

## 自定义

- **更换主题**：修改 `site/config.toml` 的 `theme` 与 `daily.yml` 里的克隆命令
- **修改评分提示词**：编辑 `pipeline/prompts/analyze.txt`
- **更换 LLM**：修改 `pipeline/config.py` 与 `pipeline/analyze.py`（OpenAI 兼容接口）
- **调整运行频率**：修改 `daily.yml` 的 `cron` 表达式

## License

MIT
