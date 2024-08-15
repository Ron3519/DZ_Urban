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








h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)