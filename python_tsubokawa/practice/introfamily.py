import introduce

class IntroFam(introduce.Intro):
    '''飼い猫を出力するメソッドを作成'''
    def __init__(self, age, name, cat_name):
        '''初期値設定'''
        #基底クラスのinitを呼び出し
        #age, nameを設定
        super().__init__(age, name)
        # 新たにcat_nameを設定
        self.cat_name = cat_name

    def cat_out(self):
        '''飼い猫の名前を出力するメソッド'''
        return (f'飼い猫の名前は、{self.cat_name}です')
    
import sys 
args = sys.argv
print(args)

name = args[1]
age = args[2]
cat_name = args[3]

# インスタンス化
introfam1  =IntroFam(args[1], args[2], args[3])
print(introfam1.get_name())
print(introfam1.get_age())
print(introfam1.cat_out())


