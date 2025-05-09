import random 

def game():
    user_choise = input("Enter Your choise, Rock, Paper, Sissor :").lower()
    generate_choise = ["rock","paper","sissor"]
    count = 0

    # Generate computer choise 
    
    computer_choise = random.choice(generate_choise)
    if user_choise == computer_choise:
        print("Tie")
    elif user_choise == "rock" and computer_choise == "sissor" or user_choise == "sissor" and computer_choise == "paper" or user_choise == "paper" and computer_choise == "rock":
        print("You won this game")
        count +=1
    else: 
        
        print("Computer wins")

    print("The computer gess:",computer_choise)
    print("User choise:",user_choise)

game()    