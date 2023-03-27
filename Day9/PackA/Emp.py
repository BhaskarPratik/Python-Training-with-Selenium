class Employee:
    def __init__(self,eid,name,sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def displayemp(self):
        print(self.eid,self.name,self.sal)