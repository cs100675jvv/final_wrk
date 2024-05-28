from _classes.adress_book import AddressBook
from _classes.record import Record
from _decorator.decorator import input_error, input_error_birthday, input_error_email


@input_error
def add_contact(args, book: AddressBook):
    """
    Adds or updates a contact in the address book.

    Args:
        args (list): A list containing the contact details (name, phone).
        book (AddressBook): The address book object.

    Returns:
        str: A message indicating whether the contact was added or updated.
    """
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
    """
    Adds a birthday to a contact in the address book.

    Args:
        args (list): A list containing the name and birthday of the contact.
        book (AddressBook): The address book object.

    Returns:
        str: A message indicating the success or failure of the operation.
    """
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
    """
    Adds or updates an email for a contact in the address book.

    Args:
        args (list): A list containing the name and email of the contact.
        book (AddressBook): The address book object.

    Returns:
        str: A message indicating the result of the operation.
    """
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
    """
    Adds an address to a contact in the address book.

    Args:
        args (list): A list containing the name and address.
        book (AddressBook): The address book object.

    Returns:
        str: A message indicating the result of the operation.
    """
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
