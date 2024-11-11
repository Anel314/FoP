def nth_root(n,x):
    if n<0:
        raise ValueError
    return n**(1/x)


def gcd(a,b):
    n = 0
    if a > b:
        a,b = b,a
    for i in range(a,b):
        if a%i == 0 and b%i == 0:
            n = i
    return n


def is_prime(n):
    if n<0:
        raise ValueError
    elif n == 1 or n == 0:
        return False
    
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

def fibbonaci(n):
    curr = 0
    prev = 1
    res = 0
    results = []
    for i in range(n):
        results.append(res)
        res = prev + curr
        prev = curr
        curr = res
    return results


def factorial(n):
    if n<0:
        raise ValueError
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)


def is_palindrom(s):
    return s.lower() == s.lower()[::-1]


def reverse_string(s):
    return s[::-1]


def word_count(s):
    return sum(1 for word in s.split())


def longest_word(s):
    s = s.split()
    longest = 0
    for word in s:
        if len(word)>longest:
            longest = len(word)
    return longest





