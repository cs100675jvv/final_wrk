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
    if record:
        record.add_birth(birthday)
        message = f"Birthday for contact {name} updated."
    else:
        message = f"Contact {name} not found."
    return message


@input_error_email
def add_email(args, book: AddressBook):
    name, email, *_ = args
    record = book.find(name)
    message = f"Contact {name} updated with email {email}."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact {name} added with email {email}."
    if email:
        record.add_mail(email)
    return message


def add_address(args, book: AddressBook):
    if len(args) < 2:
        message = "Please provide both name and address."
        return message
    name, address = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_addr(address)
    message = f'Address {address} added'
    return message
