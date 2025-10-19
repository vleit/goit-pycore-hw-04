def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    cmd = cmd.lower()
    return cmd, args

# Функції команд
def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add <username> <phone>"
    name, phone = args
    if name in contacts:
        return f"Contact '{name}' already exists. Use 'change' to update."
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change <username> <phone>"
    name, phone = args
    if name not in contacts:
        return f"Contact '{name}' not found."
    contacts[name] = phone
    return "Contact updated."


def get_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone <username>"
    name = args[0]
    if name not in contacts:
        return f"No contact found with name '{name}'."
    return f"{name} -> {contacts[name]}"


def get_all_contacts(contacts):
    if not contacts:
        return "No contacts saved yet."
    return "\n".join([f"{name} -> {phone}" for name, phone in contacts.items()])

# Основна функція
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

##