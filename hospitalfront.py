# -*- coding: utf-8 -*-

#Import all Tkinter module
"""
Created on Thu Aug 23 14:21:31 2018

@author: Aryman
"""
from tkinter import *
import sqlite3
import tkinter .messagebox

#connect with DB
conn = sqlite3.connect('appointment.kexi')

#cursor to move around the DB
c = conn.cursor()

#empty list which append later
ids = [0]

#tkinter window
class Application:
    def __init__(self, master):
        self.master = master
        
        #creatin the frames
        self.left = Frame(master, width=850, height=720,bg='cadetblue2')
        self.left.pack(side=LEFT)
        
        self.right = Frame(master, width=850, height=720, bg='aqua')
        self.right.pack(side=RIGHT)
        
        #labels for the window
        self.heading = Label(self.left, text="HOSPITAL MANAGEMENT SYSTEM", font=("Helvetica 37 bold"),fg='red', bg='cadetblue2') 
        self.heading.place(x=0, y=10)
        
        #Donor Name
        self.name = Label(self.left, text="Patient's Name", font=('arial 15 bold'), fg='black', bg='cadetblue2')
        self.name.place(x=90, y=100)
        
        #Donor Age
        self.age = Label(self.left, text="Age", font=('arial 15 bold'), fg='black', bg='cadetblue2')
        self.age.place(x=90, y=140)
        
        #Donor Gender
        self.gender = Label(self.left, text="Gender", font=('arial 15 bold'), fg='black', bg='cadetblue2')
        self.gender.place(x=90, y=180)
        
        #Donor NLocation
        self.location = Label(self.left, text="Location", font=('arial 15 bold'), fg='black', bg='cadetblue2')
        self.location.place(x=90, y=220)
        
        #Donor time
        self.time = Label(self.left, text="Time", font=('arial 15 bold'), fg='black', bg='cadetblue2')
        self.time.place(x=90, y=260)
        
        #Phone Number
        self.phone = Label(self.left, text="Phone Number", font=('arial 15 bold'), fg='black', bg='cadetblue2')
        self.phone.place(x=90, y=300)
        
        #Entries for all the fields
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=350, y=100)
        
        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=350, y=140)
        
        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=350, y=180)
        
        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=350, y=220)
        
        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=350, y=260)
        
        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=350, y=300)
        
        #Button for Donation
        self.submit = Button(self.left, text="Fix Appointment", width=20, height=2, bg='steelblue', command=self.add_donation)
        self.submit.place(x=260, y=380)
        
       #code is not work #getting total Number of Donar
        sql2 = "SELECT ID FROM donar"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
            
        #ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
            
        #Display the logs
        self.box = Text(self.right, width=60, height=40)
        self.box.place(x=50, y=30)
        self.box.insert(END, "\n\n\n\n\n\t\tTotal Appointment till now : " + str(self.final_id))
        
    #function to call Donation button
    def add_donation(self):
        #getting input from the user
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()
        
        #checking if data is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '' :
            tkinter.messagebox.showinfo("Warning", "Please Fill up all boxes")
        else:
            #add in database
            sql = "INSERT INTO 'donar' (name, age, gender, location, time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()          
            tkinter.messagebox.showinfo("Nice Job", "Good to go " +str(self.val1) + " See you soon.")
            
            self.box.insert(END, '\n\n\n\n\tWe will connect as soon as possible ' +str(self.val1))
            
#creating the object
root = Tk()
#title of App
root.title("Hospital Management System")
b = Application(root)

#resolution of the window
root.geometry('1200x720+0+0')

#preventing he resize feature
root.resizable(True, True)

#end the loop
root.mainloop()