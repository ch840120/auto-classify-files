# auto-classify-files

自動分類資料夾內檔案的小工具，能依照副檔名將檔案自動搬移到對應的分類資料夾。  
支援圖片、文件、壓縮檔、影片、音樂及其他檔案，讓你的資料夾井然有序！

## 功能特色

- 自動偵測並分類常見類型檔案
- 支援自訂分類邏輯
- 一鍵執行，操作簡單
- 自動建立分類資料夾
- 
## 運作流程圖

```commandline
# 執行前：原始 {input_folder} 資料夾
{input_folder}/
├── a.jpg
├── b.docx
├── c.pdf
├── d.mp3
└── e.zip

# 執行程式後，自動分類成
{input_folder}/
├── images/
│   └── a.jpg
├── documents/
│   ├── b.docx
│   └── c.pdf
├── music/
│   └── d.mp3
└── compressed/
    └── e.zip
```