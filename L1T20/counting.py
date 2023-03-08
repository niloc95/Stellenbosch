
word_str = input(" Please enter something: ")
char_freq = {}

for i in word_str:
    if i in char_freq:
        char_freq[i] += 1
    else:
        char_freq[i] = 1
print(char_freq)
