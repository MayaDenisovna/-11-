class Character():
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    def get_info(self):
        return [self.name, self.__health]

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            print(f'персонаж {self.name} мёртв!')
            self.__health = 0
        else:
            print(f'персонаж {self.name} получил -{damage} хп!')


class Prisoner(Character):
    def __init__(self, name, health, srok):
        super().__init__(name, health)
        self.srok = srok

    def act(self, damage):
        print(f'заключённый {self.name} реагирует на получение урона!')
        self.take_damage(damage)


class Guard(Character):
    def __init__(self, name, health, zvanie):
        super().__init__(name, health)
        self.__zvanie = zvanie

    def act(self, target, damage):
        print(f'охранник {self.name} ({self.__zvanie}) наносит -{damage} хп заключённому {target.name}')
        target.act(damage)


guard = Guard('Смирнов', 100, 'сержант')
prisoner = Prisoner('Иванов', 40, 5)

guard.act(prisoner, 10)
guard.act(prisoner, 35)
print(prisoner.get_info())
