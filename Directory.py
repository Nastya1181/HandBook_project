from PersonInfo import PersonInfo


class Directory:
    name = ""
    directory = []

    def __init__(self, name):
        self.name = name

    def add_person(self, name, surname, phone_number, city, email):
        person = PersonInfo(name, surname, phone_number, city, email)
        self.directory.append(person)

    def find_person(self, email):
        found = PersonInfo("нет", "нет", "нет", "нет", "нет")
        for obj in self.directory:
            if obj.email == email:
                found = obj
        return found

    def delete_person(self, email):
        self.directory.remove(self.find_person(email))

    def change_data(self, email, characteristic, changes):
        self.find_person(email).change_info(characteristic, changes)
