import random

x = random.randint(0, 9)
while True:
    y = int(input("Ввести чесло от 0 до 9 включительно: "))
    if y != x:
        print("Проиграл.")
    else:
        print("Выиграл!")


import random

mylist = range(10)
for z in range(1, 10):
    x = random.sample(mylist, z)
    y = int(input("Ввести значение: "))
    if y in x:
        print("Проиграл.")
        print(x)
        break
    else:
        print("Выиграл!")
        print(x)


def giga_list_generator_9000(x) -> list:
    import datetime
    import random

    autolist = [random.randint(16, 32) for i in range(x)]
    dt_now = datetime.datetime.now()
    print(dt_now)
    print(autolist)


giga_list_generator_9000(16)