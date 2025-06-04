
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

# Get the MongoDB URI
uri = os.getenv("MONGO_URI")


# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB! wooza")
except Exception as e:
    print(e)