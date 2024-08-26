"""

class Bank:


    def __init__(self, name, balance = 0):
        self.__name = name
        self.__balance = balance


    def deposit(self, amount = 0):
        self.__balance += amount
        print(f"{self.__name} ваш счет "
              f"Паполнен на  {amount} рублей\n"
              f"{self.__name}:Ваш счет {self.__balance} руб ")

    def kill(self):
        self.__balance = 0
        print(f"Cчет {self.__balance} обнулен ")


    def __jackpot(self):
        self.__balance *= 10
        print(f"{self.__name} ваш баланс умножен на 10.")

    def over_balance(self, other_account):
        self.__balance += other_account.__balance

        print(f"{other_account.__name} ваш баланс переданы на  Счет {self.__name}.\n"
              f"{self.__name} ваш баланс: {self.__balance} ")

#
accaunt1 = Bank("Maksat", 1000)
accaunt2 = Bank("Nurik", 2000)
accaunt1.deposit(140)
accaunt2.deposit(250)

accaunt1.over_balance(accaunt2)
"""
#=================================================================



# rint("Здрастувуйте.")
# class InstallmentPlan:
#     def __init__(self, phone, price):
#         self.phone = phone
#         self.price = price
#
#     def calculate_total_cost(self):
#         print("Товар стоимость наличии")
#         print("Смартфон:", self.phone, "цена:", self.price)
#
# class FixedInstallment(InstallmentPlan):
#     def __init__(self, phone,  price, months, ):
#         super().__init__( phone, price)
#         self.months = months
#
#     def calculate_total_cost(self):
#         print("В рассрочку. До 12 месяц")
#         print("Смартфон:", self.phone,
#               "цена:", self.price, "В месяц:", self.price / self.months)
#
#
# class VariableInstallment(InstallmentPlan):
#     def __init__(self, phone, price, months, interest_rate):
#         super().__init__(phone, price)
#         self.months = months
#         self.interest_rate = interest_rate
#
#     def calculate_total_cost(self):
#         percent = self.interest_rate / 100
#         to_percent = self.price * percent
#         get = self.price + to_percent
#
#         print(f"В кредит {self.interest_rate}%. До {self.months}\n"
#               f"Смартфон:{self.phone}\n"
#               f"Цена:{self.price}\n"
#               f"Вы месяц:{get / self.months}")
#
#
#
# product = InstallmentPlan("Iphone Pro Max 15", 120000)
# product.calculate_total_cost()
#
# fixed_inst = FixedInstallment("Iphone Pro Max 15", 120000, 12)
# va_cost = VariableInstallment("Samsung Galaxy Ultra 24", 107000, 24, 7)
# fixed_inst.calculate_total_cost()
# va_cost.calculate_total_cost()
#


#================================================================================

#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# for i in a:
#     if i < 5:
#         b.append(i)
# print(a)
# print(b)
# print(list(filter(lambda elem: elem < 5, a)))

#================================================================================
#1===============================================================================
#
# user_numbers = int(input("Введите число:"))
# if user_numbers % 2 == 0:
#     print("Четное число", user_numbers,'.')
#
# else:
#     print("Не  четное число", user_numbers,'.')
#
# #2=================================================================================
#
#
# def set (a, b):
#     print( "Резултат:", a + b)
#
# a = int(input("Введите первое число:"))
# b = int(input("Введите второе число:"))
# set(a, b)
#
# number = input("Введите число черес пробел:").split()
# total = sum(int(num) for num in number)
# print("Сумма:", total)
#=========================================================

#3

#
# user_string = str(input("Введите текс:"))
# print(user_string[::-1])
#
# ##=========================================================

#4# ##=========================================================




# user_name = str(input("Введите имя:"))
# print("Здрастувуйте", user_name)

# ##=========================================================
#
# a = []
#
# for i in range(1, 100):
#     a.append(i)
# print(a)
# total = sum(a)
# print("Сумма всех чисел от 1 до 100:", total)
#

# ##=========================================================

user_numbers = int(input("Введите число:"))

for x in range(user_numbers):
    print(x)