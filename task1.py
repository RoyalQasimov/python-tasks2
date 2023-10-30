tuple1 = (1, 2, 3)
list_tuple = list(tuple1)
print(type(tuple1))

list_tuple.append(4)

new_tuple = tuple(list_tuple)
# print(type(list_tuple))
print(new_tuple)
