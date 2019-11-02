# Parameters, Unpacking, Variables

#In this exercise we will cover one more input method you can use
#to pass Variables to a script.

from sys import argv #This is how you add features to your script from py deature set.
#argv is the argument variable, the variable holds the arguments you pass ro your py script when you run it.
#read the WYSS section for how to run this 

script, first, second, third = argv 
#unpacks argv so that, rather than holding all the arguments, it gets assigned to four variables you
#you can work with script , first, second,third.


print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)