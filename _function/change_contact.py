from datetime import datetime

from _classes.adress_book import AddressBook
from _decorator.decorator import input_error_phones, input_error_birthday, input_error_emailes


@input_error_phones
def change_contact(args, book: 'AddressBook'):
    """
    Change the phone number of a contact in the address book.

    Args:
        args (list): A list of arguments containing the name, current phone number, new phone number.
        book (AddressBook): The address book object.

    Returns:
        str: A message indicating the result of the operation.
    """
    name, phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(phone, new_phone)
        message = f"Contact {name} now has phone: {new_phone}"
    else:
        message = f"Contact {name} not found in our dictionary."
    return message


@input_error_birthday
def change_birthday(args, book: 'AddressBook'):
    """
    Change the birthday of a contact in the address book.

    Args:
        args (list): A list containing the name and new birthday of the contact.
        book (AddressBook): The address book object.
    """
    name, birthday, *_ = args
    record = book.find(name)
    if record:
        record.edit_birth(birthday)
        return print(f"Contact {name} now has birthday: {datetime.strptime(birthday, '%d.%m.%Y')}")
    else:
        return print(f"Contact {name} not found in our dictionary.")


@input_error_emailes
def change_email(args, book: 'AddressBook'):
    """
    Change the email of a contact in the address book.

    Args:
        args (list): A list containing the name and new email of the contact.
        book (AddressBook): The address book object.

    Returns:
        str: A message indicating whether the contact was found and the email was changed.
    """
    name, email, *_ = args
    record = book.find(name)
    if record:
        record.edit_mail(email)
        return f"Contact {name} now has email: {email}"
    else:
        return f"Contact {name} not found in our dictionary."


def change_address(args, book: 'AddressBook'):
    """
    Change the address of a contact in the address book.

    Args:
        args (list): A list containing the name and new address of the contact.
        book (AddressBook): The address book object.
    """
    name, address, *_ = args
    record = book.find(name)
    if record:
        record.edit_address(address)
        return print(f"Contact {name} now has address: {address}")
    else:
        return print(f"Contact {name} not found in our dictionary.")
