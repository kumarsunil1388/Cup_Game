def game():

    import random
    i=0
    p=0
    c=0
    d=0
    print("Welcome to game")
    try:
        num = int(input("Numbner of times you want to play "))
        print(f"You want {num} times to play ")
    except:
        print("Invalid option")
    while i<num:
        choise = ["SNAKE","WATER","GUN"]
        com= random.choice(choise).upper()
        print(com)
        player = input("Enter your choise Snake , Water , Gun ").upper()
        if player in choise:
            if (player == "SNAKE" and com == "WATER") or (player =="WATER" and com == "GUN") or (player == "GUN" and com == "SNAKE"):
                print("Player Win")
                p= p+1
                num= num-1
                print(f"Your score is {p} and Computer score is {c}  and Draw {d} ",end="")
                print(f"Chance left {num}")

            elif player == com:
                print("It's a Tie")
                d =d+1
                num=num-1
                print(f"Your score is {p} and Computer score is {c}  Draw {d} ", end="")
                print(f"Chance left {num}")
            else:
                print('Computer Win')
                c=c+1
                num=num-1
                print(f"Your score is {p} and COmputer score is {c} draw {d} ", end="")
                print(f"Chance left {num}")

        else:
                print("Invalid Option Try again")
                continue
    if p>c:
        print("Congratulation you won")
    elif c==p:
        print("Its a draw")
    else:
        print("Sorry you lost")


while True:
    game()
    try:
        z = input("Want to play again Y or N \n").lower()
        if z=="y":
            continue
        else:
            print("Thank You")
            break
    except:
            print("Invalid Choise")
