# 🎓 信息系统项目管理师学习平台

> 专业的软考高级资格考试学习系统 - 完整、高效、易用

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Web-green.svg)](https://github.com)
[![Status](https://img.shields.io/badge/status-Active-success.svg)](https://github.com)
[![Version](https://img.shields.io/badge/version-2.0.0-brightgreen.svg)](https://github.com)

## 📚 项目简介

这是一个功能完整的静态网站学习平台，专为**信息系统项目管理师**考试打造。提供完整的25个章节内容、精心整理的重点提纲和核心必背内容，帮助您高效备考软考高级资格。

> 📊 [查看项目状态](PROJECT_STATUS.md) | 📝 [查看更新日志](CHANGELOG.md) | 📚 [查看所有文档](docs/)

### ✨ 核心特性

- 🎯 **三种学习模式**: 完整章节、重点提纲、必背内容
- 📚 **25个完整章节**: 覆盖信息系统项目管理师全部考点
- 📱 **完美响应式**: 支持手机、平板、电脑多端学习
- 🚀 **零配置启动**: 双击即用，无需安装任何软件
- 🔍 **智能搜索**: 快速定位章节内容
- 📥 **打印下载**: 支持打印和下载Markdown格式
- 🎨 **精美设计**: 现代化UI，流畅动画效果
- 📊 **学习跟踪**: 内置学习进度跟踪表

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

### 方法3：直接打开（最简单）

1. 双击 `web/index.html` 文件
2. 开始学习

**注意：** 某些浏览器可能有跨域限制，建议使用方法1或方法2

## 📖 功能说明

### 主要页面

| 页面 | 功能 | 访问方式 |
|------|------|----------|
| 主页 | 平台介绍和功能入口 | `web/index.html` |
| 章节学习 | 三种学习模式 | `web/chapters.html` |
| 快速导航 | 所有功能快速访问 | `web/nav.html` |
| 文档查看器 | 查看索引和速查表 | `web/viewer.html` |

### 学习模式

#### 📖 完整章节
- 查看完整的教材内容
- 适合系统学习和深入理解
- 25个章节，覆盖所有考点
- 包含信息化发展、项目管理、案例分析、论文写作等

#### ⭐ 重点提纲
- 精心整理的重难点知识
- 包含详细的公式、方法和案例
- 25个章节的重点提纲
- 重点标注5星章节

#### 🎯 必背内容
- 核心公式、概念、方法论
- 快速查询和考前突击
- 9个重点章节的必背内容
- 包含项目管理十大知识领域核心内容

## 📊 内容统计

### 学习资源
- **完整章节**: 25个（01-25章）
- **重点提纲**: 25个章节提纲
- **必背内容**: 9个核心章节
- **辅助文档**: 必背索引、公式速查表、快速查询索引、学习进度跟踪表

### 章节结构
1. **信息化基础**（01-05章）：信息化发展、信息技术、信息系统治理与管理、信息系统工程
2. **项目管理核心**（06-18章）：项目管理概论、十大知识领域、项目绩效域
3. **高级管理**（19-23章）：配置管理、高级项目管理、组织治理、法律法规
4. **实战应用**（24-25章）：案例分析、论文写作

### 重点章节（5星）⭐⭐⭐⭐⭐
1. **06_项目管理概论** - 项目管理基础理论
2. **08_项目整合管理** - 项目整体管理核心
3. **09_项目范围管理** - WBS与需求管理
4. **10_项目进度管理** - 网络图与关键路径
5. **11_项目成本管理** - EVM挣值管理
6. **12_项目质量管理** - 质量管理体系
7. **15_项目风险管理** - 风险识别与应对
8. **24_项目管理案例分析** - 案例分析技巧
9. **25_论文写作指导** - 论文写作方法

## 🎯 学习路径

### 第一阶段：系统学习（1-2个月）
1. 使用"完整章节"模式
2. 按顺序学习每个章节
3. 重点关注5星章节
4. 做笔记和练习题

### 第二阶段：强化复习（2-3周）
1. 使用"重点提纲"模式
2. 重点复习每章的核心知识点
3. 做大量练习题
4. 整理错题和难点

### 第三阶段：考前冲刺（1周）
1. 使用"必背内容"模式
2. 快速过一遍所有公式和概念
3. 查漏补缺
4. 模拟考试

## 💡 使用技巧

### 快速定位
- 使用搜索框快速查找章节
- 收藏常用章节（浏览器书签）
- 使用URL参数直接访问：
  ```
  chapters.html?type=projectmanager&view=keypoint&chapter=10
  ```

### 高效学习
- 先看重点提纲，了解框架
- 再看完整章节，深入理解
- 最后看必背内容，强化记忆

### 移动学习
- 手机访问时点击左上角"☰"打开目录
- 支持离线使用（下载整个文件夹）
- 可以添加到主屏幕

## 📁 项目结构

```
.
├── web/                           # 网页文件目录
│   ├── index.html                 # 主页入口
│   ├── chapters.html              # 章节学习页面（核心功能）
│   ├── viewer.html                # 文档查看器
│   ├── nav.html                   # 快速导航
│   ├── config.js                  # 章节配置文件
│   └── marked-fallback.js         # Markdown解析备用方案
│
├── start_server.bat               # Windows启动脚本
├── start_server.sh                # Linux/Mac启动脚本
│
├── 01-25_*.md                     # 25个完整章节文件
│
├── keypoint/                      # 重点提纲和必背内容
│   ├── 01-25_*_知识提纲.md        # 25个章节重点提纲
│   ├── *_必背补充.md              # 9个核心章节必背内容
│   ├── 📌必背内容总索引.md        # 必背内容总索引
│   ├── 常用公式速查表.md          # 常用公式快速查询
│   ├── 快速查询索引.md            # 知识点快速索引
│   └── 学习进度跟踪表.md          # 学习进度管理
│
├── images/                        # 图片资源目录
│   └── 01-25_*/                   # 各章节配图
│
├── docs/                          # 文档目录
│   ├── 快速开始.md
│   ├── 使用演示.md
│   ├── 问题排查指南.md
│   ├── 项目结构说明.md
│   └── Cloudflare_Pages部署指南.md
│
├── README.md                      # 项目说明文档
├── CHANGELOG.md                   # 更新日志
├── DEPLOYMENT_CHECKLIST.md        # 部署检查清单
├── LICENSE                        # 开源协议
├── wrangler.toml                  # Cloudflare配置
├── _headers                       # HTTP头配置
└── _redirects                     # 重定向规则
```

## 🔧 技术栈

- **前端框架**: 纯HTML5 + CSS3 + JavaScript ES6+
- **布局技术**: Flexbox、Grid响应式布局
- **Markdown解析**: Marked.js v9.1.6
- **样式库**: GitHub Markdown CSS v5.2.0
- **特效**: CSS3渐变、动画、过渡效果
- **架构**: 静态网站，无需后端服务器
- **部署**: 支持Cloudflare Pages、GitHub Pages、Netlify等

## 🐛 常见问题

### Q1: 页面显示空白或加载失败？
**A:** 可能是跨域问题，请使用启动脚本运行本地服务器，或部署到Web服务器。

### Q2: 图片无法显示？
**A:** 确保 `images` 文件夹在项目根目录下，且图片路径正确。

### Q3: Markdown格式显示异常？
**A:** 确保网络连接正常，页面需要从CDN加载Marked.js和GitHub Markdown CSS。

### Q4: 某些章节提示"暂无内容"？
**A:** 该章节的对应视图内容尚未整理，请切换到"完整章节"模式查看。

### Q5: 如何离线使用？
**A:** 下载整个项目文件夹，使用启动脚本运行本地服务器即可离线使用。

### Q6: 支持哪些浏览器？
**A:** 支持Chrome、Firefox、Safari、Edge等现代浏览器，建议使用最新版本。

更多问题请查看 [docs/问题排查指南.md](docs/问题排查指南.md)

## 📦 部署

### Cloudflare Pages（推荐）⚡

Cloudflare Pages 提供免费、快速、全球CDN加速的静态网站托管服务。

#### 方式1：通过 Git 集成（推荐）

1. **准备工作**
   - 注册 [Cloudflare 账号](https://dash.cloudflare.com/sign-up)
   - 将项目推送到 GitHub/GitLab

2. **创建 Pages 项目**
   ```
   登录 Cloudflare Dashboard
   → 左侧菜单选择 "Workers & Pages"
   → 点击 "Create application"
   → 选择 "Pages" 标签
   → 点击 "Connect to Git"
   ```

3. **连接仓库**
   - 授权 Cloudflare 访问你的 Git 仓库
   - 选择本项目仓库
   - 点击 "Begin setup"

4. **配置构建设置**
   ```
   Project name: 信息系统项目管理师学习平台（或自定义）
   Production branch: main
   Build command: （留空）
   Build output directory: /
   Root directory: /
   ```

5. **环境变量**（可选）
   - 无需配置，本项目为纯静态网站

6. **部署**
   - 点击 "Save and Deploy"
   - 等待部署完成（通常1-2分钟）
   - 获得访问链接：`https://your-project.pages.dev`

7. **自定义域名**（可选）
   ```
   进入项目设置
   → "Custom domains"
   → "Set up a custom domain"
   → 输入域名并按提示配置DNS
   ```

#### 方式2：通过 Wrangler CLI

1. **安装 Wrangler**
   ```bash
   npm install -g wrangler
   # 或
   yarn global add wrangler
   ```

2. **登录 Cloudflare**
   ```bash
   wrangler login
   ```

3. **部署项目**
   ```bash
   # 在项目根目录执行
   wrangler pages deploy . --project-name=projectmanager-learning
   ```

4. **后续更新**
   ```bash
   wrangler pages deploy .
   ```

#### 方式3：直接上传（最简单）

1. **打包项目**
   - 将整个项目文件夹压缩为 ZIP
   - 或直接准备项目文件夹

2. **上传部署**
   ```
   登录 Cloudflare Dashboard
   → Workers & Pages
   → Create application
   → Pages 标签
   → Upload assets
   → 拖拽文件夹或选择 ZIP 文件
   → 点击 "Deploy site"
   ```

3. **完成**
   - 部署完成后获得访问链接
   - 支持拖拽更新

#### 配置优化建议

1. **创建 `_headers` 文件**（可选）
   ```
   /*
     X-Frame-Options: DENY
     X-Content-Type-Options: nosniff
     X-XSS-Protection: 1; mode=block
     Referrer-Policy: strict-origin-when-cross-origin
   
   /*.html
     Cache-Control: public, max-age=3600
   
   /*.md
     Cache-Control: public, max-age=3600
   
   /*.js
     Cache-Control: public, max-age=31536000, immutable
   
   /*.css
     Cache-Control: public, max-age=31536000, immutable
   
   /images/*
     Cache-Control: public, max-age=31536000, immutable
   ```

2. **创建 `_redirects` 文件**（可选）
   ```
   # 重定向根目录到 web 目录
   /  /web/index.html  200
   
   # 404 页面
   /* /web/index.html  404
   ```

3. **创建 `wrangler.toml` 配置**（可选）
   ```toml
   name = "projectmanager-learning"
   compatibility_date = "2024-01-01"
   
   [site]
   bucket = "."
   ```

#### 部署后优化

1. **性能优化**
   - ✅ 自动全球 CDN 加速
   - ✅ 自动 HTTPS
   - ✅ HTTP/2 和 HTTP/3 支持
   - ✅ 自动图片优化（可选）

2. **访问分析**
   ```
   项目设置 → Analytics
   查看访问量、流量、性能指标
   ```

3. **自动部署**
   - 推送到 Git 仓库自动触发部署
   - 支持预览部署（Pull Request）
   - 支持回滚到历史版本

#### 常见问题

**Q: 部署后页面空白？**
A: 检查 `Build output directory` 是否设置为 `/`，确保 `web/index.html` 可访问。

**Q: 如何设置默认首页？**
A: 使用 `_redirects` 文件将根路径重定向到 `/web/index.html`。

**Q: 如何更新网站？**
A: 
- Git 集成：推送代码到仓库自动部署
- 直接上传：重新上传文件覆盖
- CLI：运行 `wrangler pages deploy .`

**Q: 免费版有什么限制？**
A: 
- ✅ 无限请求
- ✅ 无限带宽
- ✅ 500 次构建/月
- ✅ 100 个自定义域名

**Q: 如何查看部署日志？**
A: 项目页面 → Deployments → 点击具体部署查看详情

#### 访问地址

部署成功后，你的网站将可通过以下地址访问：
- 默认域名：`https://your-project.pages.dev`
- 自定义域名：`https://your-domain.com`（需配置）

#### 推荐配置

```bash
# 项目根目录结构
.
├── web/              # 网站文件
├── keypoint/         # 学习资料
├── images/           # 图片资源
├── _headers          # HTTP 头配置
├── _redirects        # 重定向规则
└── wrangler.toml     # Wrangler 配置
```

---

### GitHub Pages

1. **启用 GitHub Pages**
   ```
   仓库 Settings
   → Pages
   → Source: Deploy from a branch
   → Branch: main, /root
   → Save
   ```

2. **访问网站**
   - `https://username.github.io/repository-name/web/`

3. **自定义域名**（可选）
   - 在 Pages 设置中添加自定义域名
   - 配置 DNS CNAME 记录

### Netlify

1. **连接仓库**
   - 登录 [Netlify](https://netlify.com)
   - New site from Git
   - 选择仓库

2. **构建设置**
   ```
   Build command: （留空）
   Publish directory: /
   ```

3. **部署**
   - 自动部署
   - 获取访问链接

### Vercel

1. **导入项目**
   - 登录 [Vercel](https://vercel.com)
   - Import Project
   - 选择仓库

2. **配置**
   ```
   Framework Preset: Other
   Root Directory: ./
   Output Directory: ./
   ```

3. **部署**
   - 自动部署
   - 获取访问链接

---

### 部署对比

| 平台 | 速度 | CDN | 免费额度 | 推荐度 |
|------|------|-----|----------|--------|
| **Cloudflare Pages** | ⚡⚡⚡ | 全球 | 无限 | ⭐⭐⭐⭐⭐ |
| GitHub Pages | ⚡⚡ | 有限 | 100GB/月 | ⭐⭐⭐⭐ |
| Netlify | ⚡⚡⚡ | 全球 | 100GB/月 | ⭐⭐⭐⭐ |
| Vercel | ⚡⚡⚡ | 全球 | 100GB/月 | ⭐⭐⭐⭐ |

**推荐使用 Cloudflare Pages**：速度最快、无限流量、全球CDN、完全免费！

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

本项目仅供学习使用。

## 📞 支持与文档

- 📖 [快速开始](docs/快速开始.md) - 新手入门指南
- 🎬 [使用演示](docs/使用演示.md) - 功能演示说明
- 🔧 [问题排查指南](docs/问题排查指南.md) - 常见问题解决
- 📁 [项目结构说明](docs/项目结构说明.md) - 详细的项目结构
- ☁️ [Cloudflare Pages部署指南](docs/Cloudflare_Pages部署指南.md) - 部署教程

## 🎉 致谢

感谢所有为软考学习资料做出贡献的人！

---

## 🌟 Star History

如果这个项目对您有帮助，请给个Star⭐

## 📈 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解详细更新历史

### v2.0.0 (2024-12)
- ✅ 更新为信息系统项目管理师学习平台
- ✅ 25个完整章节内容
- ✅ 25个章节重点提纲
- ✅ 9个核心章节必背内容
- ✅ 完善的辅助文档（索引、速查表、进度表）
- ✅ 优化的响应式设计
- ✅ 完整的部署文档

### v1.0.0 (2024)
- ✅ 初始版本发布
- ✅ 基础学习平台框架
- ✅ 三种学习模式
- ✅ 响应式设计

---

**祝您考试顺利！通过信息系统项目管理师考试！** 🎓💪

Made with ❤️ for 信息系统项目管理师考生
