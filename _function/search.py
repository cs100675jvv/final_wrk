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
#        if record.address and search_term in record.address.value.lower():
#            results.append(record)
#            continue

        # Check if the search term matches the birthday
        if record.birthday and search_term in record.birthday.value.strftime('%d-%m-%Y').lower():
            results.append(record)
            continue

    # Print all found results
    if results:
        for result in results:
            print(result)
    else:
        print("No matching records found.")
