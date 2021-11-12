import unittest

from ..moving_average import MovingAverage

AVG_N = 10

class ImageStatsCalculator_TestCase(unittest.TestCase):
    mov_avg = MovingAverage(AVG_N)

    def test_moving_avg(self):
        i = 0
        sum = 0
        while True:
            i += 1
            if i < AVG_N:
                sum += i
                val, n = self.mov_avg(i)
                self.assertEqual(val, sum / i)
                self.assertEqual(n, i)
            elif i <= AVG_N + 10:
                # add i to the sum and subtract (i - AVG_N)
                # i.e. sum + i - (i - AVG_N)
                sum = sum + AVG_N

                val, n = self.mov_avg(i)
                self.assertEqual(val, sum / AVG_N)
                self.assertEqual(n, 10)
            else:
                break

if __name__ == '__main__':
    unittest.main()
