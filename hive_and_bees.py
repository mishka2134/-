import time
import random
import multiprocessing

def collect_nectar(bee_id):
    time_to_collect = random.uniform(1, 3)
    time.sleep(time_to_collect)
    print(f"Пчела {bee_id} собрала нектар за {time_to_collect:.2f} секунд.")

def build_combs(bee_id):
    time_to_build = random.uniform(1, 2)
    time.sleep(time_to_build)
    print(f"Пчела {bee_id} построила соты за {time_to_build:.2f} секунд.")

def hive(hive_id, num_bees):
    print(f"Улей {hive_id} начал свою работу.")
    processes = []
    for bee_id in range(1, num_bees + 1):
        task = random.choice([collect_nectar, build_combs])
        process = multiprocessing.Process(target=task, args=(bee_id,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    print(f"Улей {hive_id} завершил свою работу.")

def multiple_hives(num_hives, bees_per_hive):
    processes = []
    for hive_id in range(1, num_hives + 1):
        process = multiprocessing.Process(target=hive, args=(hive_id, bees_per_hive))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

if __name__ == "__main__":
    num_hives = 3
    bees_per_hive = 5
    print("Запуск симуляции работы пчел в улье...")
    start_time = time.time()
    multiple_hives(num_hives, bees_per_hive)
    end_time = time.time()
    print(f"Симуляция завершена. Время работы: {end_time - start_time:.2f} секунд.")



