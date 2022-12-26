import random

def main():
    hometask = int(input("Введіть, будь ласка, номер завдання з 1 по 6: "))
    if hometask == 1:
        print("         Завдання 1      ")
        task1()
    if hometask == 2:
        print("         Завдання 2      ")
        task2()
    if hometask == 3:
        print("         Завдання 3      ")
        task3()
    if hometask == 4:
        print("         Завдання 4      ")
        task4()
    if hometask == 5:
        print("         Завдання 5      ")
        task5()
    if hometask == 6:
        print("         Завдання 6      ")
        task6()
    if 1 < hometask > 6:
        print("Не вірно! Введіть з 1 по 6 )")

def my_list():
    mylist = []
    for i in range(0, 5):
        n = random.randint(50, 300)
        mylist.append(n)
    return mylist

def task1():
    mylist = my_list()
    print(mylist)
    for i in range(len(mylist)):
        if mylist[i] > 100:
            print(mylist[i],end=" ")

def task2():
    mylist = my_list()
    print(mylist)
    my_result = []
    for i in range(len(mylist)):
        if mylist[i] > 100:
            my_result.append(mylist[i])
    print(my_result)

def task3():
    mylist = my_list()
    print(mylist)
    if len(mylist) < 2:
        mylist.append(0)
    else:
        mylist.append(mylist[-1] + mylist[-2])
    print(mylist)

def task4():
    mylist = my_list()
    print(mylist)
    k = int(input("Індекс елементу: "))
    for i in range(k, len(mylist) - 1):
        mylist[i] = mylist[i + 1]
    mylist.pop(len(mylist) - 1)
    for i in range(len(mylist)):
        print(mylist[i], end=' ')

def task5():
    mylist = my_list()
    print(mylist)
    k = int(input('Ввести k '))
    с = int(input('Ввести с '))
    mylist = mylist[:k] + [с] + mylist[k:]
    print(mylist)

def task6():
    my_list1: list = list(map(int, input("Введіть числа, розділених пробілами для першого списку: ").split()))
    my_list2: list = list(map(int, input("Введіть числа, розділених пробілами для другого списку: ").split()))
    print(len(set(my_list1) & set(my_list2)))

main()

