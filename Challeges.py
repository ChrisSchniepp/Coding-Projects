import random

# Varible Declarations
a = []
b = []
i = 0

# Make two random lists, one half the size of the other
while i < 10:
    n = random.randint(1,10)
    a.insert(i,n)
    if i<7:
        b.append(random.randint(1,10))
    i=i+1

#creates d which is a but with no duplicates
d = a[:]
d.sort()
a.sort()
b.sort()
iii = 0
for i in range(1,len(a)):
    ii = i-1
    if a[i]==a[ii]:
        del d[i-iii]
        iii = 1+iii

# Now find the common parts between each list
c = []    
for i in d:
    for ii in b:
        if i == ii:
            c.append(i)
            break




print(a,len(a))
print(d,len(d))
print(b,len(b))
print(c,len(c))