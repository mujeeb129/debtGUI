from tkinter import *
from tkinter import ttk



window = Tk()
window.title('Debt app')
window.geometry('500x500+100+100')

mainFrame = Frame(window)
mainFrame.grid()

name = StringVar()

nameLabel = Label(mainFrame , text = 'Name')
nameLabel.grid(row = 0 , column = 0)

nameEntry = Entry(mainFrame , textvariable = name)
nameEntry.grid(row = 0 , column = 1)

amount = StringVar()

amountLabel = Label(mainFrame , text = 'Amount')
amountLabel.grid(row = 1 , column = 0)

amountEntry = Entry(mainFrame , textvariable = amount)
amountEntry.grid(row = 1 , column = 1)

listBox = Listbox(mainFrame , width = 50)
listBox.grid(row = 2 , column =  0 , columnspan = 8 , rowspan = 6)








window.mainloop()