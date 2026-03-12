print("Simple Calculator")

from colorama import init, Fore
from config import APP_NAME, VERSION, WELCOME_TEXT
from utils import add, subtract, multiply, divide

init(autoreset=True)


def main():
    print(Fore.CYAN + f"{APP_NAME} v{VERSION}")
    print(Fore.GREEN + WELCOME_TEXT)

    while True:
        print("\nChoose operation:")
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "0":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print(Fore.RED + "Invalid choice")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print(Fore.RED + "Please enter valid numbers")
            continue

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        else:
            result = divide(a, b)

        print(Fore.YELLOW + f"Result: {result}")


if __name__ == "__main__":
    main()

# main application logic