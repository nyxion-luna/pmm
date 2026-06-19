import threading
from pmm.utils.process import *


stop = threading.Event()


def keepsudo():
    while not stop.is_set():
        run(['sudo', '-v'], stdout=DEVNULL)
        stop.wait(150)
