from _classes.adress_book import AddressBook


def delete_contact(args, book: 'AddressBook'):
    name, *_ = args
    record = book.find(name)
    if record is None:
        message = f"Contact with name {name} does not exist. Use `all` to list all contacts."
    else:
        book.delete(name)
        message = f"Contact {name} deleted."
    return message

