import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["lab_x"]

# Read CSV files into dataframes
proteins_df = pd.read_csv("proteins.csv")
interactions_df = pd.read_csv("interactions.csv")
organisms_df = pd.read_csv("organisms.csv")

# Insert dataframes into MongoDB
db.proteins.insert_many(proteins_df.to_dict(orient="records"))
db.interactions.insert_many(interactions_df.to_dict(orient="records"))
db.organisms.insert_many(organisms_df.to_dict(orient="records"))
