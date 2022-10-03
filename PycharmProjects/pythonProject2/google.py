from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import datetime
import time

username_tiktok    = ('sdsadsa@fdsfsd.com')
password_tiktok    = ('dsad13213')

web_tiktok_login   = ('https://www.tiktok.com/login/phone-or-email/email')
web_tiktok_live    = ('')

def get_values(spreadsheet_id, range_name):
    """
    Creates the batch_update the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
        """
    creds, _ = google.auth.default()
    # pylint: disable=maybe-no-member
    try:
        service = build('sheets', 'v4', credentials=creds)

        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])
        # print(f"{len(rows)} rows retrieved")
        # print(rows)
        for date in rows:
            print(date[0])
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

if __name__ == '__main__':
    # Pass: spreadsheet_id, and range_name

    a = get_values("1muBCO_GTCEZDB7IX2WeDev9nKkHdUS1iDhAoOqRnRFY", "A1:A10").text
    b = get_values("1muBCO_GTCEZDB7IX2WeDev9nKkHdUS1iDhAoOqRnRFY", "B1:B10").text
    c = get_values("1muBCO_GTCEZDB7IX2WeDev9nKkHdUS1iDhAoOqRnRFY", "C1:C10").text

