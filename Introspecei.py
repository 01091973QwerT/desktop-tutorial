def introspection_info(obj):
    """
    Функция для подробной интроспекции объекта.

    Args:
        obj: Объект для интроспекции.

    Returns:
        Словарь с информацией об объекте, включая его тип, атрибуты, методы, модуль и другие свойства.
    """

    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    # Получение модуля, к которому объект принадлежит
    try:
        info['module'] = obj.__module__
    except AttributeError:
        info['module'] = 'unknown'

    # Дополнительная информация в зависимости от типа объекта
    if isinstance(obj, str):
        info['length'] = len(obj)
    elif isinstance(obj, list):
        info['length'] = len(obj)
    elif isinstance(obj, dict):
        info['length'] = len(obj)

    return info

# Пример использования
number_info = introspection_info(42)
print(number_info)

# Пример использования для объекта класса
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

my_object = MyClass("Alice")
object_info = introspection_info(my_object)
print(object_info)