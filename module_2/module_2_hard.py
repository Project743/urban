number = int(input('Введите заданое число (от 3 до 20): '))


def get_result(numder):
    result = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if (i + j) > number:
                break
            if number % (i + j) == 0:
                result += str(i) + str(j)
    return result


if number >= 3 and number <= 20:
    print(get_result(number))
else:
    print('Число выходит за указанные границы!')
