#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 13:57:31 2018

@author: aryman
"""
from tkinter import *
import sqlite3
import pyttsx3

#connect with DB
conn = sqlite3.connect('appointment.kexi')
c = conn.cursor()

#empty list
number = []
patients = []

sql = "SELECT * FROM donar"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)
    

#window
class Application:
    def __init__(self, master):
        self.master = master
        
        self.x = 0
        
        self.heading = Label(master, text="Appointment", font=('arial 40 bold'))
        self.heading.place(x=250, y=2)
        
        #button to chnage patients
        self.change = Button(master, text="Next Patient", width=25, bg='steelblue', command=self.func)
        self.change.place(x=600, y=600)
        
        #empty 
        self.n = Label(master, text="", font=('arial 150 bold'))
        self.n.place(x=500, y=200)
        
        #patient
        self.pname = Label(master, text="", font=('arial 150 bold'))
        self.pname.place(x=200, y=480)
        
    #fuction to speak
    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        engine = pyttsx3.init()
        voices = engine.getProperty('voice')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate=50)
        engine.say('Patient Number ' + str(number[self.x]) + str(patients[self.x]))
        engine.runAndWait()
        self.x += 1
#creating the object
root = Tk()

#title of App
root.title("Appointment")
b = Application(root)

#resolution of the window
root.geometry('1200x720+0+0')

#preventing he resize feature
root.resizable(True, True)

#end the loop
root.mainloop()
    