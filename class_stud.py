from tkinter import *
import sqlite3
import random
import time
import class_show
con = sqlite3.connect('Quiz.db')
cur = con.cursor()

class student_window:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1000x800+100+200')
        self.master.title('Records')
        self.conn = sqlite3.connect('Quiz.db')
        self.cur = self.conn.cursor()
        self.textLabel = Label(self.master, text="Sr.", width=10)
        self.textLabel.grid(row=0, column=0)
        self.intLabel = Label(self.master, text="Questions", width=10)
        self.intLabel.grid(row=0, column=1)
        self.optLabel = Label(self.master, text="Option1", width=5)
        self.optLabel.grid(row=0, column=3)
        self.opt2Label = Label(self.master, text="Option2", width=5)
        self.opt2Label.grid(row=0, column=5)
        self.opt3Label = Label(self.master, text="Option3", width=5)
        self.opt3Label.grid(row=0, column=7)
        self.opt4Label = Label(self.master, text="Option4", width=5)
        self.opt4Label.grid(row=0, column=9)
        self.showallrecords()
        self.templabel = Label(self.master, text="                             ",height=1, width=5).grid(row=self.row_check+8,column=4)
        self.button4=Button(self.master,font=('Helvetica', '25','bold'),text="Save",bg='yellow',command=lambda: self.save_ans()).grid(row=self.row_check+10,column=4)
###########Function for closing questions window and showing result window###########
    def save_ans(self):
        #cur.execute("INSERT INTO users WHERE VALUES(1, 'What is input function in Python?', 'Input', 'cin', 'Scanf', 'system.in', 'Input')")
        #conn.commit()
        root=Toplevel(self.master)
        myGUI=class_show.Show(root,sum(self.total))
        self.exit()



    ########Function that updates score on the basis of input answer and stores number of question that is answered inn check array########
    def value(self,data,i):
        if i not in (self.check):
            self.check.append(i)
            self.answered.append(i+1)
        if(data==TRUE):
            self.total[i]=1
        else:
            self.total[i]=0
        print('Total Score is : ',sum(self.total))
        self.answered.sort()
        print('Answered Questions are : ',self.answered)
        self.textLabel = Label(self.master, text="Attempted", width=10,bg='red').grid(row=i+1,column=12)
    

############## Function that sends answer of Numeric Questions to value function#######
    def num_check(self,value,i):
        self.value(value==int(self.answers[i]),i)
        
############### Function that inputs answer for Numeric Question################
    def num_ans(self,i):
        self.answer_input[i]=IntVar()
        self.int_entry=Entry(self.master,textvariable=self.answer_input[i]).grid(row=i+1,column=3)
        self.button=Button(self.master,text="submit",fg='red',command=lambda: self.num_check(self.answer_input[i].get(),i)).grid(row=i+1,column=4)

#################  Function That takes input for MCQs and True False Answers and returns true or false after checking answer#########3
    def adder(self, i):
        Label(self.master, text=i+1).grid(row=i+1, column=0)
        Label(self.master, text=self.questions[i]).grid(row=i+1, column=1)
        if(self.keys[i]==0):
            self.num_ans(i)
    
        else:        
            if(self.opt1[i]):
                self.button1=Button(self.master,text="a",fg='red',command=lambda: self.value(self.opt1[i] == self.answers[i],i)).grid(row=i+1,column=2)
                Label(self.master, text=self.opt1[i]).grid(row=i+1, column=3,padx = 20)
            if(self.opt2[i]):
                self.button2=Button(self.master,text="b",fg='red',command=lambda: self.value(self.opt2[i] == self.answers[i],i)).grid(row=i+1,column=4)
                Label(self.master, text=self.opt2[i]).grid(row=i+1, column=5,padx = 20)
            if(self.opt3[i]):
                self.button3=Button(self.master,text="c",fg='red',command=lambda: self.value(self.opt3[i] == self.answers[i],i)).grid(row=i+1,column=6)
                Label(self.master, text=self.opt3[i]).grid(row=i+1, column=7,padx = 30)
            if(self.opt4[i]):
                self.button4=Button(self.master,text="d",fg='red',command=lambda: self.value(self.opt4[i] == self.answers[i],i)).grid(row=i+1,column=8)
                Label(self.master, text=self.opt4[i]).grid(row=i+1, column=9,padx = 20)
        self.row_check=i+1

    marks=0
    answer_input=[0] * 100 #Array for storing answers of Numeric Questions
    check = []             #Array for storing Answered Questions
    answers = []           #Array to store correct answers of all the questions
    questions = []         #Array to store all the questions
    opt1 = []
    opt2 = []
    opt3 = []
    opt4 = []
    keys = []             #Array to store question types for each question i.e MCQs,T/F,Numeric
    number=0              #Stores Number of Questions
    total = [0] * 100     #stores all the marks scores per question 1/0
    answered = []         #check++ i.e since check stores 1 as 0 as behaviour of array, it stores values of check incremented by 1
            
    def showallrecords(self):
        Data = self.readfromdatabase()
        #########storing all the records from database in arrays
        for index,dat in enumerate(Data):
            self.keys.append(dat[0])
            self.answers.append(dat[6])
            self.questions.append(dat[1])
            self.opt1.append(dat[2])
            self.opt2.append(dat[3])
            self.opt3.append(dat[4])
            self.opt4.append(dat[5])
            self.number=self.number+1
            
        for i in range(self.number):
            self.adder(i)

            
    def readfromdatabase(self):
        self.cur.execute("SELECT * FROM questions")
        return self.cur.fetchall()

    def exit(self):
        self.master.withdraw()
if __name__ == '__main__':
    root=Tk()
    login_window=student_window(root)
    root.mainloop()


