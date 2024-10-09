import time
from multiprocessing import Pool

def read_info(name):
    """Считывает информацию из файла построчно."""
    all_data = []
    with open(name, "r", encoding="utf-8") as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()

if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

     #Линейный вызов
    start_time = time.time()
    for filename in filenames:
         read_info(filename)
    end_time = time.time()
    print(end_time - start_time)

    # Многопроцессный вызов
    # start_time = time.time()
    # with Pool(processes=4) as pool:
    #     pool.map(read_info, filenames)
    # end_time = time.time()
    # print(end_time - start_time)
