import logging

import sib_api_v3_sdk

from sib_api_v3_sdk.rest import (
    ApiException
)

from config import settings

logger = logging.getLogger(__name__)


def load_email_template(
    nombre: str
):
    """
    Carga template HTML
    """

    with open(
        "app/templates/birthday_email.html",
        "r",
        encoding="utf-8"
    ) as file:

        html = file.read()

    html = html.replace(
        "{{nombre}}",
        nombre
    )

    html = html.replace(
        "{{base_url}}",
        settings.APP_BASE_URL
    )

    return html


def send_birthday_email(
    receiver_email: str,
    nombre: str
):
    """
    Envía correo cumpleaños
    """

    try:

        configuration = (
            sib_api_v3_sdk.Configuration()
        )

        configuration.api_key[
            "api-key"
        ] = settings.BREVO_API_KEY

        api_instance = (
            sib_api_v3_sdk
            .TransactionalEmailsApi(
                sib_api_v3_sdk
                .ApiClient(configuration)
            )
        )

        html_content = (
            load_email_template(
                nombre
            )
        )

        send_smtp_email = (
            sib_api_v3_sdk
            .SendSmtpEmail(

                to=[
                    {
                        "email":
                        receiver_email
                    }
                ],

                sender={
                    "name": "MADAS",

                    "email": (
                        settings.EMAIL_USER
                    )
                },

                subject=(
                    f"🎂 Feliz cumpleaños {nombre}"
                ),

                html_content=(
                    html_content
                )
            )
        )

        api_instance.send_transac_email(
            send_smtp_email
        )

        logger.info(
            f"Correo enviado correctamente "
            f"a {receiver_email}"
        )

        return True

    except ApiException as e:

        logger.error(
            f"Error enviando correo "
            f"a {receiver_email}: {str(e)}"
        )

        return False