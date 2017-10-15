from tkinter import *
import sqlite3
import random
import time
import class_fac
import class_stud
con = sqlite3.connect('Quiz.db')
cur = con.cursor()
class Show():
    names = []
    passwords =[]
    roles = []
    key = []
    def __init__(self,master,score):
        self.master = master
        self.master.geometry('400x100')
        self.master.title('Data Entry')
        self.label2=Label(self.master,text='Here Are Your Results',fg='#123456',font=("Georgia", 10)).grid(row=3,column=2)
        self.label3=Label(self.master,text='You Scored : ',fg='red',font=("Georgia", 16)).grid(row=5,column=3)
        self.label3=Label(self.master,text=score,fg='green',font=("Helvetica", 16)).grid(row=5,column=4)
