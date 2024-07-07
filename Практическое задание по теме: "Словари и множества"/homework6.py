my_dict = {'Иван' : 1991, 'Петр' : 1823, 'Фатима' : 1933, 'Николай' : 1985}
print(my_dict)
print(my_dict['Фатима'])
print(my_dict.get('Елена'))
my_dict['Денис'] = 1978
my_dict['Руслан'] = 1979
remove_from_my_dict = my_dict.pop('Иван')
print(remove_from_my_dict)
print(my_dict)
my_set = {1, 2, 3, 1, 'Ivan', 2.5, 'Ivan', 3, True, (1,2,3)}
print(my_set)
my_set.add(4)
my_set.add((8,9))
my_set.remove('Ivan')
print(my_set)