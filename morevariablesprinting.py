###Format String###


#Everythime you "(double-quotes) around a peice of text you have been making a string.
#A string is how you make something that your program might give to a human.
#In  this excise you will learn how to make string that have variables embedded in them.
#You  embed variables inside a string by using {} sequences and then put the variable inside the {} characters.



My_name = 'Sandra M. Nova'
My_age = 27
My_height = 58 #inches
My_weight = 149 # lbs
My_teeth = 'White'
My_hair = 'Black'
My_eyes = 'Brown'

print(f"Let's tal about {My_name}.")
print(f"She's [My_weight] inches tall.")
print(f"She's [My_weight] pounds heave.")
print("Actually that's not too heavy.")
print(f"She's got {My_eyes} eyes  and [My_hair] hair.")
print(f"Her teeth are usually {My_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right

total = My_age + My_age + My_weight
print(f"If I add {My_age} , {My_height}, and {My_weight} I get {total}.")
