import  fake_math
import true_math
from fake_math import divide as fake_divide
from true_math import divide as true_divide

first_number = 10
second_number = 0

fake_result = fake_divide(first_number, second_number)
true_result = true_divide(first_number, second_number)

print(f"Результат деления в fake_math: {fake_result}")
print(f"Результат деления в true_math: {true_result}")