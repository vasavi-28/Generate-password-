#welcome to hollywood game
import random
name=input("What's your name?")
print("Good luck" , name)
cartoonNames=['doremon','shinchan','pokemon','cindrella','tangled']
cartoonName=random.choice(cartoonNames)
print("guess the cartoon name")
guesses=''
turns=5
while turns>0:
    fails=0
    for char in cartoonName:
        if char in guesses:
            
            print(char,end="")

        else:
            print("-")
            fails+=1
    if fails==0:
        print("you've won")
        print("The word is," , cartoonName)
        break
    print()
    guess=input('guess a letter: ')
    guesses+=guess

    if guess not in cartoonName:
        turns-=1
        print("you've lost one chance!")
    if turns==0:
        print('YOU LOSE THE GAME!')


