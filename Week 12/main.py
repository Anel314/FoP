print("-------------------------Task 1------------------------------")
students = []
with open("studentdata.txt") as f:
    students = f.readlines()
print(students)
for student in students:
    studentdata = student.split()
    if len(studentdata)-1 > 6:
        print(studentdata[0])    


print("-------------------------Task 2------------------------------")
students = []
with open("studentdata.txt") as f:
    students = f.readlines()
for student in students:
    studentdata = student.split()
    studentgrades = [int(grade) for grade in studentdata[1:]]
    print(studentdata[0], end=" ")
    avg = sum([int(grade) for grade in studentgrades])
    print(avg/len(studentgrades))


print("-------------------------Task 3------------------------------")
students = []
with open("studentdata.txt") as f:
    students = f.readlines()
for student in students:
    studentdata = student.split()
    print(studentdata[0], "Min:", end=" ")
    print(min([int(grade) for grade in studentdata[1:]]), end=" ")
    print("Max:", end=" ")
    print(max([int(grade) for grade in studentdata[1:]]))


print("-------------------------Task 4------------------------------")
with open("song.txt", 'w') as f:
    f.write("Arms around you")
with open("song.txt") as f:
    print(f.readline())


print("-------------------------Task 5------------------------------")
with open("song.txt", 'a') as f:
    f.write(" by XXXtentacion")
with open("song.txt") as f:
    print(f.readline())

