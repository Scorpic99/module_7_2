def custom_write(file_name, strings):
    my_file = open(file_name, 'w+', encoding='utf-8')
    my_dict = {}
    for i in range(len(strings)):
        cursor_pos = my_file.tell()
        my_file.write(strings[i] + '\n')
        my_file.seek(0, 2)
        my_dict.update(dict({(i + 1, cursor_pos):strings[i]}))
    my_file.close()
    return my_dict

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
