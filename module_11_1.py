import numpy as np

# Создание массива
array = np.array([1, 2, 3, 4, 5])
print("Массив:", array)

# Математические операции
squared = array ** 2  # Квадрат каждого элемента
sum_array = np.sum(array)  # Сумма элементов массива
mean_value = np.mean(array)  # Среднее значение

# Вывод результатов
print("Квадраты элементов:", squared)
print("Сумма элементов массива:", sum_array)
print("Среднее значение массива:", mean_value)