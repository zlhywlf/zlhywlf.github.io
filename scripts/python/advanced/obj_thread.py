import threading
import time
from concurrent.futures import ThreadPoolExecutor


def test(func):
    print(f"==== {func.__doc__} ====")
    start = time.time()
    func()
    print(f"tasks done :{time.time() - start}")
    return lambda: None


def run(id_):
    print(f"task{id_}: start")
    time.sleep(1)
    print(f"task{id_}: end")


@test
def simple():
    """线程"""
    tasks01 = []

    for _ in range(2):
        task = threading.Thread(target=run, args=(_,))
        tasks01.append(task)
        task.start()

    for task in tasks01:
        task.join()


@test
def pool():
    """线程池"""
    with ThreadPoolExecutor(max_workers=2) as executor:
        # from concurrent.futures import wait
        # wait([executor.submit(run, _) for _ in range(2)])
        # from concurrent.futures import as_completed
        # list(as_completed([executor.submit(run, _) for _ in range(2)]))
        for _ in range(2):
            executor.submit(run, _)
