class MyClass():
    pass


def speak(self):
    print("hoooo")


if __name__ == '__main__':
    MyClass.speak = speak

    mc = MyClass()
    mc.speak()
