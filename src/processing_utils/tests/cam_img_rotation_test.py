import unittest

from ..camera_image_rotation import rotate_coordinates_on_ccd, rotate_roi


class CameraImageRotation_TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.CCD_WIDTH = 10
        cls.CCD_HEIGHT = 8

    def test_rotate_coordinates(self):
        triangle = [
            (1, 1),
            (1, 5),
            (3, 5)
        ]

        triangle_90 = [
            (1, 9),
            (5, 9),
            (5, 7)
        ]

        triangle_180 = [
            (9, 7),
            (9, 3),
            (7, 3)
        ]

        triangle_270 = [
            (7, 1),
            (3, 1),
            (3, 3)
        ]

        for rotation, expected in [(90, triangle_90),
                                   (180, triangle_180),
                                   (270, triangle_270)]:
            output_triangle = []
            for x_in, y_in in triangle:
                output_triangle.append(
                    rotate_coordinates_on_ccd(x_in, y_in, rotation,
                                              self.CCD_WIDTH, self.CCD_HEIGHT))
            self.assertEqual(output_triangle, expected)
            
    def test_rotate_roi(self):
        roi = {'x': 2, 'y': 1, 'width': 5, 'height': 4}
        roi_90 = {'x': 1, 'y': 3, 'width': 4, 'height': 5}
        roi_180 = {'x': 3, 'y': 3, 'width': 5, 'height': 4}
        roi_270 = {'x': 3, 'y': 2, 'width': 4, 'height': 5}
        
        for rotation, expected in [(90, roi_90),
                                   (180, roi_180),
                                   (270, roi_270)]:
            res_x, res_y, res_width, res_height = \
                rotate_roi(roi['x'], roi['y'], roi['width'], roi['height'], 
                           rotation, self.CCD_WIDTH, self.CCD_HEIGHT)
            self.assertEqual(res_x, expected['x'])
            self.assertEqual(res_y, expected['y'])
            self.assertEqual(res_width, expected['width'])
            self.assertEqual(res_height, expected['height'])


if __name__ == '__main__':
    unittest.main()
