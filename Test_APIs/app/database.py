from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'), tls=True, tlsCAFile=certifi.where())
 
db = client['test']
employee_collection = db['employees']

ecomm_db = client['ecommerce_db']
users_collection = ecomm_db['users']
products_collection = ecomm_db['products']
orders_collection = ecomm_db['orders']

# for emp in employee_collection.find():
#     print("the emp is : ",emp)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
