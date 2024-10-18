my_dict = {'Kate': 2001, 'Den': 1980}
print('Мой словарь:', my_dict)
print('Существующий ключ:', my_dict['Kate'])
print('Отсутствующий ключ:', my_dict.get('John'))
my_dict = {**my_dict, 'Nika': 1987, 'Max': 1977}
print('Дополненный словарь:', my_dict)
print('Удаленный ключ:', my_dict.pop('Kate'))
print('Словарь после удаления ключа:', my_dict)

# множества
print('Далее часть ДЗ про множества:')
my_set = {1, 1, 2, 'ava', 'ava', True, (1, 2, 3)}
print('Множество:', my_set)
my_set.add(5.45)
my_set.add('test')
my_set.discard(2)
print('Измененное множество: ', my_set)