class MyClass():
    pass


def speak(self):
    print("hoooo")


MyClass.speak = speak

mc = MyClass()
mc.speak()
