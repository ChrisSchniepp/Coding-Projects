import random
x = int(input("enter number pls 1-100 "))

a = []
i = 0
while i < 25:
    n = random.randint(1,100)
    a.insert(i,n)
    i=i+1
b = []    
for i in range(0,len(a)):
    if a[i] < x:
        b.append(a[i])
        b.sort()
print(a,len(a))
print(b,len(b))