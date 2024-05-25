import os
import pickle
import getpass

# pycryptodome-3.20.0
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256

from _classes.adress_book import AddressBook
from _classes.notes import NoteBook

class DataBundle:
    def __init__(self, address_book, note_book):
        self.address_book = address_book
        self.note_book = note_book

class DataManager:
    def __init__(self, data_path):
        self.data_path = data_path
        self.plain_handler = PlainDataHandler()
        self.encrypted_handler = EncryptedDataHandler()

    def load_data_plain(self, filename):
        filename = f"{self.data_path}/{filename}.pkl"
        data_bundle = self.plain_handler.load_data(filename)
        print("Data loaded successfully.")
        return data_bundle

    def load_data_encrypted(self, filename):
        filename = f"{self.data_path}/{filename}.pklc"
        password = getpass.getpass("Loading encrypted saved data. Enter password: ")
        data_bundle = self.encrypted_handler.load_data(filename, password)
        print("Secured data loaded successfully.")
        return data_bundle

    def save_data_plain(self, data, filename):
        filename = f"{self.data_path}/{filename}.pkl"
        self.plain_handler.save_data(data, filename)
        print("Data saved successfully.")

    def save_data_encrypted(self, data, filename):
        filename = f"{self.data_path}/{filename}.pklc"
        password = getpass.getpass("Enter password: ")
        self.encrypted_handler.save_data(data, filename, password)
        print("Data saved successfully and securely.")

class PlainDataHandler:
    def save_data(self, book, filename):
        data_path = os.path.dirname(filename)
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        with open(filename, "wb") as f:
            pickle.dump(book, f)

    def load_data(self, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            address_book = AddressBook()
            note_book = NoteBook()
            data_bundle = DataBundle(address_book, note_book)
            self.save_data(data_bundle, filename)
            return data_bundle

class EncryptedDataHandler:

    # Generates an AES object using a hashed password.
    # see https://uk.wikipedia.org/wiki/Advanced_Encryption_Standard
    # AES (Advanced Encryption Standard) is a symmetric encryption algorithm used for data encryption.
    # The password is hashed using SHA256 to create a fixed-size byte string.
    def get_aes(self, password):
        password_hash = SHA256.new(password.encode()).digest()
        return AES.new(password_hash, AES.MODE_ECB)

    # Save data in an encrypted form.
    # First checks if the directory for the file exists, if not, it creates it.
    # Then opens the file in write-binary mode, encrypts the data using AES and writes it to the file.
    def save_data(self, book, filename, password):
        aes = self.get_aes(password)
        data_path = os.path.dirname(filename)
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        with open(filename, "wb") as f:
            data = pickle.dumps(book)
            encrypted_data = aes.encrypt(pad(data, AES.block_size)) #encrypting data
            f.write(encrypted_data)

    # Load and decrypt data.
    # Opens the file in read-binary mode, reads the encrypted data, and then decrypts it using AES.
    def load_data(self, filename, password):
        try:
            aes = self.get_aes(password)
            with open(filename, "rb") as f:
                encrypted_data = f.read()
                data = unpad(aes.decrypt(encrypted_data), AES.block_size) #decrypting data
                return pickle.loads(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"No file found at {filename}")