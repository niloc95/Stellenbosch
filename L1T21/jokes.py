import random  #import this module to generate a random number
#import pyjokes to get random jokes
# ref: https://www.geeksforgeeks.org/python-script-to-create-random-jokes-using-pyjokes/
import pyjokes
#create a list of jokes using the get_jokes() method of the pyjoke module
#set the language to English and category to all

jokes = pyjokes.get_jokes(language="en", category="all")
#print a random joke from the list of jokes using the choice() method
#of the random module
print(random.choice(jokes))