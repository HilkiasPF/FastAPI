from fastapi import FastAPI
from database import User, engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

Session = sessionmaker(bind=engine)
session = Session()

@app.get('/')
async def list():
    return session.query(User).all()

@app.post('/')
async def post(name:str, age: int, id:int):
    ad = User(nome=name, age=age, id=id)
    session.add(ad)
    session.commit()
    return ad.nome



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(reload=True, app='main:app')