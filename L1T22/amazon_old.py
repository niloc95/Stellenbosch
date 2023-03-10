# Funcition import
import statistics
# File opening
with open( 'input.txt' ) as textFile :
    # Reading the file
    textRead = textFile.read()
#Opening and writing to the output file "out.txt" 
text_files = open("out.txt", "x")
text_files = open("out.txt", "w")
#Looping thru each line of the file
for line in textRead.split('\n') :
    operations, numbers = line.split(':')
    operations = operations.strip()  
    numbers = map( float, numbers.strip().split(",") )

    if operations == 'Avg' :
        text_files.write('\nThe value of average of [1,2,3,5,6] is '+str(statistics.mean(numbers)))

    if operations == 'Min' :
        text_files.write('The value of min of [1,2,3,5,6] is '+str(min(numbers)))

    if operations == 'Max' :
        text_files.write('\nThe value of max of [1,2,3,5,6] is '+str(max(numbers)))
    

text_files.close()
text_files = open("out.txt", "r")
print(text_files.read())