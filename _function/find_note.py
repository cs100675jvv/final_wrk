from _classes.notes import NoteBook, Note

def find_note(args, notebook: NoteBook) -> str:
    substring = ' '.join(args)
    for note in notebook.values():
        if substring in note.body:
            return str(note)
    return None