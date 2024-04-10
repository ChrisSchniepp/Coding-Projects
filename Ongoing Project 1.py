import random

s = str(input('Pls type a sentence '));

smatrix = s.split()
print(" ".join(smatrix[::-1]))

def fib(x):
    f = []
    f.append(1)
    if x == 1:
        return f
    f.append(1)
    for i in range(2,x):
        f.append(f[i-2]+f[i-1])
    return f

print(fib(2))    

