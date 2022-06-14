import json
import logging
import threading
import time
import requests

logging.basicConfig(filename='date.log', filemode='w', level=logging.INFO)
logger = logging.getLogger(__name__)


def query(lock) -> None:
    start = time.time()
    while int(time.time() - start) <= 20:
        url = f'https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp={int(time.time())}'
        thread_name = threading.current_thread().name
        response = requests.get(url, timeout=5)
        data = json.loads(response.content)
        with lock:
            logger.info(f'{thread_name} - {data}')
            print(f'{thread_name} - {data}')


def main_threading() -> None:
    threads = []
    lock = threading.Lock()

    for i in range(10):
        thread = threading.Thread(target=query, args=(lock,))
        threads.append(thread)
        thread.start()
        time.sleep(1)


if __name__ == "__main__":
    main_threading()
