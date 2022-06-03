class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        list_info = []
        for value in self.__dict__.values():
            list_info.append(value)
        return list_info.__repr__()


person = Profile('Dude', 'Lebovsky', '0770507088', 'Lviv', 'thedude@gmail.com', '20.06.1993', '28', 'male')
print(person)
