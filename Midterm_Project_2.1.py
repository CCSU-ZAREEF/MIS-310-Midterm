from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

# Window setup
root = Tk()
root.title('CCSU Mobile App')
root.geometry("600x500")
root.resizable(0, 0)
root.configure(bg='light blue')

# Make white in logo transparent and show it
img = Image.open('logo1.PNG')

try:
    img = img.resize((120, 120), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((120, 120), Image.ANTIALIAS)

img = img.convert("RGBA")
data = img.getdata()

newData = []
for item in data:
    # if pixel is white make it transparent; else keep it
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("transparent.png")

logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = Label(root, image=logo, bg='light blue')
logoLabel.place(x=260, y=10)  # center top

data = pd.read_csv("midterm_exam.csv")

# Label used to display results
lb = Label(root, justify="left", bg="light blue", anchor="w", font=("Arial", 10))
lb.place(x=150, y=180)

# button 1: calendar
def calendar():
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=100, y=200)

# button 2: buildings
def buildings():
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=250, y=200)

# button 3: faculty
def faculty():
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=400, y=200)


# Button
button1 = Button(root, text='Calendar', command=calendar, bg="light green", width=12)
button1.place(x=100, y=140)

button2 = Button(root, text='Buildings', command=buildings, bg="light green", width=12)
button2.place(x=250, y=140)

button3 = Button(root, text='Faculty', command=faculty, bg="light green", width=12)
button3.place(x=400, y=140)

root.mainloop()