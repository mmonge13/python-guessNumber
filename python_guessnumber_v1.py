import random

def get_user_input(prompt, is_integer=True):
    while True:
        user_input = input(prompt)
        if is_integer:
            try:
                return int(user_input)
            except ValueError:
                print("Please enter a valid integer.")
        else:
            return user_input

def load_scores():
    try:
        with open("scores.txt", "r") as file:
            scores = file.readlines()
        return [line.strip() for line in scores]
    except FileNotFoundError:
        return []

def save_scores(scores):
    with open("scores.txt", "w") as file:
        for score in scores:
            file.write(score + "\n")

def main():
    lower = 1
    upper = 100
    max_attempts = 10

    target_number = random.randint(lower, upper)
    attempts = 0

    print(f"You are guessing a number between {lower} and {upper}.\nYou have a maximum of {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = get_user_input(f"Attempt {attempts + 1}: Guess the number: ")

        if guess == target_number:
            print(f"Congratulations! You guessed the number {target_number} in {attempts + 1} attempts.")
            player_name = get_user_input("Enter your name to save your score: ", is_integer=False)
            scores = load_scores()
            scores.append(f"{player_name}: {attempts + 1} attempts")
            save_scores(scores)
            break
        elif guess < target_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        attempts += 1
    else:
        print(f"You've exhausted your {max_attempts} attempts. The correct number was {target_number}.")

    print("\nTop 5 Scores:")
    scores = load_scores()
    scores.sort(key=lambda x: int(x.split(":")[1]))  # Sort by the number of attempts
    for score in scores[:5]:  # Display the top 5 scores
        print(score)

if __name__ == "__main__":
    main()
