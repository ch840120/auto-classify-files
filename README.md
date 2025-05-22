# 📂 auto-classify-files

自動分類檔案小工具，支援依副檔名、自訂規則將檔案自動移動到對應資料夾，減少手動整理的麻煩。

## ✨ 特色

- 🚀 批次自動分類檔案，省時省力
- 🗂️ 支援自訂副檔名與分類資料夾對應規則
- 💡 操作簡單，適用 Windows、macOS、Linux
- 🔄 支援遞迴處理子目錄（可選）
- 📋 可記錄處理日誌，方便追蹤

## 🖥️ 使用需求

- 🐍 Python 3.6+
- （建議）安裝虛擬環境：`python -m venv .venv`

## ⚡ 安裝與使用

1. **下載/複製專案**
    ```bash
    git clone https://github.com/ch840120/auto-classify-files.git
    cd auto-classify-files
    ```

2. **執行程式**
    ```bash
    python main.py
    ```

## ⚙️ 自訂規則說明

- 可新增 `config.json` 來自訂副檔名與分類目錄，例如：
    ```json
     {
        "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],  # 圖片
        "documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],  # 文件
        "compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],  # 壓縮檔
        "videos": [".mp4", ".avi", ".mov", ".mkv"],  # 影片
        "music": [".mp3", ".wav", ".aac", ".flac"],  # 音樂
        "others": [],  # 其他（沒有被歸類的檔案）
    }
    ```
- 或直接於main.py內修改對應字典。

## 📁 運作流程圖

```commandline
# 📁 執行前：原始 {input_folder} 資料夾
📁 {input_folder}/
├── 📝 a.jpg
├── 📝 b.docx
├── 📝 c.pdf
├── 📝 d.mp3
└── 📝 e.zip

# 執行程式後，自動分類成
📁 {input_folder}/
├── 📁 images/
│   └── 📝 a.jpg
├── 📁 documents/
│   ├── 📝 b.docx
│   └── 📝 c.pdf
├── 📁 music/
│   └── 📝 d.mp3
└── 📁 compressed/
    └── 📝 e.zip
```
