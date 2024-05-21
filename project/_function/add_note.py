from _classes.notes import Note

def add_note(args, notebook="notebook"):
    '''Function to add a new note'''
    if not args:
        print("Error: Note header cannot be empty.")
        return

    header = " ".join(args)
    note = Note(header)
    print(f"Adding note with header '{header}'. Enter the Note text (Type ':end' to finish text editing):")
    
    body_lines = []
    while True:
        line = input()
        if line.strip() == ":end":
            break
        body_lines.append(line)

    note.body = "\n".join(body_lines)
    note.size = len(note.body)
    notebook.add_note(note)
    print(f"Note '{note.header}' added.")
