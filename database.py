import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

cluster = MongoClient(os.getenv("MONGODB_CLUSTER"))
db = cluster.get_database("Albion-Associate-Discord-Bot")