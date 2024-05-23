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



def main():
    book = load_data()
    notebook = NoteBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            add_contact(args, book)

        elif command == "delete":
            delete_contact(args, book)

        elif command == "show":
            show_phone(args, book)

        elif command == "change":
            change_contact(args, book)

        elif command == "phone":
            show_phone (args, book)

        elif command == "all":
            show_all(book)

        elif command == "add-birthday":
            add_birthday(args, book)

        elif command == "change-birthday":
            change_birthday(args, book)    

        elif command == "show-birthday":
            show_birthday(args, book)

        elif command == "birthdays":
            birthdays(book)


        elif command == "add-note":
            add_note(args, notebook)

        elif command == "list-notes":
            list_notes(notebook)

        elif command == "add-email":
            add_email(args, book)

        elif command == "change-email":
            change_email(args, book)  

        elif command == "add-address":
            add_address(args, book)

        elif command == "change-address":
            change_address(args, book)     

        elif command == "help":
            print_help() 

        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()
