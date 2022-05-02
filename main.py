# import secrets
# import string
# from tkinter import *
#
# window = Tk()
#
# window.geometry("300x120")
#
# length = StringVar()
#
#
# def submit():
#     dlugosc = int(length.get())
#     lower = string.ascii_lowercase
#     upper = string.ascii_uppercase
#     num = string.digits
#     symbols = string.punctuation
#     all = lower + upper + num + symbols
#     password = ''.join(secrets.choice(all) for i in range(dlugosc))
#     print(password)
#     return dlugosc
#
#
#
# question = Label(window, text="Enter length")
# question.pack()
# e1 = Entry(window, textvariable=length)
# e1.pack()
#
# sub = Button(window, text="Generate password", command=submit)
# sub.pack()
#
# window.mainloop()

from tkinter import *
import secrets
import string

window = Tk()
window.title("Generate password")

canvas = Canvas(window, width=400, height=300, relief='raised')
canvas.pack()

title = Label(window, text='Generate a random password')
title.config(font=('helvetica', 14))
canvas.create_window(200, 25, window=title)

text = Label(window, text='Enter the length of password:')
text.config(font=('helvetica', 10))
canvas.create_window(200, 100, window=text)

entry1 = Entry(window)
canvas.create_window(200, 140, window=entry1)


def get_length():
    a1 = entry1.get()

    textresult = Label(window, text='Generated password: ', font=('helvetica', 10))
    canvas.create_window(200, 210, window=textresult)

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    result = Label(window, text=''.join(secrets.choice(all) for i in range(int(a1))), font=('helvetica', 10, 'bold'))
    canvas.create_window(200, 230, window=result)


button = Button(text='Generate', command=get_length, bg='blue', fg='white',
                font=('helvetica', 9, 'bold'))
canvas.create_window(200, 180, window=button)

window.mainloop()