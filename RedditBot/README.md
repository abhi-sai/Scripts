# Reddit Defintion Bot

This script runs a Reddit Bot that defines a word when the user comments on a thread in the format 'define [word]'.

Directory:

Files : Contains html files with word definitions for each letter. This has been taken from http://www.mso.anu.edu.au/~ralph/OPTED/

WebScraper.py : Parses HTML files in the FILES directory and creates a JSON file with the complete dictionary.

Define_Bot.py : Reddit Bot script. Please note, I have imported config.py which is a file that you can create containing 
- Client ID
- Client Secret
- Username
- Password

These can be obtained from the reddit apps page.

Run the script as python Define_Bot.py
