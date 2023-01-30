import random
player1=input("choose:rock,paper,scissor:")
number=random.randint(1,3)
player2=""
if number==1:
    player2="rock"
    print("player 2 choise rock")
elif number==2:
    player2="paper"
    print("player 2 choise paper")
elif number==3:
    player2="scissor"
    print("player 2 choise scissor")

if player2=="rock" and player1=="paper":
    print("player 1 win")
elif player2=="rock" and player1=="scissor":
    print("player 2 win")
elif player2=="rock"and player1=="rock":
    print("draw")
elif player2=="paper" and player1=="rock":
    print("player 2 win")
elif player2 == "paper" and player1 == "scissor":
    print("player 1 win")
elif player2 == "paper" and player1 == "paper":
    print("draw")
elif player2 == "scissor" and player1 == "rock":
    print("player 1 win")
elif player2 == "scissor" and player1 == "paper":
    print("player 2 win")
elif player2 == "scissor" and player1 == "scissor":
    print("draw")


