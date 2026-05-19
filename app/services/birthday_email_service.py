from app.services.sheets_service import SheetsService
from app.services.email_service import send_birthday_email


def process_birthdays():

    sheets_service = SheetsService()

    clientes = sheets_service.get_birthdays_today()

    if not clientes:
        return

    for cliente in clientes:

        if (
            cliente["correo"]
            and cliente["nombre"]
        ):

            send_birthday_email(
                cliente["correo"],
                cliente["nombre"]
            )

            sheets_service.mark_email_sent(
                cliente["row_number"]
            )