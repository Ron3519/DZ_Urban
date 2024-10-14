from time import sleep
import queue
from threading import Thread
from random import randint
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            check = False
            for i in self.tables:

                if i.guest == None:
                    i.guest = guest
                    print(f"{guest.name} сел(-а) за стол номер {i.number}")
                    check = True
                    break

            if check == False:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        check = 0
        while check < len(self.tables) and self.queue.empty() == False:
            check = 0
            for i in self.tables:

                if i.guest == None:
                    check += 1

                elif i.guest.is_alive() == False:
                    print(f"{i.guest.name} покушал(-а) и ушёл(ушла)")
                    i.guest = None
                    print(f"Стол номер {i.number} свободен")
                    check += 1

                if i.guest == None and self.queue.empty() == False:
                    check -= 1
                    i.guest = self.queue.get()
                    print(f"{i.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i.number}")
                    i.guest.start()




# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()










