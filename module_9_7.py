def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        num_info = 'Простое'
        for i in range(2, result):
            if result % i == 0:
                num_info = 'Составное'
        print(num_info)
        return result
    return wrapper
@is_prime
def sum_three(x,y,z):
    return x + y + z

result = sum_three(2, 3, 6)
print(result)