import unittest

import random

from time import sleep, time

from ..image_stats_calculator import ImageStatsCalculator


class ImageStatsCalculator_TestCase(unittest.TestCase):
    statParameter = ImageStatsCalculator(refresh_interval=1.0)

    def test_init(self):
        self.assertEqual(self.statParameter.get_average_value(), 0.)

    def test_elapsed_time(self):
        self.statParameter.reset()
        sleep(1.0)
        self.assertAlmostEqual(self.statParameter.elapsedTime(), 1.0,
                               delta=0.01)

    def test_reset(self):
        counts = 100
        for v in range(counts):
            self.statParameter.update(v)
        self.statParameter.reset()
        self.assertEqual(self.statParameter.get_average_value(), 0.)

    def test_avg_val(self):
        counts = 1000
        self.statParameter.reset()
        for _ in range(counts):
            sleep(1.0 / counts)
            self.statParameter.update(random.random())
        self.assertAlmostEqual(self.statParameter.get_average_value(), 0.5,
                               delta=0.05)

    def test_refresh(self):
        counts = 100
        self.statParameter.reset()
        for _ in range(counts):
            sleep(0.5 / counts)
            self.statParameter.update(random.random())
        val = self.statParameter.refresh()
        self.assertIsNone(val)

        for _ in range(counts):
            sleep(0.6 / counts)
            self.statParameter.update(random.random())
        val = self.statParameter.refresh()
        self.assertAlmostEqual(val, 0.5, delta=0.05)

    def test_time_average(self):
        val = 3
        counts = 100
        expected_total = val * counts
        self.statParameter.reset()

        t0 = time()
        for _ in range(counts):
            sleep(1.6 / counts)
            self.statParameter.update(val)
        t1 = time()
        time_avg_val = self.statParameter.refresh(True)
        self.assertAlmostEqual(time_avg_val, expected_total / (t1 - t0),
                               delta=0.05)


if __name__ == '__main__':
    unittest.main()
