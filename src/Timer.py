import time


class Timer:
    def __init__(self):
        self.start = time.time()

    def restart(self):
        self.start = time.time()

    def get_time_s(self):
        end = time.time()
        s = end - self.start
        time_str = "%02d" % s
        return time_str
