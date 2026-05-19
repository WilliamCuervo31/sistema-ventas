import logging
from datetime import datetime
from dateutil import parser
import gspread
from google.oauth2.service_account import Credentials

from config.settings import (
    GOOGLE_CREDENTIALS_JSON,
    GOOGLE_SHEETS_ID,
    GOOGLE_SHEETS_WORKSHEET
)

logger = logging.getLogger(__name__)


FORM_FIELDS = {

    "name": (
        "Nombre y apellido"
    ),

    "email": (
        "Dirección de correo electrónico"
    ),

    "phone": (
        "Cual es tu numero de Whatsapp? "
    ),

    "birthday": (
        "Cual es tu fecha de cumpleaños?"
    ),

    "email_sent": (
        "email_enviado"
    ),

    "whatsapp_sent": (
        "whatsapp_enviado"
    )
}


class SheetsService:

    def __init__(self):

        self.client = self._connect()

        self.sheet = self._get_worksheet()

    def _connect(self):
        """
        Conexión con Google Sheets API
        """

        try:

            scopes = [
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive"
            ]

            credentials = Credentials.from_service_account_info(
                GOOGLE_CREDENTIALS_JSON,
                scopes=scopes
            )

            client = gspread.authorize(credentials)

            logger.info(
                "Conexión exitosa con Google Sheets"
            )

            return client

        except Exception as e:

            logger.error(
                f"Error conectando con Google Sheets: {str(e)}"
            )

            raise

    def _get_worksheet(self):
        """
        Obtiene la worksheet configurada
        """

        try:

            spreadsheet = self.client.open_by_key(
                GOOGLE_SHEETS_ID
            )

            worksheet = spreadsheet.worksheet(
                GOOGLE_SHEETS_WORKSHEET
            )

            logger.info(
                f"Worksheet cargada correctamente: "
                f"{GOOGLE_SHEETS_WORKSHEET}"
            )

            return worksheet

        except Exception as e:

            logger.error(
                f"Error obteniendo worksheet: {str(e)}"
            )

            raise

    def get_all_clients(self):
        """
        Obtiene todos los clientes
        """

        try:

            records = self.sheet.get_all_records()

            logger.info(
                f"Clientes obtenidos correctamente. "
                f"Total: {len(records)}"
            )

            return records

        except Exception as e:

            logger.error(
                f"Error obteniendo clientes: {str(e)}"
            )

            return []

    def get_birthdays_today(self):
        """
        Obtiene clientes que cumplen años hoy
        """

        try:

            clients = self.get_all_clients()

            today = datetime.now().strftime(
                "%m-%d"
            )

            birthday_clients = []

            for index, client in enumerate(
                clients,
                start=2
            ):
                """
                start=2 porque:
                fila 1 = headers
                fila 2 = primer cliente
                """

                birthday = client.get(
                    FORM_FIELDS["birthday"]
                )

                if not birthday:
                    continue

                try:

                    logger.info(
                        f"Fecha recibida: {birthday}"
                    )

                    birth_date = parser.parse(
                        str(birthday),
                        dayfirst=True
                    )

                    email_sent = (
                        str(
                            client.get(
                                FORM_FIELDS[
                                    "email_sent"
                                ]
                            )
                        )
                        .strip()
                        .upper()
                    )

                    if (
                        birth_date.strftime(
                            "%m-%d"
                        ) == today
                        and email_sent != "SI"
                    ):

                        birthday_clients.append({

                            "row_number": index,

                            "nombre": client.get(
                                FORM_FIELDS["name"]
                            ),

                            "correo": client.get(
                                FORM_FIELDS["email"]
                            ),

                            "telefono": client.get(
                                FORM_FIELDS["phone"]
                            ),

                            "email_enviado": (
                                client.get(
                                    FORM_FIELDS[
                                        "email_sent"
                                    ]
                                )
                            ),

                            "whatsapp_enviado": (
                                client.get(
                                    FORM_FIELDS[
                                        "whatsapp_sent"
                                    ]
                                )
                            )
                        })

                except ValueError:

                    logger.warning(
                        f"Fecha inválida para cliente: "
                        f"{client.get(FORM_FIELDS['name'])}"
                    )

            logger.info(
                f"Cumpleaños encontrados hoy: "
                f"{len(birthday_clients)}"
            )

            return birthday_clients

        except Exception as e:

            logger.error(
                f"Error obteniendo cumpleaños: {str(e)}"
            )

            return []

    def mark_email_sent(
        self,
        row_number: int
    ):
        """
        Marca email como enviado
        """

        try:

            # Columna E
            self.sheet.update_cell(
                row_number,
                5,
                "SI"
            )

            logger.info(
                f"Email marcado como enviado "
                f"en fila {row_number}"
            )

        except Exception as e:

            logger.error(
                f"Error marcando email enviado: "
                f"{str(e)}"
            )