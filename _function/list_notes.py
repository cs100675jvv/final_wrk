def list_notes(notebook):
    return '\n'.join(str(note) for note in notebook.values())