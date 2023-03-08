#creating recursive function to add number 
def adding(arr_listInt, arr_indexNum):
   #id the index is 0 then return array value
   if arr_indexNum == 0: 
        return arr_listInt[0]
   #recursively add all the number until index
   else:
        return arr_listInt[0] + adding(arr_listInt[1:], arr_indexNum-1)

#print the result as shown below example
print(adding([1, 4, 3, 5, 12, 16], 4))

print(adding([4, 3, 1, 5], 1))

print(adding([1, 4, 3, 5, 12, 16], 2))