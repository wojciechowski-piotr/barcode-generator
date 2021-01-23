import os
import tkinter as tk
from tkinter import StringVar, Label, ttk, Frame, Canvas

from main import generate_barcodes, word_document, delete_images
from spreadsheet import get_dates, get_eans

HEIGHT = 350
WIDTH = 200

root = tk.Tk()
root.title('Barcode generator')

documents_path = 'E:\\pythons\\barcodes\\documents'

dates = get_dates()


def run_app():
    warn_label = Label(frame, text='Select a date from the list', bg='#81D4FA')

    if clicked.get() == 'Select date':
        warn_label.place(relx=0.5, rely=0.2, relwidth=1, relheight=0.3, anchor='n')
        pass
    else:
        generate_barcodes(get_eans(clicked.get()))
        word_document(clicked.get())
        os.startfile(documents_path)
        delete_images()
        root.destroy()


canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg='#81D4FA')
canvas.pack()

frame = Frame(root, bg='#81D4FA')
frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.9, anchor='n')

clicked = StringVar()
clicked.set('Select date')

dropdown = ttk.OptionMenu(frame, clicked, *['Select date', *dates])
dropdown.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')

button = ttk.Button(frame, text='Generate barcodes', command=lambda: run_app())
button.place(relx=0.5, rely=0.9, relwidth=1, relheight=0.1, anchor='n')

root.mainloop()
