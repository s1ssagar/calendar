"""
calendar.py - prints calendar for specifc year
"""

print "#######################"
print "##python is beautiful##"
print "#######################"
print "####### ~ sagar #######"
print "#######################"
print "\n"
__author__ = "Sagar Singh"
__credits__ = ["Sagar Singh"]
__version__ = "1.0.1"
__maintainer__ = "Sagar Singh"
__email__ = ["pythonistsagar@gmail.com", "s1ssagar.s1ssingh@gmail.com"]


from collections import OrderedDict

def check_year(year): 
    if (year % 4) == 0: 
        if (year % 100) == 0: 
            if (year % 400) == 0: 
                return True
            else: 
                return False
        else: 
             return True
    else: 
        return False

year_dict = OrderedDict([
    ("January", 31), ("February", 28), 
    ("March", 31), ("April", 30),
    ("May", 31), ("June", 30), 
    ("July", 31), ("August", 31),
    ("September", 30), ("October", 31),
    ("November", 30), ("December", 31)
])

year_leap = OrderedDict([
    ("January", 31), ("February", 29), 
    ("March", 31), ("April", 30),
    ("May", 31), ("June", 30), 
    ("July", 31), ("August", 31),
    ("September", 30), ("October", 31),
    ("November", 30), ("December", 31)
])

week_dict = {"sunday": 0, "monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6}

week_dict_num = {0: "sunday", 1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday"}

week_abb = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
year = raw_input()

#How many times does the number 12 fit as a whole into the two last digits of the year number?
step_1 = int(year[2:]) // 12

# What is the difference between the two last digits of the year number and the product of the multiples of 12 from calculation step_1?
step_2 = int(year[2:]) - (12 * step_1)

# How many times does the number 4 fit into the result of calculation 2?
step_3 = step_2 // 4

# What is the century's anchor day?
year = int(year)
if year >= 1800 and year < 1899:
    step_4 = week_dict.get('friday')
elif year >= 1900 and year < 1999:
    step_4 = week_dict.get('wednesday')
elif year >= 2000 and year < 2099:
    step_4 = week_dict.get('tuesday')
else:
    step_4 = week_dict.get('sunday')

# Add up all the results
step_5 = step_1 + step_2 + step_3 + step_4

# print step_1, step_2, step_3, step_4, step_5

# Subtract whole multiples of 7 from the result of calculation 5. This will result in a number between 0 and 6, which corresponds to the doomsday of the year(take mod).
step_6 = week_dict_num.get(step_5 % 7)
step_6_for_leap = week_dict_num.get(week_dict.get(step_6) - 1)
# print step_6

week_days_count = 0

month = 0
if check_year(year):
    year_dict_use = year_leap
    if (week_dict.get(step_6_for_leap) - 2) < 0:
        week_days_count = ((7 + week_dict.get(step_6_for_leap)) - 2) + 1
    else:
        week_days_count = week_dict.get(step_6_for_leap) - 2 + 1
else:
    year_dict_use = year_dict
    if (week_dict.get(step_6) - 2) < 0:
        week_days_count = ((7 + week_dict.get(step_6)) - 2) + 1
    else:
        week_days_count = week_dict.get(step_6) - 2 + 1

for key, val in year_dict_use.iteritems():
    print "\n"
    print key
    # print "\n"
    print '\t'.join(week_abb)
    for j in range(1, week_days_count):
            print "\t",
    for day in range(1, val + 1):
        if week_days_count % 7 == 0:
            week_days_count = 0
            print "%s\t" % (day)
        else:
            print "%s\t" % (day),
        week_days_count += 1
print "\n\n"