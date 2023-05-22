import introduce

class IntroFam(introduce.Intro):
    '''飼い猫の紹介も含めた自己紹介クラス'''
    def __init__(self, name: str, age: int, cat_name:str):
        super().__init__(name, age)
        self.cat_name = cat_name

    def cat_out(self) -> str:
        '''飼い猫の紹介文を返す'''
        cattxt = f"飼い猫の名前は、{self.cat_name}です"
        return cattxt
    