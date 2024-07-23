def print_params(a=1, b='строка', c=True):

  print(f"a: {a}")
  print(f"b: {b}")
  print(f"c: {c}")

values_list_2 = [5, 'новая строка']


print_params(*values_list_2, 42)