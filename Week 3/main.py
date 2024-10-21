print("------------------TASK 1-------------------------")

a,b = int(input("A:")),int(input("B:"))
print(a+b) if a>b else print(a*b)

print("------------------TASK 2-------------------------")

for i in range(100,400+1,2):
    print(i, end=" ")

print("------------------IDK-------------------------")
n=12
for i in range(n):
    print("* "*i)
for i in range(n):
    print("* " * (n-i))


print("------------------TASK 3-------------------------")

a,b = int(input("A:")),int(input("B:"))
for i in range(1,b+1):
    print(f"{i}*{a}={i*a}")


print("------------------TASK 4-------------------------")
suma=0
for i in range(5+1):
    suma+=i
print(suma)
ALTERNATIVE: print(sum(range(6)))


