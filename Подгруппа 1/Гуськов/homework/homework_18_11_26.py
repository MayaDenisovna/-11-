# задание 1
class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.free = True

    def show(self):
        if self.free:
            st = "доступна"
        else:
            st = "выдана"
        print(self.name, "|", self.author, "|", self.year, "|", st)

    def is_free(self):
        return self.free

    def take(self):
        if self.free:
            self.free = False
            print("книга", self.name, "выдана")
        else:
            print("книга", self.name, "уже выдана, нельзя выдать еще раз")

    def give_back(self):
        self.free = True
        print("книга", self.name, "возвращена")


class Library:
    def __init__(self, name):
        self.__name = name
        self.__books = []

    def add(self, book):
        self.__books.append(book)

    def remove(self, name):
        for b in self.__books:
            if b.name == name:
                self.__books.remove(b)
                print("книга", name, "удалена")
                return
        print("книга", name, "не найдена")

    def show_all(self):
        print("библиотека:", self.__name)
        print("всего книг:", len(self.__books))
        for b in self.__books:
            b.show()

    def find(self, name):
        for b in self.__books:
            if b.name == name:
                return b
        return None

    def show_free(self):
        print("доступные книги:")
        for b in self.__books:
            if b.is_free():
                b.show()


lib = Library("школьная библиотека")

lib.add(Book("война и мир", "толстой", 1869))
lib.add(Book("преступление и наказание", "достоевский", 1866))
lib.add(Book("мастер и маргарита", "булгаков", 1967))
lib.add(Book("отцы и дети", "тургенев", 1862))
lib.add(Book("евгений онегин", "пушкин", 1833))

print("--- весь каталог ---")
lib.show_all()

print("--- поиск книги ---")
b = lib.find("мастер и маргарита")
if b != None:
    b.show()
else:
    print("не нашли")

print("--- выдаем книгу ---")
b.take()

print("--- пробуем выдать повторно ---")
b.take()

print("--- возвращаем книгу ---")
b.give_back()
if b.is_free():
    print("книга снова доступна")
else:
    print("книга все еще выдана")

print("--- доступные книги ---")
lib.show_free()

print("--- удаляем книгу ---")
lib.remove("отцы и дети")
lib.show_all()


# задание 2
class Vehicle:
    def __init__(self, brand, model, max_speed):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        self.__speed = 0

    def get_speed(self):
        return self.__speed

    def show(self):
        print("марка:", self.brand, "| модель:", self.model,
              "| макс скорость:", self.max_speed, "| скорость:", self.__speed)

    def accelerate(self, n):
        self.__speed = self.__speed + n
        if self.__speed > self.max_speed:
            self.__speed = self.max_speed
            print("нельзя ехать быстрее", self.max_speed, "км/ч")

    def stop(self):
        self.__speed = 0
        print(self.brand, self.model, "остановился")


class Car(Vehicle):
    def __init__(self, brand, model, max_speed, doors, fuel):
        super().__init__(brand, model, max_speed)
        self.doors = doors
        self.fuel = fuel

    def show(self):
        super().show()
        print("дверей:", self.doors, "| топливо:", self.fuel)

    def ac_on(self):
        print("в", self.brand, self.model, "включили кондиционер")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, max_speed, sidecar):
        super().__init__(brand, model, max_speed)
        self.sidecar = sidecar

    def show(self):
        super().show()
        if self.sidecar:
            print("боковой прицеп: есть")
        else:
            print("боковой прицеп: нет")

    def maneuver(self):
        print(self.brand, self.model, "сделал красивый маневр")


class Bicycle(Vehicle):
    def __init__(self, brand, model, max_speed, gears):
        super().__init__(brand, model, max_speed)
        self.gears = gears
        self.gear_now = 1

    def show(self):
        super().show()
        print("передач всего:", self.gears, "| сейчас передача:", self.gear_now)

    def shift(self, g):
        if g < 1 or g > self.gears:
            print("такой передачи нет")
        else:
            self.gear_now = g
            print("передача теперь", self.gear_now)


car = Car("лада", "веста", 180, 4, "бензин")
moto = Motorcycle("урал", "имз", 120, True)
bike = Bicycle("стелс", "навигатор", 40, 7)

print("--- информация о транспорте ---")
car.show()
moto.show()
bike.show()

print("--- увеличиваем скорость ---")
car.accelerate(60)
moto.accelerate(50)
bike.accelerate(10)

print("--- пробуем больше максимума ---")
car.accelerate(500)
moto.accelerate(500)
bike.accelerate(500)

car.show()
moto.show()
bike.show()

print("--- особые методы ---")
car.ac_on()
moto.maneuver()
bike.shift(5)
bike.show()

print("--- останавливаем весь транспорт ---")
car.stop()
moto.stop()
bike.stop()

car.show()
moto.show()
bike.show()