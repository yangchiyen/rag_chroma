# AI Nursing Assistant System

## 專案描述
這是一個基於 AI 的護理助理系統，使用 OpenAI 的 text-embedding-ada-002 模型和 Chroma DB 進行向量相似度搜索，以提供高效的查詢和數據檢索功能。

## 安裝指南
請按照以下步驟進行安裝：

1. 克隆此倉庫：
    ```bash
    git clone https://github.com/yourusername/ai-nursing-assistant.git
    cd ai-nursing-assistant
    ```

2. 創建虛擬環境並安裝依賴：
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## 使用說明
1. 設置 OpenAI API 金鑰：
    - 可以在 `config.ini` 中設置
    - 或者設置環境變量 `OPENAI_API_KEY`

2. 運行主程序：
    ```bash
    python main.py
    ```

## 配置說明
配置可以通過修改 `config.ini` 文件或設置環境變量來完成。以下是 `config.ini` 的範例：

```ini
[DEFAULT]
# 指定相似度度量方法，可以是 "cosine"（預設）, "l2", 或 "ip"
similarity_measure = cosine

# 向量資料庫持久化目錄
persist_directory = ./db/nurrecs

# 向量資料庫集合名稱
collection_name = nurrecs

# OpenAI API 金鑰，必須設置
# openai_api_key 可以直接在這裡設置，或者通過環境變量設置
openai_api_key = 
```

## 文件結構
專案的主要文件結構如下：
```bash
.
├── main.py                 # 主程序文件
├── vector_store.py         # VectorStore 類和相關的數據庫操作
├── config.py               # 配置管理
├── requirements.txt        # 依賴包列表
└── config.ini              # 配置文件
```

## 貢獻指南
歡迎貢獻！請遵循以下步驟提交貢獻：

1. Fork 此倉庫
2. 創建您的分支 (git checkout -b feature-branch)
3. 提交您的修改 (git commit -am 'Add some feature')
4. 推送到分支 (git push origin feature-branch)
5. 創建新的 Pull Request

## 授權資訊
此專案使用 MIT 授權。
