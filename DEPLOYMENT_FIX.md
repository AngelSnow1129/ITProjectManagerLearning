# 🚨 Cloudflare Pages 部署错误修复

## 错误信息

```
✘ [ERROR] It looks like you've run a Workers-specific command in a Pages project.
For Pages, please run `wrangler pages deploy` instead.
```

## 🔧 快速修复（3步）

### 步骤1：登录 Cloudflare Dashboard

访问：https://dash.cloudflare.com

### 步骤2：修改构建设置

1. 进入你的 Pages 项目
2. 点击 **Settings** → **Builds & deployments**
3. 找到 **Build configurations**
4. 修改为：

```yaml
Framework preset: None
Build command: (删除或留空 - 这是关键！)
Build output directory: /
Root directory: (留空)
```

**重要**：必须删除或清空 "Build command"，不要使用任何 wrangler 命令！

### 步骤3：重新部署

1. 点击 **Save** 保存设置
2. 返回 **Deployments** 标签
3. 点击 **Retry deployment**
4. 等待部署完成

## ✅ 验证

部署成功后，你应该看到：
- ✅ 部署状态：Success
- ✅ 网站可以访问
- ✅ 无错误信息

## 📚 详细说明

本项目是**纯静态网站**，包含：
- HTML 文件
- CSS 文件
- JavaScript 文件
- Markdown 文件
- 图片文件

**不需要任何构建步骤**，直接部署即可！

## ❓ 为什么会出错？

Cloudflare Pages 尝试执行 `npx wrangler deploy`，这是 **Cloudflare Workers** 的部署命令，不适用于 **Cloudflare Pages** 项目。

正确的做法是：
- ✅ Pages 项目：不需要构建命令，直接部署静态文件
- ❌ Workers 项目：需要使用 `wrangler deploy`

## 🎯 正确的配置

```yaml
# Cloudflare Pages 项目配置
项目类型: Pages (不是 Workers)
构建命令: (空)
输出目录: /
部署方式: Git 集成或 CLI
```

## 📖 更多帮助

- [完整部署指南](docs/Cloudflare_Pages部署指南.md)
- [详细配置说明](CLOUDFLARE_PAGES_SETUP.md)
- [Cloudflare Pages 官方文档](https://developers.cloudflare.com/pages/)

---

**需要帮助？** 查看完整文档或在 GitHub 创建 Issue。
