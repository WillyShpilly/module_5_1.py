class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)


# классы и объекты
# условно свой собственный тип данных
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.say_info()
#     def say_info(self):
#         print(f'Привет, меня зовут {self.name}, мне {self.age}')
#
#     def birthday(self):
#         self.age += 1
#         print(f'У меня день рождения, мне теперь {self.age} ')
#
# den = Human('Денис', 22)
# max = Human('Максим', 20)
# print(den.name, den.age)
# den.surname = 'Повов'
# print(den.surname)
# print(max.name, max.age)
# max.birthday()