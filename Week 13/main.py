# def divideNumbers(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("No bro")
#         return ""
# print(divideNumbers(1,2))
# print(divideNumbers(3,0))
# print(divideNumbers(4,6))
# print(divideNumbers(1,0))
# print(divideNumbers(1,0))
# def getListElement(list, index):
#     try:
#         print(list[index])
#     except IndexError:
#         print("No index mate")
#     except:
#         print("Do you even know what an index is")
# getListElement([1,2,3],2)
# getListElement([1,2,3],5)
# getListElement([1,2,3],1)
# getListElement([1,2,3,4],3)
# getListElement([1,2,3,4],4)


# def convertToInt(a):
#     try:
#         b = int(a)
#     except ValueError:
#         print("Geht nicht")
#     else:
#         print("Ze intidjer was konvrted saksesfulaj")
#         print(b)

# convertToInt("4")
# convertToInt("agoh")
# convertToInt(5.8)
# convertToInt(True)


# def alarm_clock(day, vacation):
#     try:
#         if vacation:
#             if day ==0 or day == 6:
#                 print("no")
#             else:
#                 print("10:00")
#         else:
#             if day==0 or day == 6:
#                 print("10:00")
#             else:
#                 print("7:00")
#     except Exception as e:
#         print(e)

# alarm_clock(0,True)
# alarm_clock(3,False)
# alarm_clock(6,False)
# alarm_clock(3,True)


# def replaceChars(string):
#     try:
#         target = string[0]
#         new = target +""
#         for i in range(1,len(string)):
#             new+= '$' if string[i] == target else string[i]    
#     except TypeError:
#         print("Nein")
#     return new

# print(replaceChars("racecar"))
# print(replaceChars("c was it a car or a cat i saw"))
# print(replaceChars("aaaaaaaaaaaaaaaaaaaa"))

# def findItemIndex(list,value):
#     try:
#         i=0
#         while True:
#             if list[i] == value:
#                 return i
#             i+=1
#     except IndexError:
#         return "Not found"
# print(findItemIndex([1,2,3,4],1))
# print(findItemIndex([1,2,3,4],2))
# print(findItemIndex([1,2,3,4],3))
# print(findItemIndex([1,2,3,4],8))
# print(findItemIndex([1,2,3,4],-2))

# def splitList(string, split):
#     try:
#         string[split]
#         new = [string[:split],string[split:]]
#     except IndexError:
#         return "a a a a nece ti to radit"
#     else:
#         return new
# print(splitList("Hello, World", 3))
# print(splitList("Hello, World", 5))
# print(splitList("Hello, World", 19))
# print(splitList("Hello, World", 25))



# def checkKey(dic, key):
#     try:
#         val = dic[key]
#         return True
#     except KeyError:
#         print("A si glup bajo")
#         return False
# print(checkKey({1:1,2:2,3:3},1))
# print(checkKey({1:1,2:2,3:3},2))
# print(checkKey({1:1,2:2,3:3},3))
# print(checkKey({1:1,2:2,3:3},4))

# def combineListsTodict(l1,l2):
#     if len(l1)!= len(l2):
#         print("nein")
#         return
#     elif len(l1) == 0:
#         print("l1 empty")
#     elif len(l2) == 0:
#         print("l2 empty")
    
#     d = dict()
#     for i in range(len(l1)):
#         d[l1[i]] = l2[i]
    
#     return d

# print(combineListsTodict([1,2,3],[1,2,3]))
# print(combineListsTodict([1,2,3],[]))
# print(combineListsTodict([],[1,2,3]))
# print(combineListsTodict([1],[1,2,3]))
# print(combineListsTodict([1,2,3],[1]))

# def tupletoInt(tup):
#     if len(tup) == 0:
#         return"tup is empty"
#     string = ""
#     for i in tup:
#         if i>0:
#             string += str(i)
#         else:
#             print("negative")
#             return 
#     return string

# print(tupletoInt(()))
# print(tupletoInt((1,2,3)))
# print(tupletoInt((4,5,6)))
# print(tupletoInt((1,-3,4)))

# def checkElementInTuple(data,target):
#     if type(data)!= tuple:
#         print("Not a tuple")
#         return
#     for tup in data:
#         if type(tup)!= tuple:
#             print("Not a tuple")
#             return
#         for val in tup:
#             if val  == target:
#                 print("Found it")
#                 return 
#     print("not inside")
#     return
# print(checkElementInTuple((1,2,3), 3))
# print(checkElementInTuple(((1,2,3),), 3))
# print(checkElementInTuple((), 3))
# print(checkElementInTuple((()), 3))

# def sumTupleElements(data):
#     res = []
#     suma = 0
#     try:
#         data[0]
#     except IndexError:
#         return "Empty"
#     for tup in data:
#         suma = 0
#         for val in tup:
#             try:
#                 suma+=val
#             except TypeError:
#                 return "Contains non integer"
#         res.append(suma)
#     return res
# print(sumTupleElements([(1, 2), (2, 3), (3, 4)]))
# print(sumTupleElements([(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]))
# print(sumTupleElements([]))
# print(sumTupleElements([(1, 2), ('a', 3), (3, 4)]))


# def cat_dog(s):
#     if s == "":
#         return "empty"
#     elif type(s) != str:
#         return "Not a string"
#     cats = 0
#     dogs = 0
#     for i in range(len(s)):
#         if s[i:i+3] == "cat":
#             # print(s[i:i+3])
#             cats+=1
#         elif s[i:i+3] == "dog":
#             dogs+=1
#     return cats == dogs

# print(cat_dog('catdog') )
# print(cat_dog('catcat'))
# print(cat_dog('1cat1cadodog'))
# print(cat_dog(''))
# print(cat_dog(12345))



# def sortMatrixByRowSum(matrix):
#     try:
#         new_matrix = []
#         suma = 0
#         dic = {}
#         for row in matrix:
#             dic[sum(row)] = row
#         keys = list(dic.keys())
#         keys.sort()

#         for key in keys:
#             new_matrix.append(dic[key])
#         return new_matrix if len(new_matrix)>0 else "Cant be empty"               
#     except TypeError:
#         return "Val error"

# print(sortMatrixByRowSum([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))
# print(sortMatrixByRowSum([[1, 2, 3], [-2, 4, -5], [1, -1, 1]]))
# print(sortMatrixByRowSum([]))
# print(sortMatrixByRowSum([1, 2, 3]))
# print(sortMatrixByRowSum([[1, 2, 'a'], [2, 4, 5]]))



# def left2(s):
#     try:
#         print( s[2:]+s[0] +s[1] )

#     except TypeError:
#         print("Not going to work")
#     except IndexError:
#         print("Cant be empty")

# left2('Hello')
# left2('java')
# left2('Hi')
# left2(123)
# left2('')
