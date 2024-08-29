import time
import pandas as pd
from pymongo import MongoClient, errors

def insert_data_in_batches(collection, data, batch_size=1000):
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        try:
            collection.insert_many(batch)
            print(f"Inserted batch {i // batch_size + 1}")
        except errors.BulkWriteError as bwe:
            print(f"Error inserting batch {i // batch_size + 1}: {bwe.details}")

time.sleep(1)

print("Populating MongoDB with data from Feather file...")

df_feather = pd.read_feather('/app/internacoes_rn.feather')

client = MongoClient('mongodb://mongo:27017', serverSelectionTimeoutMS=5000)
db = client['mydatabase']
collection = db['internacoes_collection']

data = df_feather.to_dict(orient='records')

insert_data_in_batches(collection, data)

print("Data successfully inserted into MongoDB from Feather file")
