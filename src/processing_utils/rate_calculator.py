from .image_stats_calculator import ImageStatsCalculator


class RateCalculator(ImageStatsCalculator):
    """Class to easily calculate (e.g.) frame rate"""

    def update(self):
        """Increments counter"""
        self.counter += 1

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
