# Catdog-bot

## Description

Console bot for saving contacts, birthdays and notes

## Installation

To download and install the bot use
`install.sh`

To run the bot use `catdog-bot` command

## Usage

The bot support the following commands:

1. `hello`: Send a greeting from the bot.
2. `help`: Help output for bot commands.
3. `save`: Data storage in unencrypted form.
4. `save_secure`: Data saving in encrypted form. Requires a password.
5. `load`: Loading data stored in unencrypted form.
6. `load_secure`: Loading data stored in encrypted form. Requires a password.
7. `add [name] [phone]`: Add either a new contact with a name and phone number or a phone number to an existing contact.
   You can add multiple phone numbers.
8. `change [name] [old phone] [new phone]`: Change the phone number for the specified contact.
9. `show_phone [name]`: Show the phone numbers for the specified contact.
10. `all`: Show all contacts in the address book.
11. `add_birthday [name] [date of birth]`: Add the date of birth for the specified contact.
12. `show_birthday [name]`: Show the date of birth for the specified contact.
13. `birthdays`: Show the birthdays that are coming up in the next week.
14. `add-email [name] [email]`: Add either a new contact with a name and email or a email to an existing contact.
15. `change-email [name] [old-email] [new-email]`: Change the email for the specified contact.
16. `add-address [name] [address]`: Add either a new contact with a name and address or an address to an existing contact.
17. `change-address [name] [address]`: Change the address for the specified contact.
18. `search [string]`: Find cpntact by string.
14. `add_note [name]`: Open an editor for note's text. Type `:end` to finish editing. After this the note added.
15. `list_notes`: Show the list of all notes.
16. `show_note [note_id]`: Show all info about the Note with note_id
17. `edit_note [note_id]`: Edit existing Note by ID
18. `delete_note [note_id]`: Delete selected Note.
19. `find_note [string]`: Find notes by string.
20. `close` or `exit`: Close the program.

## Installation as package
Use the command `pip install -e .` from the root directory to install this app a package.

Then use `catdog-bot` command to run the bot.
