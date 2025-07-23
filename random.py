import random

quotes = [
    "Believe you can and you're halfway there.",
    "Push yourself, because no one else is going to do it for you.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Don’t watch the clock; do what it does. Keep going.",
    "You are capable of amazing things.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t come to you, you go to it.",
    "Doubt kills more dreams than failure ever will.",
    "The secret of getting ahead is getting started.",
    "One day or day one. You decide."
]

print(" Motivational Quote Generator ")

while True:
    input("\nPress Enter to get a motivational quote...")

    quote = random.choice(quotes)
    print(f"\n {quote} ")

    again = input("\nDo you want another quote? (y/n): ").lower()
    if again != 'y':
        print("\nStay strong. Good night ")
        break