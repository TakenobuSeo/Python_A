class Student:
    '''生徒を表すクラス'''
    def __init__(self, id: int, name: str, score: int = 0) -> None:
        '''初期化'''
        self.id = id
        self.name = name
        self.score = score

    def getId(self) -> int:
        '''IDを取得するメソッド'''
        return self.getId

    def getName(self) -> str:
        '''生徒名を取得するメソッド'''
        return self.getName

    def setScore(self, score: int) -> None:
        '''点数を設定するメソッド'''
        self.score = score

    def getScore(self) -> int:
        '''点数を取得するメソッド'''
        return self.score
    

class CalcScore:
    '''点数を計算する関数'''
    def __init__(self) -> None:
        '''初期化'''
        self.students = []

    def addStudent(self, student) -> None:
        self.students.append(student)

    def ave(self) -> float:
        v = 0
        for i in self.students:
            v += i.getScore()
        ave_v = v / len(self.students)
        return ave_v

p1 = Student(10, "佐藤")
p1.setScore(80)
p2 = Student(11, "鈴木", score = 79)
p3 = Student(12, "佐々木", score = 84)
p4 = Student(13, "井上", score = 77)

calc = CalcScore()
calc.addStudent(p1)
calc.addStudent(p2)
calc.addStudent(p3)
calc.addStudent(p4)
print(f"平均点 = {calc.ave()}")