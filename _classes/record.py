from _classes.fields import Name, Phone, Birthday, Email, Address


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.address = None
        self.birthday = None

    def add_phone(self, phone):
        phone_field = Phone(phone)
        # phone_field.validate()
        self.phones.append(phone_field)

    def delete_phone(self, phone):
        for i, phone_field in enumerate(self.phones):
            if phone_field.value == phone:
                del self.phones[i]
                return
        raise ValueError("Phone number not found.")

    def edit_phone(self, phone, new_phone):
        for phone_field in self.phones:
            if phone_field.value == phone:
                phone_field.value = new_phone
                # phone_field.validate()
                return
        raise ValueError("Phone number not found.")

    def find_phone(self, phone):
        for phone_field in self.phones:
            if phone_field.value == phone:
                return phone
        raise ValueError("Phone number not found.")

    def add_birth(self, birthday):
        self.birthday = Birthday(birthday)
        return

    def edit_birth(self, new_birthday):
        self.birthday = new_birthday
        return

    def add_mail(self, email):
        self.email = Email(email)
        return

    def edit_mail(self, new_email):
        self.email = new_email
        return

    def add_address(self, address):
        self.address = Address(address)
        return

    def edit_address(self, new_address):
        self.address = new_address
        return

    def __str__(self):
        birthday_info = f", Birthday: {self.birthday.value.strftime('%d-%m-%Y')}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}{birthday_info}"
