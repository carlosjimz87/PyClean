class Person():
    pass


person = Person()

setattr(person, 'first', 'John')
setattr(person, 'last', 'Doe')

print(person.first)
print(person.last)
