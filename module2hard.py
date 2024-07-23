def append_to_list(item, list_my=None):
  if list_my is None:
    list_my = []
  list_my.append(item)
  return list_my

my_list = append_to_list(1)
print(my_list)  # Вывод: [1]

my_list = append_to_list(2, my_list)
print(my_list)  # Вывод: [1, 2]
