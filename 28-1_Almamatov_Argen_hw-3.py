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

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def make_computations(self):
        return self.__cpu * self.__memory


class Phone:
    def __str__(self):
        return self.call()

    __sim_cards_list = ["Beeline", "Megacom", "O!"]


    def get_sim_cards_list(self):
        return self.__sim_cards_list


    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number=int(input("Выберите сим-карту: ")), call_to_number=int(input("Введите номер: "))):
        if sim_card_number == 1:
            return f"Идет звонок на номер {call_to_number} с сим-карты - {sim_card_number} {self.__sim_cards_list[0]}"
        elif sim_card_number == 2:
            return f"Идет звонок на номер {call_to_number} с сим-карты - {sim_card_number} {self.__sim_cards_list[1]}"
        elif sim_card_number == 3:
            return f"Идет звонок на номер {call_to_number} с сим-карты - {sim_card_number} {self.__sim_cards_list[2]}"

    #


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory):
        Computer.__init__(self, cpu, memory)

    def __str__(self):
        return super().__str__() + self.use_gps()

    def use_gps(self, location=str(input("Введите локацию: "))):
        return f" Маршрут проложен до {location}"


mac_book = Computer(8, 256)
samsung = Phone()
telephone = SmartPhone(64, 265)
smartphone = SmartPhone(4, 344)
print(samsung)
print(mac_book)
print(telephone)
print(smartphone)

print(smartphone.use_gps())
print(telephone.call())

print(mac_book.make_computations())
print(mac_book == smartphone)
print(mac_book != telephone)
print(mac_book < smartphone)
print(mac_book > smartphone)
print(mac_book >= telephone)
print(mac_book <= smartphone)
