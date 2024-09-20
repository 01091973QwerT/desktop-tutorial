def add_everything_up(a, b):
    """
    Складывает числа (int, float) и строки (str).
    Если типы a и b разные, возвращает строковое представление a и b.
    """
    if type(a) != type(b):
        return str(a) + str(b)
    else:
        return a + b

print(add_everything_up(123.456, 'строка')) # 123.456строка
print(add_everything_up('яблоко', 4215)) # яблоко4215
print(add_everything_up(123.456, 7)) # 130.456