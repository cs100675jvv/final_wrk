from _classes.adress_book import AddressBook


def delete_contact(args, book: 'AddressBook'):
    """
    Deletes a contact from the address book.

    Args:
        args (list): A list of arguments passed to the function. The first element is the name of the contact to be deleted.
        book (AddressBook): The address book object.

    Returns:
        str: A message indicating the result of the deletion.
    """
    name, *_ = args
    record = book.find(name)
    if record is None:
        message = f"Contact with name {name} does not exist. Use `all` to list all contacts."
    else:
        book.delete(name)
        message = f"Contact {name} deleted."
    return message

