class Student:
    def __init__(self,sid,name,grade):
        self.sid = sid
        self.name = name
        self.grade = grade


    def displaystu(self):
        print(self.sid,self.name,self.grade)