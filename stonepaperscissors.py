import random
computer=0
you=0
sring = ["stone", "scissors", "paper"]
print("for stone press 0\nfor paper press 1\nfor scissors press 2\n")
for i in range(1, 10):
    a = int(input())
    print("your choice :-",sring[a] )
    b = random.randint(0,2)
    print("computer choice :-", sring[b])
    print("your life is", 10 - i)

    if a == b:
        print("you<---->computer")

    elif a == 0 and b == 1:
        print("you win")
        you += 1
    elif a == 1 and b == 0:
        print("computer win")
        computer += 1
    elif a == 1 and b == 2:
        print("you win")
        you += 1
    elif a == 2 and b == 1:
        print("computer win")
        computer += 1
    elif a == 2 and b == 0:
        print("you win")
        you += 1
    elif a == 0 and b == 2:
        print("computer win")
        computer += 1
print("\n\n\nyour score is", you, "computer score is", computer)
if you > computer:
    print("congrats! you are a winner and got chicken dinner")
elif you == computer:
    print("draw the match")
else:
    print("sorry ,you lose the game,try next time:) ")