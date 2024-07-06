immutable_var =  (1, 2, 3, 'Hello', True, 'World', False)
print('immutable_var' , type(immutable_var ), ':', immutable_var)
# immutable_var[2] = 5 Программа выдает ошибку так как Коттедж ботносится к низменяемуму типу лаееыъ
immutable_list = [1, 2, 3, 'Hello', True, 'World', False]
immutable_list[0] = 13
immutable_list[5] = 'MAXIM'
print('immutable_list' , type(immutable_list), ':', immutable_list)
