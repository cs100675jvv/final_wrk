import re
import datetime
from collections import UserDict

class Note:
    def __init__(self, header: str, body: str = ""):
        self.header = header
        self.body = body
        self.creation_date = datetime.datetime.now()
        self.size = len(body)
        self.id = self._generate_id(header)

    def _generate_id(self, header: str) -> str:
        normalized_header = re.sub(r'\W+', '_', header.lower())
        return normalized_header

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Header: {self.header}\n"
                f"Body: {self.body}\n"
                f"Creation Date: {self.creation_date}\n"
                f"Size: {self.size} characters")

class NoteBook(UserDict):
    def add_note(self, note: Note):
        self.data[note.id] = note

    def get_note_by_id(self, note_id: str) -> Note:
        return self.data.get(note_id, None)

    def remove_note_by_id(self, note_id: str):
        if note_id in self.data:
            del self.data[note_id]
    
    # def display_notes(self):
    #     for note_id, note in self.data.items():
    #         print(f"Header: {note.header}, ID: {note.id}, Creation Date: {note.creation_date}")

    def display_notes(self):
        headers = ["Header", "ID", "Creation Date"]
        rows = [[note.header, note.id, note.creation_date.strftime("%Y-%m-%d %H:%M")] for note in self.data.values()]
        
        # Calculate the maximum width for each column
        col_widths = [max(len(str(item)) for item in col) for col in zip(*[headers] + rows)]
        
        # Create a format string for each row
        row_format = "   ".join(f"{{:<{width}}}" for width in col_widths)
        
        # Print the header row
        print(row_format.format(*headers))
        print("-+-".join('-' * width for width in col_widths))
        
        # Print each data row
        for row in rows:
            print(row_format.format(*row))

# Загорнути в функції і підключити до команд боту

#     # Отримання нотатки за id
#     note_id = note1.id
#     print(f"Note with ID '{note_id}':")
#     print(notebook.get_note_by_id(note_id))
