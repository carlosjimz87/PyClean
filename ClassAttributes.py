class Person:
    pass


if __name__ == '__main__':
    person = Person()

    setattr(person, 'first', 'John')
    setattr(person, 'last', 'Doe')

    print(person.first)
    print(person.last)
