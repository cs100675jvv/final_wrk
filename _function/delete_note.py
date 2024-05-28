from _decorator.decorator import input_error_note
from _classes.notes import NoteBook

@input_error_note
def delete_note(args, notebook: NoteBook):
    """
    Deletes a note from the notebook based on the provided note ID.

    Args:
        args (list): A list containing the note ID.
        notebook (NoteBook): The notebook object.
    """
    note_id, *_ = args
    if note_id in notebook:
        notebook.remove_note_by_id(note_id)
        return print(f"Note {note_id} deleted.")
    else:
        return print(f"Note with ID {note_id} does not exist. Use list-notes to get all Note's ID")
