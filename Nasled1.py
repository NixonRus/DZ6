class Car:
    price = 1000000

    def horse_powers(self):
        hp = 120
        return hp


class Nissan(Car):
    price = 950000

    def horse_powers(self):
        hp = 105
        return hp


class Kia(Car):
    price = 1200000

    def horse_powers(self):
        hp = 230
        return hp


car = Car()
nis = Nissan()
kia = Kia()

print(car.price)
car.horse_powers()
# print(nis.price)
# nis.horse_powers()
# print(kia.price)
# kia.horse_powers()

