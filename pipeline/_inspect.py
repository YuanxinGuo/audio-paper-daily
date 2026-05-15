"""Quick DB inspection."""
from collections import Counter
from db import connect

with connect() as c:
    rows = list(c.execute(
        "SELECT main_task FROM papers "
        "WHERE date(fetch_date)='2026-05-15' AND analyzed_at IS NOT NULL"
    ))
    print(f"total today: {len(rows)}")
    cnt = Counter(r[0] for r in rows)
    for t, n in cnt.most_common():
        print(f"  {n:3d}  {t}")

    print()
    print("--- focus tag hits today ---")
    FOCUS = ('#语音增强', '#目标说话人提取', '#语音分离',
             '#双耳音频', '#乐器分离')
    for f in FOCUS:
        n = cnt.get(f, 0)
        mark = "✓" if n else "—"
        print(f"  {mark}  {f}: {n}")
