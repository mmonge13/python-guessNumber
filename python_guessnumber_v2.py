"""
La biblioteca random se utiliza para generar números aleatorios.
"""
import random

# Diccionario de cadenas de texto en inglés y español
translations = {
    'en': {
        'welcome': 'Welcome to the Number Guessing Game!',
        'customize_prompt': 'Customize the game? (Y/N): ',
        'lower_bound_prompt': 'Enter the lower bound of the range: ',
        'upper_bound_prompt': 'Enter the upper bound of the range: ',
        'max_attempts_prompt': 'Enter the maximum number of attempts: ',
        'guess_range': 'You are guessing a number between {lower} and {upper}.',
        'max_attempts': 'You have a maximum of {max_attempts} attempts.',
        'congrats': 'Congratulations! You guessed the number {target_number} in {attempts} attempts.', # pylint: disable=line-too-long
        'enter_name': 'Enter your name to save your score: ',
        'too_low': 'Too low. Try again.',
        'too_high': 'Too high. Try again.',
        'out_of_attempts': "You've exhausted your {max_attempts} attempts. The correct number was {target_number}.", # pylint: disable=line-too-long
        'top_scores': "\nTop 5 Scores:",
        'invalid_choice': 'Invalid choice. Please select 1 or 2.',
        'guess_prompt': 'Attempt {attempts}: Guess the number: ',
        'attempts': 'attempts',
        'invalid_input': 'Please enter a valid input.',
    },
    'es': {
        'welcome': '¡Bienvenido al Juego de Adivinar el Número!',
        'customize_prompt': '¿Personalizar el juego? (S/N): ',
        'lower_bound_prompt': 'Ingrese el límite inferior del rango: ',
        'upper_bound_prompt': 'Ingrese el límite superior del rango: ',
        'max_attempts_prompt': 'Ingrese el número máximo de intentos: ',
        'guess_range': 'Estás adivinando un número entre {lower} y {upper}.',
        'max_attempts': 'Tienes un máximo de {max_attempts} intentos.',
        'congrats': '¡Felicidades! Adivinaste el número {target_number} en {attempts} intentos.',
        'enter_name': 'Ingresa tu nombre para guardar tu puntaje: ',
        'too_low': 'Demasiado bajo. Inténtalo de nuevo.',
        'too_high': 'Demasiado alto. Inténtalo de nuevo.',
        'out_of_attempts': "Has agotado tus {max_attempts} intentos. El número correcto era {target_number}.", # pylint: disable=line-too-long
        'top_scores': "\nPuntuaciones Principales:",
        'invalid_choice': 'Elección no válida. Por favor, selecciona 1 o 2.',
        'guess_prompt': 'Intento {attempts}: Adivina el número: ',
        'attempts': 'intentos',
        'invalid_input': 'Por favor, ingresa una entrada válida.',
    }
}

def get_user_language():
    """
    Pregunta al usuario que seleccione su idioma y devuelve el código de idioma correspondiente.

    Returns:
        str: El código de idioma seleccionado por el usuario ("en" para inglés o "es" para español).
    """
    print("Select your language / Selecciona tu idioma:")
    print("1. English")
    print("2. Español")
    while True:
        choice = input("Enter your choice / Ingresa tu elección: ")
        if choice == "1":
            return "en"
        elif choice == "2":
            return "es"
        else:
            print(translations['en']['invalid_choice'])

def get_user_input(prompt, is_integer=True):
    """
    Solicita una entrada al usuario y opcionalmente la valida como un entero.

    Args:
        prompt (str): El mensaje que se muestra al usuario.
        is_integer (bool, optional): Indica si la entrada debe ser un entero. Por defecto, es True.

    Returns:
        int/str: El valor ingresado por el usuario, convertido a un entero si is_integer es True,
        de lo contrario, una cadena.
    """
    while True:
        user_input = input(prompt)
        if is_integer:
            try:
                return int(user_input)
            except ValueError:
                print(translations['en']['invalid_input'])
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
        return scores
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
            file.write(score)


def main():
    """
    Función principal del juego de adivinanza de números.
    """
    user_language = get_user_language()
    translation = translations[user_language]

    print(translation['welcome'])

    customize_game = get_user_input(translation['customize_prompt'], is_integer=False)

    if customize_game.lower() == 'y':
        lower = get_user_input(translation['lower_bound_prompt'])
        upper = get_user_input(translation['upper_bound_prompt'])
        max_attempts = get_user_input(translation['max_attempts_prompt'])
    else:
        lower = 1
        upper = 100
        max_attempts = 10

    target_number = random.randint(lower, upper)
    attempts = 0

    print(translation['guess_range'].format(lower=lower, upper=upper))
    print(translation['max_attempts'].format(max_attempts=max_attempts))

    while attempts < max_attempts:
        guess = get_user_input(translation['guess_prompt'])

        if guess == target_number:
            print(translation['congrats'].format(target_number=target_number, attempts=attempts + 1)) # pylint: disable=line-too-long
            player_name = get_user_input(translation['enter_name'], is_integer=False)
            scores = load_scores()
            scores.append(f"{player_name}: {attempts + 1} {translation['attempts']}")
            save_scores(scores)
            break
        if guess < target_number:
            print(translation['too_low'])
        else:
            print(translation['too_high'])

        attempts += 1
    else:
        print(translation['out_of_attempts'].format(max_attempts=max_attempts, target_number=target_number)) # pylint: disable=line-too-long

    print(translation['top_scores'])
    scores = load_scores()
    scores.sort(key=lambda x: int(x.split(":")[-1].split()[0]))  # Ordenar por número de intentos
    for score in scores[:5]:  # Mostrar las 5 mejores puntuaciones
        print(score)

if __name__ == "__main__":
    main()
