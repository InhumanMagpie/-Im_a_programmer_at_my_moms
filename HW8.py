class Vehicle:
    sound = "BEEP!"

    def __init__(self, color: str = "Black", body_type: str = "Sedan", brand_model_name: str = "Ford Crown Victoria"):
        self.color = color
        self.body_type = body_type
        self.brand_model_name = brand_model_name

    @classmethod
    def beep(cls):
        print(cls.sound)

    @staticmethod
    def human_walk():
        print("Human see scy")

    def color(self):
        print(f"Cool {self.color} color")

    def body_type(self):
        print(f"Nice {self.body_type} lines")

    def brand_model(self):
        print(f"Best {self.brand_model_name} you can found in this city")


class Truck(Vehicle):
    sound = "BOONG!"

    def __init__(self, color, body_type, brand_model, load_capacity: int, amount_of_seats: int):
        super().__init__(color, body_type, brand_model)
        self.load_capacity = load_capacity
        self.amount_of_seats = amount_of_seats

    def body_type(self):
        print("We can order any truck for you")


def main():
    my_truck = Truck("Black", "Pickup", "Ford", 700, 7)
    my_truck.beep()


if __name__ == '__main__':
    main()
