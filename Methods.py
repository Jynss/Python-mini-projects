class Person:
    def __repr__(self):
        return str(self.__dict__)

    def __init__(self, name, age, gender):
        self.Name = name
        self.Age = age
        self.Gender = gender

    def increase_age(self):
        self.Age += 1

    def description(self):
        if self.Gender == "F":
            self.Gender = "Female"
            pronoun = "She"
        else:
            self.Gender = "Male"
            pronoun = "He"

        print(
            "Hello, how are you doing today? I hope you're ALRIGHTYYY. Today, I am going to introduce you to the newest member of our team.. Introducing... ",
            self.Name, pronoun, ",is", self.Age, "years old and", pronoun,
            "is a very polite", self.Gender)


x = Person("Jynene", 16, "F")
y = Person("Sanjay", 16, "M")
#print(x)
#print(y)
print("\n")

x.description()
print("\n"*2)
y.description()
