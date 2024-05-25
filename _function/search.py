from _classes.adress_book import AddressBook


def search_all(args, book: AddressBook):
    search_term = ' '.join(args).lower()  # Combine all args to handle multi-word search terms
    results = []

    for record in book.values():
        # Check if the search term matches the name
        if search_term in record.name.value.lower():
            results.append(record)
            continue

        # Check if the search term matches any phone number
        for phone in record.phones:
            if search_term in phone.value.lower():
                results.append(record)
                break  # No need to check other phones if one matches

        # Check if the search term matches the email
        if record.email and search_term in record.email.value.lower():
            results.append(record)
            continue

        # Check if the search term matches the address
        if record.address and search_term in record.address.value.lower():
            results.append(record)
            continue

        # Check if the search term matches the birthday
        if record.birthday and search_term in record.birthday.value.strftime('%d-%m-%Y').lower():
            results.append(record)
            continue

    # Print all found results
    if not results:
        return "No matching records found."

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
    for record in results:
        name = record.name.value
        phones = ', '.join(phone.value for phone in record.phones) if record.phones else ''
        email = record.email.value if record.email else ''
        address = record.address.value if record.address else ''
        row = (f"{name:<{name_col_width}}  {phones:<{phones_col_width}}  "
               f"{email:<{email_col_width}}  {address:<{address_col_width}}")
        rows.append(row)

    return '\n'.join(rows)