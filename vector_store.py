import os
import logging
import tiktoken
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

class VectorStore:
    def __init__(self, db):
        """
        初始化 VectorStore 類。

        :param db: Chroma 資料庫實例，用於執行向量相似度搜索。
        """
        self.db = db
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    @classmethod
    def init(cls, similarity_measure="cosine", openai_api_key=None, 
             persist_directory="./db/nurrecs", collection_name="nurrecs"):
        """
        初始化並設定 VectorStore 的資料庫連線。

        :param similarity_measure: 指定相似度度量方法，可以是 "cosine", "l2", 或 "ip"。
        :param openai_api_key: OpenAI API 金鑰。
        :param persist_directory: 向量資料庫持久化目錄。
        :param collection_name: 向量資料庫集合名稱。
        :return: 初始化後的 VectorStore 實例。
        """
        try:
            if not openai_api_key:
                openai_api_key = os.getenv('OPENAI_API_KEY')
            if not openai_api_key:
                raise ValueError("Missing OpenAI API key")

            embedding_model = "text-embedding-ada-002"
            embeddings = OpenAIEmbeddings(model=embedding_model)

            if similarity_measure == "cosine":
                collection_metadata = {"hnsw:space": "cosine"}
            elif similarity_measure == "l2":
                collection_metadata = {"hnsw:space": "l2"}
            elif similarity_measure == "ip":
                collection_metadata = {"hnsw:space": "ip"}
            else:
                raise ValueError("Unsupported similarity measure. Use 'cosine', 'l2', or 'ip'.")

            logging.info(f"Connecting to Chroma DB with similarity measure: {similarity_measure}")
            db = Chroma(
                embedding_function=embeddings,
                persist_directory=persist_directory,
                collection_metadata=collection_metadata,
                collection_name=collection_name
            )
            return cls(db)
        except Exception as e:
            logging.error(f"Failed to initialize VectorStore: {e}")
            raise

    def search(self, query, k=5):
        """
        執行向量相似度搜索。

        :param query: 搜索查詢字串。
        :param k: 返回的相似項目數量。
        :return: 包含搜索結果的字典列表。
        """
        try:
            logging.info(f"Performing similarity search for query: {query}")
            search_results = self.db.similarity_search(query, k=k)
            results = []
            for document in search_results:
                tokens = self.tokenizer.encode(document.page_content)
                source = document.metadata.get('source', '未知來源')
                result_dict = {
                    "content": document.page_content,
                    "tokens": tokens,
                    "source": source,
                    "score": 0
                }
                results.append(result_dict)
            return results
        except Exception as e:
            logging.error(f"Search failed: {e}")
            raise