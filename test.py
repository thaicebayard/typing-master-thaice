import time as t
import random

musicals = ["Jagged little pill", "Dear Evan Hansen", "Frozen the musical", "Hades Town", "Wicked", "The Lion King", "Six The musical", "In the Heights", "Chicago", "Shrek the musical", "Evita", "Rent", "Heathers", "Mean Girls", "Highschool musical"]

print(random.choice(musicals))

words = 15
mistakes = 0
correct = 0

for word in musicals:
    user_input = input(f"Type this word: {word}\n")

    if user_input == word:
        print("Good job!")
        correct += 1
    else:
        print("Misspelled! DumDum")
        mistakes += 1

accuracy = (correct / len(musicals)) * 100

print("\nGame Over!")
print(f"Mistakes: {mistakes}")
print(f"Accuracy: {accuracy:.2f}%")

#https://www.youtube.com/shorts/11TnrxRJw7Q
