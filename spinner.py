import threading
import time
import itertools
import sys


class Spinner(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()
        self.join()

    def run(self):
        spinner = itertools.cycle(['|', '/', '-', '\\'])
        while not self._stop_event.is_set():
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
