first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >= 5]
second_result = [(f_string, s_string) for f_string in first_strings for s_string in second_strings if
                 len(f_string) == len(s_string)]
third_result = {string: len(string) for string in first_strings + second_strings if not len(string) % 2}

if __name__ == '__main__':
    print(first_result)
    print(second_result)
    print(third_result)
