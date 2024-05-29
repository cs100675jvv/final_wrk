from _decorator.decorator import input_error_note

@input_error_note
def edit_note(args, notebook="notebook"):
    '''Function to edit an existing note'''
    note_id, *_ = args
    if note_id not in notebook.data:
        print(f"Note with ID {note_id} does not exist. Use list-notes to get all Note's ID")
        return

    note = notebook.data[note_id]
    print(f"Editing note with header '{note.header}'. Current text:\n{note.body}\n")
    print("Enter the new Note text (Type ':end' to finish text editing):")
    
    new_body_lines = note.body.split("\n")

    def input_with_prefill(prompt, prefill):
        import readline
        def hook():
            readline.insert_text(prefill)
            readline.redisplay()
        readline.set_pre_input_hook(hook)
        try:
            return input(prompt)
        finally:
            readline.set_pre_input_hook()

    edited_body_lines = []
    for line in new_body_lines:
        edited_line = input_with_prefill("", line)
        if edited_line.strip() == ":end":
            break
        edited_body_lines.append(edited_line)

    while True:
        new_line = input()
        if new_line.strip() == ":end":
            break
        edited_body_lines.append(new_line)

    note.body = "\n".join(edited_body_lines)
    note.size = len(note.body)
    print(f"Note '{note.header}' updated.")