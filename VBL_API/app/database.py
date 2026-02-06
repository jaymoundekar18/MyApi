from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
from dotenv import load_dotenv
import os

# load_dotenv()

# MONGO_URI = os.getenv("MONGO_URI")

os.environ.get("MONGO_URI")

client = MongoClient(MONGO_URI, server_api=ServerApi('1'), tls=True, tlsCAFile=certifi.where())
 
db = client['test']
vbl_collection = db['vbl_data']

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
