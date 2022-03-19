def get_number(question: str) -> float:
    while True:
        try:
            return float(input(question))
        except ValueError:
            print("Ну-ка стринги не пиши мне тут!")


def calculate():
    operation = input('''
        Выбери что нужно делать:
        + сумма
        - вычитание
        * умножение
        / деление
''')
    number_1 = get_number("Ввести число номер раз ")
    number_2 = get_number("Ввести число номер два ")
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        try:
            print(number_1 / number_2)
        except Exception as e:
            print(f"Не дели на ноль:{e}")
    else:
        raise InvalidExeption(f"Выбери из предложенных, БАКА!\nТы ввёл {operation}")


class InvalidExeption(Exception):
    pass


calculate()
