from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from rich.console import Console
import getpass

from _classes.command_completer import CommandCompleter
from _function.add_contact import add_contact, add_birthday, add_email, add_address
from _function.add_note import add_note
from _function.list_notes import list_notes
from _function.show_note import show_note
from _function.edit_note import edit_note
from _function.delete_note import delete_note
from _function.change_contact import change_contact, change_birthday, change_email, change_address
from _function.delete_contact import delete_contact
from _function.help import print_help
from _function.find_note import find_note
from _function.parse import parse_input
from _function.save_load_data import DataManager
from _function.show import show_phone, show_all, show_birthday
from _function.upcoming_birthdays import get_upcoming_birthdays, print_upcoming_birthdays
from _function.search import search_all

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter, Completer
from rich.console import Console

data_path = "./_files"
data_file_name = "DataBundle"

commands = [
    'close',
    'exit',
    'hello',
    'help',
    'add',
    'change',
    'delete',
    'show_phone',
    'all',
    'add_birthday',
    'show_birthday',
    'change_birthday',
    'birthdays',
    'add_note',
    'list_notes',
    'show_note',
    'edit_note',
    'delete_note',
    'find_note',
    'add_email',
    'change_email',
    'add_address',
    'change_address',
    'search',
    'save',
    'save_secure',
    'load',
    'load_secure',
    'yes'
]

completer = WordCompleter(commands, ignore_case=True)
console = Console()
data_manager = DataManager(data_path)

def main():
    # loading data plain by default
    data_bundle = data_manager.load_data_plain(data_file_name)

    # loading refs to address_book and note_book
    book = data_bundle.address_book
    notebook = data_bundle.note_book

    # changes_made flag
    changes_made = False

    # greeting
    console.print("Hello. How can I help you today?\n")
    
    # user interaction loop
    while True:
        user_input = prompt('>>> ', completer=CommandCompleter(completer))
        command, *args = parse_input(user_input)
        
        if not command:
                continue

        # commands - saving and loading data, exiting
        elif command == "save":
            data_manager.save_data_plain(data_bundle, data_file_name)
            changes_made = False
        elif command == "save_secure":
            data_manager.save_data_encrypted(data_bundle, data_file_name)
            changes_made = False
        elif command == "load":
            data_manager.load_data_plain(data_file_name)
            changes_made = False
        elif command == "load_secure":
            data_manager.load_data_encrypted(data_file_name)
            changes_made = False
        elif command in ["close", "exit"]:
            if changes_made:
                confirm = input("You have unsaved changes. Are you sure you want to exit? (yes/no) ")
                if confirm.lower() != "yes":
                    continue
            console.print("[red]Good bye![/red]")
            break

        # commands - contact viewing and editing
        elif command == "add":
            result = add_contact(args, book)
            console.print(result)
            changes_made = True
        elif command == "change":
            result = change_contact(args, book)
            console.print(result)
            changes_made = True
        elif command == "delete":
            result = delete_contact(args, book)
            console.print(result)
            changes_made = True
        elif command == "show_phone":
            result = show_phone(args, book)
            console.print(result)
        elif command == "all":
            result = show_all(book)
            console.print(result)
        
        # commands - contact birthdays
        elif command == "add_birthday":
            add_birthday(args, book)
            result = add_birthday(args, book)
            console.print(result)
            changes_made = True
        elif command == "change_birthday":
            change_birthday(args, book)
            changes_made = True
        elif command == "show_birthday":
            result = show_birthday(args, book)
            console.print(result)
        elif command == "birthdays":
            upcoming_birthdays = get_upcoming_birthdays(book)
            result = print_upcoming_birthdays(upcoming_birthdays)
            console.print(result)

        # commands - note
        elif command == "add_note":
            add_note(args, notebook)
            changes_made = True
        elif command == "delete_note":
            delete_note(args, notebook)
            changes_made = True
        elif command == "list_notes":
            list_notes(notebook)
        elif command == "show_note":
            result = show_note(args, notebook)
            console.print(result)
        elif command == "edit_note":
            edit_note(args, notebook)
            changes_made = True
        elif command == "find_note":
            result = find_note(args, notebook)
            console.print(result)
            # changes_made = True

        # commands - email and address
        elif command == "add_email":
            result = add_email(args, book)
            console.print(result)
            changes_made = True
        elif command == "change_email":
            result = change_email(args, book)
            console.print(result)
            changes_made = True
        elif command == "add_address":
            result = add_address(args, book)
            console.print(result)
            changes_made = True
        elif command == "change_address":
            change_address(args, book)
            changes_made = True
        elif command == "help":
            print_help()
        elif command == "search":
            result = search_all(args, book)
            console.print(result)
        else:
            console.print("[red]Invalid command[/red].\n")

if __name__ == "__main__":
    main()
