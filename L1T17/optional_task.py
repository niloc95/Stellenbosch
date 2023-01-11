#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T17 Optional Bonus Task 'optional_task.py' \n")

myfile = open("input.txt")
file_content = myfile.read()

#counts the total number of line in the file. 
total_lines = len(file_content.splitlines())
print("Total number of line in the file:",total_lines)

#counts the total number of words in the file.
total_words = len(file_content.split())
print("Total number of words in the file:",total_words)

#counts the total number of words in the file.
total_chars = len(file_content)
print("Total number of characters in the file:",total_chars)

# vowels list list to check against
vowels = [ 'a', 'e', 'i', 'o', 'u' ]

total_vowels = 0
for total_chars in file_content:
    if total_chars in vowels:
        total_vowels = total_vowels + 1
print("total number of vowels:", total_vowels)



