import signal
import subprocess

DEVNULL = subprocess.DEVNULL


def run(cmd: list, **kwargs):
    result = subprocess.run(cmd, **kwargs)

    if result.returncode == -signal.SIGINT:
        raise KeyboardInterrupt

    return result
