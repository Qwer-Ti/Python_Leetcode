from tkinter import *

def submit():
    username = entry.get()
    print("hello " + username)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk() #create a windows


entry = Entry(window,
              font = ("Arial", 50))
entry.pack(side=LEFT)
entry.insert(0, 'SPONGEBOB')

submit_btn = Button(window,text = 'Submit', command = submit)

submit_btn.pack(side=RIGHT)

delete_btn = Button(window,text = 'Delete', command = delete)

delete_btn.pack(side=RIGHT)

backspace_btn = Button(window,text = '<-', command = backspace)

backspace_btn.pack(side=RIGHT)



window.mainloop() #places window on computer screen, listens for events