import logging
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from app.services.scheduler_service import start_scheduler, execute_birthdays
from fastapi.responses import RedirectResponse, JSONResponse
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from sqlalchemy import text
from config.db_connection import get_db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Inciando scheduler")
    start_scheduler()

    yield #se ejecuta cuando la app se apaga
    logger.info("Cerrando aplicacion")

app = FastAPI(
    lifespan=lifespan
)

logger.info("App Iniciada")

# Static files
app.mount(
    "/static",
    StaticFiles(directory="app/static/"),
    name="static"
)

@app.get("/")
def root():
    logger.info("Se llamo el endpoint '/'")
    return RedirectResponse(url="/docs")

@app.get("/health")
def health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
    
@app.post("/birthdays/send")
async def send_birthdays():

    success = execute_birthdays()

    if success:

        return JSONResponse(
            status_code=200,
            content={
                "message": (
                    "Proceso ejecutado correctamente"
                )
            }
        )
    
    return JSONResponse(
        status_code=500,
        content={
            "message": (
                "Error ejecutando el proceso"
            )
        }
    )