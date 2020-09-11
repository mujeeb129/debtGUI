from tkinter import *
from tkinter import ttk



window = Tk()
window.title('Debt app')
window.geometry('500x500+100+100')

mainFrame = Frame(window)
mainFrame.grid()
#Name variable to store name from the entry label
name = StringVar()
#Name entry and label
nameLabel = Label(mainFrame , text = 'Name')
nameLabel.grid(row = 0 , column = 0)

nameEntry = Entry(mainFrame , textvariable = name)
nameEntry.grid(row = 0 , column = 1)
#Amount variable to input the number of cigars
amount = StringVar()
#Amount entry and cigar type combobox
amountLabel = Label(mainFrame , text = 'Amount')
amountLabel.grid(row = 1 , column = 0)

amountEntry = Entry(mainFrame , textvariable = amount)
amountEntry.grid(row = 1 , column = 1)

cigarCombobox = ttk.Combobox(mainFrame)
cigarCombobox.grid(row = 1 , column = 2)
#Add button to the cigar
addButton = Button(mainFrame , text = 'Add')
addButton.grid(row = 1 , column = 9)
#Calculation variable 
calculate = StringVar()
#Calculation display and save button
calculationListbox = Listbox(mainFrame , height = 1 , width  = 50 ,)
calculationListbox.grid(row = 2 , column = 0 , columnspan = 8 , )

saveButton = Button(mainFrame , text = 'Save')
saveButton.grid(row = 2 , column = 9)

listBox = Listbox(mainFrame , width = 50)
listBox.grid(row = 3 , column =  0 , columnspan = 8 , rowspan = 6)









window.mainloop()