import re
import tkinter as tk
from tkinter import scrolledtext
from tkinter import font as tkfont
from _function.parse import parse_input
from _function.add_contact import add_contact, add_birthday, add_email, add_address
from _function.change_contact import change_contact, change_birthday, change_email, change_address
from _function.delete_contact import delete_contact
from _function.show import show_phone, show_all, show_birthday, birthdays
from _function.save_load_data import save_data, load_data
from _function.add_note import add_note
from _function.list_notes import list_notes
from _function.help import print_help
from _classes.notes import NoteBook

# TODO: move to separate file?
def init_gui():
    window = tk.Tk()
    window.title("Assistant Bot by КотоПес team")

    # window size
    window_width = 600
    window_height = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # сenter of screen
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # dark mode
    window.configure(bg='#212121')

    # Define the font
    custom_font = tkfont.Font(family="ui-sans-serif", size=12)

    # Canvas for the rounded rectangle
    canvas = tk.Canvas(window, bg='#212121', bd=0, highlightthickness=0)
    canvas.place(relx=0.15, rely=0.9, relwidth=0.7, relheight=0.08)

    # Entry for user input
    user_input = tk.Entry(canvas, bg='#2f2f2f', fg='white', font=custom_font, insertbackground='white')
    user_input.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.6)

    # Set focus on user_input
    user_input.focus_set()

    # Listbox for displaying messages
    messages = tk.Text(window, bg='#212121', fg='white', font=custom_font, wrap=tk.WORD, borderwidth=0)
    messages.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.7)

    return window, canvas, user_input, messages

# TODO: move to separate file, review
def display_help():
    help_message = """
    Available commands:
    - hello: Greet the bot
    - add: Add a new contact. Args: name, phone
    - change: Change a contact. Args: name, new_phone
    - delete: Delete a contact. Args: name
    - show: Show a contact's phone. Args: name
    - add_birthday: Add a contact's birthday. Args: name, birthday
    - change_birthday: Change a contact's birthday. Args: name, new_birthday
    - show_birthday: Show a contact's birthday. Args: name
    - birthdays: Show upcoming birthdays
    - add-note: Add a note. Args: note_content
    - list-notes: List all notes
    - add-email: Add a contact's email. Args: name, email
    - change-email: Change a contact's email. Args: name, new_email
    - add-address: Add a contact's address. Args: name, address
    - change-address: Change a contact's address. Args: name, new_address
    - close/exit: Save data and exit
    """
    return help_message


#TODO: reactor commands to return string instead of calling print function inside or pass insert_message function to command if some loop inside etc.
def main():
    book = load_data()
    notebook = NoteBook()

    window, canvas, user_input, messages = init_gui()

    def insert_message(text):
        messages.insert(tk.END, text)
        messages.see(tk.END)  # Scroll text to bottom

    insert_message("Hello. How can I help you today?\n")

    def handle_input(event):
        # Get the user input and clear the input field
        # Parsing with cleanup of non-alphanumeric characters, whitespaces and converting command to lowercase
        input_data = re.sub(r'\W+', ' ', user_input.get().strip())
        command, *args = parse_input(input_data)
        command = command.lower()
        user_input.delete(0, tk.END)

        insert_message(f"{command} {' '.join(args)}\n")
        messages.tag_config("right", justify='right')
        messages.tag_add("right", "end-2l", "end-1l")

        if command in ["close", "exit"]:
            save_data(book)
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
            result = show_phone(book,*args)
            insert_message(f"{result}\n")
        elif command == "all":
            result = show_all(book)
            insert_message(f"{result}\n")
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
            add_note(notebook, *args)
            insert_message("Note added.\n")
        elif command == "list-notes":
            result = list_notes(notebook)
            insert_message(f"Notes: {result}\n")
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
            insert_message(display_help())
        else:
            insert_message("Invalid command.\n")

    # Bind the Return key to the handle_input function
    user_input.bind("<Return>", handle_input)
    window.mainloop()

if __name__ == "__main__":
    main()