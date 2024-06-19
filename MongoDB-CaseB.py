import pymongo
import csv

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["DataSample-CaseB-v2"]

# Define collections
proteins_collection = db["proteins"]
interactions_collection = db["interactions"]
organisms_collection = db["organisms"]

# Import Proteins Data
with open('Protein_Information.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        proteins_collection.insert_one(row)

# Import Interactions Data
with open('Interaction_Data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        interactions_collection.insert_one(row)

# Import Organisms Data
with open('Organism_Information.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        organisms_collection.insert_one(row)
