from collections import deque


class MovingAverage():
    """
    Utility for moving average calculation.
    Example of usage for moving average on N values

    Construction:
        mov_avg = MovingAverage(N)

    Feeding a value:
        avg, n_of_vals = mov_avg(a_value)

           avg is the current average value,
           n_of_vals is the number of values it is calculated on
    """

    def __init__(self, windowSize):
        self.windowSize = windowSize
        self.window = deque(maxlen=int(windowSize))
        self.avg = 0

    def __call__(self, value):
        if value is not None:
            self.window.append(value)
            n_of_vals = len(self.window)
            self.avg = sum(self.window) / n_of_vals
            return self.avg, n_of_vals
