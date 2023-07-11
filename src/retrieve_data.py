import os

import gspread
from gspread_dataframe import get_as_dataframe
import pandas as pd

from transformations import Headers


# Use credentials to create a client to interact with the Google Drive API
# gc = gspread.service_account(filename="credentials.json")
gc = gspread.service_account_from_dict({
  "type": "service_account",
  "project_id": os.getenv("PROJECT_ID"),
  "private_key_id": os.getenv("PRIVATE_KEY_ID"),
  "private_key": os.getenv("PRIVATE_KEY").replace('\\n', '\n'),
  "client_email": os.getenv("CLIENT_EMAIL"),
  "client_id": os.getenv("CLIENT_ID"),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
})

# Open the spreadsheet by its title
spreadsheet = gc.open("Controle Financeiro")

def retrieve_data(delete_na: bool = False) -> pd.DataFrame:
    # Get the first worksheet in the spreadsheet
    worksheet = spreadsheet.get_worksheet(0)

    # Use the `get_as_dataframe` method to retrieve the data as a list of lists
    data = get_as_dataframe(worksheet)

    if delete_na:
        data = data.dropna(how="all", axis=1).dropna(how="all", axis=0)

    data[Headers.DATE] = pd.to_datetime(data[Headers.DATE], format="%d/%m/%Y")
    data[Headers.STAMP] = pd.to_datetime(data[Headers.STAMP])
    data[Headers.AMOUNT] = pd.to_numeric(data[Headers.AMOUNT], errors="coerce")

    return data
