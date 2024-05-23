import tkinter as tk
from tkinter import simpledialog, font as tkfont

from _classes.notes import Note

# TODO: reuse for note editing
class MultiLineInputBox(simpledialog.Dialog):
    # custom class constuctor to pass label
    def __init__(self, parent, label):
        self.label = label
        super().__init__(parent)

    def body(self, master):
        # configure label
        tk.Label(master, text=self.label).grid(row=0)

        # configure textarea
        self.text = tk.Text(master)
        self.text.grid(row=1)
        return self.text

    def buttonbox(self): # configure buttons
        box = tk.Frame(self)

        w = tk.Button(box, text="OK", width=10, command=self.ok, default="active")
        w.pack(side="left", padx=5, pady=5)

        w = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side="left", padx=5, pady=5)
        
        box.pack()

    def apply(self): # getting output text
        self.result = self.text.get(1.0, "end-1c")

def add_note(notebook="notebook"):
    """Function to add a new note"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    header = simpledialog.askstring("Input", "Enter the note header:", parent=root)
    if not header:
        return "Error: Note header cannot be empty."

    body = MultiLineInputBox(root, "Enter the note body:").result
    if not body:
        return "Error: Note body cannot be empty."

    note = Note(header)
    note.body = body
    note.size = len(note.body)
    notebook.add_note(note)

    return f"Note '{note.header}' added."