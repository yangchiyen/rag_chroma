import os
import configparser

def load_config():
    config = configparser.ConfigParser()

    # 設定預設值
    default_config = {
        'similarity_measure': 'cosine',
        'persist_directory': './db/nurrecs',
        'collection_name': 'nurrecs',
        'openai_api_key': None  # 預設值為 None 表示必須設置
    }

    # 嘗試從配置文件讀取配置
    config.read('config.ini')
    
    file_config = config['DEFAULT'] if 'DEFAULT' in config else {}

    # 合併環境變量和配置文件中的設定，優先使用環境變量
    final_config = {
        'similarity_measure': os.getenv('SIMILARITY_MEASURE', file_config.get('similarity_measure', default_config['similarity_measure'])),
        'persist_directory': os.getenv('PERSIST_DIRECTORY', file_config.get('persist_directory', default_config['persist_directory'])),
        'collection_name': os.getenv('COLLECTION_NAME', file_config.get('collection_name', default_config['collection_name'])),
        'openai_api_key': os.getenv('OPENAI_API_KEY', file_config.get('openai_api_key', default_config['openai_api_key']))
    }

    return final_config