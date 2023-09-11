"""
La biblioteca random se utiliza para generar números aleatorios.
"""
import random


def get_user_input(prompt: any, is_integer: bool = True):
    """
    Solicita una entrada al usuario y la valida opcionalmente como un entero.

    Args:
        prompt (str): El mensaje que se muestra al usuario.
        is_integer (bool, optional): Indica si la entrada debe ser un entero. 
        Por defecto, es True.

    Returns:
        int/str: El valor ingresado por el usuario, convertido a un entero 
        si is_integer es True, de lo contrario, una cadena.
    """
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
    """
    Carga los puntajes desde un archivo llamado "scores.txt" 
    y los devuelve como una lista de cadenas.

    Returns:
        list: Una lista de cadenas que representan los puntajes.
    """
    try:
        with open("scores.txt", "r", encoding="utf-8") as file:
            scores = file.readlines()
        return [line.strip() for line in scores]
    except FileNotFoundError:
        return []


def save_scores(scores):
    """
    Guarda una lista de puntajes en un archivo llamado "scores.txt".

    Args:
        scores (list): Una lista de cadenas que representan los puntajes.
    """
    with open("scores.txt", "w", encoding="utf-8") as file:
        for score in scores:
            file.write(score + "\n")


def main():
    """
    Función principal del juego de adivinanza de números.
    """
    lower = 1
    upper = 100
    max_attempts = 10

    target_number = random.randint(lower, upper)
    attempts = 0

    print(
        f"You are guessing a number between {lower} and {upper}.\nYou have a maximum of {max_attempts} attempts.") # pylint: disable=line-too-long

    while attempts < max_attempts:
        guess = get_user_input(f"Attempt {attempts + 1}: Guess the number: ")

        if guess == target_number:
            print(
                f"Congratulations! You guessed the number {target_number} in {attempts + 1} attempts.") # pylint: disable=line-too-long
            player_name = get_user_input(
                "Enter your name to save your score: ", is_integer=False)
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
        print(
            f"You've exhausted your {max_attempts} attempts. The correct number was {target_number}.") # pylint: disable=line-too-long

    print("\nTop 5 Scores:")
    scores = load_scores()
    # Sort by the number of attempts
    scores.sort(key=lambda x: int(x.split(":")[1]))
    for score in scores[:5]:  # Display the top 5 scores
        print(score)


if __name__ == "__main__":
    main()
