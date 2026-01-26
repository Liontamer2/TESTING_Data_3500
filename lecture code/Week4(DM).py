# psudocode 

# given a list of numbers, count how many of the numbers are above the average of all the numbers in the list

#nums = [1, 2, 3, 4, 5]
#count = 0 

#for num in nums: 
#    avg = avg + num / 5 
#    if num > avg:
#        count = count + 1


"""
1. establish list of numbers 
2. calculate avg
3. set up a counter to trakc desired results 
4. loop 
5. compare num to avg and increment counter appropriately 
"""

# 1 
#nums = [1, 2, 3, 4, 5]
# 2 
#avg = (nums)
# 3
#counter = 0 

# If Else If 
#if year % 4 == 0:
#    if year % 100 == 0:
#        print("not a leap year :(")
#    else:
#        print("it's a leap year")
#else:
#    print("not a leap year")

# While Loop/Statements
#while year % 4 == 0: 
#    print("it's a leap year")
#    year = year + 1

#age = 2

#while age < 9:
#    print("aww your so cute")
#    age = age + 1 
#else: 
#    print("your no longer cute")

# guess the secret number
# if the user gets to high, tell them and let the keep guessing 
# if to low, tell them and let them keep guessing
# if correct, print out that they are correct  

import random
number = random.randint(1,100)

"""
1. Set up a secrect number 
2. set up high guess 
3. set low guess 
4. set correct guess
5. change the secrect number to random number
"""

guess = 0
solved = True
print("Welcome to the Guessing Game!")

while solved == True:
    try:
        guess = int(input("Guess the secret number: "))
        if guess < number:
            print("Your guess is low. Guess Again")
        elif guess > number:
            print("Your guess is high. Guess again")
        else:
            print("You got it correct!")
            solved == False
            break  
    except ValueError:
        print("Invalid input. Please enter a whole number.")