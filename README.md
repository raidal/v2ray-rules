# 🚀 v2ray-rules — 多功能 Xray/v2ray 路由规则集

一个为 **Xray / v2rayN / Clash Meta** 设计的 **模块化、多功能、可自动更新** 的路由规则仓库。

本项目适合需要 **精细分流、自动更新、可扩展、可维护** 的用户，尤其适合多场景使用者（游戏、流媒体、AI、Telegram、国内优化等）。

---

## ✨ 功能特性

### 🔹 多功能分流（模块化）
- 🇨🇳 **国内直连**
- 🌍 **绕过大陆（GFWList）**
- 🎮 **游戏直连（Steam / EPIC / Riot / 国服）**
- 📺 **流媒体分流（Netflix / Disney+ / YouTube / B站港澳台）**
- 🤖 **AI 分流（OpenAI / Claude / Gemini）**
- 📱 **Telegram 专线**
- 🚀 **国内 CDN 优化**
- 🛰️ **GEOIP 精细化（HK/SG/JP → proxy）**

### 🔹 自动更新
- 自动同步最新 **geosite.dat / geoip.dat**
- 自动合并所有模块生成 `full.json`
- GitHub Actions 每 12 小时自动运行

### 🔹 完全模块化
你可以按需启用或禁用任意模块，规则清晰易维护。

---

## 📁 目录结构