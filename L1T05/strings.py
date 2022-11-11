# Created a Variable called hero and assigned a string value ""
hero = "Super Man"

# Created a second variable to fromat and manipulate my first variable. 
# I referenced the addtional reading text book, 
# stackoverflow and geekforsgeeks.org on how to append a char 
# Below I create a variable called 
# s_hero and used the "join" function 
# with i the temp variable to loop thought the hero string  
s_hero = '^'.join(hero.upper()[i:i+1] for i in range(0, len(hero), 1))
# I printed the variable twice to remove the space between the period and DOG 
print(s_hero[0:9], s_hero[12:18])





