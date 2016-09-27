#Ankita Chowdhry, August 2016

import sys 
import time
from Tkinter import *

class Activity(object):
	name=""
	time=0

	def __init__(self, name, time):
		self.name=name
		self.time=time


things_to_do={}
count=0
#to_do = open(sys.argv[1],'w')
to_do=open("to_do.txt",'w')
sched=open('sched.txt','w')
total_time=0
break_time=0
work_time=0
breaks=0

def addActivity():
	global count
	name=raw_input("Thing to do: ")
	time=input("Minutes it will take: ")
	things_to_do[count]=Activity(name,time)
	count+=1

"""def printToDo():
	print("To Do: ")
	for key in things_to_do:
		print(things_to_do[key].name)
		print("Time to do: " + things_to_do[key].time + " minutes")"""

def printToDo():
	to_do.write("To Do: " + '\n')
	global total_time
	global break_time
	for key in things_to_do:
		to_do.write('\n')
		to_do.write(things_to_do[key].name + '\n')
		to_do.write("Time to do: " + str(things_to_do[key].time) + " minutes" + '\n')
	wk = round(work_time/60.0,2)
	to_do.write('\n'+ "Total work time: " + str(wk) + " hours" + '\n')
	to_do.write("Total break time: " + str(break_time) + " minutes" + '\n')

def totalWorkTime():
	global break_time
	work=0
	for key in things_to_do:
		work=work+things_to_do[key].time
	break_time=total_time-work
	return work

print("Welcome to schedule maker!")
print("Please enter your activities according to priority")
print("Let's begin!")
hours=input("How much time do you have to work today? (hours) ")
br=input("If you want to take breaks today, enter 1. If you do not want breaks, enter 0. ")
if br==1:
	breaks=input("How long do you want each break to be? (minutes) ")
else:
	breaks=0
total_time=hours*60


cont = raw_input("Add an activity? (yes/no) ")
while (cont.find("yes")>-1):
	addActivity()
	cont = raw_input("Add an activity? (yes/no) ")

work_time=totalWorkTime()
printToDo()
schedule={}
sched_count=0
tomorrow={}
work_tom=0

"""print(str(total_time))
print(str(break_time))
print(str(work_time))
print(str(breaks))"""

def schedAdd(item):
	global sched_count
	schedule[sched_count]=item
	sched_count+=1

def doTomorrow(num):
	global count
	nums=0

	for x in range(num,count):
		tomorrow[nums]=things_to_do[x]
		nums+=1


def makeSchedule():
	global break_time
	global total_time
	global work_time
	global breaks
	global work_tom
	global br

	for key in things_to_do:
		if (total_time-(things_to_do[key].time))>=0:
			schedAdd(things_to_do[key])
			total_time=total_time-things_to_do[key].time
			work_time=work_time-things_to_do[key].time
			if things_to_do[key].time<30 or break_time<=0 or br==0:
				continue
			else:
				schedAdd(Activity('break',breaks))
				break_time=break_time-breaks
				total_time=total_time-breaks
		else:
			print("Looks like you'll need to work tomorrow as well")
			work_tom=1
			doTomorrow(key)
			break

makeSchedule()

def printSched():
	global total_time
	global break_time
	global work_tom
	sched.write("Your schedule for " + time.strftime("%d/%m/%Y") + " :" + '\n')
	for key in schedule:
		sched.write('\n')
		sched.write(schedule[key].name + '\n')
		sched.write("Time to do: " + str(schedule[key].time) + " minutes" + '\n')

	if work_tom==1:
		sched.write('\n')
		sched.write("Tomorrow you'll have to finish: " + '\n')
		for key in tomorrow:
			sched.write('\n')
			sched.write(tomorrow[key].name + '\n')
			sched.write("Time to do: " + str(tomorrow[key].time) + " minutes" + '\n')

printSched()

master=Tk()

topLabel=Label(master, text="Your schedule for " + time.strftime("%d/%m/%Y") + " :" + '\n',font=('Helvetica', 16, 'bold'))
topLabel.grid(row=0,column=0)
#contentLabel=Label(master,text="To Do").grid(row=1,column=0)
doneLabel=Label(master, text="Done?").grid(row=1,column=2)
#timeLabel=

for key in schedule:
	col="#ffffff"
	if schedule[key].name=="break":
		col="#beeeea"
	Label(master, text=schedule[key].name, borderwidth=1, relief=RIDGE, font=('Helvetica', 14), bg=col).grid(row=key+2,column=0,sticky=NSEW)
	Label(master,text=str(schedule[key].time)+" minutes", borderwidth=1, relief=RIDGE, font=('Helvetica', 12), bg=col).grid(row=key+2,column=1,sticky=NSEW)
	Checkbutton(master, width=2, height=1).grid(row=key+2,column=2) 


master.mainloop()

