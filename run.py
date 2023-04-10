import gspread
from google.oauth2.service_account import Credentials
import random
import string
from colorama import Fore
import sys
import time
from hangman_parts import graphics
from hangman_parts import LOGO
from hangman_parts import game_rules

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
    while True:
            username = input(Fore.WHITE + 'Enter a username: \n')
            if len(username) == 0:
                print(f"{Fore.RED}Please enter a valid username to continue!")
            else:
                return username
                

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
    while True:        
        user_choice = input(Fore.WHITE + 'Please choose an option from the list above: \n').upper()
        if user_choice == 'A':
            hangman()
        elif user_choice == 'B':
            display_leaderboard()
        elif user_choice == 'C':
            display_instructions()  
        elif user_choice == 'D':
            print(f'Thanks for playing')
            exit()
        else:
            print(f'{Fore.RED} That is not a valid option. Please try again.\n')  
            

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
    points = (len(selected_word) * 10) + 50

    while len(word_letters) > 0 and lives > 0:
        print(graphics[wrong])
        print(Fore.WHITE + 'You have', lives, 'lives left\n')
        print(Fore.WHITE + 'You have used these letters: ', ' '.join(guessed_letters),'\n')
        print(Fore.WHITE + 'You have: ', points, 'points.\n')

        word_list = [letter if letter in guessed_letters else '_' for letter in selected_word]
        print('Selected word: ', ' '.join(word_list), )
        print("====================================\n")
        '''
        Get user input
        '''
        user_guess = input(Fore.WHITE + 'Pick a letter: \n').upper()
        
        if user_guess in alphabet - guessed_letters:
            guessed_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                
                print(Fore.GREEN + user_guess, ' is in the word.')

            else:
                lives = lives - 1
                wrong = wrong + 1
                points = points - 10
                print(Fore.RED + user_guess,' is NOT in the word.')

        elif user_guess in guessed_letters:
            print(Fore.RED + 'You have already picked', user_guess, '. Please try again.\n')

        else:
            print(Fore.RED + 'Invalid choice. Please choose a letter of the alphabet.\n')

    if lives == 0:
        print(graphics[7])
        print(graphics[9])
        print(Fore.RED + 'You just died. The word was', selected_word, '\n')
    else:
        print(Fore.GREEN + 'Congratulations! You guessed the word was ', selected_word, 'You scored', points, 'points!\n')
        print(graphics[8])


def display_instructions():
    print(game_rules)
    while True:        
        go_back = input(Fore.WHITE + 'Please hit B to go back \n').upper()
        if go_back == 'B':
            game_menu()
        else:
            print(f'{Fore.RED} That is not a valid option. Please try again.\n')  
            
welcome_msg()
game_menu()


