# Web目录说明

这个目录包含**信息系统项目管理师学习平台**的所有网页文件。

## 📄 文件说明

### 主要页面

- **index.html** - 主页，平台入口
- **chapters.html** - 章节学习页面，核心功能
- **viewer.html** - 文档查看器
- **nav.html** - 快速导航页面

### 配置文件

- **config.js** - 章节配置和路径映射

## 🚀 访问方式

### 通过启动脚本（推荐）

在项目根目录运行：
- Windows: `start_server.bat`
- Linux/Mac: `./start_server.sh`

然后访问：`http://localhost:8000/web/`

### 直接打开

双击 `index.html` 文件即可

## 📝 注意事项

1. 所有资源文件（Markdown、图片）都在上级目录
2. 文件路径使用相对路径 `../` 访问上级目录
3. 建议使用HTTP服务器运行以避免跨域问题

## 🔗 相关链接

- [项目主文档](../README.md)
- [快速开始](../docs/快速开始.md)
- [考试说明](../docs/信息系统项目管理师考试说明.md)
