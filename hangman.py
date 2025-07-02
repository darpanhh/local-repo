import random 
word_list = ["apple","banana","orange","grape","mango"]
word = random.choice(word_list)

lives = 6
hidden_word = ["_"]*len(word)

guessed_letters = []
print("-------Welcome to Hangman--------")
print(f"You have {lives} lives")
print("Word:"," ".join(hidden_word))

while(lives>0 and "_" in hidden_word):
    guess = input("Guess a letter:").lower()
    
    if guess in guessed_letters:
        print("Already guessed that letter.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        print("Correct guess")
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
                
    else:
        print("Wrong guess")
        lives -=1
        print(f"You have {lives} left")
        
        
    print("Word:"," ".join(hidden_word))
    print("Guessed so far: ","".join(guessed_letters))
    
    
if "_" not in hidden_word:
    print(f"You guessed it correct,The word was: {word}")
else:
    print(f"You lost. The word was: {word}")
    
    