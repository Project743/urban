def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        bool_1 = [x for x in range(2, int(res ** 0.5) + 1) if res % x == 0]
        if bool_1:
            print('Составное')
        else:
            print('Простое')

        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)
