from datetime import datetime, timedelta


def get_upcoming_birthdays(book):
    today = datetime.today().date()
    upcoming_birthdays = []

    for record in book.data.values():
        if record.birthday:
            user_birthday = record.birthday.value.date()
            birthday_this_year = user_birthday.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = user_birthday.replace(year=today.year + 1)
            day_delta = (birthday_this_year - today).days

            if 0 <= day_delta <= 7:
                if birthday_this_year.weekday() == 5:
                    birthday_this_year += timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    birthday_this_year += timedelta(days=1)

                upcoming_birthdays.append({
                    'name': record.name.value,
                    'congratulation_date': birthday_this_year.strftime('%Y-%m-%d')
                })
    return upcoming_birthdays

def print_upcoming_birthdays(upcoming_birthdays):
    if not upcoming_birthdays:
        message = "No upcoming birthdays."
        return message

    headers = ["Name", "Congratulation Date"]

    max_name_length = max(len(record['name']) for record in upcoming_birthdays)
    max_date_length = max(len(record['congratulation_date']) for record in upcoming_birthdays)
    
    name_col_width = max(len(headers[0]), max_name_length)
    date_col_width = max(len(headers[1]), max_date_length)

    header = f"\n{headers[0]:<{name_col_width}}  {headers[1]:<{date_col_width}}"
    separator = f"{'-' * name_col_width}  {'-' * date_col_width}"
    message = header + '\n' + separator + '\n'
    for record in upcoming_birthdays:
        name = record['name']
        date = record['congratulation_date']
        message = message + f"{name:<{name_col_width}}  {date:<{date_col_width}}\n"
        return message
