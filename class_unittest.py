
import unittest
import calc
import sqlite3


con = sqlite3.connect('Quiz.db')
cur = con.cursor()

class IntegerArithmenticTestCase(unittest.TestCase):
    role = []
    name = []
    password = []
    questions = []
    answers = []
    scores = []
    students =[]
    def read_users_Table(self):
        cur.execute("SELECT * FROM users")
        Data = cur.fetchall()
        for index,dat in enumerate(Data):
            self.role.append(dat[2])
            self.name.append(dat[0])
            self.password.append(dat[1])
            if (dat[3]):
                self.scores.append(dat[3])
            if (dat[2]=='student'):
                self.students.append(dat[0])

    def read_questions_Table(self):
        cur.execute("SELECT * FROM questions")
        Data = cur.fetchall()
        for index,dat in enumerate(Data):
            self.questions.append(dat[1])
            self.answers.append(dat[6])

        

    #function to test if all the users registered have name, passwords and roles available
    def test_login(self):
        self.read_users_Table()
        self.assertEqual(len(self.role),len(self.name),len(self.password))

    #function to test if marks stored are qual to number of student
    def test_scoreVSstudents(self):
        self.assertEqual(len(self.students),len(self.scores))

    #function to test if qusetions and answers are equal in number
    def test_ansVSques(self):
        self.read_questions_Table()
        self.assertEqual(len(self.questions),len(self.answers))
        

    

if __name__ == '__main__':
    unittest.main()
