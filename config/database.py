from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv


# Load env variables
load_dotenv()

# Mongo db uri
database_uri = os.getenv("DATABASE_URI")

# Mongo db name
database_name =os.getenv("DATABASE_NAME")

# Create mongo client
client = MongoClient(database_uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Create database
database = client[database_name]

# Create user collection
user_collection = database["user"]