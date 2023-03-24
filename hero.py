# class Superhero:
#     people = "people"
#
#     def __init__(self ,name,nickname,superpower,health_points,catchphrase ):
#         self.name = name
#         self.nickname = nickname
#         self.superpower = superpower
#         self.health_points = health_points
#         self.catchphrase = catchphrase
#
#     def names(self):
#         return self.name
#
#     def hpx2(self):
#         return self.health_points * self.health_points
#
#     def __str__(self):
#         return f'его прозвище {self.nickname} , его суперспособность {self.superpower} , eго здровье {self.health_points}'
#
#     def __len__(self):
#         return f'длина его фразы {len(self.catchphrase)}'
#
#
# hero = Superhero("BATMAN", "летучая мышь", "технологии" , 100 , "на страже города !!!")
#
# print(hero.names())
# print(hero.hpx2())
# print(hero.__str__())
# print(hero.__len__())

# ДЗ_3
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __str__(self):
        return f"cpu: {self.__cpu}, memory: {self.__memory}"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu * self.__cpu


class Phone:
    def __str__(self):
        return self.call()

    __sim_card_list = ["Beeline", "O!", "Megacom"]

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    def call(self, sim_card_number=int(input("Выберите сим-карту: ")), call_to_number=int(input("Введите номер: "))):
        if sim_card_number == 1:
            return f"Идет звонок на номер {call_to_number} с сим-карты - {sim_card_number} {self.__sim_card_list[0]}"
        elif sim_card_number == 2:
            return f"Идет звонок на номер {call_to_number} с сим-карты - {sim_card_number} {self.__sim_card_list[1]}"
        elif sim_card_number == 3:
            return f"Идет звонок на номер {call_to_number} с сим-карты - {sim_card_number} {self.__sim_card_list[2]}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory):
        Computer.__init__(self, cpu, memory)

    def __str__(self):
        return super().__str__() + self.use_gps()

    def use_gps(self, location=input("Введите локацию: ")):
        return f" Маршрут проложен до {location}"



