from unittest import TestCase
from hypothesis import given
from hypothesis.strategies import integers

from rgb.step3.rgb import RgbColor


class RgbStep3Tests(TestCase):
    def test_hex_triplet_representation_is_correct(self):
        color = RgbColor(33, 52, 165)
        self.assertEqual("#2134a5", color.to_hex_triplet())

    @given(integers(), integers(), integers())
    def test_hex_triplet_is_7_characters_long(
            self, r: int, g: int, b: int):
        color = RgbColor(r, g, b)
        triplet = color.to_hex_triplet()
        print(triplet)
        self.assertEqual(7, len(triplet))
