from _classes.adress_book import AddressBook
from _classes.record import Record
from _decorator.decorator import input_error, input_error_birthday, input_error_email


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error_birthday
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_birth(birthday)
    return print(f"Birthday for contact {name} updated.")


@input_error_email
def add_email(args, book: AddressBook):
    name, email, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if email:
        record.add_mail(email)
    return print(message)


def add_address(args, book: AddressBook):
    name, address, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_birth(address)
    return print('Address added')
