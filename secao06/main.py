from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)


"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjc1MDIxNjE0LCJpYXQiOjE2NzQ0MTY4MTQsInN1YiI6IjUifQ.Y_QPV0WIVGA6x6XSxyseW7Fg4xWmukDeJW3Wj_3r-AU
Tipo: bearer

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjUyNDQzNDk1LCJpYXQiOjE2NTE4Mzg2OTUsInN1YiI6IjMifQ.jTq0xkcILa7kgrtMJhcew6OIwXODEjX24CzCToY7bbU
"""
