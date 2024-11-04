# print("----------------Task 1------------------")
# s = "Programming"
# print(s[3:7])
# print(s[-4:])
# print(s, "is fun")

# print("----------------Task 2------------------")
# #My way
# def reverse(s):
#     return s[::-1]

# def reverse2(s):
#     new_s = ""
#     for i in s:
#         new_s = i + new_s
#     return new_s
# print(reverse2("apple"))


# print("----------------Task 3------------------")
# def number_of_occurencies(s,n):
#     count = 0
#     for i in range(len(s)):
#         if s[i:i+len(n)] == n:
#             count+=1
#     return count
# print(number_of_occurencies("aaaa", "aa"))


# print("----------------Task 4------------------")
# def dupe_chars(s):
#     new_s = ""
#     for i in s:
#         new_s+= i*2
#     return new_s
# print(dupe_chars("Anel"))

# print("----------------Task 5------------------")
# def find_xyz(s):
#     n = s.find("xyz")
#     if n==0:
#         return True
#     elif n!=-1 and s[n-1] != '.':
#         return True
#     return False


# print(find_xyz("xyz"))
# print(find_xyz(".xyz"))
# print(find_xyz("xyz.xyz"))
# print(find_xyz("xyz."))



# print("----------------Additional Task  from Lejla------------------")

# def is_palindrome1(s):
#     return s == s[::-1]

# def is_palindrome2(s):
#     return s == reverse2(s)

# def is_palindrome3(s):
#     rev = ""
#     for i in s:
#         rev = i + rev
#     return s == rev


# print(is_palindrome1("racecar"))
# print(is_palindrome2("racecar"))
# print(is_palindrome3("racecar"))

# print(is_palindrome1("Anel"))
# print(is_palindrome2("Anel"))
# print(is_palindrome3("Anel"))


# print(is_palindrome1(""))
# print(is_palindrome2(""))
# print(is_palindrome3(""))



def xyz(s):
    for i in range(len(s)-2):
        if s[i:i+3] == "xyz" and (s[i-1] != "." if i!=0 else True):
            return True
    return False


print(xyz("xyz"))
print(xyz(".xyz"))
print(xyz("xyz.xyz"))
print(xyz("xyz."))
