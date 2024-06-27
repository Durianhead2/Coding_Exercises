# Write a Python program to create a person class. 
# Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age.

from datetime import date

class Person:
    
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def determineAge(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            age -= 1
        return age
    
person1 = Person("Martha", "China", date(1962, 7, 12))
print(person1.age)

