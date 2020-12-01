import os
import dotenv 
from pymongo import MongoClient


dotenv.load_dotenv()

DBURL = os.getenv("URL")

# Conecto la base de datos con Mongo
if not (DBURL):
    raise ValueError("especificar URL")

client = MongoClient(DBURL)
db = client.get_database()
collection = db["phrases"]