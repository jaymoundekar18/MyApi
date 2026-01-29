# from pymongo import MongoClient
# import os

# MONGO_URI = os.getenv("mongodb+srv://jaymoundekar18:oaZmeQ7QdkWShFH5@cluster0.hbuswaj.mongodb.net/?appName=Cluster0")

# client = MongoClient(MONGO_URI)
# db = client.test
# employee_collection = db.employees

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = "mongodb+srv://jaymoundekar18:oaZmeQ7QdkWShFH5@cluster0.hbuswaj.mongodb.net/?appName=Cluster0"
 
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsCAFile=certifi.where())
 
db = client['test']
employee_collection = db['employees']

for emp in employee_collection.find():
    print("the emp is : ",emp)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)