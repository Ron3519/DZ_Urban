from time import sleep
from random import randint
from threading import Thread, Lock

class Bank:
    balanse = 0
    def __init__(self):
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            plus = randint(50, 500)
            if self.balanse >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)
            self.balanse += plus
            print(f"Пополнение: {plus}. Баланс: {self.balanse}")


    def take(self):
        for i in range(100):
            minus = randint(50, 500)
            print(f"Запрос на {minus}")
            if self.balanse - minus < 0:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            else:
                sleep(0.001)
                self.balanse -= minus
                print(f"Снятие: {minus}. Баланс: {self.balanse}")


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
