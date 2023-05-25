import introduce
class IntroFam(introduce.Intro):
    def __init__(self, name, age, cat):
        self.name = name
        self.age = age
        self.cat = cat
    
    def cat_out(self):
        cattxt = "飼い猫の名前は、" + self.name + "歳です"
        return cattxt