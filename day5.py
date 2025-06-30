
import random 
def number_guessing_game():
    num = random.randint(0,10)
    attempts=0
    
    while True:
        a = input("Enter the guessing number:")
        
        if not a.isdigit():
            print("Enter the numbers not characters")
            continue
        attempts+=1
        a = int(a)
        if a>num:
            print("Try guessing lower")
            
        elif a<num:
            print("Try guessing higher")
            
        else:
            print(f"You entered correctly in {attempts} and the secret number is: {num}") 
            break
number_guessing_game()
