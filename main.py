# from langflow import load_flow_from_json
# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()

# # Load LangFlow flow
# flow = load_flow_from_json("GenAI_2.json")

# @app.get("/")
# def read_root():
#     return {"message": "LangFlow is running!"}

# @app.post("/run-flow")
# async def run_flow(input: dict):
#     response = flow.run(input["data"])
#     return {"response": response}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

from langflow.interface.run import FlowExecutor
from fastapi import FastAPI
import uvicorn

app = FastAPI()

flow_executor = FlowExecutor()
flow_executor.load("GenAI_2.json")

@app.post("/run-flow")
async def run_flow(input: dict):
    response = flow_executor.run(input["data"])
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
