my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
iter = 0

while i >= 0:

    i = my_list[iter]
    if i > 0:
        print(i)

    iter += 1
    if iter == len(my_list):
        break
