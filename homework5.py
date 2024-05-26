immutable_var = (99,True,'Night',1.0)
print(immutable_var)
#immutable_var[0]= 100
#TypeError: 'tuple' object does not support item assignment
mutable_list = (1, [2 , 3])
mutable_list[1][1] = 6
print(mutable_list)