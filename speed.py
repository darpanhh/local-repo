import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Python is an amazing programming language",
    "Typing speed tests are fun and useful",
    "Practice makes a person perfect",
    "Always aim for progress not perfection"
]

def typing_test():
    sentence = random.choice(sentences)
    print("\nType this sentence:\n")
    print(sentence)
    input("\nPress Enter when you're ready to start...")

    start_time = time.time()
    typed = input("\nStart typing:\n")
    end_time = time.time()

    time_taken = round(end_time - start_time, 2)

    original_words = sentence.split()
    typed_words = typed.split()

    correct = 0
    for orig, typed in zip(original_words, typed_words):
        if orig == typed:
            correct += 1

    total_words = len(typed_words)
    accuracy = (correct / len(original_words)) * 100
    wpm = (total_words / time_taken) * 60

    print(f"\nTime Taken: {time_taken} seconds")
    print(f"Accuracy: {round(accuracy, 2)}%")
    print(f"Words Per Minute (WPM): {int(wpm)}")

typing_test()
