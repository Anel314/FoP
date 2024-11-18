def count_down(n):
    print(n)
    if n==0:
        return 0
    return count_down(n-1)

def pow(n,e):
    if e==0:
        return 1
    return pow(n,e-1)*n

def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)

def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

def count_digits(n):
    if n<=0:
        return 0
    return count_digits(n//10)+1
