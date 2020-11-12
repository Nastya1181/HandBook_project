class PersonInfo:
    name = ""
    surname = ""
    phone_number = ""
    city = ""
    email = ""

    def __init__(self, name, surname, phone_number, city, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.city = city
        self.email = email

    def print_person_info(self):
        print(f" Имя: {self.name}, Фамилия: {self.surname}, Номер телефона: {self.phone_number}, "
              f"Город: {self.city}, Адрес электронной почты: {self.email}")

    def change_info(self, characteristic, changes):
        if characteristic == "Имя":
            self.name = changes
        elif characteristic == "Фамилия":
            self.surname = changes
        elif characteristic == "Номер телефона":
            self.phone_number = changes
        elif characteristic == "Город":
            self.city = changes
        elif characteristic == "Адрес электронной почты":
            self.email = changes
