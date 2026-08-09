from functools import wraps
from typing import Callable

def input_error(func: Callable) -> Callable:
    """
    Handle input errors raised by command handlers.

    Args:
        func: Command handler function.

    Returns:
        A wrapper function that handles input errors.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."

    return inner

def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Parse user input into a command and its arguments.

    Args:
        user_input: Raw input entered by the user.

    Returns:
        A tuple containing:
            - command (str)
            - list of command arguments (list[str])
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Add a new contact or rewrite exiting.

    Args:
        args: List containing a contact name and phone number.
        contacts: Dictionary storing contacts.

    Returns:
        A status message.
    """
    name, phone = args
    contacts[name] = phone

    return "Contact added."

@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Change the phone number of an existing contact.

    Args:
        args: List containing a contact name and phone number.
        contacts: Dictionary storing contacts.
    Returns:
        A status message.
    """
    name, phone = args

    contacts[name] = phone

    return "Contact updated"

@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Display the phone number for the contact.

    Args:
        args: List containing the contact name.
        contacts: Dictionary storing contacts.

    Returns:
        The contact's phone number or an error message.
    """
    name = args[0]

    return contacts[name]

@input_error
def show_all(contacts: dict[str, str]) -> str:
    """
    Display all saved contacts.

     Args:
        contacts: Dictionary storing contacts.
    
    Returns:
        A formatted string with all contacts.
    """
    if not contacts:
        return "No contacts found."

    return "\n".join(
        f"{name}: {phone}"
        for name, phone in contacts.items()
    )

def main() -> None:
    """
    Run the assistant bot.
    """
    contacts: dict[str, str] = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        # Skip empty input
        if not user_input.strip():
            continue

        command, args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break

            case "hello":
                print("How can I help you?")

            case "add":
                print(add_contact(args, contacts))

            case "change":
                print(change_contact(args, contacts))

            case "phone":
                print(show_phone(args, contacts))

            case "all":
                print(show_all(contacts))

            case _:
                print("Invalid command")

if __name__ == "__main__":
    main()

          