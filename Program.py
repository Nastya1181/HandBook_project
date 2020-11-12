from Directory import Directory


class Program:
    # создание справочника и проверка функционала
    dir = Directory("Справочник")
    print(dir.name)
    dir.add_person("Анастасия", "Жирнова", "8912", "Екатеринбург", "gir")
    dir.directory[0].print_person_info()
    dir.add_person("Ник", "Самс", "8912", "ек", "sam")
    dir.directory[1].print_person_info()
    pers = dir.find_person("пе")
    pers.print_person_info()
    dir.change_data("gir", "Имя", "Настя")
    dir.directory[0].print_person_info()


print("Hello")