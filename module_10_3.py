from time import sleep
from random import randint
from threading import Thread, Lock

class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            plus = randint(50, 500)
            if self.balance >= 500 and Lock.locked():
                Lock.release()
            sleep(0.001)
            self.balanse += plus
            print(f"Пополнение: {plus}. Баланс: {self.balance}")


    def take(self):
        for i in range(100):
            minus = randint(50, 500)
            print(f"Запрос на {minus}")
            if self.balance - minus < 0:
                print("Запрос отклонён, недостаточно средств")
                Lock.acquire()
            else:
                sleep(0.001)
                self.balance - minus
                print(f"Снятие: {minus}. Баланс: {self.balance}")


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()


