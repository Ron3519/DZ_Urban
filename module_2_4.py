numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
chek = True
for i in numbers:
    for j in range(1,i):
        if j == 1 or j == i:
            continue 
        elif i % j == 0:
            chek = False
            break
    if chek == True:
         primes.append(i)
    elif chek == False:
         not_primes.append(i)
    chek = True
print(primes)
print(not_primes)