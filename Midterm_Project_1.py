from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

# Window setup
root = Tk()
root.title('CCSU App')
root.geometry("500x500")
root.resizable(0, 0)
root.configure(bg='light blue')

# Calculate the amount of points
def calculate_points():
    books = entry_books.get()

    if books.isdigit():
        books = int(books)
        if books == 0:
            points = 0
        elif books == 2:
            points = 5
        elif books == 4:
            points = 15
        elif books == 6:
            points = 30
        elif books >= 8:
            points = 60
        else:
            points = 0
        result_label.config(text="Points Awarded: " + str(points))
    else:
        result_label.config(text="Please enter a valid number.")

# Widgets
instruction_label = Label(root, text="Enter number of books purchased this month:", bg='light blue')
instruction_label.place(x=100, y=150)

entry_books = Entry(root, width=10)
entry_books.place(x=200, y=180)

calc_button = Button(root, text="Compute Points", command=calculate_points, bg="light green")
calc_button.place(x=180, y=210)

result_label = Label(root, text="", bg='light blue', fg="black")
result_label.place(x=170, y=250)

root.mainloop()