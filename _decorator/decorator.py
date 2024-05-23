import re
from datetime import datetime


class PhoneValidationError(ValueError):
    pass


class NameValidationError(ValueError):
    pass


class EmailValidationError(ValueError):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            name, phone = args[0]

            if not re.match(r'^[A-ZА-ЯЁ][a-zа-яё]*$', name):
                raise NameValidationError

            if not re.match(r'^\d{10,}$', phone):
                raise PhoneValidationError

            return func(*args, **kwargs)

        except PhoneValidationError:
            print('Invalid phone number. Phone number should contain only digits and be at least 10 digits long.')
        except NameValidationError:
            print("Invalid name. Name should contain only letters.")
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name and phone please")
        except IndexError:
            print("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner


def input_error_phones(func):
    def inner(*args, **kwargs):
        try:
            name, phone, new_phone, *_ = args[0]

            if not re.match(r'^[A-ZА-ЯЁ][a-zа-яё]*$', name):
                raise NameValidationError

            if not re.match(r'^\d{10,}$', phone):
                raise PhoneValidationError

            if not re.match(r'^\d{10,}$', new_phone):
                raise PhoneValidationError

            return func(*args, **kwargs)

        except PhoneValidationError:
            print('Invalid phone number. Phone number should contain only digits and be at least 10 digits long.')
        except NameValidationError:
            print("Invalid name. Name should contain only letters.")
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name and phones please")
        except IndexError:
            print("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner


def input_error_name(func):
    def inner(*args, **kwargs):
        try:
            name, = args[0]

            if not re.match(r'^[A-ZА-ЯЁ][a-zа-яё]*$', name):
                raise NameValidationError

            return func(*args, **kwargs)

        except PhoneValidationError:
            print('Invalid phone number. Phone number should contain only digits and be at least 10 digits long.')
        except NameValidationError:
            print("Invalid name. Name should contain only letters.")
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name please")
        except IndexError:
            print("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner


def input_error_birthday(func):
    def inner(*args, **kwargs):
        try:
            name, birthday = args[0]

            if not re.match(r'^[A-ZА-ЯЁ][a-zа-яё]*$', name):
                raise NameValidationError

            birthday_obj = datetime.strptime(birthday, '%d.%m.%Y')  # Перевірка та створення об'єкта дати
            current_year = datetime.now().year
            if birthday_obj.year < 1900 or birthday_obj.year > current_year:
                raise ValueError("Invalid year. Birth year should be between 1900 and current year.")

            return func(*args, **kwargs)

        except PhoneValidationError:
            print('Invalid phone number. Phone number should contain only digits and be at least 10 digits long.')
        except NameValidationError:
            print("Invalid name. Name should contain only letters with capital letter first.")
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name and birthday please")
        except IndexError:
            print("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner


def input_error_email(func):
    def inner(*args, **kwargs):
        try:
            name, email = args[0]

            if not re.match(r'^[A-ZА-ЯЁ][a-zа-яё]*$', name):
                raise NameValidationError

            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_regex, email):
                raise EmailValidationError

            return func(*args, **kwargs)

        except EmailValidationError:
            print('Invalid email. Please, enter a real email.')
        except NameValidationError:
            print("Invalid name. Name should contain only letters with capital letter first.")
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name and email please")
        except IndexError:
            print("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner


def input_error_emailes(func):
    def inner(*args, **kwargs):
        try:
            name, email, new_email, *_ = args[0]

            if not re.match(r'^[A-ZА-ЯЁ][a-zа-яё]*$', name):
                raise NameValidationError

            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_regex, email):
                raise EmailValidationError

            if not re.match(email_regex, new_email):
                raise EmailValidationError

            return func(*args, **kwargs)

        except EmailValidationError:
            print('Invalid email. Please, enter a real email.')
        except NameValidationError:
            print("Invalid name. Name should contain only letters with capital letter first.")
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name and emailes please")
        except IndexError:
            print("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner
