### IMPORTS
from time import sleep as wait
from random import randint


### FUNCTIONS

def clue(x,q):
    if x<q:
       return print ("Your clue: Number you're looking for is smaller")
    else:
       return print ("Your clue: Number you're looking for is bigger")

def cluee(x,q):
    if x/2==0:
       return print ("Your addictional clue: Number you're looking for is even")
    else:
       return print ("Your addictional clue: Number you're looking for is odd")


### CODE

while True:
    #MAIN LOOP

    print ("Hellouser!\n Would you like to play a simple game?")
    answer=input("\nWhat is your decision? (y/n): ")
    if answer=="n":
        print("You dissapionted me user")
        wait(1)
        break
    wait (2)
    print ("\nI knew it! So let me explain the rules\nI will randomly choose number between 1 to 100, your job is to guess it. So...")
    wait(1)
    print ("\n1. Proceed (Don\'t you dare to press x!)\n2. Uou start game with score of 15. With every vrong guess score gets reducted\n3. Make you first guess. If it'll be correct - you won. If not - I'll give a clue, but deduct 1 from your score\n Have fun!You that you'll finally guess it!")
    
    x=randint(1,100)
    score = 15
    print (x)
    while True:
        #GUESSING LOOP, breaks after correct guess

        q = int(input("\nWhat is your guess? : "))
        if q==x:
            print ("Correct!, your score is: ", score)
            wait(3)
            break
        else:
            score-=1
            print ("Unfortunally, no, try again. Your score is: ", score)
            clue(x,q)
            if score<13:
                cluee(x,q)
            