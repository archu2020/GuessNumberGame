import random
#number=51
#number=random.randint(0,100)
chance=10
no_of_chance=0
while(no_of_chance<10):

    inp=int(input("Please guess the Number\n"))
    number = random.randint(0,100)
    if number==inp:
        print("Congrats!! You guessed right")
    elif inp<number:
        print("You guessed very low number")
    elif inp>number:
        print("You guessed very high number")
    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance},time chance left out of {chance} chances")


