import random

secret=random.randint(1,20)
guess=0
count=0
while guess != secret:
    count+=1
    print("Guess the number")
    guess=int(input())
    if guess>secret:
        print("Your guess is too high")
    elif guess<secret:
        print("Your guess is too low")
    else:
        print("You guessed it right in ",count," attempts")
        break
exit()    