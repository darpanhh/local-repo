# for i in range(5):
#     print("Darpan")
# count = 1
# while(count<=5):
#     print(count)
#     count+=1
# while(True):
#     print("This will run forever")
# count = 5
# while(count>=1):
#     print("Countdown:",count)
#     count-=1
# print("Liftoff")
# for i in range(1,6):
#     print(i)
# for i in range(1,11):
#     print(i)
# for i in range(2,21,2):
#     print(i)
# for char in "Darpan":
#     print(char)
# Multiplication table of a number
# n = int(input("Enter the number:"))
# print(f"The multiplication table of {n} is:")

# for i in range(1,11):
#     print(f"{n}*{i} = {n*i}")
# Password retry system
# correct_password = "darpan123"
# attempts = 0
# max_attempts = 3
# while attempts<max_attempts:
#     password = input("Enter password")
#     if(password ==correct_password):
#         print("YOU GUEESED IT CORRECT")
#         break
#     else:
#         attempts+=1
#         print(f"YOU HAVE GUESSED IT WRONG")
 
# if attempts == max_attempts:
#     print("Maximum attempt reached try again later!")
# for i in range(1,6):
#     if i==3:
#         break
#     print(i)
# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)
# sum = 0
# while True:
#     n = int(input("Enter a number: "))
#     sum+=n
#     if(n==0):
#         break
# print(f"The sum of numbers is: {sum}")    
# print("You have successfully entered the numbers")

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()
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