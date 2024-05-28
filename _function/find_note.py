from _classes.notes import NoteBook, Note
from _function.format_table import format_table

def find_note(args, notebook: NoteBook) -> Note:
    """
    Find a note in the given notebook that contains the given substring.

    Args:
        args (list): List of strings representing the substring to search for.
        notebook (NoteBook): The notebook object to search in.

    Returns:
        Note or str: If a note is found, returns the formatted table of matching notes.
                    If no notes are found, returns a string indicating no notes were found.
    """
    substring = ' '.join(args)
    headers = ["ID", "Header", "Body", "Creation Date"]
    rows = []
    
    for note in notebook.values():
        if substring in note.body:
            note_id = str(note.id)
            note_header = note.header 
            note_body = note.body 
            note_creation = note.creation_date.strftime('%Y-%m-%d %H:%M:%S')
            row = [note_id, note_header, note_body, note_creation]
            rows.append(row)
    if rows:
        col_widths = [15, 15, 60, 15]
        return format_table(headers, rows, col_widths)
    else:
        return "No notes found containing the given substring."

