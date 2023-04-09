import gspread
from google.oauth2.service_account import Credentials
import random
import string
from colorama import Fore
import sys
import time
from hangman_parts import parts

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')


words = SHEET.worksheet('words')

word_options = words.get_all_values() #returns list of lists

LOGO = '''
/$$   /$$                                                                
| $$  | $$                                                                
| $$  | $$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$ 
| $$$$$$$$ |____  $$| $$__  $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$__  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$
| $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$  | $$
| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$
|__/  |__/ \_______/|__/  |__/ \____  $$|__/ |__/ |__/ \_______/|__/  |__/
                               /$$  \ $$                                  
                              |  $$$$$$/                                  
                               \______/   
'''

def type(text):
  words = text
  for char in words:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()


def get_word(word_options):
    '''
    Create a single list from words worksheet
    Use Random to select one word from single list
    '''
    single_list = [item for sublist in word_options for item in sublist]
    word = random.choice(single_list)

    return word.upper()


def welcome_msg():
    '''
    welcome message and username input
    '''
    type(f'T H A N K   Y O U   F O R   V I S I T I N G   M Y   G A M E   O F\t\n') 
    print(LOGO)
    type(f"E N T E R   Y O U R   N A M E   T O   C O N T I N U E"'\n')
    print("\n")
    username = input(Fore.WHITE + 'Enter a username: ').upper()





def game_menu():
    '''
    present user with menu options
    '''
    print( f"""{Fore.WHITE}
        A - PLAY HANGMAN
        B - LEADERBOARD
        C - INSTRUCTIONS
        D - EXIT GAME
        """)
    user_choice = input(Fore.WHITE + 'Please choose an option from the list above: ').upper()

    if user_choice == 'A':
        hangman()
    elif user_choice == 'B':
        return display_leaderboard()
    

def hangman():
    '''
    use get_word function to select random word and begin game
    '''
    print("\n")
    print(f"Great! Let's get started")
    type(f"S E L E C T I N G   W O R D . . . ."'\n')
    type(f"L E T 'S   G O!!"'\n')
    
    selected_word = get_word(word_options) # use get_word function to randomly select a word from the words worksheet
    word_letters = set(selected_word) # identify letters in the word
    alphabet = set(string.ascii_uppercase) 
    guessed_letters = set()
    wrong = 0
    lives = 7
    points = 0

    while len(word_letters) > 0 and lives > 0:
        print(parts(wrong))
        print(Fore.WHITE + 'You have', lives, 'lives left\n')
        print(Fore.WHITE + 'You have used these letters: ', ' '.join(guessed_letters),'\n')

        word_list = [letter if letter in guessed_letters else '_' for letter in selected_word]
        print('Selected word: ', ' '.join(word_list), )
        print("====================================\n")
        '''
        Get user input
        '''
        user_guess = input(Fore.WHITE + 'Pick a letter: ').upper()
        
        if user_guess in alphabet - guessed_letters:
            guessed_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                points += 50
                print(Fore.GREEN + user_guess, ' is in the word.\n')

            else:
                lives = lives - 1
                wrong = wrong + 1
                print(Fore.RED + user_guess,' is NOT in the word.\n')

        elif user_guess in guessed_letters:
            print(Fore.RED + 'You have already picked', user_guess, '. Please try again.\n')

        else:
            print(Fore.RED + 'Invalid choice. Please choose a letter of the alphabet.\n')

    if lives == 0:
        print(parts(7))
        print(Fore.RED + 'You just died. The word was', selected_word, '\n')
    else:
        print(Fore.GREEN + 'Congratulations! You guessed the word was ', selected_word, 'You scored', points, 'points!\n')
        print(parts(8))


welcome_msg()
game_menu()


