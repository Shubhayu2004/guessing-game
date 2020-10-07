import random
import time
a = random.randint(0,100)
print("enter a number")
guess_limit = 3
won = False
while guess_limit>0:
    guess = int(input())
    if guess > a:
        print("Too high, Try again:")
        guess_limit -= 1
    elif guess < a:
        print("Too low, Try again:")
        guess_limit -= 1
    else:
        print("you won")
        won = True

if not won:
    print("you lost")
    print(a)
time.sleep(1)
