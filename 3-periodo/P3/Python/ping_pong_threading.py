import time
import threading as th


def print_threading(delay: float, resp: str):
    while True:
        print(resp)
        time.sleep(delay)


th1 = th.Thread(target=print_threading, args=(1, 'ping')).start()
th2 = th.Thread(target=print_threading, args=(2, 'pong')).start()
th3 = th.Thread(target=print_threading, args=(5, 'intervalo')).start()
