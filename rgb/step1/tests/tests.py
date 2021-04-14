from unittest import TestCase

from rgb.step1.rgb import RgbColor


class RgbStep1Tests(TestCase):
    def test_hex_triplet_representation_is_correct(self):
        color = RgbColor(33, 52, 165)
        self.assertEqual("#2134a5", color.to_hex_triplet())
