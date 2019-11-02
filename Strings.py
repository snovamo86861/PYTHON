#Strings can contain any number of variables tat are in your py script. Remember that a variable is any line of code where you set a name
#name = (equal) to a value. In the code for this exercise you can put that in any string with 
# In this code, types_of_people = 10  creates a variable namesd types_of_people and sets it = (equal) to 10.


types_of_people = 10
x = f"There are {types_of_people} types of people."


binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)


print(f"I said:{x}.")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ... "
e = "a string with a right side."

print(w + e)
