class House:
    def go_to(self, new_floor):
        for i in range(1, new_floor+1):
            if self.number_of_floors < i or i < 0:
                print("Такого этажа не существует")
                break
            print(i)



    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        str_ = "Название: "+ str(self.name) + ", кол-во этажей: "+ str(self.number_of_floors)
        return str_


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))


