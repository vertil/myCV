from threading import Thread
import time

alls = ['abc', 'cde']


def readandprint(ins: list):
    while True:
        time.sleep(1)
        print(len(alls))


thread = Thread(target=readandprint, args=(alls,))
thread.daemon = True
thread.start()

while True:
    time.sleep(5)
    alls.append('qwe')
