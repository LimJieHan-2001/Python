import pymongo
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('localhost', 27017)

# Specify the database name
db_name = 'my_database'

# Get a reference to the database
db = client[db_name]

# Specify the collection name
collection_name = 'my_collection'

# Get a reference to the collection
collection = db[collection_name]

# Define the documents to insert
docs = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "Chicago"},
    {"name": "Bob", "age": 35, "city": "Los Angeles"}
]

# Insert the documents
result = collection.insert_many(docs)

# Print the inserted IDs
print(result.inserted_ids)