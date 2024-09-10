class House():
    houses_history = []   # Новый атрибут -------------------------------
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.houses_history.append(args[0])
        return obj
    def __init__(self, name, namber_of_floors):
        self.name = name
        self.namber_of_floors = namber_of_floors
    def __len__(self):
        return self.namber_of_floors
    def __str__(self):
        return 'Название '+self.name+', количество этажей '+str(self.namber_of_floors)
    def __eq__(self, other):
        if isinstance(other,House):
            return self.namber_of_floors == other.namber_of_floors
        elif isinstance(other, int):
            return self.namber_of_floors == other.namber_of_floors
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        if isinstance(other,House):
            return self.namber_of_floors < other.namber_of_floors
        elif isinstance(other, int):
            return self.namber_of_floors < other
    def __le__(self, other):
        if isinstance(other, House):
            return self.namber_of_floors <= other.namber_of_floors
        elif isinstance(other, int):
            return self.namber_of_floors <= other
    def __gt__(self, other):
        if isinstance(other, House):
            return self.namber_of_floors > other.namber_of_floors
        elif isinstance(other, int):
            return self.namber_of_floors > other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.namber_of_floors >= other.namber_of_floors
        elif isinstance(other, int):
            return self.namber_of_floors >= other
    def __add__(self, other):
        if isinstance(other, House):
            self.namber_of_floors += other.namber_of_floors
        elif isinstance(other, int):
            self.namber_of_floors += other
        return self
    def __iadd__(self, other):
        return self.__add__(other)
    def __radd__(self, other):
        return self.__add__(other)

    def __del__(self):
        print(f'{self.name} снесён, но останется в истории')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
