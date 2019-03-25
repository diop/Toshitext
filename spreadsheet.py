import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
print(creds)
client = gspread.authorize(creds)

sheet = client.open('Toshitext').sheet1

print(sheet)

addresses = sheet.get_all_records()

print(addresses)
