

class House:
    houses_history = []


    def go_to(self, new_floor):
        for i in range(1, new_floor+1):
            if self.number_of_floors < i or i < 0:
                print("Такого этажа не существует")
                break
            print(i)


    def __new__(cls, name, number_of_floors ):
        if name != 'houses_history':
            House.houses_history.append(name)
        
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        if name == 'houses_history':
            self.list = []
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
        del self

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        str_ = "Название: "+ str(self.name) + ", кол-во этажей: "+ str(self.number_of_floors)
        return str_

    def __eq__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self


houses_history = House('houses_history',None)










h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3