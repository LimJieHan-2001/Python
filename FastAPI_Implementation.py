from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

app = FastAPI()

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client["lab_x"]

# Define collections
proteins_collection = db["proteins"]
interactions_collection = db["interactions"]
organisms_collection = db["organisms"]

@app.get("/protein/{protein_id}")
async def get_protein(protein_id: str):
    # Search for the protein by using the ProteinID in MongoDB
    protein = proteins_collection.find_one({"ProteinID": protein_id})
    
    if protein:
        # Remove the '_id' field before returning
        protein.pop("_id", None)
        return protein
    else:
        # Raise a 404 error if the ProteinID is not found
        raise HTTPException(status_code=404, detail="Protein not found")

@app.get("/protein/{protein_id}/interactions")
async def get_protein_interactions(protein_id: str):
    # Search for the interactions by using Protein1ID and Protein2ID in MongoDB
    interactions = list(db.interactions.find({"$or": [{"Protein1ID": protein_id}, {"Protein2ID": protein_id}]}))

    if not interactions:
        # Raise a 404 error if the ProteinID is not found in any interactions
        raise HTTPException(status_code=404, detail="Protein not found in any interactions")
    
    return interactions

@app.get("/organism/{organism_id}/proteins")
async def get_organism_proteins(organism_id: str):
    # Search for the proteins by using OrganismID in MongoDB
    proteins = list(db.proteins.find({"OrganismID": organism_id}))
    # Search for the interactions by using Protein1ID and Protein2ID in MongoDB
    interactions = list(db.interactions.find({"$or": [{"Protein1ID": {"$in": [p["ProteinID"] for p in proteins]}}, {"Protein2ID": {"$in": [p["ProteinID"] for p in proteins]}}]}))
    
    if not proteins:
        # Raise a 404 error if the OrganismID is not found in any proteins
        raise HTTPException(status_code=404, detail="Organism not found")
    
    if not interactions:
        # Raise a 404 error if the OrganismID is not found in any interactions
        raise HTTPException(status_code=404, detail="Organism not found in any interactions")
    
    return {"proteins": proteins, "interactions": interactions}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
