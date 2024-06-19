from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client["lab_x"]

@app.get("/protein/{protein_id}")
async def get_protein(protein_id: str):
    protein = db.proteins.find_one({"ProteinID": protein_id})
    if protein:
        return protein
    raise HTTPException(status_code=404, detail="Protein not found")

@app.get("/protein/{protein_id}/interactions")
async def get_protein_interactions(protein_id: str):
    interactions = list(db.interactions.find({"$or": [{"Protein1ID": protein_id}, {"Protein2ID": protein_id}]}))
    return interactions

@app.get("/organism/{organism_id}/proteins")
async def get_organism_proteins(organism_id: str):
    proteins = list(db.proteins.find({"OrganismID": organism_id}))
    interactions = list(db.interactions.find({"$or": [{"Protein1ID": {"$in": [p["ProteinID"] for p in proteins]}}, {"Protein2ID": {"$in": [p["ProteinID"] for p in proteins]}}]}))
    return {"proteins": proteins, "interactions": interactions}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
