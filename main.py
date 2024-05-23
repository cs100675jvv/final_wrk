import re
import tkinter as tk
from tkinter import font as tkfont
from _classes.notes import NoteBook
from _function.add_contact import add_contact, add_birthday, add_email, add_address
from _function.add_note import add_note
from _function.list_notes import list_notes
from _function.show_note import show_note
from _function.edit_note import edit_note
from _function.delete_note import delete_note
from _function.change_contact import change_contact, change_birthday, change_email, change_address
from _function.delete_contact import delete_contact
from _function.display_help import display_help
from _function.list_notes import list_notes
from _function.parse import parse_input
from _function.save_load_data import save_data, load_data
from _function.show import show_phone, show_all, show_birthday, birthdays

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter,Completer, Completion
from rich.console import Console
from rich.prompt import Prompt

data_path = "./_files"

commands = [
    'close',
    'exit',
    'hello',
    'add',
    'change',
    'delete',
    'show',
    'all',
    'add_birthday',
    'show_birthday',
    'birthdays',
    'add-note',
    'list-notes',
    'show-note',
    'edit-note',
    'delete-note'
]

completer = WordCompleter(commands, ignore_case=True)

console = Console()

class FirstWordCompleter(Completer):
    def __init__(self, completer):
        self.completer = completer

    def get_completions(self, document, complete_event):
        # Якщо курсор знаходиться на першому слові, використовувати completer
        if document.cursor_position_row == 0 and len(document.text_before_cursor.split()) <= 1:
            yield from self.completer.get_completions(document, complete_event)

def main():
    book = load_data(filename=f"{data_path}/addressbook.pkl", class_name="AddressBook")
    notebook = load_data(filename=f"{data_path}/notebook.pkl", class_name="NoteBook")

    print("Hello. How can I help you today?\n")

    while True:
        # user_input = input("Enter a command: ")
        user_input = prompt('>>> ', completer=FirstWordCompleter(completer))
        # command, *args = parse_input(user_input)
        command = user_input.split()
        
        if not command:
                continue
        
        if command[0] in ["close", "exit"]:
            save_data(book, filename=f"{data_path}/addressbook.pkl")
            save_data(notebook, filename=f"{data_path}/notebook.pkl")
            console.print("[red]Good bye![/red]")
            break
        elif command[0] == "hello":
            console.print("How can I help you?\n")
        elif command[0] == "add":
            result = add_contact(args, book)
            console.print(f"{result}\n")
        elif command[0] == "change":
            change_contact(args, book)
            console.print("Contact changed.\n")
        elif command[0] == "delete":
            delete_contact(args, book)
            console.print("Contact deleted.\n")
        elif command[0] == "show":
            result = show_phone(book, *args)
            console.print(f"{result}\n")
        elif command[0] == "all":
            result = show_all(book)
            if result:
                console.print(f"{result}\n")
            else:
                console.print("No contacts found.\n")
        elif command[0] == "add_birthday":
            add_birthday(args, book)
            console.print("Birthday added.\n")
        elif command[0] == "change_birthday":
            change_birthday(args, book)
            console.print("Birthday changed.\n")
        elif command[0] == "show_birthday":
            result = show_birthday(args, book)
            console.print(f"Birthday: {result}\n")
        elif command[0] == "birthdays":
            result = birthdays(book)
            console.print(f"Upcoming birthdays: {result}\n")
        
        elif command[0] == "add-note":
            add_note(args, notebook)
        elif command[0] == "delete-note":
            delete_note(args, notebook)
        elif command[0] == "list-notes":
            list_notes(notebook)
        elif command[0] == "show-note":
            show_note(args, notebook)
        elif command[0] == "edit-note":
            edit_note(args, notebook)
        
        elif command[0] == "add-email":
            add_email(book, *args)
            console.print("Email added.\n")
        elif command[0] == "change-email":
            change_email(args, book)
            console.print("Email changed.\n")
        elif command[0] == "add-address":
            add_address(args, book)
            console.print("Address added.\n")
        elif command[0] == "change-address":
            change_address(args, book)
            console.print("Address changed.\n")
        elif command[0] == "help":
            console.print(display_help())
        else:
            console.print("[red]Invalid command[/red].\n")

if __name__ == "__main__":
    main()
