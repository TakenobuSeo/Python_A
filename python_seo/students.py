class Student:
    def __init__(self, id, name, score=0):
        self.id = id
        self.name = name
        self.score = score

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score
    
class CalcScore:
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def ave(self):
        v = 0
        for i in self.students:
            v += i.getScore()
        ave_v = v / len(self.students)
        return ave_v
    
