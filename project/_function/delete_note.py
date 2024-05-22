from _decorator.decorator import input_error_note
from _classes.notes import NoteBook


@input_error_note
def delete_note(args, notebook: NoteBook):
    note_id, *_ = args
    if note_id in notebook:
        notebook.remove_note_by_id(note_id)
        return print(f"Note {note_id} deleted.")
    else:
        return print(f"Note with id {note_id} does not exist")
