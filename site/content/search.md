---
title: "搜索"
url: "/search/"
hidemeta: true
ShowToc: false
ShowBreadCrumbs: false
---

<link href="https://cdn.jsdelivr.net/npm/@pagefind/default-ui@1/css/ui.css" rel="stylesheet">
<div id="search"></div>
<script src="https://cdn.jsdelivr.net/npm/@pagefind/default-ui@1/npm/dist/coupled_search.min.js"></script>
<script>
  window.addEventListener('DOMContentLoaded', () => {
    new PagefindUI({ element: "#search", showImages: false, translations: { placeholder: "搜索论文标题、标签、内容..." } });
  });
</script>
