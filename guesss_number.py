import random
number = random.randrange(1,50)
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
# guess= int(input("Enter your guess number between 1 to 50 "))
while number_of_guesses<=9:
    try:
        guess = int(input("Guess the number :\n"))
        if guess in range(1, 50):
            if guess<number:
                print("you enter less number please input greater number.\n")
            elif guess>number:
                print("you enter greater number please input smaller number.\n ")
            else:
                print("you won\n")
                print(number_of_guesses,"no.of guesses you took to finish.")
                print(9 - number_of_guesses, "no. of guesses left")
                break
        else:
            print("Your guess number is out of range Please try again")
            continue

        number_of_guesses = number_of_guesses + 1
    except:
        print("InValid number")

if(number_of_guesses>9):
    print("Secret Number is ",number)
    print("Game Over ")