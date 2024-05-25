from datetime import datetime

from _classes.adress_book import AddressBook
from _decorator.decorator import input_error_phones, input_error_birthday, input_error_emailes


@input_error_phones
def change_contact(args, book: 'AddressBook'):
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
    name, birthday, *_ = args
    record = book.find(name)
    if record:
        record.edit_birth(birthday)
        return print(f"Contact {name} now has birthday: {datetime.strptime(birthday, '%d.%m.%Y')}")
    else:
        return print(f"Contact {name} not found in our dictionary.")


@input_error_emailes
def change_email(args, book: 'AddressBook'):
    name, email, *_ = args
    record = book.find(name)
    if record:
        record.edit_mail(email)
        return f"Contact {name} now has email: {email}"
    else:
        return f"Contact {name} not found in our dictionary."


def change_address(args, book: 'AddressBook'):
    name, address, *_ = args
    record = book.find(name)
    if record:
        record.edit_address(address)
        return print(f"Contact {name} now has address: {address}")
    else:
        return print(f"Contact {name} not found in our dictionary.")
