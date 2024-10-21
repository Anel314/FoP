# print("------------------TASK 1-------------------------")
# def hotel_cost(nights,guests):
#     return nights*25*guests

# n=int(input("How many nights>"))
# g=int(input("How many guests>"))
# print(f"The cost for your hotel reservation will be {hotel_cost(n,g)}$")



# print("------------------TASK 2-------------------------")
# def bingo(n):
#     if n==7:
#         return "Bingo"
#     return "Better luck next time"

# print(bingo(7))
# print(bingo(1))

# print("------------------TASK 3-------------------------")

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)



# def many_factorials(n):
#     for i in range(n):
#         print(factorial(i))

# n = int(input("Enter a number: "))
# while n==0 or n==1:
#     n = int(input("Enter a number that aint 1 or 0 : "))


# many_factorials(n)



# print("------------------TASK 4-------------------------")
# def add_digits_of_number(n):
#     suma = 0
#     while n>0:
#         suma+= n%10
#         n = n // 10
#     return suma

# def sub_digits_of_number(n):
#     sub = n%10
#     n = n//10
#     while n>0:
#         sub-= n%10
#         n = n // 10
#     return sub




# n = int(input("Enter a number: "))

# if n<1000:
#     print(add_digits_of_number(n))
# else:
#     print(sub_digits_of_number(n))



# print("------------------TASK 5-------------------------")
# n = int(input("Enter a number>"))

# def is_even(n):
#     return n%2==0

# if is_even(n):
#     n = n**2
# else:
#     n = n * (n+1)

# print(n)

# print("------------------TASK 6-------------------------")

# def greet(name = "Guest", message = "Hello ", punctuation = '!'):
#     return str(message+name+punctuation)

# print(greet(message="Hi "))


# print("------------------TASK 7-------------------------")

# age = int(input("Enter your age> "))

# def how_long(age):
#     n = int(input("For how long did you drive:"))
#     return (age-n)>=18

# def driving_license_test(age):
#     if age>=18:
#         return how_long(age)
#     return False

# print(driving_license_test(age))

# print("------------------TASK 8-------------------------")

# NUM = 6

# def guess_game():
#     print("WELCOME TO THE GUESSING GAME!")
#     attempts = 5
#     while True and attempts>0:
#         n = int(input("Guess the number:"))
#         if n>10 or n<1:
#             continue
#         if n == NUM:
#             print("Congrats you guessed the number!")
#             break
#         else:
#             attempts-=1 
#     else:
#         print("You used up all your attempts")

# guess_game()




# print("------------------TASK 9-------------------------")

# def caught_speeding(n,bday):
#     over = 5 if bday else 0
#     if n-over<=60:
#         return 0
#     elif n-over>61 and n-over<80:
#         return 1
#     elif n-over>80:
#         return 2
#     else:
#         print("Something aint good")

# print(caught_speeding(60,False))
# print(caught_speeding(65,False))
# print(caught_speeding(65,True))



# print("------------------TASK 10-------------------------")

# def funky_sum(a,b):
#     if a+b<20 and a+b>9:
#         return 20
#     return a+b
# print(funky_sum(3,4))
# print(funky_sum(9,4))
# print(funky_sum(10,11))


# print("------------------TASK 11-------------------------")

# def make_bricks(small,big,goal):
#     return small+big*5>=goal
# print(make_bricks(3,1,8))
# print(make_bricks(3,1,9))
# print(make_bricks(3,2,10))
