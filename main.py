class Worker():

    def __init__(self, name, workname):
        self.__name = name
        self.__workname = workname
        self.__payment = 0
        self.__startyear = 0

    def __str__(self):
        return (f"ФИО: {self.__name} Должность: {self.__workname} Зарплата {self.__payment} ГНР {self.__startyear}")

    def __del__(self):
        return (self.__name, self.__workname, self.__payment, self.__startyear)


workerlist = []
menuset = 0

def showmenu() :
    print("Menu")
    print(""
          "1.Добавить работника"
          "2.Найти работника"
          "3.Редактировать работника"
          "4.Удалить работника"
          "5.Вывести список работников"
          "6.Выход")
    menuset = int(input("Выберите раздел меню: "))
    return menuset

menuset = showmenu()

if menuset == 0 :
    print("До свидания!")
    exit()
elif menuset == 1:  # Добавление работника
    name, workname, payment, startyear = map(str, input("Введите Фамилию, Должность, Зарплату и ГНР работника через пробел").split())
    payment = int(payment)
    startyear = int(startyear)
    workerlist.append(Worker(name, workname, payment, startyear))
elif menuset == 2:  # Найти работника
    chosefindmenu = int(input("Введите критерий, по которому собираетесь искать"
                              "1 - Фамилия  2 - Должноть  3 - Зарплата  4 - ГНР"))
    if chosefindmenu == 1:
        whatname = str(input("Введите Фамилию работника"))
    elif chosefindmenu == 2:
        whatworkername = str(input("Введите Фамилию работника"))
    elif chosefindmenu == 3:
        whatpayment = str(input("Введите Фамилию работника"))
    elif chosefindmenu == 4:
        whatstartyear = str(input("Введите Фамилию работника"))
    else:
        print("Ошибка!")
elif menuset == 3:
    pass
elif menuset == 4:
    pass
elif menuset == 5:
    print("Список работников:")
    for i in range(len(workerlist)):
        print(i + 1, ": ", workerlist[i].__str__(), "")