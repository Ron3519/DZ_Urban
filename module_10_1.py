from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):

    file = open(file_name, 'a',encoding='utf-8')
    for i in range(1,word_count+1):
        file.write(f"Какое-то слово № {i}")
        sleep(0.1)
    file.close()

    print(f"Завершилась запись в файл {file_name}")

first_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.now()
print(end_time - first_time)


q = Thread(target=write_words,args=(10, 'example5.txt'))
w = Thread(target=write_words,args=(20, 'example6.txt'))
e = Thread(target=write_words,args=(200, 'example7.txt'))
r = Thread(target=write_words,args=(100, 'example8.txt'))



first_time = datetime.now()
q.start()
w.start()
e.start()
r.start()

q.join()
w.join()
e.join()
r.join()
end_time = datetime.now()
print(end_time - first_time)




