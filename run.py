import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')

leaderboard = SHEET.worksheet('leaderboard')
words = SHEET.worksheet('words')

word_options = words.get_all_values()

#options = word_options.split() # Converts string of words into a list of strings 
print(word_options)

data = leaderboard.get_all_values()



print(data)