import logging
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from app.services.birthday_email_service import process_birthdays
from fastapi.responses import RedirectResponse, JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import text
from config.db_connection import get_db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()
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

    process_birthdays()

    return JSONResponse(
        status_code=200,
        content={
            "message": (
                "Proceso ejecutado correctamente"
            )
        }
    )