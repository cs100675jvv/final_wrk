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
