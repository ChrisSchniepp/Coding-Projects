import random
print("""Welcome to the Cows and Bulls game. The game works like this: I will randomly 
generate a 4-digit number,and your job is to guess it. For every digit that you guess 
correctly in the correct place, I will call a “cow”. For every digit you guess correctly 
in the wrong place is a “bull.” Type 'quit' to leave the game early""")

# creat a 4-digit 'number'
daiichi = random.randint(0,9)
daini = random.randint(0,9)
while daiichi == daini:
    daini = random.randint(0,9)
daisan = random.randint(0,9)
while daiichi == daisan or daini == daisan:
    daisan = random.randint(0,9)
daiyon = random.randint(0,9)
while daiichi == daiyon or daini == daiyon or daisan == daiyon:
    daisan = random.randint(0,9)

# Start loop
while True:
    #initialize cows a bulls each loop
    cows = 0
    bulls = 0

    # user input, and invalid input conditions
    guess = str(input("Enter a number "))
    if guess == 'quit':
        break
    elif len(guess) != 4:
        print('invalid input')
        continue

    # First digit
    if int(guess[0])==daiichi:
        cows+=1
    if int(guess[1])==daiichi:
        bulls+=1
    if int(guess[2])==daiichi:
        bulls+=1
    if int(guess[3])==daiichi:
        bulls+=1     

    # Second digit
    if int(guess[1])==daini:
        cows+=1
    if int(guess[0])==daini:
        bulls+=1
    if int(guess[2])==daini:
        bulls+=1
    if int(guess[3])==daini:
        bulls+=1

    if int(guess[2])==daisan:
        cows+=1
    if int(guess[1])==daisan:
        bulls+=1
    if int(guess[0])==daisan:
        bulls+=1
    if int(guess[3])==daisan:
        bulls+=1

    if int(guess[3])==daiyon:
        cows+=1
    if int(guess[1])==daiyon:
        bulls+=1
    if int(guess[2])==daiyon:
        bulls+=1
    if int(guess[0])==daiyon:
        bulls+=1        

    if int(guess[0])==daiichi and int(guess[1])==daini and int(guess[2])==daisan and int(guess[3])==daiyon:
        print('dubs')
        break
    else:
        print(cows,'cows,',bulls,'bulls')
        
