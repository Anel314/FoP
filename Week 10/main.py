# person = {
#     'name':"John",
#     'age':6,
#     'class': "First"
# }
# print(person['age'])
# person['school'] = "Elementary"
# del person['class']

# person['age'] = 8

# print(len(person))
# print(list(person.keys()))
# print(list(person.values()))
# print(list(person.items()))

# print(person.get('grade',0))

# for k in person:
#     print(k, "in this dictionary is related to the following value: ", person[k])

# print('age' in person)

# person2 = person.copy()
# person2['name'] = "Alice"
# person2['age'] = 17
# person2['school'] = "High School"


# del person
# # print(person)
# print(person2)
#--------------------------------------------------
# d = { 
#     "num1" : 15,
#     "num2" : 4,
#     "num3" : 9,
#     "num4" : 16
# }
# def doubleValues(d):
#     for key in d:
#         d[key]*= 2 if d[key]<9 else 1

# print(d)
# doubleValues(d)
# print(d)
#--------------------------------------------------
# dict1 = { "num1" : 315, "num2" : 1497, "num3" : 9, "num4" : 16, "num5" : 723476}
# def replaceDigits(d):
#     for k in d:
#         d[k] = int(str(d[k])[0])        

# replaceDigits(dict1)
# print(dict1)
#--------------------------------------------------
# def combineLists(l1,l2):
#     length = len(l1)
#     if length > len(l2):
#         length = len(l2)
#     d = {}
#     for i in range(length):
#         d[l1[i]] = l2[i]
#     return d

# keys_list1 = ['a', 'b', 'c', 'd', 'e','f','g','h']
# values_list1 = [1, 2, 3, 4, 5,6,7,8]
# print(combineLists(keys_list1,values_list1))
#--------------------------------------------------
# def matchKeys(d1,d2):
#     for item in d1.items():
#         if item in d2.items():
#             print(item[0], ":",item[1],'is present in both dictionaries')
        

# matchKeys({'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2})
#--------------------------------------------------
# def removeSpaces(d):
#     newd = {}
#     for key in d:
#         if ' ' in key:
#             val = d[key]
#             key = key.replace(' ','')
#             newd[key] = val
#     return newd
# d = {"key 1": 10, "key 2": 20, "key 3": 30}
# print(removeSpaces(d))
#--------------------------------------------------
# def combineValues(l):
#     res = {}
#     for d in l:
#         if d['item'] not in res:
#             res[d['item']] = d['amount']
#         else:
#             res[d['item']] += d['amount']
#     return res

# l =  [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# print(combineValues(l))
#--------------------------------------------------
# def displayCombinations(data):

#     def combine(keys, index, current):
#         if index == len(keys):
#             print(''.join(current))
#             return
#         for letter in data[keys[index]]:
#             combine(keys, index + 1, current + [letter])
    
#     keys = list(data.keys())
#     combine(keys, 0, [])

# sample_data = {'1': ['a', 'b','c'], '2': ['c', 'd']}
# displayCombinations(sample_data)
   
            



