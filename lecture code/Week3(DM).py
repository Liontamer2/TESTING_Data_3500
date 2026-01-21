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
Adam is running a half marathon. His avg. mile time is 6:00. 
For the half (13.1), what is his projected finish time?
Output result in Time: hr:min:sec
"""

avg_mile_time = 6.00
half_length = 13.1
avg_half_time_hr = (avg_mile_time * half_length) // 60
avg_half_time_min = round((avg_mile_time * half_length) - 60)
avg_half_time_sec =  round((avg_mile_time * half_length) - 78)
print("Time:",avg_half_time_hr,":",avg_half_time_min, ":",avg_half_time_sec)



