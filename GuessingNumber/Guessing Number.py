import random 
import math 

l=int(input(" give the lower bound of the interval in which you want the computer to guess "))
u=int(input("give the upper bound of the interval in which the computer has to guess "))

x=random.randint(l,u)
print(x)
num_of_guesses=round(math.log(u-l + 1))

print("you have {} guesses ".format(num_of_guesses))

guesses_over=0
while(guesses_over<num_of_guesses or your_choice==x):
     
    guesses_over +=1
    your_choice=int(input("your guess is "))

    if(your_choice==x):
        print("you won !! and you did it in {} guesses ".format(guesses_over))
        break
    elif(abs(your_choice-x)>u/2):
        print("you guessed it too far and you have {} guesses left over ".format(num_of_guesses-guesses_over))
        clue_choice=input("do you need a clue ? but its gonna cost 2 guesses ")
        num_of_guesses=num_of_guesses-2
        if((num_of_guesses-guesses_over)<2):
            print("you dont have a chance to afford for the clue ")
        if(clue_choice in ['y','yes']):
            if(x<u/2):
                print(" the clue is to guess 'below' {}".format(u/2))
            elif(x>u/2):
                print("the clue is to guess 'above' {}".format(u/2))
        else:
            print("well go on you have your two guesses intact ")
    else:
        print("maybe near but this is wrong, guess other number and you have {} guesses ".format(num_of_guesses-guesses_over))
    if(guesses_over==num_of_guesses):
        print("your guesses are over")
