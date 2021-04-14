import string
from unittest import TestCase

from hypothesis import given, assume
from hypothesis.strategies import integers, SearchStrategy, composite, \
    text, deferred, just

from rgb.step10.rgb import RgbColor


def color_components() -> SearchStrategy[int]:
    return integers(min_value=0, max_value=255)


@composite
def colors(draw):
    return RgbColor(
        draw(color_components()),
        draw(color_components()),
        draw(color_components()))


# new strategies
@composite
def text_starting_with_hash(draw) -> SearchStrategy[str]:
    return draw(just("#")) + draw(text(min_size=0, max_size=20))


@composite
def text_starting_with_hash_with_len_7(draw) -> SearchStrategy[str]:
    return draw(just("#")) + draw(text(min_size=6, max_size=6))


def random_invalid_hex_triplet() -> SearchStrategy[str]:
    return deferred(lambda:
                    text()
                    | text_starting_with_hash()
                    | text_starting_with_hash_with_len_7())


@composite
def hex_triplet(draw) -> SearchStrategy[str]:
    return draw(just("#"))\
           + draw(text(alphabet=string.hexdigits, min_size=6, max_size=6))


class RgbStep10Tests(TestCase):
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

    @given(random_invalid_hex_triplet())
    def test_parsing_raises_value_error_on_wrong_input(
            self, parsing_input: str):
        print(f"{parsing_input}")

        # filtering out valid cases
        is_valid = (len(parsing_input) == 7 and parsing_input[0] == "#"
                    and _is_hex(parsing_input[1:]))
        assume(not is_valid)

        with self.assertRaises(ValueError):
            RgbColor.parse_hex_triplet(parsing_input)

    # new property
    @given(hex_triplet())
    def test_parsing_any_6_digit_hex_value_works(self, triplet: str):
        parsed_color = RgbColor.parse_hex_triplet(triplet)
        triplet_ = parsed_color.to_hex_triplet()
        self.assertEqual(triplet.lower(), triplet_.lower())


def _is_valid_component(value: int) -> bool:
    return 0 <= value <= 255


def _is_hex(value: str) -> bool:
    for char in value:
        if char not in string.hexdigits:
            return False

    return True
