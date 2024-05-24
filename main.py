# import re
# import tkinter as tk
# from tkinter import font as tkfont
# from _classes.notes import NoteBook
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
from _function.save_load_data import save_data, load_data
from _function.show import show_phone, show_all, show_birthday, birthdays
from _function.search import search_all

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter, Completer
from rich.console import Console

data_path = "./_files"

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
    'search'
]

completer = WordCompleter(commands, ignore_case=True)

console = Console()

class FirstWordCompleter(Completer):
    def __init__(self, completer):
        self.completer = completer

    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor
        if ' ' in text_before_cursor:
            return
        
        yield from self.completer.get_completions(document, complete_event)

def main():
    book = load_data(filename=f"{data_path}/addressbook.pkl", class_name="AddressBook")
    notebook = load_data(filename=f"{data_path}/notebook.pkl", class_name="NoteBook")

    print("Hello. How can I help you today?\n")

    while True:
        user_input = prompt('>>> ', completer=FirstWordCompleter(completer))
        command, *args = parse_input(user_input)
        
        if not command:
                continue
        
        if command in ["close", "exit"]:
            save_data(book, filename=f"{data_path}/addressbook.pkl")
            save_data(notebook, filename=f"{data_path}/notebook.pkl")
            console.print("[red]Good bye![/red]")
            break
        elif command == "hello":
            console.print("How can I help you?\n")
        elif command == "add":
            result = add_contact(args, book)
            console.print(f"{result}\n")
        elif command == "change":
            change_contact(args, book)
            console.print("Contact changed.\n")
        elif command == "delete":
            delete_contact(args, book)
            console.print("Contact deleted.\n")
        elif command == "show_phone":
            result = show_phone(book, *args)
            console.print(f"{result}\n")
        elif command == "all":
            result = show_all(book)
            if result:
                console.print(f"{result}\n")
            else:
                console.print("No contacts found.\n")
        elif command == "add_birthday":
            add_birthday(args, book)
            # console.print("Birthday added.\n")
        elif command == "change_birthday":
            change_birthday(args, book)
            # console.print("Birthday changed.\n")
        elif command == "show_birthday":
            result = show_birthday(args, book)
            console.print(f"Birthday: {result}\n")
        elif command == "birthdays":
            result = birthdays(book)
            console.print(f"Upcoming birthdays: {result}\n")
        
        elif command == "add_note":
            add_note(args, notebook)
        elif command == "delete_note":
            delete_note(args, notebook)
        elif command == "list_notes":
            list_notes(notebook)
        elif command == "show_note":
            show_note(args, notebook)
        elif command == "edit_note":
            edit_note(args, notebook)
        elif command == "find_note":
            find_note(args, notebook)
        
        elif command == "add_email":
            add_email(args, book)
            # console.print("Email added.\n")
        elif command == "change_email":
            change_email(args, book)
            # console.print("Email changed.\n")
        elif command == "add_address":
            add_address(args, book)
            # console.print("Address added.\n")
        elif command == "change_address":
            change_address(args, book)
            # console.print("Address changed.\n")
        elif command == "search":
            search_all(args, book)
        elif command == "help":
            console.print(print_help())
        else:
            console.print("[red]Invalid command[/red].\n")

if __name__ == "__main__":
    main()
