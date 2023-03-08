#create a function that recursively replaces the string
def search_replace():
    #read a string from the user
    string = input("Please enter a string: ")
    #if the user enters  q then quits
    if string != 'q':
        #read substring to be replaced
        sub_str = input("Please enter the substring you wish to find: ")
        #read new string to replace
        replace_str = input("Please enter a string to replace the given substring: ")
        #Replace the substring with a new string
        new_str = string.replace(sub_str, replace_str)
        print("Your new string is: " + new_str)
        #recursively call the function
        search_replace()
        print()
    

search_replace()