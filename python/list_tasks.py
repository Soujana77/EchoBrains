lst = [1, 2, 3, [22, 55], 4, 5]
normal_list = []
nested_list = []
for i in lst:
    if type(i) == list:
        nested_list = i
    else:
        normal_list.append(i)
print(normal_list)
print(nested_list)
