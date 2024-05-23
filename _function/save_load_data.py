import os
import pickle

from _classes.adress_book import AddressBook
from _classes.notes import NoteBook

# def load_data(filename, class_name=None):
data_path = "./_files"


def save_data(book, filename=f"{data_path}/addressbook.pkl"):
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    with open(filename, "ab") as f:
        pickle.dump(book, f)


def load_data(filename=f"{data_path}/addressbook.pkl", class_name=None):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        if class_name is not None and class_name in globals():
            return globals()[class_name]()
        else:
            raise ValueError(f"Class '{class_name}' not found in global scope.")
        # return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено
