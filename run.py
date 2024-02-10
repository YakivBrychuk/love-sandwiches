import gspread 
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)  # Authorize the client
SHEET = GSPREAD_CLIENT.open('love_sandwiches')  # Open the spreadsheet

sales = SHEET.worksheet('sales')  # Open the sales worksheet

data = sales.get_all_values()  # Get all the data from the worksheet

print(data)  # Print the data