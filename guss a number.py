import random
player1=random.randint(0,50)
rang=random.randint(1,9)
print(f"you can guss {rang} times")
chance=rang
for i in range(rang):
    print(f"{chance} chances left! ")
    player2=int(input("guss a number between 0,50: "))
    if player2==player1:
        print("player 2 win")
    elif player1>player2:
        print("your guss is lower! ")
        chance-=1
    else:
        print("your guss is bigger! ")
        chance-=1
if player2!=player1:
    print("player 2 you lose")
print(f"ai guss was {player1}")


