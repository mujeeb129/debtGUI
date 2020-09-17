from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database as db
import time

data = db.SetUp('debtbook.db')

additions = ""
additionList = []
cigarDict = {'King - 17': 17 ,
			 'Gold - 10': 10 ,
			 'Mini Gold - 6' : 6 ,
			 'Essay - 10' : 10 ,
			 'Essay Pack - 110' : 110 ,
			 'Scissors - 8' : 8 , 
			 'Wills - 11' : 11 ,
			 'M Wills - 8' : 8 ,
			 'Mini Wills - 5' : 5 }

def populate():
	global additions , cigarDict , additionList
	cigarname = cigarName.get()
	amountS = amount.get()
	rate = cigarDict[cigarname]
	if cigarname != '':
		if additions == '' :
			additions = additions + str(rate * int(amountS))
		else :
			additions = additions + ' + ' + str(rate * int(amountS))
		calculate.set(additions)
		additionList.append(rate * int(amountS))
		print(additionList)
	else :
		messagebox.showerror('Please fill' , 'Please fill all the fields')


def populateList():
	listBox.delete(0 , END)
	for row in data.fetch():
		listBox.insert(END , row)

def selectedItem(event):
	if listBox.curselection() != 0:
		global selecteditem
		item = listBox.curselection()[0]
		selecteditem = listBox.get(item)
		nameEntry.delete(0,END)
		name.set(selecteditem[1])


def save():
	global additionList
	total = sum(additionList)
	nameS = name.get()
	amountS = amount.get()
	instanceS = time.ctime()
	if nameS != '' or amountS != '' :
		data.insert(nameS , total , instanceS)

	else :
		messagebox.showerror('Please fill' , 'Please fill all the fields')
	populateList()


def delete():
	global selecteditem
	identity = selecteditem[0]
	data.delete(identity)
	populateList()
 
def remove():
	global additionList , additions
	if additionList != [] or additions != '':
		


window = Tk()
window.title('Debt app')
window.geometry('500x300+100+100')
window.configure(bg = '#FFFFFF')

mainFrame = Frame(window , bg = '#FFFFFF')
mainFrame.grid()
#Name variable to store name from the entry label
name = StringVar()
#Name entry and label
nameLabel = Label(mainFrame , text = 'Name' , bg = '#FFFFFF')
nameLabel.grid(row = 0 , column = 0)

nameEntry = Entry(mainFrame , textvariable = name)
nameEntry.grid(row = 0 , column = 1)
#Amount variable to input the number of cigars
amount = StringVar()
#Amount entry and cigar type combobox
amountLabel = Label(mainFrame , text = 'Amount' , bg = '#FFFFFF')
amountLabel.grid(row = 1 , column = 0)

amountEntry = Entry(mainFrame , textvariable = amount)
amountEntry.grid(row = 1 , column = 1)

cigarName = StringVar()
cigarCombobox = ttk.Combobox(mainFrame , state = 'readonly' , textvariable = cigarName)
cigarCombobox.grid(row = 1 , column = 2)

cigarCombobox['values'] = ('King - 17' ,
						   'Gold - 10' ,
						   'Mini Gold - 6' ,
						   'Essay - 10' ,
						   'Essay Pack - 110' ,
						   'Scissors - 8' , 
						   'Wills - 11' ,
						   'M Wills - 8' ,
						   'Mini Wills - 5')


#Add button to the cigar
addButton = Button(mainFrame , text = 'Add' , command = populate , bg = '#FFFFFF' , bd = 0)
addButton.grid(row = 1 , column = 9 , sticky = 'E')
#Calculation variable 
calculate = StringVar()
#Calculation display and save button
calculationEntry = Entry(mainFrame , textvariable = calculate)
calculationEntry.grid(row = 2 , column = 0 , columnspan = 8 , )


saveButton = Button(mainFrame , text = 'Save' , command = save , bg = '#FFFFFF' , bd = 0)
saveButton.grid(row = 2 , column = 9 , sticky = 'E')

listBox = Listbox(mainFrame , width = 50)
listBox.grid(row = 3 , column =  0 , columnspan = 8 , rowspan = 6)
listBox.bind('<<ListboxSelect>>' , selectedItem)

scrollbar = Scrollbar(mainFrame)
listBox.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = listBox.yview)

deleteButton = Button(mainFrame , text = 'Delete' , bd = 0 , bg = '#FFFFFF' , command = delete)
deleteButton.grid(row = 3 , column = 9)

updateButton = Button(mainFrame , text = 'Update' , bd = 0 , bg = '#FFFFFF')
updateButton.grid(row = 4 , column = 9)







populateList()
window.mainloop()