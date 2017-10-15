from tkinter import *
import sqlite3
import random
import time
import class_fac
import class_stud
con = sqlite3.connect('Quiz.db')
cur = con.cursor()
class Log_In():
    names = []
    passwords =[]
    roles = []
    key = []
    def __init__(self,master):
        print("  ")
        self.master = master
        self.master.geometry('400x200')
        self.master.title('Data Entry')

        self.label2=Label(self.master,text='Welcome to the data entry menu',fg='red').grid(row=0,column=0)
        self.label3=Label(self.master,text='Please enter your Name',fg='black').grid(row=3,column=0)
        self.label4=Label(self.master,text='Please enter your Password',fg='black').grid(row=4,column=0)
        self.fetch_data()
        print(self.names,self.passwords,self.roles,self.key)
        self.name=StringVar()
        self.text_entry=Entry(self.master,textvariable=self.name).grid(row=3,column=1)
        self.password=StringVar()
        self.text_entry=Entry(self.master,textvariable=self.password).grid(row=4,column=1)
        self.button4=Button(self.master,text="Log In",fg='red',command=lambda: self.savedata(self.name.get(), self.password.get())).grid(row=7,column=1)
    ############ compares names and passwords in database and asks again if not available otherwise sends the user to respective window on the basis of role#####3
    def savedata(self, name, password):
        for i in (self.key):
            if (name==self.names[i] and password == self.passwords[i]):
                self.role = self.roles[i]
                if(self.role=='faculty'):
                    self.goto_fac()
                    return 0
                elif (self.role=='student'):
                    self.goto_stud()
                    return 0
        self.label2=Label(self.master,text='Username or Password is Wrong Enter Again',fg='red').grid(row=8,column=0)

    def goto_fac(self):
        root=Toplevel(self.master)
        myGUI=class_fac.faculty_window(root)
        self.exit()

    def goto_stud(self):
        root=Toplevel(self.master)
        mygui=class_stud.student_window(root)
        self.exit()

    def fetch_data(self):
        cur.execute("SELECT * FROM users")
        Data = cur.fetchall()
        for index,dat in enumerate(Data):
            self.names.append(dat[0])
            self.passwords.append(dat[1])
            self.roles.append(dat[2])
            self.key.append(dat[4])

    def exit(self):
        self.master.withdraw()
if __name__ == '__main__':
    root=Tk()
    login_window=Log_In(root)
    root.mainloop()

