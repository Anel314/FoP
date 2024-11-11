#TASK 1
# import math
# number  = -13
# print(math.cos(number))
# print(math.sin(number))
# print(math.fabs(number))
# print(math.sqrt(math.fabs(number)))
# print(math.log(math.fabs(number)))
# print(math.pow(number,3))
#TASK 2
# import calendar as c  
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# print(c.calendar(year,month))
# print(f"Your year is ", "a leap year"if c.isleap(year) else "not a leap year ")

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# day = int(input("Enter a day: "))
# print(c.weekday(year,month,day))

# print(list(c.day_name))
# print(list(c.month_name))

#TASK3
# import random as r
# n = r.randint(0,10)
# x = int(input("Guess: "))
# while x != n :
#     print("Guess higher") if x<n else print("Guess lower")
#     x = int(input("Guess: "))
# print("You got it")


#Task 4
# import mymodule as mm
# print(mm.nth_root(81,2))
# print(mm.gcd(6,2))
# print(mm.is_prime(8))
# print(mm.fibbonaci(10))
# print(mm.factorial(5))

#Task 5
# import mymodule as mm
# s = "Anel pravi module"
# print(mm.is_palindrom(s))
# print(mm.reverse_string(s))
# print(mm.word_count(s))
# print(mm.longest_word(s))


# Task 6
# import datetime as dt
# current_date = dt.datetime.now().date()
# new_date = dt.datetime(2050,1,1).date()
# print((new_date - current_date).days)




