# ScheduleMaker
Python code for creating a GUI with a daily schedule. Program was written to make it easier to plan daily activities and have a to-do list to check off.

GUI using Tkinter package.
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

master=Tk()

topLabel=Label(master, text="Your schedule for " + time.strftime("%d/%m/%Y") + " :" + '\n',font=('Helvetica', 16, 'bold'))
topLabel.grid(row=0,column=0)
doneLabel=Label(master, text="Done?").grid(row=1,column=2)

master.mainloop()

Run python script to use program.
