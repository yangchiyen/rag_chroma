import logging
from vector_store import VectorStore
from config import load_config

def main():
    config = load_config()
    
    try:
        # 初始化資料庫連線
        logging.info("Initializing database connection...")
        db = VectorStore.init(
            similarity_measure=config.get("similarity_measure", "cosine"),
            openai_api_key=config.get("openai_api_key"),
            persist_directory=config.get("persist_directory"),
            collection_name=config.get("collection_name")
        )

        # 定義查詢及預期的結果數量
        query = "現當科依醫囑開立3月16日抽血追蹤。"
        k = 5

        # 執行查詢
        logging.info(f"Executing query: {query}")
        results = db.search(query, k)

        # 輸出查詢結果
        logging.info("Query results:")
        for result in results:
            print(f"內容: {result['content']}")
            print(f"分詞數量: {len(result['tokens'])}")
            print(f"來源: {result['source']}")
            print(f"相似度分數: {result['score']}\n")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()