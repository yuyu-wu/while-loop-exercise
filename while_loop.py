# Use a while loop to generate a random number between 1 and 10 until you get the number 5. Every time the loop runs, increment the variable i .

from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration


while number != 5:
    number = randint(1,10)
    i += 1
print(i)