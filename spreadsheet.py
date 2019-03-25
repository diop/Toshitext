import gspread
import pprint
from oauth2client.service_account import ServiceAccountCredentials

scope = scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
google_client = gspread.authorize(creds)

sheet = google_client.open('Toshitext').sheet1

from_privkey = sheet.cell(2,1).value
print('from_privkey --> ', from_privkey)

address = sheet.cell(2,3).value
print('address --> ', address)

# pp = pprint.PrettyPrinter()
# pp.pprint(result)

# result = sheet.get_all_records()
# result = sheet.row_values(2)
# result = sheet.col_values(5)
# result = sheet.cell(2,5).value
# sheet.update_cell(3, 5, '15555555555')
# To insert rows - row = ['priv_key', 'pub_key', 'address', 'wif', 'phone']
# index = 3
# sheet.insert_row(row, index)
# sheet.delete_row(3)
# print(sheet.row_count) to get row count
# Get phone numbers