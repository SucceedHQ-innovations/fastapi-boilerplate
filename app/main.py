from fastapi import FastAPI
from app.routes import auth, users
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title='FastAPI Boilerplate', version='1.0.0')

app.include_router(auth.router, prefix='/api/v1/auth', tags=['auth'])
app.include_router(users.router, prefix='/api/v1/users', tags=['users'])

@app.get('/health')
def health_check():
    return {'status': 'healthy'}
