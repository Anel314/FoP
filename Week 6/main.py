task1 = lambda a,b : a if a>b else b 
task2 = lambda a,b,c : a+b+c
task3 = lambda s: len(s)
task4 = lambda s: len(s)>5
task5 = lambda s: s.upper() if s[0].lower() in "aeiou" else s.lower()
task6 = lambda s : s[::-1] if len(s)%2==0 else s
task7 = lambda s,c : "String too short" if len(s)<10 else s.count(c)


print(task1(1,6)) #6
print(task2(5,5,-6)) #4
print(task3("This string has 29 characters"))#29
print(task4("FIVE")) #False
print(task5("Einstein is cool")) #EINSTEIN IS COOL
print(task5("Tesla is not cool")) #tesla is not cool
print(task6("Oh mein gott!")) # Oh mein gott!
print(task6("Please reverse me!")) #!em esrever esaelP
print(task7("Im short","m")) #String too short
print(task7("Im not really short", "l")) #2










