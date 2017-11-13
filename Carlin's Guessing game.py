import random
def main():
    guess=0
    guess1=0
    True=0
    False=0

    print(" Welcome to a guessing game!")
    print("1.Easy(10)2. Medium(20) 3. Hard(100)")
    type=input("Choose what type of level you want to be in ")
    if type ==1:
        print("1- vs Computer 2.-vs Human")
        type= input("Choose what type you want to be in ")
        if type ==1:
            print(" First to six tries loses. Good luck in this game!")
            print("Player try and guess the random number(1-10)")
        #guess = input("Please choose random number")

            while guess< 6:
                print('Take a guess.')  # There are four spaces in front of print.
                guess = input()
                guess=int(guess)

                guessTaken = guess + 8

            if guess < type:
                print('Your guess is too high.')

              # There are eight spaces in front of print.

            if guess > type:

                 print('Your guess is too low.')
            if guess >=type:
                if guess < type:
                    print('Your guess is too high.')

                    print('Your guess is too low.')

            if guess <=type:

                print('Your guess is too low.')



        if guess != type:
                number = str(type)
                #print('Round two')
                print('Take a guess.')  # There are four spaces in front of print.
                guess = input()
                guess = int(guess)

                guessTaken = guess + 2
        if guess < type:
            print('Your guess is too high.')
            # There are eight spaces in front of print.

        if guess > type:
                print('Your guess is too low.')
                print('Computer wins')

        if guess < type:
                 print("Computer wins")




# to determine the winner
# do we really hae to determine the out come of the computer's languge



        if type ==2:
            print(" Players,Welcome the first player who does six tries loses. Good luck in this game!")
            print("Player one and try and guess the random number(1-10)")
# 1st player
            while guess< 6:
                print('Player 1 Take a guess.')  # There are four spaces in front of print.
                guess = input()
                guess=int(guess)
                guessTaken = guess + 2
            if guess < type:
                print('Your guess is too high.')  # There are eight spaces in front of print.

            if guess > type:
                print('Your guess is too low.')

            if guess == type:
                print('Good job player one,! You guessed my number 8 in guesses!')
            if guess1 != type:
                number = str(type)
            while guess1<6:
                print('Player 2 Take a guess.')  # There are four spaces in front of print.
                guess1 = input()
                guess1=int(guess1)
                guess1Taken = guess1 + 2

            if guess1 < type:
                    print('Your guess is too low.')  # There are eight spaces in front of print.

            if guess1 > type:
                    print("Good job players you both tried your best but player two is the winner.")

            if guess1 == type:
                print('Good job player 2,! You guessed my number 8 in guesses!')
            if guess1!= type:
                number = str(type)
            if guess<guess1:
                 print(" player two wins")
            if guess>guess1:
                 print("player one wins")
            if guess==guess1:
                 print(" both of the players would have a draw")



#Mediium
    if type == 2:
        print("1- vs Computer 2.-vs Human")
        type = input("Choose what type you want to be in ")
        print(" First to eight tries loses. Good luck in this game!")
        print("Players try and guess the random number(1-20)")
        if type==1:

            while guess< 8 :
                print('Take a guess.')  # There are four spaces in front of print.
                guess = input()
                guess = int(guess)
                guessTaken = guess + 5

            if guess < type:
                print('Your guess is too low.')
                print("Computer wins")# There are eight spaces in front of print.

            if guess > type:
                print('Your guess is somewhat right.')
            if guess >= type:
                print('Your guess is right.')


        if guess == type:
            guessTaken = str(guessTaken)



        if guess != type:
                number = str(type)# mediumm two
        if type == 2:

            while guess < 8:
                print('Player 1 Take a guess.')  # There are four spaces in front of print.
                guess = input()
                guess = int(guess)
                guessTaken = guess + 5

                if guess < type:
                     print('Your guess is too low.')  # There are eight spaces in front of print.

                if guess > type:
                     print('Your guess is somewhat right.')
                if guess >= type:
                    print('Your guess is right.')
                if guess < guess1:
                    print(" player two wins")
                if guess > guess1:
                    print("player one wins")
                    break
                if guess == guess1:
                    print(" both of the players would have a draw")

            if guess == type:
                guessTaken = str(guessTaken)



        if guess != type:
            number = str(type)
            while guess1 < 8:
                print('Player 2 Take a guess.')  # There are four spaces in front of print.
                guess1 = input()
                guess1 = int(guess1)

                guess1Taken = guess1 + 5

                if guess1 < type:
                    print('Your guess is too low.')  # There are eight spaces in front of print.

                if guess1 > type:
                    print('Your guess is somewhat right.')
                if guess1 >= type:
                    print('Your guess is right.')

            if guess1 == type:
                guess1Taken = str(guess1Taken)



        if guess1 != type:
            number = str(type)
#Hard
    if type == 3:
        print(" First to ten tries loses. Good luck in this game!")
        print("Player try and guess the random number(1-100)")
        print("1- vs Computer 2.-vs Human")
        type = input("Choose what type you want to be in ")

        if type==1:
            while guess < 10:
                print('Take a guess.')  # There are four spaces in front of print.
                guess = input()
                guess = int(guess)
                guessTaken = guess + 7

            if guess < type:
                print('Your guess is too low.')  # There are eight spaces in front of print.

            if guess > type:
                print('Your guess is somewhat right.')
            if guess >= type:
                print('Your guess is right.')

        if guess == type:
            guessTaken = str(guessTaken)
            while guess <= 10:
                print('Take a guess.')
                print('round 2')# There are four spaces in front of print.
                guess = input()
                guess = int(guess)
                guessTaken = guess + 7

            if guess < type:
                print('Your guess is too low.')  # There are eight spaces in front of print.


            if guess >= type:
                print('Your guess is right.')

            if guess == type:
                guessTaken = str(guessTaken)
            while guess > 10:
                print('Take a guess.')
                print('round 2')  # There are four spaces in front of print.
                guess = input()
                guess = int(guess)
                guessTaken = guess + 7

            if guess < type:
                print('Your guess is too low.')  # There are eight spaces in front of print.

            if guess > type:
                print('Your guess is somewhat right.')
            if guess >= type:
                print('Your guess is right.')

            if guess == type:
                guessTaken = str(guessTaken)
            while guess >= 10:
                print('Take a guess.')
                print('round 3')  # There are four spaces in front of print.
                guess = input()
                guess = int(guess)
                guessTaken = guess + 7

            if guess < type:
                print('Your guess is too low.')  # There are eight spaces in front of print.

            if guess > type:
                print('Your guess is somewhat right.')
            if guess >= type:
                print('Your guess is right.')

            if guess == type:
                guessTaken = str(guessTaken)

        if type == 2:
            while guess < 10:
                print('Player one Take a guess.')  # There are four spaces in front of print.
                guess = input()
                guess = int(guess)

            guessTaken = guess + 7

            if guess < type:
                print('Your guess is too low.')  # There are eight spaces in front of print.

            if guess > type:
                print('Your guess is somewhat right.')
            if guess >= type:
                print('Your guess is right.')

            if guess == type:
                guessTaken = str(guessTaken)



            while guess1 < 10:
                print('Player two Take a guess.')  # There are four spaces in front of print.
                guess1 = input()
                guess1 = int(guess)

                guess1Taken = guess1 + 7

                if guess1 < type:
                    print('Your guess is too low.')  # There are eight spaces in front of print.

                if guess1 > type:
                    print('Your guess is somewhat right.')
                if guess1 >= type:
                    print('Your guess is right.')

                if guess1 == type:
                    guess1Taken = str(guess1Taken)
            while guess > 10:
                print('Player one Take a guess.')
                print('Round 2')  # There are four spaces in front of print.
                guess = input()
                guess = int(guess)

                guessTaken = guess + 7

            if guess < type:
                print('Your guess is too low.')  # There are eight spaces in front of print.

            if guess > type:
                print('Your guess is somewhat right.')
            if guess >= type:
                print('Your guess is right.')

            if guess == type:
                        guessTaken = str(guessTaken)

            while guess1 > 10:
                        print('Player two Take a guess.')  # There are four spaces in front of print.
                        guess1 = input()
                        guess1 = int(guess)

                        guess1Taken = guess1 + 7

                        if guess1 < type:
                            print('Your guess is too low.')  # There are eight spaces in front of print.

                        if guess1 > type:
                            print('Your guess is somewhat right.')
                        if guess1 >= type:
                            print('Your guess is right.')

                        if guess1 == type:
                            guess1Taken = str(guess1Taken)
            while guess > 10:
                        print('Player one Take a guess.')
                        print('Round 3')  # There are four spaces in front of print.
                        guess = input()
                        guess = int(guess)

                        guessTaken = guess + 7

                        if guess < type:
                            print('Your guess is too low.')  # There are eight spaces in front of print.

                        if guess > type:
                            print('Your guess is somewhat right.')
                        if guess >= type:
                            print('Your guess is right.')

                        if guess == type:
                            guessTaken = str(guessTaken)

            while guess1 > 10:
                        print('Player two Take a guess.')  # There are four spaces in front of print.
                        guess1 = input()
                        guess1 = int(guess)

                        guess1Taken = guess1 + 7

                        if guess1 < type:
                            print('Your guess is too low.')  # There are eight spaces in front of print.

                        if guess1 > type:
                            print('Your guess is somewhat right.')
                        if guess1 >= type:
                            print('Your guess is right.')

                        if guess1 == type:
                            guess1Taken = str(guess1Taken)

main()
def play_again():
    guess=0

    print("Do you want to play again?")
    print("Please type 1.yes or 2.no")
    type=input("Choose what yes or no")
    if type ==1:
        print(" please restart the game and countinue playing it")

    if type ==2:
        print(" Please exit the game. It was nice of you to try playing this game")

play_again()

