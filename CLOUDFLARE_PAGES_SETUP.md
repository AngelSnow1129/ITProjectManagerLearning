# Cloudflare Pages 部署配置说明

## ⚠️ 重要：修复部署错误

如果遇到以下错误：
```
✘ [ERROR] It looks like you've run a Workers-specific command in a Pages project.
For Pages, please run `wrangler pages deploy` instead.
```

这是因为 Cloudflare Pages 的构建设置不正确。

## 🔧 正确的配置方法

### 方法1：在 Cloudflare Dashboard 中配置（推荐）

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com)
2. 进入你的 Pages 项目
3. 点击 **Settings** → **Builds & deployments**
4. 修改以下设置：

```yaml
Framework preset: None
Build command: (留空或删除)
Build output directory: /
Root directory: /
```

**关键点**：
- ✅ **Build command 必须留空**（本项目是纯静态网站，无需构建）
- ✅ **Build output directory 设置为 `/`**（项目根目录）
- ❌ **不要使用 `npx wrangler deploy`**（这是 Workers 命令，不是 Pages 命令）

5. 保存设置
6. 点击 **Retry deployment** 重新部署

### 方法2：删除错误的构建命令

如果在项目设置中看到：
```
Build command: npx wrangler deploy
```

请将其**删除或留空**。

### 方法3：使用 Wrangler CLI 部署

如果你想使用命令行部署，请使用正确的命令：

```bash
# ❌ 错误的命令（Workers）
npx wrangler deploy

# ✅ 正确的命令（Pages）
npx wrangler pages deploy .

# 或者全局安装后使用
npm install -g wrangler
wrangler pages deploy .
```

## 📋 完整的部署步骤

### Git 集成部署（推荐）

1. **连接 Git 仓库**
   - 在 Cloudflare Dashboard 中创建 Pages 项目
   - 连接你的 GitHub/GitLab 仓库

2. **配置构建设置**
   ```yaml
   项目名称: projectmanager-learning
   生产分支: main
   构建命令: (留空)
   构建输出目录: /
   根目录: /
   ```

3. **保存并部署**
   - 点击 "Save and Deploy"
   - 等待部署完成

4. **自动部署**
   - 每次推送代码到 Git 仓库
   - Cloudflare Pages 会自动部署

### CLI 部署

```bash
# 1. 安装 Wrangler
npm install -g wrangler

# 2. 登录 Cloudflare
wrangler login

# 3. 部署项目（首次）
wrangler pages deploy . --project-name=projectmanager-learning

# 4. 后续更新
wrangler pages deploy .
```

## 🗂️ 项目结构

本项目是纯静态网站，结构如下：

```
项目根目录/
├── web/              # 网站主要文件
│   ├── index.html
│   ├── chapters.html
│   ├── study.html
│   └── ...
├── md/               # Markdown 内容
│   ├── 基础知识/
│   ├── 案例分析/
│   └── 搜集资料/
├── keypoint/         # 重点内容
├── docs/             # 文档
├── _headers          # HTTP 头配置
├── _redirects        # 重定向规则
├── index.html        # 根目录首页
└── wrangler.toml     # Wrangler 配置
```

**重要**：
- ✅ 所有文件都是静态的（HTML, CSS, JS, MD, 图片）
- ✅ 无需任何构建步骤
- ✅ 无需 Node.js 或其他运行时
- ✅ 直接部署即可

## ❓ 常见问题

### Q: 为什么会出现 "Workers-specific command" 错误？

**A**: 因为 Cloudflare Pages 的构建设置中配置了 `npx wrangler deploy`，这是 Workers 的部署命令，不适用于 Pages 项目。

**解决方案**：删除或清空构建命令。

### Q: 如何确认配置正确？

**A**: 在 Cloudflare Dashboard 中检查：
- Settings → Builds & deployments
- Build command 应该是空的
- Build output directory 应该是 `/`

### Q: 部署后页面空白怎么办？

**A**: 检查以下几点：
1. 确保 `web/index.html` 文件存在
2. 检查 `_redirects` 文件配置
3. 查看浏览器控制台的错误信息
4. 检查 Cloudflare Pages 的部署日志

### Q: 如何查看部署日志？

**A**: 
1. 进入 Cloudflare Dashboard
2. 选择你的 Pages 项目
3. 点击 "Deployments" 标签
4. 点击具体的部署查看日志

## 📚 相关文档

- [Cloudflare Pages 官方文档](https://developers.cloudflare.com/pages/)
- [Wrangler CLI 文档](https://developers.cloudflare.com/workers/wrangler/)
- [项目部署指南](docs/Cloudflare_Pages部署指南.md)

## 🎯 快速修复清单

- [ ] 登录 Cloudflare Dashboard
- [ ] 进入 Pages 项目设置
- [ ] 删除或清空 "Build command"
- [ ] 确认 "Build output directory" 为 `/`
- [ ] 保存设置
- [ ] 重新部署
- [ ] 验证网站正常访问

---

**需要帮助？** 查看 [完整部署指南](docs/Cloudflare_Pages部署指南.md)
