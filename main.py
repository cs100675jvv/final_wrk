import re
import tkinter as tk
from _classes.notes import NoteBook
from _function.find_note import find_note
from _function.add_contact import add_contact, add_birthday, add_email, add_address
from _function.add_note import add_note
from _function.change_contact import change_contact, change_birthday, change_email, change_address
from _function.delete_contact import delete_contact
from _function.help import print_help
from _function.list_notes import list_notes
from _function.parse import parse_input
from _function.save_load_data import save_data, load_data
from _function.show import show_phone, show_all, show_birthday, birthdays
from gui import init_gui

data_path = "./_files"

def main():
    book = load_data(filename=f"{data_path}/addressbook.pkl", class_name="AddressBook")
    notebook = load_data(filename=f"{data_path}/notebook.pkl", class_name="NoteBook")

    window, canvas, user_input, messages = init_gui()

    def insert_message(text):
        messages.insert(tk.END, text)
        messages.see(tk.END)  # Scroll text to bottom

    def clear_messages():
        messages.delete('1.0', tk.END)

    insert_message("Hello. How can I help you today?\n")

    def handle_input(event):
        input_data = re.sub(r'[^\w-]+', ' ', user_input.get().strip())
        command, *args = parse_input(input_data)
        command = command.lower()
        user_input.delete(0, tk.END)

        insert_message(f"{command} {' '.join(args)}\n")
        messages.tag_config("right", justify='right')
        messages.tag_add("right", "end-2l", "end-1l")

        if command in ["close", "exit"]:
            save_data(book, filename=f"{data_path}/addressbook.pkl")
            save_data(notebook, filename=f"{data_path}/notebook.pkl")
            insert_message("Good bye!\n")
            window.quit()
        elif command == "hello":
            insert_message("How can I help you?\n")
        elif command == "add":
            result = add_contact(args, book)
            insert_message(f"{result}\n")
        elif command == "change":
            change_contact(args, book)
            insert_message("Contact changed.\n")
        elif command == "delete":
            delete_contact(args, book)
            insert_message("Contact deleted.\n")
        elif command == "show":
            result = show_phone(book, *args)
            insert_message(f"{result}\n")
        elif command == "all":
            result = show_all(book)
            if result:
                insert_message(f"{result}\n")
            else:
                insert_message("No contacts found.\n")
        elif command == "add_birthday":
            add_birthday(args, book)
            insert_message("Birthday added.\n")
        elif command == "change_birthday":
            change_birthday(args, book)
            insert_message("Birthday changed.\n")
        elif command == "show_birthday":
            result = show_birthday(args, book)
            insert_message(f"Birthday: {result}\n")
        elif command == "birthdays":
            result = birthdays(book)
            insert_message(f"Upcoming birthdays: {result}\n")
        elif command == "add-note":
            result = add_note(notebook)
            insert_message(f"{result}\n")
        elif command == "find-note":
            result = find_note(args, notebook)
            insert_message(f"Search results:\n {result}\n")
        elif command == "list-notes":
            result = list_notes(notebook)
            insert_message(f"Notes:\n{result}\n")
        elif command == "add-email":
            add_email(book, *args)
            insert_message("Email added.\n")
        elif command == "change-email":
            change_email(args, book)
            insert_message("Email changed.\n")
        elif command == "add-address":
            add_address(args, book)
            insert_message("Address added.\n")
        elif command == "change-address":
            change_address(args, book)
            insert_message("Address changed.\n")
        elif command == "help":
            insert_message(print_help() + "\n")
        elif command == 'clear':
            clear_messages()
            return
        else:
            insert_message("Invalid command.\n")

    # Bind the Return key to the handle_input function
    user_input.bind("<Return>", handle_input)
    window.mainloop()


if __name__ == "__main__":
    main()
