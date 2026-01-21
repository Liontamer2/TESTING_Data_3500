"""
Programming Activity 1
 1. make a variable called apple_price (set it to whatever you want)
 2. make a variable called number_purchased (set it to whatever you want)
 3. make a variable called tax and set it equal to 1.07
 4. make a variable, total_bill and calculate it by: total_bill = apple_price * number_purchased * tax
 5. print clearly and cleanly how many apples were purchased and the total_bill
 6. add a check before the final print statement to see if total_bill is equal to 0.  If so, print a message to the user to check their inputs.
"""

apple_price = 3.50
number_purchased = 12
tax = 1.07
total_bill = apple_price * number_purchased * tax 
print("You purchased", number_purchased,"many apples for this price", apple_price,".", "Your total bill was", round(total_bill,2))

"""
Programming Activity 2
Write a program that asks the user how old they are, and what age they would like to live to. Calculate how long they have left to live (approximately), and then print a friendly message telling the user how long they have to live.
"""
age = int(input("What is your age: "))
age_hope = int(input("What age do you want to live to: "))

life_hope_time = age_hope - age 
print("You have", life_hope_time, "many years to live my friend.")

"""
Programming Activity 3
Write a program that gets a user's score in this class, as a percentage i.e. 90 or 95. Write an if statement that checks to see if their score is equal to or greater than 93.  If so, print "Congratulations you got an A" else print "Congratulations, you still learned a ton!!!!"
"""

grade = int(input("What is your score in Data 3500?: "))
if grade >= 93: 
    print("Congratulations you got an A!")
else: 
    print("Congratulations, you still learned a ton!!!!")