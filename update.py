#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:21:31 2018

@author: Aryman
"""

from tkinter import *
import tkinter .messagebox
import sqlite3
#connect with DB
conn = sqlite3.connect('appointment.kexi')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
         
        #Heading label
        self.heading = Label(master, text="Update Patient Information", fg='steelblue', font=('Times 40 bold'))
        self.heading.place(x=270, y=10)
        
        #Search Criteria NAME
        self.name = Label(master, text="Enter Donar's Name", font=('arial 20 bold'))
        self.name.place(x=300, y=100)
        
        #Entry for the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=600, y=110)
        
        #Search Button
        self.search = Button(master, text="SEARCH", width=17, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=620, y=160)
        
    #funtion to search tin db
    def search_db(self):
        self.input = self.namenet.get()
        
        #Execute the db
        sql = "SELECT * FROM donar WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[5]
            self.phno = self.row[6]
            
        #Creating the update form
        self.uname = Label(self.master, text="Patient's Name", font=('arial 18 bold'))
        self.uname.place(x=170, y=240)
        
        self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
        self.uage.place(x=170, y=280)
        
        self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
        self.ugender.place(x=170, y=320)
        
        self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
        self.ulocation.place(x=170, y=360)
        
        self.utime = Label(self.master, text="Time", font=('arial 18 bold'))
        self.utime.place(x=170, y=400)
        
        self.uphno = Label(self.master, text="Phone Number", font=('arial 18 bold'))
        self.uphno.place(x=170, y=440)
        
        #Entries of there relivant are show in the box
        #Entry for all label
        self.lab1 = Entry(self.master, width=30)
        self.lab1.place(x=420, y=240)
        self.lab1.insert(END, str(self.name1))
        
        self.lab2 = Entry(self.master, width=30)
        self.lab2.place(x=420, y=280)
        self.lab2.insert(END, str(self.age))
        
        self.lab3 = Entry(self.master, width=30)
        self.lab3.place(x=420, y=320)
        self.lab3.insert(END, str(self.gender))
        
        self.lab4 = Entry(self.master, width=30)
        self.lab4.place(x=420, y=360)
        self.lab4.insert(END, str(self.location))
        
        self.lab5 = Entry(self.master, width=30)
        self.lab5.place(x=420, y=400)
        self.lab5.insert(END, str(self.time))
        
        self.lab6 = Entry(self.master, width=30)
        self.lab6.place(x=420, y=440)
        self.lab6.insert(END, str(self.phno))
        
        #Button for Update
        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=420, y=490)
        
        #Button for Deletion
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=200, y=490)
        
    def update_db(self):
        #defing updated variables
        self.var1 = self.lab1.get()
        self.var2 = self.lab2.get()
        self.var3 = self.lab3.get()
        self.var4 = self.lab4.get()
        self.var5 = self.lab5.get()
        self.var6 = self.lab6.get()
        
        query = "UPDATE donar SET name=?, age=?, gender=?, location=?, time=?, phone=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get()))
        conn.commit()
        tkinter.messagebox.showinfo("SUCCESS", "Data of " +str(self.var1) + " updated.")
        
    def delete_db(self):
        #delete in db
        sql2 = "DELETE FROM donar WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Data Deleted.")
        #destory all the data
        self.lab1.destroy()
        self.lab2.destroy()
        self.lab3.destroy()
        self.lab4.destroy()
        self.lab5.destroy()
        self.lab6.destroy()
        
                       

#creating the object
root = Tk()

#title of App
root.title("Update In Donar Information")
b = Application(root)

#resolution of the window
root.geometry('1200x720+0+0')

#preventing he resize feature
root.resizable(True, True)

#end the loop
root.mainloop()