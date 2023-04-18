class Greeter():
    def hello(self):
        return "Hello!"
    def good_bye(self):
        return "Good bye!"
    

class Person():
    def __init__(self, name, birthday, favourite_language):
        self.name = name
        self.birthday = birthday
        self.favourite_language = favourite_language
    
person1 = Person("Afzaa Atcha", "25th September 1992", "Python")

class Animal():
    def __init__(self, )