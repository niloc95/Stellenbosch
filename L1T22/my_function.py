# First Function
def funcWeekdays():
    #print the day of a week using the print statement
    print("Sunday")
    print("Monday")
    print("Tuesday")
    print("Wednesday")
    print("Thursday")
    print("Friday")
    print("Saturday")
        
# Second Function
def funcHello(str_Sentence):
    Hello = ""
    i = 0
    for hello in str_Sentence.split():
        #if the index is 2, add hello to the sentenceWithHello in place 
        #of the actual word in the sentence
        if i % 2 == 1:
            Hello += "hello "
        else:   #Otherwise add the word in the sentence
            Hello += hello + " "
        i += 1
    #remove the space added at the end in the sentence 
    Hello = hello[:-1]
    #return the value of the Hello
    return hello

#Functions call 
funcWeekdays()
#function call hello() and pass a sentence

#the function will return a string in which every second word is hello
the_sentence = "This function replaces every second word of the sentence with hello"
print(the_sentence, ": => The below sentence is the using the function funcHello which replaces every second word")
print(funcHello(the_sentence))