import random 
name = raw_input("What is your name? ")
print "I am thinking of a number 1 through 10. "
secret_number = random.randint(1, 10);
guess = 0;
gameOn = True
number_of_guesses = 3;
keepPlaying = True
while (keepPlaying):
    while (gameOn and guess != secret_number):
        if (number_of_guesses == 3):
            print "You have %i guesses. " % number_of_guesses
        guess = int(raw_input("What is the secret number? "))
        number_of_guesses -= 1
        if (guess == secret_number):
            print "Yes, you win. Good job %s" % name
        else:
            print "Nope, try again"
            if (number_of_guesses < 5):
                print "You have " + str(number_of_guesses) + " guesses left."
            if (number_of_guesses == 0):
                print "You ran out of guesses."
                print "The secret number is %i" % secret_number
                gameOn = False
            elif (number_of_guesses == 0):
                print "Wrong answer"
            elif (guess > secret_number):
                print "%i is too high" % guess
            elif (guess < secret_number):
                print "%i is too low" % guess
    playAgain = raw_input("Would you like to play again? (Y or N) ")
    playAgain = playAgain.upper()
    if (playAgain == "N"):
        keepPlaying = False
        print "Thank you for playing %s, bye" % name
    else:
        print "Awesome! Good luck!"
        secret_number = random.randint(1, 10)
        number_of_guesses = 5 
        gameOn = True