from _classes.notes import NoteBook, Note

def find_note(args, notebook: NoteBook) -> Note:
    substring = ' '.join(args)
    for note in notebook.values():
        if substring in note.body:
            return print(note)
    return None