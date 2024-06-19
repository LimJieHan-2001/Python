# Lab X Protein-Protein Interaction Database and API

## Setup
1. Ensure MongoDB is installed and running.
2. Run the data import script:
    ```bash
    python import_data.py
    ```
3. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

## API Endpoints
1. Get Protein by ID: `GET /protein/{protein_id}`
2. Get Interactions for a Protein: `GET /protein/{protein_id}/interactions`
3. Get Proteins and Interactions for an Organism: `GET /organism/{organism_id}/proteins`
