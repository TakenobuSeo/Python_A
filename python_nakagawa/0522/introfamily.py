import introduce

class IntroFam(introduce.Intro):
    def __init__(self, name, age, catName):
        super().__init__(name, age)
        self.catName = catName

    def cat_out(self):
        catTxt = "飼い猫の名前は" + self.catName + "です"
        print(catTxt)
        return catTxt
    
    def all_out(self):
        self.name_age_out()
        self.cat_out()
