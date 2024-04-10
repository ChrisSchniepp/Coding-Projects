print("Welcome to the Divisor Program. In this program, you enter 2 numbers. One for the range (i.e. 1-1000) and """
      "one for number of Divisors. The program then returns how many numbers in that range have the specified devisors. """
      "For example, if you entered 1000 and 12 the program would return every number with 12 divisors from 1-1000")
r = int(input("Now please enter your first number "))
d = int(input("Now enter your second number "))

a = range(1,r)
gg = []

for x in a:
    g = []
    for y in range(1,x+1):
        if x % y == 0:
            g.append(y)

    if len(g) == d:
        gg.append(x)
       
print(gg)    
print()    
        
