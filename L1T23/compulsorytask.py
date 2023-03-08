# def print_values_of(dictionary, keys):
#     for key in keys:
#         print(dictionary[k])

# simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": 'd'oh', "maggie": " (Pacifier Suck)"}

# print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')

# '''
#     Expected console output:

#     BAAAAAART!
#     Eat My Shorts!
#     d'oh!

# '''

def print_values_of(dictionary, *keys):
    for key in keys:
        print(dictionary[key])

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": " (Pacifier Suck)"}

print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')

#In the function definition, keys should be changed to *keys to indicate that it accepts any number of positional arguments.
#In the for loop, dictionary[k] should be changed to dictionary[key] to access the value associated with the current key.
#When calling print_values_of, the keys should be passed as separate arguments, so they should be 
# enclosed in parentheses to indicate a tuple of arguments. Alternatively, you can change the 
# function definition to accept a list of keys instead of multiple arguments, and then pass a list of keys to it.
