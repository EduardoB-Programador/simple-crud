import datetime

class Person():
    age:int
    email:str
    name:str
    phone_number:str
    registration_date:datetime.datetime

    def __init__(self, age:int|None = None,
                 email:str|None = None,
                 name:str|None = None,
                 phone_number:str|None = None) -> None:

        self.age = age
        self.email = email
        self.name = name
        self.phone_number = phone_number
        self.registration_date = datetime.datetime.now()

    @staticmethod
    def decrement_id() -> None:
        Person.id -= 1

    def __str__(self) -> str:

        return f'''ID: {self.id}
Name: {self.name}
Age: {self.age}
Email: {self.email}
Phone Number: {self.phone_number}
Creation Date: {self.registration_date}
        '''