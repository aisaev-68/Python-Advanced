import threading
import time

sem = threading.Semaphore()


def fun1(ev):
    while not ev.is_set():
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(.25)
    print('Exit from function fun1')


def fun2(ev):
    while not ev.is_set():
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(.25)
    print('Exit from function fun2')


event = threading.Event()
t1 = threading.Thread(target=fun1, args=(event,))
t1.start()
t2 = threading.Thread(target=fun2, args=(event,))
t2.start()
while True:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        print('Ctrl-C!')
        event.set()
        break
print('exit')
