def is_prime(func):
    """
    Декоратор, который определяет, является ли результат функции простым числом.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, int(result**0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    return result
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    """
    Функция, которая складывает три числа.
    """
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
