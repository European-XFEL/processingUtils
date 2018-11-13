import time


class RateCalculator:
    """Class to easily calculate (e.g.) frame rate"""
    def __init__(self, type='input', refresh_interval=1.0):
        self.counter = 0
        self.lastTime = time.time()
        self.type = type
        self.refresh_interval = refresh_interval

    def update(self):
        """Adds one to the counter"""
        self.counter += 1

    def elapsedTime(self):
        """Returns elapsed time"""
        return time.time() - self.lastTime

    def reset(self):
        """Resets counter and elapsed time"""
        self.counter = 0
        self.lastTime = time.time()

    def rate(self):
        """Returns frame rate"""
        if self.counter > 0:
            return self.counter / self.elapsedTime()
        else:
            return 0.

    def refresh(self):
        """If refresh interval has elapsed, it returns the frame rate and
        resets counter and elapsed time. Otherwise, it returns None"""
        fps = None
        if self.elapsedTime() >= self.refresh_interval:
            fps = self.rate()
            self.reset()
        return fps
