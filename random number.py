import random
lower_bound=1
upper_bound=10
max_attempts=5
secret_number=random.randint(lower_bound,upper_bound)
def get_guess():
    while True:
        guess=int(input("Guess a random number between 1 to 10:"))
        if lower_bound<=guess<=upper_bound:
            return guess
        else:
            print("invalid input.please try again with a new number between 1 to 10")
def check_guess(guess,secret_number):
    if guess==secret_number:
        return "correct"
    elif guess<secret_number:
        print("too low")
    else:
        print("too high")
def play_game():
    attempts=0
    won=False
    while attempts<max_attempts:
        attempts+=1
        guess=get_guess()
        result=check_guess(guess,secret_number)
        if result=="correct":
            print(f"Congratulations!you guessed the secret number {secret_number} in {attempts} attempts.")
            won=True
            break
        else:
            print(f"{result}.try again!!!")
    if not won:
        print(f"sorry,you ran out of attemts.the secret number is {secret_number}.try again...")
if __name__=="__main__":
    print("welcome to number guessing game!!hope you enjoy it...")
    play_game()



