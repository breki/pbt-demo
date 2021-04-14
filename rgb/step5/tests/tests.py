from unittest import TestCase
from hypothesis import given, assume
from hypothesis.strategies import integers

from rgb.step5.rgb import RgbColor


def color_components():
    return integers(min_value=0, max_value=255)


class RgbStep5Tests(TestCase):
    def test_hex_triplet_representation_is_correct(self):
        color = RgbColor(33, 52, 165)
        self.assertEqual("#2134a5", color.to_hex_triplet())

    @given(color_components(), color_components(), color_components())
    def test_hex_triplet_is_7_characters_long(
            self, r: int, g: int, b: int):
        color = RgbColor(r, g, b)
        triplet = color.to_hex_triplet()
        self.assertEqual(7, len(triplet))

    @given(integers(), integers(), integers())
    def test_constructor_raises_value_error_on_invalid_component(
            self, r: int, g: int, b: int):
        assume(not _is_valid_component(r)
               or not _is_valid_component(g)
               or not _is_valid_component(b))

        with self.assertRaises(ValueError):
            RgbColor(r, g, b)


def _is_valid_component(value: int) -> bool:
    return 0 <= value <= 255
