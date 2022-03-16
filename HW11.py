from time import sleep


def geometric_progression(number: float, progression_denominator: float):
    while True:
        number = number * progression_denominator
        yield number
        sleep(1)


qwerty = geometric_progression(2, 2)
for i in qwerty:
    print(i)


