#Import libraries
from tkinter import *
from PyDictionary import PyDictionary

#CREATE OBJECTS
dictionary = PyDictionary() #dictionary object
root = Tk()#window object

# set window title title to empty string(otherwise it shows "tk")
root.title("")

#set window size
root.geometry("600x400")


#function getting words from dictionary 
def dict():
     meaning.config(text=dictionary.meaning(word.get()))
#     synonym.config(text=dictionary.synonym(word.get()))
#     antonym.config(text=dictionary.antonym(word.get()))



#ADD LABELS, BUTTONS, FRAMES(learn about frames https://www.pythontutorial.net/tkinter/tkinter-frame/)
Label(root, text="Dictionary", font=("Arial 21 bold"),fg="Blue").pack(pady=10) #set title 

#Frame1

frame1 = Frame(root)

Label(frame1, text="Type Word", font=("Arial 15 bold")).pack(side=LEFT)
#frame1.columnconfigure(0, weight=1)
#frame1.columnconfigure(0, weight=3)

word = Entry(frame1, font=("Arial 15 bold"))

word.pack()

frame1.pack(pady=10)


#Frame2

frame2 = Frame(root)

Label(frame2, text="meaning: ", font=("Arial 10 bold")).pack(side=LEFT)

meaning = Label(frame2, text="", font=("Arial 10 bold"))

meaning.pack(padx=20)

frame2.pack(pady=10)


#Button
Button(root, text="Submit", font=("Arial 10 bold"), command=dict).pack()

frame2.pack(pady=10)





#execute tkinter
root.mainloop()

