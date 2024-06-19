import pymongo
import csv

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["lab_x"]

# Define collections
proteins_collection = db["proteins"]
interactions_collection = db["interactions"]
organisms_collection = db["organisms"]

# Import Proteins Data
with open('proteins.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        proteins_collection.insert_one(row)

# Import Interactions Data
with open('interactions.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        interactions_collection.insert_one(row)

# Import Organisms Data
with open('organisms.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        organisms_collection.insert_one(row)
