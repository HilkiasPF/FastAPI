from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def list():
    return '123'



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(reload=True, app='main:app')