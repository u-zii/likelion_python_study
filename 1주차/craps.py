from random import *

print("주사위 던지기")
dice1 = randint(1,6)
dice2 = randint(1,6)
result=dice1+dice2
print("주사위 1 : " + str(dice1))
print("주사위 2 : " + str(dice2))
print("주사위 합 : " + str(result) + "\n")



if (result==7)|(result==1):
    print("승리")
elif (result==2)|(result==3)|(result==12):
    print("패배")
else:
    while True:
        dice3 = randint(1,6)
        dice4 = randint(1,6)
        print("주사위 3 : " + str(dice3))
        print("주사위 4 : " + str(dice4))
        print("주사위 합 : "+ str(dice3+dice4)+"\n")

        if dice3+dice4==result:
            print("승리")
            break
        elif (dice3+dice4==7):
            print("패배")
            break