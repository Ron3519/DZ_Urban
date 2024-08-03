def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params('E = mc^2',0, False)
print_params('IDDQD',c = 'DOOM')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['int',3.14,True]
values_dict = {'a': 10, 'b': False, 'c': 'king'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['pelmeny',True]
print_params(*values_list_2, 42)