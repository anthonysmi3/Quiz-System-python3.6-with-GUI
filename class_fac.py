import sqlite3
from tkinter import *

con = sqlite3.connect('Quiz.db')
cur = con.cursor()
class faculty_window():
    def __init__(self,master):
        self.master = master
        self.master.geometry('600x400')
        self.frame=Frame(self.master)
        self.master.title('Data Entry')
        self.init=Label(self.master,text='choose Question type.',fg='red').grid(row=0,column=0)
        self.MCQs=Button(self.master,text="MCQs",fg='blue',command=self.mcqs).grid(row=1,column=3)
        self.MCQs=Button(self.master,text="TRUE/FALSE",fg='blue',command=self.tfq).grid(row=1,column=4)
        self.MCQs=Button(self.master,text="Numeric",fg='blue',command=self.numeric).grid(row=1,column=5)

    def mcqs(self):
        
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=9,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=10,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=11,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=12,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=13,column=0)
        ###################Labels And Text Entry Fields For MCQs#########################################
        self.init=Label(self.master,text='Enter The Question Here.',fg='red').grid(row=0,column=0)
        self.quest=Label(self.master,text='Question : ',fg='black').grid(row=8,column=0)
        self.quest=Label(self.master,text='Option1 : ',fg='black').grid(row=9,column=0)
        self.quest=Label(self.master,text='Option2 : ',fg='black').grid(row=10,column=0)
        self.quest=Label(self.master,text='option3 : ',fg='black').grid(row=11,column=0)
        self.quest=Label(self.master,text='Option4 : ',fg='black').grid(row=12,column=0)
        self.quest=Label(self.master,text='Answer : ',fg='black').grid(row=13,column=0)

        
        self.quest1=StringVar()
        self.text_entry=Entry(self.master,textvariable=self.quest1).grid(row=8,column=1)
        self.opt1=StringVar()
        self.text_entry=Entry(self.master,text=self.opt1).grid(row=9,column=1)
        self.opt2=StringVar()
        self.text_entry=Entry(self.master,text=self.opt2).grid(row=10,column=1)
        self.opt3=StringVar()
        self.text_entry=Entry(self.master,text=self.opt3).grid(row=11,column=1)
        self.opt4=StringVar()
        self.text_entry=Entry(self.master,text=self.opt4).grid(row=12,column=1)
        self.answer=StringVar()
        self.text_entry=Entry(self.master,text=self.answer).grid(row=13,column=1)
        self.saving_data=Button(self.master,text="save",fg='red',command=lambda : self.save_data_mcq(self.quest1.get(),
                    self.opt1.get(), self.opt2.get(), self.opt3.get(),self.opt4.get(), self.answer.get())).grid(row=14,column=1)

    def save_data_mcq(self, quest1, opt1, opt2, opt3, opt4, answer):
        k1=4
        ###############INSERTING MCQs data in database#########
        print (quest1, opt1, opt2, opt3, opt4, answer)
        cur.execute('INSERT INTO questions (key, Question, Option1, Option2, Option3, Option4, Answer) VALUES (?, ?, ?, ?, ?, ?, ?)',
                    (k1, quest1, opt1, opt2, opt3, opt4, answer))
        con.commit()
        print('Record Inserted')

        
    def tfq(self):
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=9,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=10,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=11,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=12,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=13,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=9,column=1)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=10,column=1)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=11,column=1)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=12,column=1)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=13,column=1)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=14,column=1)
    #######################Labels and Text Entry Fields for True False Questions#############
        self.init=Label(self.master,text='Enter The Question Here.',fg='red').grid(row=0,column=0)
        self.quest=Label(self.master,text='Question : ',fg='black').grid(row=8,column=0)
        self.quest=Label(self.master,text='Answer(T/F) : ',fg='black').grid(row=9,column=0)
        self.quest1=StringVar()
        self.text_entry=Entry(self.master,textvariable=self.quest1).grid(row=8,column=1)
        self.answer=StringVar()
        self.text_entry=Entry(self.master,text=self.answer).grid(row=9,column=1)
        self.saving_data=Button(self.master,text="save",fg='red',command=lambda : self.save_data_tfq(self.quest1.get(),self.answer.get())).grid(row=10,column=1)

    def save_data_tfq(self, quest1, answer):
        k1=2
        ###############INSERTING TRUE/FALSE data in database#########
        print (quest1, answer)
        cur.execute("INSERT INTO questions (key, Question, Option1, Option2, Answer) VALUES (?, ?,'T' , 'F', ?)",
                    (k1, quest1, answer))
        con.commit()
        print('Record Inserted')

    def numeric(self):
        
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=9,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=10,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=11,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=12,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=13,column=0)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=9,column=1)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=10,column=1)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=11,column=1)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=12,column=1)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=13,column=1)
        self.quest=Label(self.master,text='                                                           ',fg='black').grid(row=14,column=1)
        #######################Labels and Text Entry Fields for Numeric Questions########
        self.init=Label(self.master,text='Enter The Question Here.',fg='red').grid(row=0,column=0)
        self.quest=Label(self.master,text='Question : ',fg='black').grid(row=8,column=0)
        self.quest=Label(self.master,text='Answer(Numerical) : ',fg='black').grid(row=9,column=0)
        self.quest1=StringVar()
        self.text_entry=Entry(self.master,textvariable=self.quest1).grid(row=8,column=1)
        self.answer=StringVar()
        self.text_entry=Entry(self.master,text=self.answer).grid(row=9,column=1)
        self.saving_data=Button(self.master,text="save",fg='red',command=lambda : self.save_data_num(self.quest1.get(),self.answer.get())).grid(row=10,column=1)
        
    def save_data_num(self, quest1, answer):
        k1=0
        ###############INSERTING Numric Questions data in database#########
        print (quest1, answer)
        cur.execute("INSERT INTO questions (key, Question, Answer) VALUES (?, ?,?)",
                    (k1, quest1, answer))
        con.commit()
        print('Record Inserted')


    def exit(self):
        self.master.withdraw()


if __name__ == '__main__':
    root=Tk()
    login_window=faculty_window(root)
    root.mainloop()
