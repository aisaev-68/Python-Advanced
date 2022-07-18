import time
import threading

import requests

endpoints = 'connection'


def run():
    while True:
        try:
            requests.get("http://app:5000/%s" % endpoints, timeout=1)

        except:
            pass


if __name__ == '__main__':
    for _ in range(4):
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

    while True:
        time.sleep(1)