"""
Programming Activity 1
Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
 - Gen Beta - Everything greater then 2025 
 - Gen Alpha 2025
 - Gen Z 2012
 - Zoomer 1997
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""

year_born = 0000
year_born = int(input("What year were you born in: "))

if year_born <= 1946:
    print("You are a Baby Boomer!")
elif year_born > 1946 and year_born <= 1965: 
    print("You are Gen X!")
elif year_born > 1965 and year_born <= 1981: 
    print("You are a Millennial!")
elif year_born > 1981 and year_born <= 1997: 
    print("You are a Zoomer!")
elif year_born > 1997 and year_born <= 2012: 
    print("You are Gen Z!")
elif year_born > 2012 and year_born <= 2025: 
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

