names = ["Alice", "Bob", "Charlie", "Dave", "Francis", "Gerald", "Hazel"]
ages = [17, 42, 13, 22, 25, 31, 39]
genders = ["F", "M", "M", "M", "M", "M", "F"]


class Person:
    def __repr__(self):
        return str(self.__dict__)

    def __init__(self, name, age, gender):
        self.Name = name
        self.Age = age
        self.Gender = gender


for i in range(7):
    x = Person(names[i], ages[i], genders[i])
    print(x)
    print("\n")
