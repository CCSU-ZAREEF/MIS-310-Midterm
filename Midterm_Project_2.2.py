from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

# Window setup
root = Tk()
root.title('CCSU Mobile App')
root.geometry("650x550")
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
logoLabel.place(x=265, y=10)  # top center

data = pd.read_csv("midterm_exam.csv")

# Label used to display results
lb = Label(root, justify="left", bg="white", anchor="w", font=("Arial", 10),
           relief="solid", width=60, height=25)
lb.place(x=130, y=250)

# button 1: calendar
def calendar():
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=250)

# button 2: buildings
def buildings():
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=250)

# button 3: faculty
def faculty():
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=250)

# button 4: business
def business():
    programs = [
        "Accounting",
        "Finance",
        "Management & Organization",
        "Marketing",
        "Management Information Systems (MIS)",
        "Business Analytics"
    ]
    text = "School of Business Programs:\n\n" + "\n".join(programs)
    lb.config(text=text)
    lb.place(x=130, y=250)

# button 5: mis department
def mis_department():
    courses = [
        "Intro to MIS",
        "Databases Management",
        "Systems Analysis & Design",
        "Business Analytics / Data Visualization",
        "Network and Information Security",
        "Project Management"
    ]
    text = "MIS Department Courses:\n\n" + "\n".join(courses)
    lb.config(text=text)
    lb.place(x=130, y=250)


# Button
button1 = Button(root, text='Calendar', command=calendar, bg="#8FBC8F", width=12)
button1.place(x=50, y=150)

button2 = Button(root, text='Buildings', command=buildings, bg="#8FBC8F", width=12)
button2.place(x=250, y=150)

button3 = Button(root, text='Faculty', command=faculty, bg="#8FBC8F", width=12)
button3.place(x=450, y=150)

button4 = Button(root, text='School of Business', command=business, bg="#8FBC8F", width=18)
button4.place(x=100, y=200)

button5 = Button(root, text='MIS Department', command=mis_department, bg="#8FBC8F", width=18)
button5.place(x=350, y=200)

root.mainloop()