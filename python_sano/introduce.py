class Intro:
    '''自己紹介をするクラス'''
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def name_out(self) -> str:
        '''名前の自己紹介文を返す'''
        nametxt = f"私の名前は、{self.name}です"
        return nametxt
    
    def age_out(self) -> str:
        '''年齢の自己紹介文を返す'''
        agetxt = f"年齢は、{self.age}歳です"
        return agetxt