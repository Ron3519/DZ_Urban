def save_program(boss_num):
    numbers = []
    final = ''
    for i in range(2, boss_num + 1):
        if boss_num % i == 0:
            numbers.append(i)
    
    for i in numbers:
        x = 1
        if i % 2 == 0:
            x = 0
        for j in range(1, i // 2 + x):
            final += str(j) + str(i - j) + '  '

    return final

print(save_program(10))






