from .rate_calculator import RateCalculator


class ImageStatsCalculator(RateCalculator):
    """
    Utility to calculate average of any image related parameter, and throttle
    its refresh to the desired interval
    """
    def update(self, value):
        self.counter += value
