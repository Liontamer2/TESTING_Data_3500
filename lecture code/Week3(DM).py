# variables 

first_name = "Daniel"
last_name = "Moore"
age = 20 
is_it_monday = False
gas_price = 2.50

# math

age = 21
#print(age)
age = age + 1
#print(age)  

# print function

#print()
#print(age, first_name, last_name)

# triple quote 

"""
2.3 Description of the problem here. Do all math. Solve all problems

Can be multi line but you can put it all here and it not be output
"""

menu = """
Pizza          $5
Hot Dog        $5
Soda           $3
Fries          $4
Popcorn        $10
Popcorn Bucket $30
"""
#print(menu)

#Example Problem 
""" 
Adam is running a half marathon. His avg. mile time is 5:55. 
For the half (13.1), what is his projected finish time?
Output result in Time: hr:min:sec
"""

minutes = 5
sec = 55
pace_secs = sec + (minutes * 60)

total_half_sec = pace_secs * 13.1 

projected_hrs = total_half_sec // 3600 
projected_min = (total_half_sec % 3600) // 60
projected_secs = (total_half_sec % 3600) % 60
print("Time:", int(projected_hrs), ":", int(projected_min),":", projected_secs)

# Dynamic Types
# x = 1 
# x = " Aggie Basketball"
# x = True

# print(type(x))
# Input
#age = int(input("Please enter your age: "))
#print("On your next brithday you will be", int(age) + 1)

# Casting
#int()
#str() 
#float() 
#bool()
#eval() # trying to figure out the best type

# If
#age = 12 
#if age > 19: 
#    print("The best years of your life.")
#if age >= 13:
#    print("You are a teenager. Have Fun :)")
#if age < 13:
#    print("You are still a child :)")

#if age >= 18:
#    print("Adult")
#elif age >= 13:
#    print("teenager") 
#else:
#    print("child")

# If - Hurd Premium EX
#student = input("Are you a Student at USU: (Y/N)")
#hurdP = input("Do you have Hurd Premium: (Y/N)")

#if student == "Y":
#    print("You get into the game for free!")
#if hurdP == "Y"
#  print("You get into the game 15 minutes early!")
#else: 
#    print("Buy a ticket. They are not to expensive!")
# Min, Max, Range

#grades = [89, 56, 100, 100, 90, 0, 5]

#print("min:", min(grades))
#print("max:", max(grades))

#print(range(1,10))