def calculate_structure_sum(data_structure):
  """
  Рекурсивная функция для подсчета суммы чисел и длин строк в вложенных структурах данных.

  Args:
    data_structure: Вложенная структура данных, содержащая числа и строки.

  Returns:
    Сумма всех чисел и длин строк в структуре.
  """
  total_sum = 0
  for item in data_structure:
    if isinstance(item, (int, float)):
      total_sum += item
    elif isinstance(item, str):
      total_sum += len(item)
    elif isinstance(item, (list, tuple, dict, set)):
      total_sum += calculate_structure_sum(item)
    elif isinstance(item, tuple):
      for i in item:
        if isinstance(i, (int, float)):
          total_sum += i
        elif isinstance(i, str):
          total_sum += len(i)
        elif isinstance(i, (list, tuple, dict, set)):
          total_sum += calculate_structure_sum(i)
  return total_sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)