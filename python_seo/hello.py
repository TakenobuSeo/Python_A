# 挨拶を出力
print('Hello world!')

# 東京大阪まで何時間？
kyori = 507.5
jisoku = 80
jikan = kyori / jisoku
print(jikan)

class Hello:
    def __init__(self, hello, name):
        self.hello1 = hello
        self.name = name
    
    def hello_world(self):
        greeting = str(self.hello1) + "～～、" + str(self.name)
        return greeting
    
class Dinner(Hello):
    def __init__(self, hello, name, food, drink):
        super().__init__(hello, name)
        self.food = food
        self.drink = drink

    def today_dinner(self):
        return "{}さんの今晩のご飯は{}で、{}を飲みました。".format(self.name, self.food, self.drink)
        
hello = Hello("こんにちは-----","Kenshin")
print(hello.hello_world())

dinner = Dinner("こんばんは", "隆一","お寿司", "お茶")
print(dinner.today_dinner())