class Building:
    total = 0  # Классовый атрибут

    def __init__(self, name):  # Инициализатор или конструктор класса
        self.name = name
        Building.total += 1

    def __str__(self):
        return f'{self.name}'

    # def __del__(self):
    #     print(f'освободили память от {self.name}')


building = [Building(f'Здание_{i}') for i in range(40)] # Циклом создаём объекты
for i in range(40):
    print(f'Объект_{i}: ', building[i])

# print()
# print('total=', Building.total)
