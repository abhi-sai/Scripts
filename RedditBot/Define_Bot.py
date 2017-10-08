# Import praw and json libraries. config file contains security details for reddit
import praw
import config
import json

# Creates and instance of reddit using account credentials
bot = praw.Reddit(user_agent='RedditBot',
                  client_id=config.client_id,
                  client_secret=config.client_secret,
                  username=config.username,
                  password=config.password
                  )

# Customize the subreddit where the bot is needed
subreddit = bot.subreddit('test')

# Open JSON file containing the dictionary
dictionary = json.loads(open('Dict.json').read())

# Get every new comment
for comment in subreddit.stream.comments():
    # Fetch Body and Author
    text = comment.body
    author = comment.author

    # Format of comment should be 'define [word]'
    if 'define' in text.lower():
        # Get word
        word = text.lower().split(None,1)[1]
        # Generate a Message
        c = 'Hi, u/{0}, here is the definition for {1}:\n\n'.format(author,word)
        if word in dictionary:
            for definition in dictionary[word]:
                c = c + definition + "\n\n"
            comment.reply(c)
        else:
            comment.reply("Sorry u/{0}, that is not a valid word.")