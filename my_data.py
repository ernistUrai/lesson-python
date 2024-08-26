# class Car:
#     def __init__(self, make, model, year, color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#
#     def __str__(self):
#         return f"{self.make}, {self.model}, {self.year}, {self.color}"
#
# car1 = Car(make="Toyota", model="Camry", year=2020, color="Blak")
# print(car1)




# class Car:
#     def _init_(self, make, model, year, color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#
#     def display_info(self):
#         print(f"Make: {self.make}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")
#         print(f"Color: {self.color}")
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#
# # Example usage:
# car1 = Car("Toyota", "Camry", 2023, "Red")
# car1.display_info()








class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        while True:
            card = int(input("1) Узнать ваш баланс\n2)Пополнить баланс "))
            if card == 1:
                print(f"Ваш баланс {self._balance}")
                break
            elif card == 2:
                top_up = int(input("Сколько хотите добавить? "))
                print(f"Теперь ваш баланс составляет {self._balance + int(top_up)}")
                break
            else:
                print("Введите правильный номер!!!")

    def _kill(self):
        print("Ваш счет обнуляется...")
        self._balance = self._balance - self._balance
        return self._balance

    def __jackpot(self):
        self._balance *= 10
        print(f"Баланс после джекпота {self._balance}")

    @property
    def jackpot(self):
        return self.__jackpot

    def copy(self, other):
        if isinstance(other, Bank):
            self._balance += other._balance
            print(f"Ваш баланс объединен. Новый баланс {self._balance}")
        else:
            print("Можно объединить только с объектом класса Bank")

    def __str__(self):
        return f"Name {self._name}, balance {self._balance}"



account1 = Bank("Bektur", 2000)
account2 = Bank("Baiel", 1000)
account2.moneyX()
print(account1._kill())
print(dir(Bank))
account1._Bank__jackpot()
account1.copy(account2)
print(account1.__str__())
print(account2.__str__())