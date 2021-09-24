name = "Chars"
age = 33

print("Hi, I'm {} and I'm {} years old".format(name, age))
print(
    "Hi, I'm {1} years old and my name is {0}. Yeah, {1} years".format(name, age))

data = {'day': 'Saturday', 'office': 'Home', 'other': 'UNUSED'}

print("On {day} I was working at {office}!".format(**data))

print(f"(three years later )Hi, I'm {name} and I'm {age + 3} years old.")
