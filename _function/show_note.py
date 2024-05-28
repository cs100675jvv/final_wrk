from _classes.notes import NoteBook
from _decorator.decorator import input_error_note
from _function.format_table import format_table




@input_error_note
def show_note(args, notebook: NoteBook):
    """
    Display the details of a specific note.

    Args:
        args (list): The first element is the note ID.
        notebook (NoteBook): The notebook object containing the notes.

    Returns:
        str: The formatted table
    """
    note_id, *_ = args
    if note_id not in notebook:
        return print(f"Note with ID {note_id} does not exist. Use list-notes to get all Note's ID")
    note = notebook.get_note_by_id(note_id)
    headers = ["ID", "Header", "Body", "Creation Date"]
    note_id = str(note.id)
    note_header = note.header 
    note_body = note.body 
    note_creation = note.creation_date.strftime('%Y-%m-%d %H:%M:%S')
    data = [[note_id, note_header, note_body, note_creation]]
    
    col_widths = [15, 15, 60, 15]
    return format_table(headers, data, col_widths)




