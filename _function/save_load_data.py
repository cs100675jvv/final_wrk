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
    """
    Manages the loading and saving of data.
    """

    def __init__(self, data_path):
        self.data_path = data_path
        self.plain_handler = PlainDataHandler()
        self.encrypted_handler = EncryptedDataHandler()

    def load_data_plain(self, filename):
        """
        Load plain data from a file.

        Args:
            filename (str): The name of the file to load.

        Returns:
            data_bundle: The loaded data.
        """
        filename = f"{self.data_path}/{filename}.pkl"
        data_bundle = self.plain_handler.load_data(filename)
        print("Data loaded successfully.")
        return data_bundle

    def load_data_encrypted(self, filename):
        """
        Load encrypted data from a file.

        Args:
            filename (str): The name of the file to load.

        Returns:
            data_bundle: The loaded data.
        """
        filename = f"{self.data_path}/{filename}.pklc"

        while True:
            try:
                password = getpass.getpass("Loading encrypted saved data. Enter password: ")
                data_bundle = self.encrypted_handler.load_data(filename, password)
                print("Secured data loaded successfully.")
                return data_bundle
            except ValueError:
                print("Incorrect password. Please try again.")
            except FileNotFoundError:
                print(f"No file found at {filename}. Creating new data bundle.")
                address_book = AddressBook()
                note_book = NoteBook()
                data_bundle = DataBundle(address_book, note_book)
                self.encrypted_handler.save_data(data_bundle, filename, password)
                return data_bundle

    def save_data_plain(self, data, filename):
        """
        Save plain data to a file.

        Args:
            data: The data to save.
            filename (str): The name of the file to save.
        """
        filename = f"{self.data_path}/{filename}.pkl"
        self.plain_handler.save_data(data, filename)
        print("Data saved successfully.")

    def save_data_encrypted(self, data, filename):
        """
        Save encrypted data to a file.

        Args:
            data: The data to save.
            filename (str): The name of the file to save.
        """
        filename = f"{self.data_path}/{filename}.pklc"
        password = getpass.getpass("Enter password: ")
        self.encrypted_handler.save_data(data, filename, password)
        print("Data saved successfully and securely.")

class PlainDataHandler:
    """
    Handles saving and loading data using pickle.
    """

    def save_data(self, book, filename):
        """
        Saves the given data to a file.

        Parameters:
        - book: The data to be saved.
        - filename: The path of the file to save the data to.
        """
        data_path = os.path.dirname(filename)
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        with open(filename, "wb") as f:
            pickle.dump(book, f)

    def load_data(self, filename):
        """
        Loads data from a file, or creates a new data bundle if the file doesn't exist.

        Parameters:
        - filename: The path of the file to load the data from.

        Returns:
        - The loaded data bundle.
        """
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
    """
    Handles saving with encryption and decryption of data using AES algorithm.
    """

    def get_aes(self, password):
        """
        Generates an AES object using a hashed password.
        see https://uk.wikipedia.org/wiki/Advanced_Encryption_Standard
        AES (Advanced Encryption Standard) is a symmetric encryption algorithm used for data encryption.
        The password is hashed using SHA256 to create a fixed-size byte string.

        Args:
            password (str): The password used for encryption.

        Returns:
            AES object: The AES object used for encryption.
        """
        password_hash = SHA256.new(password.encode()).digest()
        return AES.new(password_hash, AES.MODE_ECB)

    def save_data(self, book, filename, password):
        """
        Save data in an encrypted form.
        First checks if the directory for the file exists, if not, it creates it.
        Then opens the file in write-binary mode, encrypts the data using AES and writes it to the file.

        Args:
            book (object): The data to be saved.
            filename (str): The path to the file where the data will be saved.
            password (str): The password used for encryption.

        Raises:
            FileNotFoundError: If the directory for the file does not exist.

        """
        aes = self.get_aes(password)
        data_path = os.path.dirname(filename)
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        with open(filename, "wb") as f:
            data = pickle.dumps(book)
            encrypted_data = aes.encrypt(pad(data, AES.block_size))
            f.write(encrypted_data)

    def load_data(self, filename, password):
        """
        Load and decrypt data.
        Opens the file in read-binary mode, reads the encrypted data, and then decrypts it using AES.

        Args:
            filename (str): The path to the file containing the encrypted data.
            password (str): The password used for decryption.

        Returns:
            object: The decrypted data.

        Raises:
            FileNotFoundError: If the file does not exist.

        """
        try:
            aes = self.get_aes(password)
            with open(filename, "rb") as f:
                encrypted_data = f.read()
                data = unpad(aes.decrypt(encrypted_data), AES.block_size)
                return pickle.loads(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"No file found at {filename}")