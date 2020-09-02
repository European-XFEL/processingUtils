from .rate_calculator import RateCalculator


class ImageStatsCalculator(RateCalculator):
    def update(self, value):
        self.counter += value
