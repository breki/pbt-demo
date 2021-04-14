from unittest import TestCase

from hypothesis import given, assume
from hypothesis.strategies import integers, SearchStrategy, composite, \
    text

from rgb.step9.rgb import RgbColor


def color_components() -> SearchStrategy[int]:
    return integers(min_value=0, max_value=255)


@composite
def colors(draw):
    return RgbColor(
        draw(color_components()),
        draw(color_components()),
        draw(color_components()))


class RgbStep9Tests(TestCase):
    def test_hex_triplet_representation_is_correct(self):
        color = RgbColor(33, 52, 165)
        self.assertEqual("#2134a5", color.to_hex_triplet())

    @given(colors())
    def test_hex_triplet_is_7_characters_long(self, color: RgbColor):
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

    @given(colors())
    def test_parsing_hex_triplet_returns_same_color(
            self, color: RgbColor):
        triplet = color.to_hex_triplet()
        parsed_color = RgbColor.parse_hex_triplet(triplet)
        self.assertEqual(color, parsed_color)

    # problem: this property setup is not representative of all the ways
    # the parsing could fail
    @given(text())
    def test_parsing_raises_value_error_on_wrong_input(
            self, parsing_input: str):
        with self.assertRaises(ValueError):
            RgbColor.parse_hex_triplet(parsing_input)


def _is_valid_component(value: int) -> bool:
    return 0 <= value <= 255
