import numpy as np
mymatrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
mynums = np.array([1,2,3,4,5,6,7,8])

def replace_with_condition(array, condition, replace):
    for subarray in array:
        subarray[subarray > condition] = replace
# replace_with_condition(mymatrix,5,0)
# print(mymatrix)

def custom_mask_with_logic(array, condition, replacement):
    array[array>condition] **= 2
    array[array<condition] = replacement
# custom_mask_with_logic(mynums,5,0)
# print(mynums)



def double_diagonal_elements(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if i==j:
                if array[i][j]%2==0:
                    array[i][j]*=2
                else:
                    array[i][j]+=3 
# double_diagonal_elements(mymatrix)
# print(mymatrix)

def generate_checkerboard():
    row = []
    res = []
    place = 0
    for i in range(8):
        row=[]
        for j in range(8):
            if place%2==0:
                row.append(0)
            else:
                row.append(1)
            place+=1
        res.append(row)
        place -=1
    
    return np.array(res)
# print(generate_checkerboard())

def move_zeroes(array):
    length = len(array)
    count=0
    new = []

    for i in range(length):
        if array[i] == 0:
            count+=1
        else:
            new.append(array[i])
    for i in range(count):
        new.append(0)
    return np.array(new)

# myarray = np.array([3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1])
# print(move_zeroes(myarray))
             
def remove_consecutive_duplicates(array):
    length = len(array)-1
    for i in range(length):
        try:
            if array[i] == array[i+1]:
                array.pop(i+1) 
        except IndexError:
            break    
# new_nums = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# remove_consecutive_duplicates(new_nums)
# print(new_nums)

def most_occurencies(array):
    d = dict()
    for i in array:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d[max(d)]
# print(most_occurencies([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]))

def max_consecutive(text):
    nums = text.split('1')
    consecutives = [len(el) for el in nums]
    return max(consecutives)
# print(max_consecutive("'111000111'"))

def not_poor(text):
    if "not" in text and "poor" in text:
        notindex = text.index("not")
        poorindex = text.index("poor")
        if notindex<poorindex:
            return text[:notindex]+ "good"
    return text
# print(not_poor("The lyrics is that poor! The lyrics is poor!"))

def only_unique(d):
    l = []
    for dictionary in d:
        for value in dictionary.values():
            if value not in l:
                l.append(value)
    return l
# data=[
#     {"V":"S001"},
#     {"V": "S002"}, 
#     {"VI": "S001"},
#     {"VI": "S005"}, 
#     {"VII":"S005"}, 
#     {"V":"S009"},
#     {"VIII":"S007"}
# ]

# print(only_unique(data))   


def combinations(d):
    values = list(d.values())
    for i in range(len(values)):
        for j in range(len(values)):
            if i!=j:
                for val in values[i]:
                    for val2 in values[j]:
                        print(val+val2, sep="")


# combinations({'1':['a','b'], '2':['c','d']})
