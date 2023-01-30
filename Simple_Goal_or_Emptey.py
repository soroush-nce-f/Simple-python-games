import random
cup=int(input("how many cups: "))
chance=int(input("ho many chances: "))

player1=random.randint(0,cup)
for i in range(chance):
    print(f"{chance} chances left! ")
    guss=int(input(f"guss number between {0,cup}: "))
    if guss==player1:
        print("guss won. ")
        break
    else:
        print("wrong")
        chance-=1
print("----------")
if guss!=player1:
    print("your guss is worng")
    print(f"ai guss is {player1}")
