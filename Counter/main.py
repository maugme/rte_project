import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI

COUNTER = 0

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(counter(), name="counter")
    yield
    task.cancel()

async def counter():
    global COUNTER
    while True:
        print(f"Counter: {COUNTER} sec.")
        COUNTER += 1
        await asyncio.sleep(1)

app = FastAPI(lifespan=lifespan)

@app.get("/count")
def get_counter():
    return {"Counter": COUNTER}
