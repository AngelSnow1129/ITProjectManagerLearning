# 🎓 信息系统项目管理师学习平台

> 专业的软考高级资格考试学习系统 - 完整、高效、易用

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Web-green.svg)](https://github.com)
[![Status](https://img.shields.io/badge/status-Active-success.svg)](https://github.com)

## 📚 项目简介

这是一个功能完整的静态网站学习平台，专为**信息系统项目管理师**考试打造。提供完整的25个章节内容、精心整理的重点提纲和核心必背内容，帮助您高效备考软考高级资格。

### ✨ 核心特性

- 🎯 **三种学习模式**: 完整章节、重点提纲、必背内容
- 📚 **25个完整章节**: 覆盖信息系统项目管理师全部考点
- 📱 **完美响应式**: 支持手机、平板、电脑多端学习
- 🚀 **零配置启动**: 双击即用，无需安装任何软件
- 🔍 **智能搜索**: 快速定位章节内容
- 📥 **打印下载**: 支持打印和下载Markdown格式

## 🚀 快速开始

### 方法1：使用启动脚本（推荐）

**Windows:**
```bash
双击 start_server.bat
```

**Linux/Mac:**
```bash
chmod +x start_server.sh
./start_server.sh
```

脚本会自动启动服务器并打开浏览器访问 `http://localhost:8000/web/`

### 方法2：手动启动服务器

```bash
python -m http.server 8000
# 然后访问 http://localhost:8000/web/
```

### 方法3：直接打开

双击 `web/index.html` 文件开始学习

## 📖 内容结构

### 学习资源
- **完整章节**: 25个（第01-24章 + 前言目录）
- **重点提纲**: 25个章节提纲
- **必背内容**: 9个核心章节
- **辅助文档**: 必背索引、公式速查表、快速查询索引、学习进度跟踪表

### 章节结构
1. **信息化基础**（01-05章）：信息化发展、信息技术、信息系统治理与管理、信息系统工程
2. **项目管理核心**（06-18章）：项目管理概论、十大知识领域、项目绩效域
3. **高级管理**（19-24章）：配置管理、高级项目管理、组织治理、法律法规

## 📁 项目结构

```
.
├── web/                    # 网页文件目录
│   ├── index.html          # 主页入口
│   ├── chapters.html       # 章节学习页面
│   ├── viewer.html         # 文档查看器
│   └── config.js           # 章节配置
├── md/                     # Markdown学习内容
│   ├── 基础知识/           # 25个章节完整内容
│   ├── 案例分析/           # 案例分析资料
│   └── 搜集资料/           # 补充学习资料
├── keypoint/               # 重点提纲和必背内容
├── docs/                   # 项目文档
├── start_server.bat        # Windows启动脚本
├── start_server.sh         # Linux/Mac启动脚本
└── README.md               # 项目说明
```

## 🎯 学习路径

### 第一阶段：系统学习（1-2个月）
使用"完整章节"模式，按顺序学习每个章节

### 第二阶段：强化复习（2-3周）
使用"重点提纲"模式，重点复习核心知识点

### 第三阶段：考前冲刺（1周）
使用"必背内容"模式，快速过一遍所有公式和概念

## 📦 部署

支持多种静态网站托管平台：
- **Cloudflare Pages**（推荐）
- GitHub Pages
- Netlify
- Vercel

### 🚨 Cloudflare Pages 部署重要提示

**如果遇到部署错误**：
```
✘ [ERROR] It looks like you've run a Workers-specific command in a Pages project.
```

**必须在 Cloudflare Dashboard 中修改设置**：
1. 进入项目 Settings → Builds & deployments
2. **清空 Build command**（不要填写任何命令）
3. 设置 Build output directory 为 `/`
4. 保存并重新部署

📖 **详细修复步骤**：[DEPLOYMENT_FIX.md](DEPLOYMENT_FIX.md) ⭐ 必读！

### 快速部署

**Cloudflare Pages（推荐）**：
1. 连接 GitHub 仓库
2. 配置构建设置：
   - Build command: **留空**（关键！）
   - Build output directory: `/`
3. 保存并部署

📖 **完整教程**：[Cloudflare Pages 部署指南](docs/Cloudflare_Pages部署指南.md)

## 🔧 技术栈

- **前端**: HTML5 + CSS3 + JavaScript ES6+
- **Markdown解析**: Marked.js
- **样式**: GitHub Markdown CSS
- **架构**: 纯静态网站，无需后端

## 📞 文档

- [快速开始](docs/快速开始.md)
- [使用演示](docs/使用演示.md)
- [问题排查指南](docs/问题排查指南.md)
- [项目结构说明](docs/项目结构说明.md)
- [考试说明](docs/信息系统项目管理师考试说明.md)

## 📄 许可证

本项目采用 MIT 许可证，仅供学习使用。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

**祝您考试顺利！通过信息系统项目管理师考试！** 🎓💪
