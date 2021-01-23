import gspread
from oauth2client.service_account import ServiceAccountCredentials

from datetime import datetime

# use creds to create a client to interact with the Google Drive API
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client-secret-1b2169c48bf5.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("EANy").sheet1

# Extract and print all of the values
ean_file = sheet.get_all_records()


def get_dates():
    date_list = []

    for date_item in ean_file:
        date_list.append(date_item['Data'])

    date_list = list(set(date_list))
    date_list.sort(key=lambda date_str: datetime.strptime(date_str, "%d-%m-%Y"), reverse=True)

    return date_list


def get_eans(selected_date):
    filter_eans = [ean['Ean'] for ean in ean_file if ean['Data'] == selected_date]

    return filter_eans


date = get_dates()
