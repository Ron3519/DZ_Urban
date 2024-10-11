
def custom_write(file_name, strings):
    iters = 0
    text = open(file_name, 'a', encoding='utf-8')
    result = {}
    for i in strings:
        t = text.tell()
        iters += 1
        text.write(i + '\n')
        result[(iters, t)] = i
    return result




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)