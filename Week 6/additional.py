#ONE
def palindrome_number(n):
    new_n = 0
    n_copy = n
    while n>0:
        new_n*=10
        new_n += n%10
        n//=10
    return n_copy == new_n

def next_smallest_palindrome(n):
    if palindrome_number(n+1):
        return n+1
    return next_smallest_palindrome(n+1)

#TWO
def xyz_there(s):
    for i in range(len(s)):
        if s[i:i+3] == 'xyz' and s[i-1] != '.':
            return True
    return False

#THREE
def remove_even_and_print(s):
    new_arr = []
    for i in s:
        if i%2==0:
            continue

        new_arr.append(i)
    for i in new_arr:
        print(i, end=" ")
    print()

#FOUR
def is_harshad(n):
    sum_of_digits = sum(int(i) for i in str(n))

    return n%sum_of_digits == 0

#FIVE
def alarm_clock(week_day, vacation):
    if vacation:
        if week_day==0 or week_day == 6:
            return "off"
        return "10:00"
    if week_day==0 or week_day == 6:
        return "10:00"
    return "7:00"

#SIX
def round_avg_input():
    avg = 0
    i = 0
    print("Enter nothing and press Enter if you wish to stop")
    n = input("Enter a word: ")
    while n!="":
        print("Enter nothing and press Enter if you wish to stop")
        n = input("Enter a word: ")
        avg+=len(n)
        i+=1
    return avg//(i-1)
