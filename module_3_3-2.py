def print_params(a=1, b='строка', c=True):
  """Функция, печатающая переданные параметры."""
  print(f"a: {a}")
  print(f"b: {b}")
  print(f"c: {c}")

values_list = [10, 'новая строка', False]
values_dict = {'a': 20, 'b': 'еще одна строка', 'c': True}

# Распаковка параметров из списка
print_params(*values_list)

# Распаковка параметров из словаря
print_params(*values_dict)