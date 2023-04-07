import gspread
from google.oauth2.service_account import Credentials
import random
import string


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

word_options = words.get_all_values() #returns list of lists

data = leaderboard.get_all_values()

print(data)


def get_word(word_options):
	'''
    Get word list from words worksheet
    convert to a single list 
    use Random to pick a word from the list
    '''
    for word in word_options:
        single_list = [item for sublist in word_options for item in sublist]
        word = random.choice(single_list)

    return word.upper()


