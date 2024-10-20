from _datetime import datetime
import multiprocessing
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            i = file.readline()
            all_data.append(i)
            if not i:
                break









filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
'''x = datetime.now()
for i in filenames:
    read_info(i)
y = datetime.now()
'''
# Многопроцессный
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4):
        x = datetime.now()
        for i in filenames:
            read_info(i)
        y = datetime.now()
        print(y - x)

