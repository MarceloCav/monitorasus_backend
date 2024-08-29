from pymongo import MongoClient
import os

mongo_host = os.getenv('MONGO_HOST', 'mongo')
mongo_port = int(os.getenv('MONGO_PORT', 27017))
mongo_db_name = os.getenv('MONGO_DB_NAME', 'mydatabase')

client = MongoClient(f'mongodb://{mongo_host}:{mongo_port}', serverSelectionTimeoutMS=5000)
db = client[mongo_db_name]
# collection = db['internacoes_collection']  # Nome da coleção
