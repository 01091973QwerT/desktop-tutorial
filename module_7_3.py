import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем названия файлов в кортеже

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()  # Читаем содержимое и переводим в нижний регистр
                # Убираем пунктуацию
                for sym in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(sym,"")
                words = content.split()  # Разделяем строку на слова
                all_words[file_name] = words  # Записываем в словарь
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            if word.lower() in words:  # Поиск слова в нижнем регистре
                result[name] = words.index(word.lower()) + 1  # Возвращаем позицию (начиная с 1)
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            count = words.count(word.lower())  # Считаем количество слов
            if count > 0:
                result[name] = count  # Записываем только если количество больше 0
        return result

# Пример использования класса
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # Позиция слова по счёту
print(finder2.count('teXT'))  # Количество слова 'teXT' в тексте