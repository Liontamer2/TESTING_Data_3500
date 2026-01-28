"""
Programming Activity 1
Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
 - Gen Beta - Everything greater then 2025 
 - Gen Alpha 2025
 - Gen Z 2010
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""

year_born = 0000
year_born = int(input("What year were you born in: "))

if year_born <= 1946:
    print("You are a Silent Generation!")
elif year_born > 1946 and year_born <= 1965: 
    print("You are Baby Boomer!")
elif year_born > 1965 and year_born <= 1981: 
    print("You are a Gen X!")
elif year_born > 1981 and year_born <= 1997: 
    print("You are a Millennial!")
elif year_born > 1997 and year_born <= 2010: 
    print("You are Gen Z!")
elif year_born > 2010 and year_born <= 2025: 
    print("You are Gen Alpha!")
else: 
    print("You are Gen Beta!")

"""
Programming Activity 2:
Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
 - continue the loop while age is greater than 1
 - print each time "you were alive in year: " current_year
 - decrease age and current_year by one each time
 - add an else saying "you were born in year: " current_year
"""

age = int(input("What age do you turn this year: ")) 
current_year = 2026

while age != 0:
    print("You were alive during", current_year)
    age = age - 1
    current_year = current_year - 1 
else:
    print("You were born in", current_year)

"""
Programming Activity 3
Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""
for i in range(5, 100,5):
    print("i:", i)

"""
Programming Activity 4
Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
"""

num = 5
while num < 96:
    if num % 5 == 0:
        print("num:", num)
    num += 5

"""
Write in pseudocode and then in Python a program that simulates a guessing game. The program should randomly choose a number between 1 and 100. The user must guess the number, and the program will tell the user if their guess is too high, too low, or correct. The game should continue until the user guesses the correct number or chooses to quit. The program should also keep track of how many guesses the user made.
"""
import random
number = random.randint(1,100)
solved = True
guess_counter = 0
while solved == True:
    try:
        guess = int(input("Guess the secret number: "))
        if guess < number:
           print("Your guess is low. Guess Again")
           guess_counter += 1
        elif guess > number:
           print("Your guess is high. Guess again")
           guess_counter += 1
        else:
            guess_counter += 1
            print("You got it correct!")
            print("It took you", guess_counter, "guesses.")
            solved == False
            break  
    except ValueError:
        print("Invalid input. Please enter a whole number.")

"""
1. Find all the prime numbers within a given range using a for loop
2. Write a Python program to reverse a given three or more digit integer WITHOUT using lists (hint, use // and % to isolate numbers)
"""