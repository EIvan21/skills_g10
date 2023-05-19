from fastapi import FastAPI,HTTPException,status

app = FastAPI()


@app.get("/",status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello world"}