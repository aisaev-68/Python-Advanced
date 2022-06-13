import json
import logging
import threading
import time
import requests


logging.basicConfig(filename='date.log', filemode='w', level=logging.INFO)
logger = logging.getLogger(__name__)


def query(numb: int, lock: threading.Lock) -> None:
    url = f'https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp={int(time.time())}'


    with lock:
        threadName = threading.current_thread().name
        start = time.time()
        while int(time.time() - start) <= 20:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = json.loads(response.content)
                # print(data)
                logger.info(f'{threadName} - {data}')
            else:
                logger.info(f'{threadName} - {data} {response.status_code}')


def main_threading() -> None:
    threads = []
    lock = threading.Lock()
    for i in range(10):
        thread = threading.Thread(target=query, args=(i, lock))
        threads.append(thread)
        thread.start()
        time.sleep(1)
    for t in threads:
        t.join()

    logger.info('Done')


if __name__ == "__main__":
    main_threading()


