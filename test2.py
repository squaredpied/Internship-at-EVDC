import tkinter as tk
#from tkinter import *
#from tkinter import ttk

import time
import RPi.GPIO as GPIO
import os, sys

global scr_height, scr_width

class StopWatch(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Timer')
		self.width=self.winfo_screenwidth
		self.height=self.winfo_screenheight
		self.run=0
		self.start=0
		self.val=0
		self.again=0
		self.wm_attributes('-fullscreen','true')
		self.start_button=tk.Button(self,text='Start', command=self.Startbut)
		self.exit_button=tk.Button(self, text='Exit', command=self.Exit)
		self.timer_label=tk.Label(self, text='0.000', font='Arial 250 bold')
		self.start_button.pack()
		self.exit_button.pack()
		self.timer_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
		GPIO.setmode(GPIO.BCM)
		self.startinput=23
		self.stopinput=24
		self.notagain=0
		GPIO.setup(self.startinput, GPIO.IN)
		GPIO.setup(self.stopinput, GPIO.IN)

		self.CheckGPIO()
		
	def CheckGPIO(self):
		if GPIO.input(self.startinput) == 1 and self.notagain==0:
			self.Start()
			
		if GPIO.input(self.stopinput) == 1 and self.run==1:
			self.Stop()
		#elif GPIO.input(self.stopinput)  == 1:
		#	self.Stop()
		self.after(1, self.CheckGPIO)
	
	
	def Start(self):
			self.start = time.time()
			self.run=1
			self.notagain=1
			self.Update()

		
	def Update(self):
		if self.run==1:
			#print('run')
			#self.val=self.val+1
			self.timer=time.time()-self.start
			self.timer=str(round(self.timer,3))
			self.message=self.timer
			#self.message=str(self.val)
			self.timer_label.config(text=self.message)
			print(self.message)
			self.after(1,self.Update)
		
	def Stop(self):
		self.run=0


	
	def Startbut(self):
		self.notagain=0
		self.timer_label.config(text='0.000')
	
	def Exit(self):
		self.destroy()

watch=StopWatch()
watch.mainloop()
