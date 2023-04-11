# Hangman - Python

[View the live project here](https://pp3-hangman-lb.herokuapp.com/)

![image](put image here)

This is a game of Hangman built using Python which runs in the Code Institute mock terminal on Heroku.
Users will be able to enter their username, play the game of hangman and view a leaderboard. 


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
        3. As a First Time Visitor, I want to be able to easily interact with the site to tner my username.
        4. As a First Time Visitor, I want to be able to access the leaderboard.
        5. As a First Time Visitor, I want to be able to easily play another game or quit when I want.
        
    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to be able to access and view the quiz quickly and easily.

    -   #### Frequent Visitor Goals
    
        1. As a Frequent Visitor, I want to be able to find different categories to keep the game interesting.
      
## Features

#### Existing Features

- __F01 Title__

    - Game starts by displaying typed message to welcome user to the game of hangman.


    
- __F02 Username__

    - The user is invited to enter their name in order to continue.
    - The user will see an error if they do not enter a name.


- __F03 Instructions screen__
    
    - The user can see how the game is played.
    - The user can return to the main menu.
    
- __F04 Hangman screen__
    
    - The user can see how many points they have.
    - The user can see how many letters are in the randomly selected word.
    - The user can see which letters they have already chosen.
    - The user can see which letters are in the selected word.
    - The user can see a hangman graphic illustrating the hangman body parts.
    
- __F05 Leaderboard screen__
    
    - The user can see the top 10 leaderboard.
    - The user can return to the main menu.
    

#### Future Features

- Categories can be added for future development to ensure return users are getting value and finding new things to keep them interested


## Design

-   ### Title/Logo
    -   The Hangman title/logo was created on patorjk.com. This design was selected as it is easy for the user to read and has a strong impact on the screen

-   ### Imagery
    -   The hangman graphics are adapted from [Tech With Mike](https://www.mrmichaelsclass.com/python-programming/python-projects/hangman#h.p_gOiYJsG0n6_P)

-   ### Colour
    -   Imported colorama to enable different colour text to improve user experience and user feedback


-   ### Flow chart

    ![image](/docs/flowchart.png)

#### Home Screen chart
![image]( )

#### Quiz Screen chart
![image]( )

#### Leaderboard Screen chart
![image]( )

## Technologies Used

### Languages Used

-   [Python](https://www.python.org/)


### Python Modules

* [random](https://docs.python.org/3/library/random.html?highlight=random#module-random) - to select random words 

* [gspread](https://docs.gspread.org/en/latest/index.html) - to edit worksheets on Google Sheets.

* [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html) - to connect with Google account and have access to Google Drive.

* [colorama](https://pypi.org/project/colorama/) - to add colour to the text displayed to user.

* [string](https://docs.python.org/3/library/string.html?highlight=string#module-string) - .

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

- kiku

 ### Automated Validator Testing

- [HTML Validator](https://validator.w3.org/)

    - result for index.html

    ![image]( )

 - [CSS Validator](https://jigsaw.w3.org/css-validator/)

    ![image]( )

- [PageSpeed Insights](https://pagespeed.web.dev/)



## Deployment

### How this site was deployed

- Login to Github
- gegege
  
### How to clone the repository

- vree

### How to clone the repository

- Ggeerebe

## Credits

### Content

- Avvfdve

### Code research

- Initial inspiration to build hangman game from Code Institute PP3 MVP example project [Link](https://github.com/PedroCristo/portfolio_project_3)
- Research ways to code hangman game Youtube [Link](https://www.youtube.com/watch?v=7sVnul-StrU&t=944s)
- Research ways to code hangman game YouTube provided by [freeCodeCamp Youtube](https://www.youtube.com/watch?v=8ext9G7xspg)
- Typewriter effect researched on Stack Overflow [Link](https://stackoverflow.com/questions/20302331/typing-effect-in-python)

### Acknowledgements

- Thank you to my family that have made the time for me to get my head around javascript (to some extent). And for continually testing and providing feedback so I could push myself and improve my knowledge along with the site.
- A massive thanks also goes to my mentor, Elaine Roche, who continues to support me and help me to grow with her excellent feedback and expertise which has been much appreciated throughout the development of this project.
