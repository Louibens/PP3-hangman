# Hangman - Python

[View the live project here](https://pp3-hangman-lb.herokuapp.com/)

![image](put image here)

This is a game of Hangman built using Python which runs in the Code Institute mock terminal on Heroku.
Users will be able to enter their username, play the game of hangman and view a leaderboard. 
The leaderboard and a list of words are stored on a google sheet.


## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals
        1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        2. As a First Time Visitor, I want to be able to easily view the instructions on how to play.
        3. As a First Time Visitor, I want to be able to easily interact with the site to enter my username.
        4. As a First Time Visitor, I want to be able to easily access the leaderboard.
        5. As a First Time Visitor, I want to be able to easily play another game or quit when I want.
        
    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to be able to access and view the game quickly and easily.

    -   #### Frequent Visitor Goals
    
        1. As a Frequent Visitor, I want to be able to find different categories or levels to keep the game interesting.
      
## Features

#### Existing Features

- __F01 Title__

    - Game starts by displaying typed message to welcome user to the game of hangman.

![image](/docs/game_screenshot.png)
    
- __F02 Username__

    - The user is invited to enter their name in order to continue.
    - The user will see an error if they do not enter a name.

![image](/docs/HM_username.png)

- __F03 Menu__

    - The user must choose an option from the menu.
    - The user will see an error if they do not enter a valid option.

![image](/docs/HM_menu.png)

- __F04 Instructions screen__
    
    - The user can see how to play the game.
    - The user can return to the main menu.
    
![image](/docs/HM_instructions.png)

- __F05 Hangman screen__
    
    - The user can see how many points they have.
    - The user can see how many letters are in the randomly selected word.
    - The user can see which letters they have already chosen.
    - The user can see which letters are in the selected word.
    - The user can see a hangman graphic illustrating the hangman body parts.
    
![image](/docs/HM_gameplay.png)

- __F06 Leaderboard screen__
    
    - The user can see the top 10 leaderboard.
    - The user can return to the main menu.
    
![image](/docs/HM_leaderboard.png)    

#### Future Features

- Categories/levels can be added for future development to ensure return users are getting value and finding new things to keep them interested.


## Design

-   ### Title/Logo
    -   The Hangman title/logo was created on patorjk.com. This design was selected as it is easy for the user to read and has a strong impact on the screen

-   ### Imagery
    -   The hangman graphics are adapted from [Tech With Mike](https://www.mrmichaelsclass.com/python-programming/python-projects/hangman#h.p_gOiYJsG0n6_P)

-   ### Colour
    -   Imported colorama to enable different colour text to improve user experience and user feedback


-   ### Flow chart

    ![image](/docs/flowchart.png)


## Technologies Used

### Languages Used

-   [Python](https://www.python.org/)


### Python Modules

* [random](https://docs.python.org/3/library/random.html?highlight=random#module-random) - to select random words 

* [gspread](https://docs.gspread.org/en/latest/index.html) - to edit worksheets on Google Sheets.

* [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html) - to connect with Google account and have access to Google Drive.

* [colorama](https://pypi.org/project/colorama/) - to add colour to the text displayed to user.

* [string](https://docs.python.org/3/library/string.html?highlight=string#module-string) - to import alphabet letters to verify and record users entry.

* [PrettyTable](https://pypi.org/project/prettytable/) - to display leaderboard scores.

### Frameworks, Libraries & Programs Used

This project used:

* [Git](https://git-scm.com/) for version control.

* [GitHub](https://github.com/) to store the project files.

* [VS Code](https://code.visualstudio.com/) as the IDE for development.

* [Heroku](https://www.heroku.com/home/) to deploy the website.

* [Lucidchart](https://www.lucidchart.com/) to create the flow chart.

* [patorjk - Text to ASCII Art Generator (TAAG)](https://patorjk.com/software/taag/#p=display&f=Big%20Money-ne&t=Hangman) to create the logo and win/lose graphic displays.
    
## Testing

### Manual Test Cases and Results

![image](/docs/manual_testing.png)

 ### Automated Validator Testing

- [Python Validator](https://pep8ci.herokuapp.com)

    - result for run.py

    ![image](/docs/linter-resolved.png)

    2 issues below flagged and have been resolved 

    - 97: W293 blank line contains whitespace
    - 229: W292 no newline at end of file

## Deployment

### How this site was deployed

- Login to Heroku.
- On the Dashboards page click 'New' and select 'Create New App'.
- Enter a unique app name and select your region. Then click 'Create App' .
- On the next page displayed, click on the Settings tab.
- Click 'Reveal Config Vars' and enter PORT as key and 8000 as the value. Click 'Add'.
- Also add CREDS as Key and the google credentials into the value box.
- In the Buildpack section, select Python from 'Add Buildpack' and Save.
- In the same Buildpack section, select node.js from 'Add Buildpack' and Save. Node.js to be done after Python as needs to be in this order.
- Go to the Deploy tab and choose Gibhub as the deployment method.
- Find the repository name and connect.
- At the bottom of the page select to deploy manually or automatically.
- A link to the deployed page can be seen once deployment is complete.


  The live link can be found here - [Hangman](https://pp3-hangman-lb.herokuapp.com/) 
  
### How to clone the repository

- Go to the [PP3-hangman](https://github.com/Louibens/PP3-hangman) repository on GitHub 
- Click the "Fork" button in the top right corner

### How to clone the repository

- Go to the [PP3-hangman](https://github.com/Louibens/PP3-hangman) repository on GitHub 
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there
- Open a GitBash terminal and navigate to the directory where you want to locate the clone
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process

## Credits

### Code research

- Initial inspiration to build hangman game from Code Institute PP3 MVP example project [Link](https://github.com/PedroCristo/portfolio_project_3)
- Research ways to code hangman game Youtube [Link](https://www.youtube.com/watch?v=7sVnul-StrU&t=944s)
- Research ways to code hangman game YouTube provided by [freeCodeCamp Youtube](https://www.youtube.com/watch?v=8ext9G7xspg)
- Typewriter effect researched on Stack Overflow [Link](https://stackoverflow.com/questions/20302331/typing-effect-in-python)
- Clear terminal screen researched on Stack Overflow [Link](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
- How to sort leaderboard by score and show top 10 researched on Stack Overflow [Link](https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda)
- How to handle line too long error researched on Stack Overflow [Link](https://stackoverflow.com/questions/53158284/python-giving-a-e501-line-too-long-error)

### Acknowledgements

- Thanks to my mentor, Elaine Roche, who continues to support me and help me to grow with her excellent feedback and expertise which has been much appreciated throughout the development of this project.
