from dataclasses import dataclass


@dataclass(frozen=True)
class RgbColor:
    r: int
    g: int
    b: int

    def __post_init__(self) -> None:
        self._assert_8_bit(self.r)
        self._assert_8_bit(self.g)
        self._assert_8_bit(self.b)

    def to_hex_triplet(self) -> str:
        return f"#{self._hex(self.r)}{self._hex(self.g)}{self._hex(self.b)}"

    @staticmethod
    def _assert_8_bit(value: int):
        if value < 0 or value > 255:
            raise ValueError()

    @staticmethod
    def _hex(value: int) -> str:
        return "{:02x}".format(value)

    @classmethod
    def parse_hex_triplet(cls, triplet: str) -> "RgbColor":
        if len(triplet) != 7:
            raise ValueError()

        if triplet[0] != "#":
            raise ValueError()

        triplet_hex_value = triplet[1:]
        triplet_int_value = int(triplet_hex_value, 16)
        b = triplet_int_value & 0xff
        triplet_int_value >>= 8
        g = triplet_int_value & 0xff
        triplet_int_value >>= 8
        r = triplet_int_value & 0xff
        return RgbColor(r, g, b)
