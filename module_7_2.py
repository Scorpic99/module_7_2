def custom_write(file_name, strings):
    my_file = open(file_name, 'w', encoding='utf-8')
    my_dict = {}
    for i in range(len(strings)):
        my_file.write(strings[i])
        for_convert = my_file.tell()
        start_str_byte = int.to_bytes(for_convert)
        start_str_byte = start_str_byte.decode()
        my_file.seek(0, 2)
        my_file.write('\n')
        #my_file.seek(0, 2)
        my_dict.update(dict({(i + 1, start_str_byte):strings[i]}))
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