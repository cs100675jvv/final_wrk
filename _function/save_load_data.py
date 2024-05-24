import os
import pickle

from _classes.adress_book import AddressBook
from _classes.notes import NoteBook

def save_data(book, filename):
    data_path = os.path.dirname(filename)
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename, class_name=None):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        if class_name is not None and class_name in globals():
            return globals()[class_name]()
        raise ValueError(f"Class '{class_name}' not found in global scope.")
