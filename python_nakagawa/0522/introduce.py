class Intro:
    def __init__(self, name, age):
        self.name = name
        self.age = str(age)
      
    def name_out(self):
        nameTxt = "私の名前は" + self.name + "です"
        return nameTxt
    
    def age_out(self):
        ageTxt = "年齢は" + self.age + "です"
        return ageTxt