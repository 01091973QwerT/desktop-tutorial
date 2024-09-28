first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# First task
first_result = (abs(len(first_string) - len(second_string))
                 for first_string, second_string in zip(first, second)
                 if len(first_string) != len(second_string))

# Second task
second_result = (len(first[i]) == len(second[i])
                 for i in range(len(first)))

# Output
print(list(first_result))
print(list(second_result))