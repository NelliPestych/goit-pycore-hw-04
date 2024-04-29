import sys
from pathlib import Path
from colorama import Fore, Style


def recursive_iterdir(directory, white_space):
    for subdirectory in directory.iterdir():
        if subdirectory.is_dir():
            print(Fore.BLUE + f"{white_space}{subdirectory.name}/")
            recursive_iterdir(subdirectory, white_space + ' ')
        elif subdirectory.is_file():
            print(Fore.GREEN + f"{white_space}{subdirectory.name}")

def visualize_directory_structure(directory):
    try:
        directory_path = Path(directory)
        if not directory_path.is_dir():
            print("Вказаний шлях не є директорією.")
            return

        print(Fore.BLUE + f"{directory}/")
        recursive_iterdir(directory_path, ' ')

    except FileNotFoundError:
        print("Шлях не існує.")
    except Exception as e:
        print("Сталася помилка:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Введіть шлях до директорії як аргумент командного рядка.")
    else:
        directory_path = sys.argv[1]
        visualize_directory_structure(directory_path)
