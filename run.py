import gspread
from google.oauth2.service_account import Credentials
import random
import string
from colorama import Fore
import sys
import time
from hangman_parts import GRAPHICS
from hangman_parts import LOGO
from hangman_parts import GAME_RULES
from prettytable import PrettyTable


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')
# returns list of lists
WORD_OPTIONS = SHEET.worksheet('words').get_all_values()
username = ''


def type(text):
    '''
    Function to enable typewriter effect
    Researched code on StackOverflow
    '''
    words = text
    for char in words:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()


def get_word(WORD_OPTIONS):
    '''
    Create a single list from words worksheet
    Use Random to select one word from single list
    '''
    single_list = [item for sublist in WORD_OPTIONS for item in sublist]
    word = random.choice(single_list)
    return word.upper()


def update_leaderboard(points):
    '''
    Create leaderboard entry and add to leaderboard
    '''
    entry = [username, points]
    leaderboard = SHEET.worksheet('leaderboard')
    leaderboard.append_row(entry)


def display_leaderboard():
    """
    Displays the top 10 scores
    Filters to only show users top score
    so same user is not displayed multiple times
    """
    print("TOP 10 SCORES")
    table = PrettyTable()
    table.field_names = SHEET.worksheet('leaderboard').row_values(1)
    data = SHEET.worksheet('leaderboard').get_all_values()
    # sorts worksheet data by second column values
    sorted_data = sorted(data[1:], key=lambda x: int(x[1]), reverse=True)
    top_ten = sorted_data[:10]
    table.add_rows(top_ten)
    print(table)

    while True:
        go_back = input(Fore.WHITE + 'Please hit B to go back \n').upper()
        if go_back == 'B':
            game_menu()
        else:
            print(Fore.RED + 'That is not a valid option. Please try again.\n')


def welcome_msg():
    '''
    welcome message and username input

    '''
    print("\033c")  # clear the screen
    type('T H A N K   Y O U   F O R   V I S I T I N G   M Y   G A M E   O F\n')
    print(LOGO)
    type("E N T E R   Y O U R   N A M E   T O   C O N T I N U E"'\n')
    print("\n")
    global username  
    while True:
        username = input(Fore.WHITE + 'Enter a username: \n').capitalize()
        if len(username) == 0:
            print(f"{Fore.RED}Please enter a valid username to continue!")
        else:
            break


def game_menu():
    '''
    present user with menu options
    '''
    print(f"""{Fore.WHITE}
        A - PLAY HANGMAN
        B - LEADERBOARD
        C - INSTRUCTIONS
        D - EXIT GAME
        """)
    while True:
        user_choice = input(Fore.WHITE + 'Please choose an option from the '
                            'list above: \n').upper()
        if user_choice == 'A':
            hangman()
        elif user_choice == 'B':
            display_leaderboard()
        elif user_choice == 'C':
            display_instructions()
        elif user_choice == 'D':
            print(f'Thanks for playing {username}')
            exit()
        else:
            print(Fore.RED + 'That is not a valid option. Please try again.\n')


def hangman():
    '''
    Use get_word function to select random word and begin game.
    Researched elements of below code on FreeCodeCamp youtube - link in readme
    '''
    print("\n")
    print(f"Great! Let's get started {username}!")
    type("S E L E C T I N G   W O R D . . . ."'\n')
    type("L E T 'S   G O!!"'\n')
    # use get_word function to randomly select a word from the words worksheet
    selected_word = get_word(WORD_OPTIONS)
    word_letters = set(selected_word)  # identify letters in the word
    # specify letters that are valid user choices
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()
    wrong = 0
    lives = 7
    points = (len(selected_word) * 10) + 50

    while len(word_letters) > 0 and lives > 0:
        print(GRAPHICS[wrong])  # displays appropriate hangman graphic
        print(Fore.WHITE + 'You have', lives, 'lives left\n')
        print(Fore.WHITE + 'You have used these letters: ', ', '
              .join(guessed_letters), '\n')
        print(Fore.WHITE + 'You have: ', points, 'points.\n')

        word_list = [letter if letter in guessed_letters
                     else '_' for letter in selected_word]
        print('Selected word: ', ' '.join(word_list))
        print("====================================\n")
        # get user to pick a letter
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
                print(Fore.RED + user_guess, ' is NOT in the word.')
        elif user_guess in guessed_letters:
            print(Fore.RED + 'You have already picked', user_guess,
                  '. Please try again.\n')
        else:
            print(Fore.RED + 'Invalid choice. Please choose a '
                  'letter of the alphabet.\n')
    if lives == 0:
        print(GRAPHICS[7])  # full hangman graphic
        print(GRAPHICS[9])  # you lose graphic
        print(Fore.RED + 'You just died. The word was', selected_word, '\n')
    else:
        print(Fore.GREEN + 'Congratulations! You guessed the word was ',
              selected_word, 'You scored', points, 'points!\n')
        print(GRAPHICS[8])  # you win graphic
    update_leaderboard(points)
    game_menu()


def display_instructions():
    '''
    display instructions stored in hangman_parts.py
    '''
    print(GAME_RULES)
    while True:
        go_back = input(Fore.WHITE + 'Please hit B to go back \n').upper()
        if go_back == 'B':
            game_menu()
        else:
            print(f'{Fore.RED} That is not a valid option.'
                  'Please try again.\n')


welcome_msg()
game_menu()
