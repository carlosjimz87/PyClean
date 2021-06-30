class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)

            return cls._inst


s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
