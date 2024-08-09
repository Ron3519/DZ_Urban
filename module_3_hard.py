data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

def master_score(list_):
    final = 0
    for items in list_:

        if type(items) == int:
            final += items
        elif type(items) == str:
            final += len(items)
        elif isinstance(items, (list ,tuple,set)) == True:
            final += master_score(items)
        elif isinstance(items, dict) == True:
            list_in = list(items.items())
            final += master_score(list_in)
        elif isinstance(items, ) == True:
            list_in = list(items.items())
            final += master_score(list_in)
        
    return final

print(master_score(data_structure))





















