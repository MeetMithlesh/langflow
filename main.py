from fastapi import FastAPI, HTTPException
import uvicorn
from langflow.interface import load_flow_from_json

app = FastAPI()

# Load the exported LangFlow JSON file
try:
    flow = load_flow_from_json("langflow.json")
except Exception as e:
    raise RuntimeError(f"Failed to load LangFlow JSON: {e}")

@app.get("/")
def root():
    return {"message": "LangFlow is running!"}

@app.post("/run-flow")
async def run_flow(input: dict):
    try:
        # Process the input through the loaded flow
        result = flow.run(input["data"])
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Flow execution error: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
