import logging
from fastapi import FastAPI
from langserve import add_routes
from model import llm
from settings import WEBAPP_HOST, WEBAPP_PORT

app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)


add_routes(
    app,
    llm,
    path="",
)

if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.DEBUG)
    uvicorn.run(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
