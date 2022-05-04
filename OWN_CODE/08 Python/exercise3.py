###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

import random

# Generate random number
def generate_answer():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

# Get guess of player
def get_guess():
    return list(input("Please input your guess: "))

# Generate clues
def generate_clues(guess, ans):
    if guess == ans:
        return "CODE CRACKED"

    clues = []

    for ind,num in enumerate(guess):
        if num == ans[ind]:
            clues.append("Match")
        elif num in ans:
            clues.append("Close")

    if clues == []:
     return "Nope"

    return clues


# Logic
print("Welcome to Code Breaker!")
print("A random non-repeating 3-digit code has been generated for you.")
print("Your task is to figure out the code to win!")

ans = generate_answer()
clues = []

while clues != "CODE CRACKED":
    guess = get_guess();
    clues = generate_clues(guess, ans);
    print(clues);
guess_int = ""
for n in guess:
    guess_int += n
print(f"The answer is {(int(guess_int)):03}")
print("Congratulations Codemaster! Thank you for playing!")
