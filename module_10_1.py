import time
from time import sleep
from threading import Thread

def write_words(word_count, file_name):
    """
    Записывает слова в файл с задержкой после каждого слова.

    Args:
        word_count (int): Количество слов для записи.
        file_name (str): Имя файла для записи.
    """
    with open(file_name, "w") as file:
        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}\n"
            file.write(word)
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

if __name__ == "__main__":
    start_time = time.time()

    # Запись в файлы с помощью функций
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")

    end_time = time.time()
    print(f"Работа функций {time.strftime('%H:%M:%S.%f', time.gmtime(end_time - start_time))}")

    start_time = time.time()

    # Создание и запуск потоков
    threads = [
        Thread(target=write_words, args=(10, "example5.txt")),
        Thread(target=write_words, args=(30, "example6.txt")),
        Thread(target=write_words, args=(200, "example7.txt")),
        Thread(target=write_words, args=(100, "example8.txt")),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Работа потоков {time.strftime('%H:%M:%S.%f', time.gmtime(end_time - start_time))}")