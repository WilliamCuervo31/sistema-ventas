from email.mime.multipart import MIMEMultipart

from config import settings
import smtplib
from email.mime.text import MIMEText
import logging

logger = logging.getLogger(__name__)

def load_email_template(nombre):

    with open(
        "app/templates/birthday_email.html",
        "r",
        encoding="utf-8"
    ) as file:

        html = file.read()

    html = html.replace("{{nombre}}", nombre)

    return html

def send_birthday_email(receiver_email, nombre):

    try:

        html_content = load_email_template(nombre)

        html_content = html_content.replace(
            "{{base_url}}",
            settings.APP_BASE_URL
        )

        msg = MIMEMultipart("alternative")

        msg["Subject"] = f"Feliz Cumpleaños {nombre} - MADAS"
        msg["From"] = settings.EMAIL_USER
        msg["To"] = receiver_email

        html_part = MIMEText(
            html_content,
            "html"
        )

        msg.attach(html_part)


        with smtplib.SMTP(
            settings.SMTP_SERVER,
            int(settings.SMTP_PORT)
        ) as server:

            server.starttls()

            server.login(
                settings.EMAIL_USER,
                settings.EMAIL_PASSWORD
            )

            server.sendmail(
                settings.EMAIL_USER,
                receiver_email,
                msg.as_string()
            )

        logger.info(
            f"Correo enviado correctamente a "
            f"{receiver_email}"
        )

    except Exception as e:

        logger.error(
            f"Error enviando correo a "
            f"{receiver_email}: {str(e)}"
        )
