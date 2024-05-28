from datetime import datetime
from _decorator.decorator import input_error_note
from _classes.adress_book import AddressBook
# from _function.upcoming_birthdays import get_upcoming_birthdays


def show_phone(args, book: 'AddressBook'):
    """
    Display the phone numbers of a contact in the address book.

    Args:
        args (list): A list of arguments. The first argument is the name of the contact.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A string containing the contact's name and their phone numbers, if found.
    """
    name, *_ = args
    record = book.find(name)
    if record:
        return f"Contact {name} has phone: {'; '.join(str(p) for p in record.phones)}"
    else:
        return f"Contact {name} not found in our dictionary."


def show_all(book: 'AddressBook'):
    """
    Display all records in the address book.

    Args:
        book (AddressBook): The address book containing the records.

    Returns:
        str: A formatted string representing all the records in the address book.
             If no records are available, it returns "No records available."
    """
    if not book.data:
        return "No records available."

    headers = ["Name", "Phones", "Email", "Address"]

    max_name_length = max(len(record.name.value) for record in book.data.values())
    max_phones_length = max(len(', '.join(phone.value for phone in record.phones)) if record.phones else 0 for record in book.data.values())
    max_email_length = max(len(record.email.value) if record.email else 0 for record in book.data.values())
    max_address_length = max(len(record.address.value) if record.address else 0 for record in book.data.values())

    name_col_width = max(len(headers[0]), max_name_length)
    phones_col_width = max(len(headers[1]), max_phones_length)
    email_col_width = max(len(headers[2]), max_email_length)
    address_col_width = max(len(headers[3]), max_address_length)

    header = (f"{headers[0]:<{name_col_width}}  {headers[1]:<{phones_col_width}}  "
              f"{headers[2]:<{email_col_width}}  {headers[3]:<{address_col_width}}")
    separator = (f"{'-' * name_col_width}  {'-' * phones_col_width}  "
                 f"{'-' * email_col_width}  {'-' * address_col_width}")

    rows = [header, separator]
    for record in book.data.values():
        name = record.name.value
        phones = ', '.join(phone.value for phone in record.phones) if record.phones else ''
        email = record.email.value if record.email else ''
        address = record.address.value if record.address else ''
        row = (f"{name:<{name_col_width}}  {phones:<{phones_col_width}}  "
               f"{email:<{email_col_width}}  {address:<{address_col_width}}")
        rows.append(row)

    return '\n'.join(rows)

@input_error_note
def show_birthday(args, book: 'AddressBook'):
    """
    Show the birthday of a contact.

    Args:
        args (list): List of arguments passed to the function.
        book (AddressBook): The address book containing the contact records.

    Returns:
        str: A string indicating the birthday of the contact, or a message indicating that the contact has no added birthday
    """
    name, *_ = args
    record = book.find(name)
    if record:
        if record.birthday:
            date_obj = datetime.strptime(str(record.birthday), "%Y-%m-%d %H:%M:%S")
            return f"Contact {name} has birthday: {date_obj.strftime('%d-%m-%Y')}"
        
        return f"Contact {name} has no added birthday."
    return f"Contact {name} not found in our dictionary."
