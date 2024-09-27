number = int(input('Введите заданое число (от 3 до 20): '))


def get_result(num):
    result = ''
    for i in range(1, num):
        for j in range(i + 1, num):
            if (i + j) > num:
                break
            if num % (i + j) == 0:
                result += str(i) + str(j)
    return result


if 3 <= number <= 20:
    print(get_result(number))
else:
    print('Число выходит за указанные границы!')
