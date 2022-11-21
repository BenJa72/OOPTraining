class Worker():

    def __init__(self, name="", workname="", payment=0, startyear=0):
        self.__name = name
        self.__workname = workname
        self.__payment = payment
        self.__startyear = startyear

    def __str__(self):
        return (f"ФИО: {self.__name} Должность: {self.__workname} Зарплата {self.__payment} ГНР {self.__startyear}")

    def __del__(self):
        return self.__name, self.__workname, self.__payment, self.__startyear

workerlist = []
name = str("")
while True:
    print("Menu")
    print(""
          " 1.Добавить работника"
          " 2.Найти работника"
          " 3.Редактировать работника"
          " 4.Удалить работника"
          " 5.Вывести список работников"
          " 6.Выход")
    menuset = int(input("Выберите раздел меню: "))
    if menuset == 0 :
        print("До свидания!")
        exit()
    elif menuset == 1:  # Добавление работника
        try:
            name, workname, payment, startyear = map(str, input("Введите Фамилию, Должность, Зарплату и ГНР работника через пробел: ").split())
            payment = int(payment)
            startyear = int(startyear)
            workerlist.append(Worker(name, workname, payment, startyear))
            print("Работник успешно создан!")
        except:
            print("Ошибка, возвращение в главное меню...")
    elif menuset == 2:  # Найти работника
        chosefindmenu = int(input("Введите критерий, по которому собираетесь искать: "
                                  "1 - Фамилия  2 - Должноть  3 - Зарплата  4 - ГНР"))
        if chosefindmenu == 1:
            whatname = str(input("Введите Фамилию работника"))
            for i in range(len(workerlist)):
                if (Worker[i].__name() == name):
                    print(workerlist[i].__str__())
                else:
                    print("Работник с такой Фамилией не существует")
        elif chosefindmenu == 2:
            whatworkname = str(input("Введите Должность работника"))
            for i in range(len(workerlist)):
                if (i.workname == whatworkname):
                    print(i)
                else:
                    print("Работник с такой Должностью не существует")

        elif chosefindmenu == 3:
            whatpayment = int(input("Введите Зарплату работника"))
            for i in range(len(workerlist)):
                if (i.payment == whatpayment):
                    print(i)

                else:
                    print("Работник c такой Зарплатой не существует")
        elif chosefindmenu == 4:
            whatstartyear = int(input("Введите ГНР работника"))
            for i in range(len(workerlist)):
                if (i.startyear == whatstartyear):
                    print(i)
                else:
                    print("Работник с таким ГНР не существует")
        else:
            print("Ошибка!")
    elif menuset == 3:
        whatname = str(input("Введите Фамилию работника"))
        for i in range(len(workerlist)):
             if (i.name == whatname):
                 print("Выбран: ", i)
                 chosechange = int(input("Что вы хотите изменить? "
                       "1.Фамилию, 2.Должность, 3.Зарплата, 4.ГНР"))
                 if chosechange == 1:
                     i.name = str(input("Введите новую Фамилию работника"))
                 elif chosechange == 2:
                     i.workname = str.input(("Введите новую Должность работника"))
                 elif chosechange == 3:
                     i.payment = int(input("Введите новую зарплату работника"))
                 elif chosechange == 4:
                     i.startyear = int(input("Введите новый ГНР работника"))
                 else:
                     print("Ошибка!")
             else:
                 print("Работник с такой Фамилией не существует")
        else:
            print("Ошибка!")
    elif menuset == 4:
        chosedellworker = str(input("Введите имя работника которого хотите удалить: "))
        for i in range(len(workerlist)):
            if (workerlist[i],name == chosedellworker):
                workerlist[i].__del__()
    elif menuset == 5:
        print("Список работников:")
        for i in range(len(workerlist)):
            print(i + 1, ": ", workerlist[i].__str__(), "")
    else:
        print("Ошибка!")
