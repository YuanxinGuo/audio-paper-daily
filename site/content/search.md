---
title: "搜索"
url: "/search/"
hidemeta: true
ShowToc: false
ShowBreadCrumbs: false
---

<link href="/audio-paper-daily/pagefind/pagefind-ui.css" rel="stylesheet">
<div id="search"></div>
<script src="/audio-paper-daily/pagefind/pagefind-ui.js"></script>
<script>
  window.addEventListener('DOMContentLoaded', () => {
    new PagefindUI({
      element: "#search",
      showImages: false,
      showSubResults: true,
      resetStyles: false,
      translations: {
        placeholder: "搜索论文标题、标签、正文……",
        clear_search: "清空",
        load_more: "加载更多",
        search_label: "搜索本站",
        filters_label: "筛选",
        zero_results: "没有找到与 [SEARCH_TERM] 相关的结果",
        many_results: "找到 [COUNT] 条 [SEARCH_TERM] 的结果",
        one_result: "找到 1 条 [SEARCH_TERM] 的结果",
        searching: "正在搜索 [SEARCH_TERM]…"
      }
    });
  });
</script>

<style>
  /* Make Pagefind UI follow our gradient theme */
  .pagefind-ui {
    --pagefind-ui-primary: var(--grad-mid);
    --pagefind-ui-text:    var(--primary);
    --pagefind-ui-background: var(--entry);
    --pagefind-ui-border: var(--border);
    --pagefind-ui-tag: var(--code-bg);
    --pagefind-ui-border-radius: 12px;
    --pagefind-ui-border-width: 1px;
    --pagefind-ui-font: inherit;
    --pagefind-ui-image-side-length: 0;
    margin: 1rem 0;
  }
  .pagefind-ui__search-input {
    font-size: 1.05rem !important;
    padding: 0.85rem 1rem !important;
  }
  .pagefind-ui__result {
    border-radius: 10px;
    padding: 0.9rem 1rem !important;
    transition: all 0.2s ease;
  }
  .pagefind-ui__result:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 14px rgba(99,102,241,0.10);
  }
  .pagefind-ui__result-title a {
    color: var(--primary) !important;
  }
  .pagefind-ui__result-title a:hover {
    background: linear-gradient(90deg, var(--grad-start), var(--grad-end));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent !important;
  }
</style>
