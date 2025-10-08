# 文件

此資料夾包含 Spec Kit 的文件原始檔案，使用 [DocFX](https://dotnet.github.io/docfx/) 建置。

## 本地建置

要在本地建置文件：

1. 安裝 DocFX：
   ```bash
   dotnet tool install -g docfx
   ```

2. 建置文件：
   ```bash
   cd docs
   docfx docfx.json --serve
   ```

3. 在瀏覽器中開啟 `http://localhost:8080` 檢視文件。

## 結構

- `docfx.json` - DocFX 配置檔案
- `index.md` - 主要文件首頁
- `toc.yml` - 目錄配置
- `installation.md` - 安裝指南
- `quickstart.md` - 快速開始指南
- `_site/` - 產生的文件輸出（git 忽略）

## 部署

當變更推送到 `main` 分支時，文件會自動建置並部署到 GitHub Pages。工作流程定義在 `.github/workflows/docs.yml` 中。
