import os
import pickle

from _classes.adress_book import AddressBook

data_path = "./_files"


def save_data(book, filename=f"{data_path}/addressbook.pkl"):
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    with open(filename, "ab") as f:
        pickle.dump(book, f)


def load_data(filename=f"{data_path}/addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено
