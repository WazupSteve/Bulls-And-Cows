import random
from tkinter import messagebox

MAX_ATTEMPTS = 10
number = []
attempts = 0
bulls = 0
cows = 0
guess = []


def make_number():
    global number, guess
    number.clear()
    guess.clear()
    for i in range(0, 4):
        x = random.randrange(9)
        number.append(x)
    if len(number) > len(set(number)):
        make_number()


def game_rules():
    # game rules
    rule = """
    *Guess number should consist of a four-digit number.
    *Bulls mean correct numbers in the correct position.
    *Cows mean correct numbers in the wrong position."""
    messagebox.showinfo("Game Rules", rule)


def play_game(user_input):
    global attempts, bulls, cows, guess

    if attempts >= MAX_ATTEMPTS:
        messagebox.showinfo("Warning", f"You have LOST the game!!!\n" f"You have exceeded MAX allowed count of {MAX_ATTEMPTS} rounds."
                                       f"\nNumber that needed to be guessed: {number}\nClick [Back to Home] to play again")
        guess.clear()
        make_number()
    else:
        attempts += 1
        validate(user_input)


def validate(guess_number):
    global guess, bulls, cows, number

    if len(str(guess_number)) == 4:
        guess = [int(guess_number[i]) for i in range(4)]
        print("guess: ", guess)

        bulls = 0
        cows = 0
        for j in range(0, 4):
            if guess[j] == number[j]:
                bulls += 1
            if guess[j] in number and guess[j] != number[j]:
                cows += 1

        if bulls == 4:
            messagebox.showinfo("VICTORY", f"You have WON the game,\n The number of attempts taken: {attempts}")
            number.clear()
            make_number()
        elif bulls != 4:
            guess = []
            message = f"Bulls={bulls} Cows={cows}"
            messagebox.showinfo("info", message)

    else:
        messagebox.showinfo("ERROR", "Input must be 4 digits")


if __name__ == '__main__':
    make_number()
