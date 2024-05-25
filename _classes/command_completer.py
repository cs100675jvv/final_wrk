from prompt_toolkit.completion import Completer

class CommandCompleter(Completer):
    def __init__(self, completer):
        self.completer = completer

    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor
        if ' ' in text_before_cursor:
            return
        
        yield from self.completer.get_completions(document, complete_event)