# NTQQ 图片缓存清理工具 🧹

[![Build and Release](https://github.com/SuperWaterGod/NTQQImageCleaner/actions/workflows/build.yml/badge.svg)](https://github.com/SuperWaterGod/NTQQImageCleaner/actions/workflows/build.yml)
[![GitHub release](https://img.shields.io/github/v/release/SuperWaterGod/NTQQImageCleaner)](https://github.com/SuperWaterGod/NTQQImageCleaner/releases)
[![License](https://img.shields.io/github/license/SuperWaterGod/NTQQImageCleaner)](LICENSE)

一个用于清理 NTQQ（QQ NT 版本）过期图片缓存的 Python 工具，支持按时间和文件大小筛选，帮助释放磁盘空间。

## ✨ 特性

- 🔍 **递归扫描** - 自动扫描目录及所有子目录
- 📅 **时间筛选** - 按文件创建时间筛选（支持自定义天数）
- 📦 **大小筛选** - 按文件大小筛选（支持自定义最小大小）
- 🎨 **美观界面** - 使用 Rich 库提供美观的终端界面
- 📊 **清晰展示** - 表格形式展示扫描结果，包含文件路径、创建时间、大小
- ⚠️ **安全确认** - 删除前二次确认，防止误操作
- ✅ **格式丰富** - 支持多种图片格式（jpg, png, gif, bmp, webp, svg, ico 等）
- 📈 **统计信息** - 显示文件总数和总大小

## 📥 下载安装

### 方式一：下载可执行文件（推荐）

前往 [Releases](https://github.com/SuperWaterGod/NTQQImageCleaner/releases/latest) 页面下载最新版本：

- **Windows 64位**: `ntqq-image-cleaner-vX.X.X-windows-x64.exe`

下载后无需安装 Python 环境即可直接运行。

### 方式二：从源码运行

需要 Python 3.8 或更高版本。

```bash
# 克隆仓库
git clone https://github.com/SuperWaterGod/NTQQImageCleaner.git
cd NTQQImageCleaner

# 安装依赖
pip install -r requirements.txt

# 运行程序
python main.py
```

## 🚀 使用方法

### 快速开始

1. **下载程序**
   
   - 从 [Releases](https://github.com/SuperWaterGod/NTQQImageCleaner/releases/latest) 下载最新版本
   
2. **放置程序**
   - 将 exe 文件复制到需要清理的目录
   - 或者在 NTQQ 缓存目录运行

3. **运行程序**
   - 双击运行 `ntqq-image-cleaner-vX.X.X-windows-x64.exe`

4. **设置筛选条件**
   ```
   请输入天数（筛选多少天前创建的文件）[30]: 30
   请输入最小文件大小（KB）[1000]: 1000
   ```

5. **查看结果并确认**
   - 程序会显示符合条件的文件列表
   - 确认无误后输入 `y` 执行删除

### 使用示例

```bash
# 示例1：清理 30 天前且大于 1MB 的图片
天数: 30
最小大小: 1000 KB

# 示例2：清理 7 天前且大于 500KB 的图片
天数: 7
最小大小: 500 KB

# 示例3：清理 90 天前且大于 2MB 的图片
天数: 90
最小大小: 2000 KB
```

## 📂 NTQQ 缓存目录位置

NTQQ 的图片缓存文件通常位于以下路径：

### Windows

```
C:\Users\你的用户名\Documents\Tencent Files\你的QQ号\nt_qq\nt_data\Pic\
```

或者

```
C:\Users\你的用户名\AppData\Local\Tencent\QQ\nt_qq\nt_data\Pic\
```

### 查找方法

1. 打开 NTQQ 设置
2. 查看"文件管理"相关设置
3. 找到缓存文件存储位置

## 📋 支持的图片格式

| 格式 | 扩展名 |
|------|--------|
| JPEG | .jpg, .jpeg |
| PNG | .png |
| GIF | .gif |
| BMP | .bmp |
| TIFF | .tiff, .tif |
| WebP | .webp |
| SVG | .svg |
| ICO | .ico |

## 🛠️ 开发指南

### 环境要求

- Python 3.8+
- pip 包管理器

### 安装开发依赖

```bash
# 克隆仓库
git clone https://github.com/SuperWaterGod/NTQQImageCleaner.git
cd NTQQImageCleaner

# 安装依赖
pip install -r requirements.txt

# 安装开发依赖（可选）
pip install pyinstaller
```

### 项目结构

```
.
├── .github/
│   └── workflows/
│       └── build.yml          # GitHub Actions 工作流
├── main.py                    # 主程序
├── requirements.txt           # Python 依赖
├── README.md                  # 项目文档
└── LICENSE                    # 许可证文件
```

### 本地构建 exe

```bash
# 安装 PyInstaller
pip install pyinstaller

# 构建单文件 exe
pyinstaller --onefile --name ntqq-image-cleaner-v1.0.0-windows-x64 --console main.py

# 生成的文件位于 dist 目录
```

### 代码说明

- `get_file_info()` - 获取文件的路径、创建时间和大小
- `find_images()` - 递归查找所有图片文件
- `filter_images()` - 根据条件筛选图片
- `display_results()` - 使用表格展示结果
- `delete_files()` - 执行删除操作

## 📦 发布新版本

```bash
# 1. 更新版本号并提交
git add .
git commit -m "Release v1.0.0"
git push

# 2. 创建并推送标签
git tag v1.0.0
git push origin v1.0.0

# 3. GitHub Actions 会自动构建并创建 Release
```

## ⚠️ 注意事项

> **重要提示：删除操作不可撤销！**

- ✅ 建议先使用较小的天数（如 7 天）进行测试
- ✅ 建议在删除前备份重要文件
- ✅ 程序会递归扫描所有子目录，请确保在正确的目录下运行
- ✅ 首次使用建议只查看结果，不执行删除
- ✅ 可以先设置较大的文件大小阈值（如 5MB）来避免误删小文件

### 安全建议

1. **测试运行**：首次使用时，先用不重要的目录测试
2. **备份数据**：删除前备份重要文件
3. **仔细确认**：删除前仔细查看列表，确认无误
4. **从保守开始**：使用较大的天数和文件大小阈值

## 🤝 贡献指南

欢迎贡献代码、报告问题或提出建议！

### 报告问题

如果你发现了 bug 或有功能建议，请：

1. 前往 [Issues](https://github.com/SuperWaterGod/NTQQImageCleaner/issues) 页面
2. 搜索是否已有相关问题
3. 如没有，创建新的 Issue，并提供：
   - 问题描述
   - 复现步骤
   - 系统环境信息
   - 截图（如有）

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

简单来说，你可以自由地：
- ✅ 使用本软件
- ✅ 修改本软件
- ✅ 分发本软件
- ✅ 用于商业用途

但需要：
- 📋 保留版权声明
- 📋 包含许可证副本

## 🙏 致谢

本项目使用了以下优秀的开源项目：

- [Rich](https://github.com/Textualize/rich) - 提供精美的终端输出
- [PyInstaller](https://www.pyinstaller.org/) - Python 打包工具

## 📮 联系方式

- 📧 邮箱: yancaiwudi@foxmail.com
- 🐛 问题反馈: [Issues](https://github.com/SuperWaterGod/NTQQImageCleaner/issues)
- 💬 讨论: [Discussions](https://github.com/SuperWaterGod/NTQQImageCleaner/discussions)

## 🌟 Star History

如果这个项目对你有帮助，请给它一个 Star ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=SuperWaterGod/NTQQImageCleaner&type=Date)](https://star-history.com/#YOUR_USERNAME/YOUR_REPO_NAME&Date)

## ❓ 常见问题

### Q: 程序删除的文件可以恢复吗？
A: 不能。程序使用的是永久删除，不会放入回收站。请务必在删除前确认。

### Q: 可以用于清理其他程序的缓存吗？
A: 可以。本程序可以用于清理任何目录下的图片文件，不限于 NTQQ。

### Q: 为什么扫描不到某些图片？
A: 请检查：
- 文件扩展名是否在支持列表中
- 文件是否符合设置的时间和大小条件
- 程序是否有权限访问该目录

### Q: 程序运行很慢怎么办？
A: 如果目录下文件很多，扫描会需要一些时间。这是正常现象。

### Q: 可以在 macOS 或 Linux 上使用吗？
A: 目前只提供 Windows 版本的 exe。但你可以在任何系统上运行 Python 源码。

---

**⚠️ 免责声明**

使用本工具产生的任何数据丢失，开发者概不负责。请谨慎使用删除功能，务必在删除前确认文件列表。建议首次使用时先进行测试，或备份重要数据。

---

<div align="center">

Made with ❤️ by Super_Water_God

[⬆ 回到顶部](#ntqq-图片缓存清理工具-)

</div>