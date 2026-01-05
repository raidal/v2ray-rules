import json
import os

base_path = "rules"
modules = [
    "base.json",
    "cn-direct.json",
    "gfw-proxy.json",
    "game-direct.json",
    "media.json",
    "ai.json",
    "telegram.json",
    "cdn-opt.json",
    "geo-precision.json"
]

merged = {"domainStrategy": "IPIfNonMatch", "rules": []}

for m in modules:
    with open(os.path.join(base_path, m), "r", encoding="utf-8") as f:
        data = json.load(f)
        if "rules" in data:
            merged["rules"].extend(data["rules"])

with open(os.path.join(base_path, "full.json"), "w", encoding="utf-8") as f:
    json.dump(merged, f, indent=2, ensure_ascii=False)

print("full.json 已生成")