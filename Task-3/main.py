import sys
from pathlib import Path
from colorama import Fore, init, Style

init(autoreset=True)
# Декор
def print_tree(path: Path, indent: str = ""):

    try:
        items = sorted(path.iterdir(), key = lambda x: (not x.is_dir(), x.name.lower()))
    except PermissionError:
        print(indent + Fore.GREEN + "Доступ заборонено")
        return
    
    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        branch = "└── " if is_last else "├── "
        next_indent  = indent + ("  " if is_last else "│   ")

        if item.is_dir():
            print(indent + branch + Fore.BLUE + item.name + "/")
            print_tree(item, next_indent)
        else:
            print(indent + branch + Fore.GREEN + item.name)
# Основна функція
def main():
    if len(sys.argv) != 2:
        print("Використання скрипту")
        sys.exit(1)
    
    root = Path(sys.argv[1])

    if not root.exists():
        print("Шляху не існує")

    if not root.is_dir():
        print("Не являється директорією")
    
    print(Fore.CYAN + f"Структура директорії {root.resolve()}")
    print_tree(root)

if __name__ == "__main__":
    main()


    

