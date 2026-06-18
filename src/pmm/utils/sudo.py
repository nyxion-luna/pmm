import subprocess
import threading


stop = threading.Event()


def keepsudo():
    while not stop.is_set():
        subprocess.run(['sudo', '-v'], stdout=subprocess.DEVNULL)
        stop.wait(150)
