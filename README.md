# final_wrk

## Description
Console bot for saving contacts, birthdays and notes

## Usage
To run the bot use `main.py`

The bot support the following commands:

1. `add [name] [phone]`: Add either a new contact with a name and phone number or a phone number to an existing contact. You can add multiple phone numbers.
2. `change [name] [old phone] [new phone]`: Change the phone number for the specified contact.
3. `phone [name]`: Show the phone numbers for the specified contact.
4. `all`: Show all contacts in the address book.
5. `add-birthday [name] [date of birth]`: Add the date of birth for the specified contact.
6. `show-birthday [name]`: Show the date of birth for the specified contact.
7. `birthdays`: Show the birthdays that are coming up in the next week.
8. `hello`: Send a greeting from the bot.
9. `add-note [name]`: Open an editor for note's text. Type `:end` to finish editing. After this the note added.
10. `list-notes`: Show the list of all notes.
11. `show-note` [note_id]: Show all info about the Note iwth note_id
12. `delete-note` [note_id]: Delete selected Note.
13. `close` or `exit`: Close the program.

## Example Usage
