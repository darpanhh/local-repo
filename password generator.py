import random
import string
print(" Welcome to the Password Generator!")
length = int(input("Enter desired password length: "))
letters = string.ascii_letters  
digits = string.digits          
symbols = string.punctuation   
all_chars = letters + digits + symbols
password = ''.join(random.choice(all_chars) for _ in range(length))

print(f"Your generated password is: {password}")