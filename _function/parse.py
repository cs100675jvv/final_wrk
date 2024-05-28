def parse_input(user_input):
    """
    Parses the user input and returns the command and arguments.

    Args:
        user_input (str): The user input to be parsed.

    Returns:
        tuple: A tuple containing the command and arguments
    """
    if not user_input.strip():
        print("Please, give me a command.")
        return None, []

    try: 
        parts = user_input.split()
        cmd = parts[0].strip().lower()
        if cmd == "add_address":
            cmd, *args = user_input.split(maxsplit=1)
            args = args[0].split(maxsplit=1) if args else []
        else:
            cmd, *args = parts
        return cmd, *args
    except Exception:
        print("Please, give me a command.")
        return None, []


