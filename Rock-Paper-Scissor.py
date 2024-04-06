import random

x = random.randint(1,9)

print("""Welcome to the Guessing name, a number has been assigned a random number from
      1 to 9, the game will continue until you guess the number of enter 'quit'""")

guess = 0
counter = 0

while True:
    guess = input("please enter a number between 1 and 9 ")
    if guess == 'quit':
        break
    else:
        guess = int(guess)
    if guess == x:
        print('当たった！おめでとうございます！')
        counter +=1
        print('it took you',counter,'guesses to get the right answer')
        x = random.randint(1,9)
        counter = 0
    elif guess > x:
        print('Too high bro')
        counter +=1
    elif guess < x:
        print('Too low')
        counter += 1
    


