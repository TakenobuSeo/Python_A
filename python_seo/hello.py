print('Hello world!')

class Hello:
    def __init__(self, hello, name):
        self.hello1 = hello
        self.name = name
    
    def hello_world(self):
        greeting = str(self.hello1) + "～～、" + str(self.name)
        return greeting

hello = Hello("こんにちは","Kenshin")
print(hello.hello_world())