def custom_write(file_name, strings):
    striping_positions = {}
    n_str = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        n_str += 1
        striping_positions[(n_str,file.tell())] = string

        file.write(f'{string}\n')
    file.close()
    return striping_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
