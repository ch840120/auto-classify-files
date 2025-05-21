import os
import shutil

# 定義不同檔案類型對應的副檔名
FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],  # 圖片
    "documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],  # 文件
    "compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],  # 壓縮檔
    "videos": [".mp4", ".avi", ".mov", ".mkv"],  # 影片
    "music": [".mp3", ".wav", ".aac", ".flac"],  # 音樂
    "others": [],  # 其他（沒有被歸類的檔案）
}


# 判斷檔案屬於哪一個分類
def get_category(filename):
    # 取得檔案副檔名並轉成小寫
    ext = os.path.splitext(filename)[1].lower()
    # 依照副檔名比對類別
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "others"


# 自動分類資料夾裡的檔案
def auto_classify_files(source_folder):
    for filename in os.listdir(source_folder):  # 取得資料夾內所有檔名
        file_path = os.path.join(source_folder, filename)  # 檔案的完整路徑
        if os.path.isfile(file_path):  # 只處理檔案（不處理資料夾）
            category = get_category(filename)  # 取得檔案的分類
            target_folder = os.path.join(source_folder, category)  # 目標資料夾路徑
            os.makedirs(target_folder, exist_ok=True)  # 若目標資料夾不存在則建立
            shutil.move(file_path, os.path.join(target_folder, filename))  # 移動檔案到分類資料夾
            print(f"已移動 {filename} 到 {category}/")  # 顯示移動訊息

if __name__ == "__main__":
    # 自動偵測 Windows 預設的下載資料夾路徑
    download_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    user_input = input(f"請輸入要分類的資料夾路徑（直接 Enter 使用預設下載資料夾 {download_folder}）:\n")
    if user_input.strip() == "":
        source_folder = download_folder  # 使用預設下載資料夾
    else:
        source_folder = user_input.strip()  # 使用使用者自訂路徑

    # 檢查資料夾是否存在
    if not os.path.isdir(source_folder):
        print(f"找不到這個資料夾：{source_folder}")
    else:
        auto_classify_files(source_folder)  # 執行自動分類
        print("檔案分類完成！")

