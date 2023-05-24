class Intro:
    '''自己紹介の基底クラス'''
    #Introクラスの初期値を設定
    def __init__(self,name, age):
        '''初期値設定'''
        self.name = name
        self.age = age
    
    def get_name(self):
        '''名前の取得'''
        return f'私の名前は{self.name}です'
    
    def get_age(self):
        '''年齢の取得'''
        return f'年齢は、{self.age}歳です'
    


