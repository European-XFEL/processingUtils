import time

class ImageStatsCalculator:
    """
    Utility to calculate average of any image related parameter, and throttle
    its refresh to the desired interval
    """
    def __init__(self, type='input', refresh_interval=1.0):
        self.sum_value = 0
        self.counter = 0
        self.lastTime = time.time()
        self.type = type
        self.refresh_interval = refresh_interval

    def update(self, value):
        """Adds :value: to the sum_value"""
        self.sum_value += value
        self.counter += 1

    def elapsedTime(self):
        """Returns elapsed time"""
        return time.time() - self.lastTime

    def reset(self):
        """Resets sum_value, counter and elapsed time"""
        self.sum_value = 0
        self.counter = 0
        self.lastTime = time.time()

    def get_average_value(self):
        if self.sum_value > 0:
            return self.sum_value / self.counter
        else:
            return 0.

    def refresh(self):
        """If refresh interval has elapsed, it resets sum_value and elapsed
        time, and returns the averaged value. Otherwise, it returns None"""
        val = None
        if self.elapsedTime() >= self.refresh_interval:
            val = self.get_average_value()
            self.reset()
        return val
