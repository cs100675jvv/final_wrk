from _classes.notes import NoteBook
from _decorator.decorator import input_error_note

@input_error_note
def show_note(args, notebook: NoteBook):
    note_id, *_ = args
    if note_id in notebook:
        note = notebook.get_note_by_id(note_id)
        return print(note)
    else:
        return print(f"Note with ID {note_id} does not exist. Use list-notes to get all Note's ID")

