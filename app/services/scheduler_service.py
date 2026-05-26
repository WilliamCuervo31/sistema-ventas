import schedule
import time
import threading
import logging

from app.services.birthday_email_service import process_birthdays

logger = logging.getLogger(__name__)

is_running = False
#Evita que corra dos veces al mismo tiempo

def execute_birthdays():

    global is_running

    if is_running:
        logger.info("Proceso de email de cumpleaños en ejecucion")
        return False
    
    try:
        is_running = True
        logger.info("Inicia proceso de email de cumpleanos")

        process_birthdays()
        logger.info("Proceso finalizado correctamente")
        return True

    except Exception as e:
        logger.error(f"Error ejecutando email cumpleaños: {str(e)}")
        return False

    finally:
        is_running = False

def run_scheduler():
    schedule.every().day.at("12:00").do(execute_birthdays)
    logger.info("Scheduler iniciado")

    while True:
        #Esto mantiene vivo el schedule
        schedule.run_pending()
        time.sleep(60)
        #Revisa cada minuto

def start_scheduler():
    schedule_thread = threading.Thread(
        target=run_scheduler,
        daemon=True
    )

    schedule_thread.start()