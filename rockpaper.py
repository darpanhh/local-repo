import random 
options = ["rock","paper","scissor"]
user_win = 0
computer_win = 0
draws = 0
while True:
    user_choice = input("Enter your move:(rock,paper or scissor) or type quit for quiting the game: ").lower()
    if user_choice =="quit":
        print(f"Your win: {user_win}")
        print(f"Computer win: {computer_win}")
        print(f"Draws: {draws}")
        print("Thank you for playing!!!")
        break
    if user_choice not in options:
        print("Invalid choice.Try again!!")
        
    computer_choice = random.choice(options)
    print(f"The computer's move is: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Draw!!!")
        draws+=1
    elif (user_choice =="rock" and computer_choice == "scissor") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissor" and computer_choice == "paper"):
            print("You wins!!!")
            user_win+=1
    else:
        print("Computer wins!!!") 
        computer_win+=1        
    print(f"Score : Your score: {user_win} and computer score: {computer_win} and draws: {draws} ")   
        