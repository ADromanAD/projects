import time
from questions import *


points = 0
version = 1.0
results = {}

print(f"\nWelcome to the Quiz Game {version}\n"
      f"Enter your name:", end=' ')
name = input()
print(f"Ready to start, {name}? y/n", end=' ')
answer = input()
while answer.lower() != 'y' or answer.lower() != 'n':
    if answer.lower() == 'n':
        print("Okey then, bye")
        exit(0)
    elif answer.lower() == 'y':
        break
    else:
        print("Y or N only", end=' ')
        answer = input()
print("Alright, let's get it started...")

time.sleep(3)

# Writing list of questions
_ = 0
while _ != 10:
    print(questions[_])
    answer = input()
    if answer.lower() == answers[_].lower():
        points += 1
    _ += 1

time.sleep(0.5)
print("\nCongratulations! That was the last question!")
time.sleep(2)
print(f"Thanks for the game. Here's your score: {points}")

results[name] = points
print(results)
