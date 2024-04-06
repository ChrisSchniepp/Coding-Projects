import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

SYMBOLS = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=',',','.','/','?','<','>','~',':',';']

def upper_and_lower(w):
    w_up = list(w.upper())
    w_new = list(w)
    r1 = random.randint(0,len(w))
    capital = []
    for i in range(0,r1):
        while True:
            r2 = random.randint(0,len(w)-1)
            if r2 not in capital:
                break
        w_new[r2] = w_up[r2]
        capital.append(r2)

    return "".join(w_new)   

def generate(x):
    w = ""
    while len(w) != x:
        r1 = random.randint(0,1)
        if r1 == 0:
            r2 = random.randint(0,len(SYMBOLS)-1)
            if len(w + SYMBOLS[r2]) <= x:
                w = w + SYMBOLS[r2]
            else:
                continue
        else:
            while len(w) + 1 != x:
                r3 = random.randint(0,len(WORDS)-1)
                w2 = WORDS[r3].decode('ASCII')
                w3 = upper_and_lower(w2)
                if len(w + w3) <= x:
                    w = w + w3
                    break
                else:
                    continue
    return w        

x = int(input("Welcome to the pasword generator! Please enter a number for the length of your new Password "))

print(generate(x))
