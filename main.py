import os
from gtts import gTTS
from googletrans import Translator
from colorama import Fore, Style, init
import itertools
import datetime
import time
import random

init(autoreset=True)

def text_to_speech(text, language='en', filename="audio.mp3"):
    """Convierte texto a voz, lo guarda en una carpeta y lo reproduce."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    folder_path = f"audio_{today}"
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, filename)
    tts = gTTS(text=text, lang=language)
    tts.save(file_path)

    try:
        os.startfile(file_path)
    except Exception as e:
        print(Fore.RED + f"Error al reproducir: {e}. Asegúrate de tener un reproductor de audio instalado.")

def show_welcome_message():
    """Muestra el mensaje de bienvenida con arte ASCII."""
    # Arte ASCII de una hoja de maple
    maple_leaf = """
         🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁
                                 HASHMALWARE 2024 
         🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁
    """

    print(Fore.RED + maple_leaf)
    print(Fore.GREEN + "Welcome to the multilingual text-to-speech converter!")

def show_falling_snow():
    """Simula nieve cayendo en la consola."""
    width = os.get_terminal_size().columns
    for _ in range(1):  # Ajusta el número de líneas de nieve
        snowflakes = ["🍁" for _ in range(width)]
        for i in range(width):
            if random.random() < 0.1:
                snowflakes[i] = " "
        print("".join(snowflakes))
        time.sleep(0.1)

def main():
    translator = Translator()
    colors = [Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    color_cycle = itertools.cycle(colors)

    show_welcome_message()

    # Selección inicial de idioma (solo la primera vez)
    print(next(color_cycle) + "\nChoose your language:")
    print("1. French (fr)")
    print("2. Spanish (es)")
    print("3. Italian (it)")
    print("4. English (en)")
    lang_choice = input(next(color_cycle) + "Enter your choice (1-4): ")
    language_code = {'1': 'fr', '2': 'es', '3': 'it', '4': 'en'}.get(lang_choice, 'en')

    while True:
        print(next(color_cycle) + "\nChoose an action:")
        print("1. Convert text to speech")
        print("2. Change language")
        print("3. Exit")
        choice = input(next(color_cycle) + "Enter your choice (1-3): ")

        if choice == '1':
            text = input(next(color_cycle) + "Enter the text you want to convert to speech: ")
            filename = input(next(color_cycle) + "Enter the desired filename (e.g., my_audio.mp3): ")
            text_to_speech(text, language_code, filename)
        elif choice == '2':
            print(next(color_cycle) + "\nChoose a language for text-to-speech:")
            print("1. French (fr)")
            print("2. Spanish (es)")
            print("3. Italian (it)")
            print("4. English (en)")
            lang_choice = input(next(color_cycle) + "Enter your choice (1-4): ")
            language_code = {'1': 'fr', '2': 'es', '3': 'it', '4': 'en'}.get(lang_choice, 'en')
        elif choice == '3':
            show_falling_snow()
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
