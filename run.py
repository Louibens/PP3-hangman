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


def get_word(word_options):
    '''
    Create a single list from words worksheet
    Use Random to select one word from single list
    '''
    single_list = [item for sublist in word_options for item in sublist]
    word = random.choice(single_list)

    return word.upper()


def hangman():
    '''
    use get_word function to select random word

    '''
    selected_word = get_word(word_options) # use get_word function to randomly select a word from the words worksheet
    word_letters = set(selected_word) # identify letters in the word
    alphabet = set(string.ascii_uppercase) 
    guessed_letters = set()

    lives = 7
    points = 0

    while len(word_letters) > 0 and lives > 0:

        print('You have used these letters: ', ' '.join(guessed_letters))
        print('You have', lives, 'lives left')

        word_list = [letter if letter in guessed_letters else '_' for letter in selected_word]
        print('Current word: ', ' '.join(word_list))

        '''
        Get user input
        '''
        user_guess = input('Pick a letter: ').upper()

        if user_guess in alphabet - guessed_letters:
            guessed_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                points += 50

            else:
                lives = lives - 1
                print('That letter is not in the word.')

        elif user_guess in guessed_letters:
            print('You have already picked that letter. Please try again.')

        else:
            print('Invalid choice. Please choose a letter of the alphabet')

    if lives == 0:
        print('You just died. The word was', selected_word)
    else:
        print('Congratulations! You guessed the word was ', selected_word, 'You scored', points, 'points!')

hangman()
