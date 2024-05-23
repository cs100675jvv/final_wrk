import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk

# GUI initialization. Responsible: Viacheslav
def init_gui():
    window = tk.Tk()
    window.title("Assistant Bot by КотоПес team")

    # window size
    window_width = 1000
    window_height = 800
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # сenter of screen
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # dark mode
    window.configure(bg='#212121')

    # Define the font
    custom_font = tkfont.Font(family="Consolas", size=12)

    # Canvas
    canvas = tk.Canvas(window, bg='#212121', bd=0, highlightthickness=0)
    canvas.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.08)

    # Entry for user input
    user_input = tk.Entry(canvas, bg='#2f2f2f', fg='white', font=custom_font, insertbackground='white', bd=0)
    user_input.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.6)


    # Set focus on user_input
    user_input.focus_set()

    # Listbox for displaying messages
    messages = tk.Text(window, bg='#212121', fg='white', font=custom_font, wrap=tk.WORD, borderwidth=0)
    messages.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.8)

    return window, canvas, user_input, messages