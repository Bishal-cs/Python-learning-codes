import random
def number_guessing_game():
    ai_guess = random.randint(1,10)
    human_guess = 0
    attempt = 1
    n = int(input("How many attempt you want :"))
    while attempt < n:
        print("Your ",attempt,"st try")
        human_guess = int(input("Enter your guess number :"))
        if human_guess == ai_guess :
            print("CONGRATULATION ! YOU SUCCESSFULLY GUESSED THE NUMBER.",attempt,"st attempt")
            break
        elif human_guess < ai_guess :
            print("Sorry Your Guess Is Too Low.\n Better luck next time.")
        else:
            print("Sorry Your guess is too high.\n Better luck next time.")
        attempt += 1
print(":::Lets play number guessing game:::")
number_guessing_game()