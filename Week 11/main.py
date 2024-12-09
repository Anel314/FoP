tup = (1,2,3,4,5,6)
def first_last(tup):
    return (tup[0], tup[-1])
print(first_last(tup))

def even_and_sum(tup):
    new = tuple((el for el in tup if el%2==0))
    new += (sum(tup),)
    return new
print(even_and_sum(tup))

def double_div_3(tup):
    return tuple(element*2 if element%3==0 else element for element in tup) 
print(double_div_3(tup))

s = {1,2,3,4,5,6,7,8}
def find_return_value_set(s,n):
    if n in s:
        print("Found")
    return set((element for element in s if element>n))
print(find_return_value_set(s,2))

def sets_n(set1,n):
    news1 = {item for item in set1 if item>n}
    news2 = {item for item in set1 if item<n}
    for e in set1:
        if e%n==0:
            print("Found a multiple of n: ", e)
    return news1,news2
print(sets_n(s,2))

chartup = tuple("Fundamentals of programming")
def chars_in_s(tup):
    d = dict()
    for element in tup:
        if element in d:
            d[element]+=1
        else:
            d[element] = 1
    return d
print(chars_in_s(chartup))

def combine_tups(t1,t2):
    new = ()
    for e in t1:
        if e in t2:
            new+= (e,)
    return new


print(combine_tups((1,2,3),(1,2,4)))