from multiprocessing import Process, Lock
from pathlib import Path

from time import time
import requests


url = 'https://cataas.com/cat'
OUT_PATH = Path(__file__).parent / 'cats'
OUT_PATH.mkdir(exist_ok=True, parents=True)
OUT_PATH = OUT_PATH.absolute()


def query(lock: Lock, idx: int) -> None:
    response = requests.get(url, timeout=8)
    with lock:
        write_to_disk(response.content, idx)


def write_to_disk(content: bytes, id: int):
    file_path = "{}/{}.png".format(OUT_PATH, id)
    with open(file_path, mode='wb') as f:
        f.write(content)


def main() -> None:
    start_time = time()
    procs = []
    lock = Lock()

    for i in range(10):
        proc = Process(target=query, args=(lock, i))
        procs.append(proc)
        proc.start()

    for p in procs:
        p.join()
    print(round(time() - start_time, 2))


if __name__ == "__main__":
    main()

