"""Generate 4 digit number. User inputs a guess for the four digit number.
You get one cow for guessing the right digit in the right spot. You get 1 bull
for the right digit in the wrong spot. Don't include the count for bulls if they
are already accounted for in the cows count."""

import random as r

print("Welcome to the Cows and Bulls game!")
print("You must guess the four digit number. If you guess it correctly, you "
    "win! To help you guess the number, you get one cow for the right digit in "
    "the correct spot. You also get one bull for the right digit in the wrong "
    "spot. However, you do not get a bull for having the right digit in the "
    "wrong spot if the spot is already accounted for by a cow.")
four_dig_num = r.randint(1000,9999)
attempts = 0
while True:
    #Make guess lists of characters for the guess and four_dig_num
    guess = input("Guess what the four digit number is: ")
    guess_char = list(guess)
    num_list = list(str(four_dig_num))
    cows = 0
    bulls = 0
    if int(guess) != four_dig_num:
        for num_dig in range(4):
            if guess_char[num_dig] != num_list[num_dig]:
                for num in range(4):
                    if guess_char[num] != num_list[num] and guess_char[num_dig] == num_list[num]:
                        bulls += 1
            else:
                cows += 1
        attempts += 1
        print(f"You have {cows} cow(s) and {bulls} bull(s). That was your "
            f"{attempts} attempt. Try again.")
    else:
        attempts += 1
        print(f"You guessed the number {four_dig_num} correctly! It only "
        f"took you {attempts} attempts!")
        play_again = input("Would you like to play again (y/n)? ")
        if play_again == 'n':
            break
        elif play_again == 'y':
            four_dig_num = r.randint(1000,9999)
            attempts = 0