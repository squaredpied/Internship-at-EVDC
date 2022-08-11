import RPi.GPIO as GPIO
import time
from tkinter import *

global startinput, stopinput, run, start_time

def exit1 ():
	GPIO.cleanup()
	root.destroy()
	
def StartAgain():
	global run, jo
	run=0
	jo=1
	Label_time.configure(text='0.000')
	
def microsec(start_time):
	current_time=time.time() - start_time
	current_time=round(current_time, 3)
	return current_time

def CheckGPIO():
	global run, startinput, start_time, stopinput , jo
	if GPIO.input(startinput) == 1 and run==0 and jo == 1:
		run=1
		start_time=time.time()
	if run==1:
		Label_time.configure(text=str(microsec(start_time)))
	if GPIO.input(stopinput) == 1 and run == 1:
		run=0
		jo = 2
	root.after(1, CheckGPIO)
	
def StartTime(pin):
	global run, start_time, jo
	if GPIO.input(startinput)==1:
		if run == 0 and jo==1:
			start_time=time.time()
			run=1

def ShowTimer():
	global run
	if run==1:
		Label_time.configure(text=format(microsec(start_time), '.3f'))
	root.after(1, ShowTimer)
	
def StopTime(pin):
	global run, jo
	if GPIO.input(stopinput)==1:
		if run == 1:
			run=0
			Label_time.configure(text=str(microsec(start_time)))
			jo=2


run=0
start_time=0
jo = 1


root=Tk()
root.title('Timer')
root.width=root.winfo_screenwidth
root.height=root.winfo_screenheight
root.wm_attributes('-fullscreen','true')
Label_time=Label(root, text='0.000', font='Arial 250 bold')
Label_time.place(relx=0.5, rely=0.5, anchor=CENTER)

start_but=Button(root, text='Reset', command=StartAgain)
start_but.pack()

exit_but=Button(root, text='Exit', command=exit1)
exit_but.pack()

GPIO.setmode(GPIO.BCM)
startinput=23
stopinput=24
root.after(1, ShowTimer)
GPIO.setup(startinput, GPIO.IN)
GPIO.setup(stopinput, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(startinput, GPIO.RISING, callback=StartTime)
GPIO.add_event_detect(stopinput, GPIO.RISING, callback=StopTime)
#CheckGPIO()

root.mainloop()
