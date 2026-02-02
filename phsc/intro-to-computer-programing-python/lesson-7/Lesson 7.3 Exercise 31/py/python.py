class person:
    pass

print(type(person))

jack = person()

jill = person()

print(jack is jill)

jack2=jack

print(jack2 is jack)

person1 = person()
person1.name = "gol D. Roger"

print(person1.name)

person1.__dict__
{}
person1.name = "Gol D. roger"
person1.age = 53
person1.height_in_cm = 180
person1.__dict__
{'age':53, 'height_in_cm':180, 'name': 'Gol D. Roger'}

print(person1.name,person1.age, person1.height_in_cm)
