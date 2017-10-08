# Import json, BeautifulSoup4 and os libraries

import json
import bs4
import os

# Directory of the files to parse
directory = os.path.join(os.getcwd(), 'Files')

# Final dictionary to dump into JSON File
word_def = {}

# Loop through all files in the directory
for filename in os.listdir(directory):

    # Open the file and create a BeautifulSoup object
    file = open(os.path.join(directory, filename))
    Soup = bs4.BeautifulSoup(file)

    # Get the words surrounded by <p> and <b> tags
    # <b> contains the words and <p> contains the word and definition
    wordsWithTags = Soup.select('b')
    fullWithTags = Soup.select('p')

    for w, d in zip(wordsWithTags, fullWithTags):
        l = []

        # Convert word to lower case for easy accessibility
        word = w.get_text().lower()
        text = d.get_text()

        # Get the definition from the line, exception might occur if the definition is blank
        try:
            t = (text.split(None, 1)[1]).split(None, 1)[1]
        except IndexError as indexerror:
            t = ' '

        # If word is already in the dictionary, append it to the list of definitions
        if word in word_def:
            s = word_def[word]
            s.append(t)
            word_def[word] = s
        else:
            l.append(t)
            word_def[word] = l

    file.close()

    # Dump into the JSON file
    with open('Dict.json', 'w') as d:
        json.dump(word_def, d)
