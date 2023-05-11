from fastapi import FastAPI

app = FastAPI()


def rate_limiter():
    """
    Rate limiter decorator.
    """
    pass


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def say_hello():
    return "OK"
