from dataclasses import dataclass


@dataclass(frozen=True)
class RgbColor:
    r: int
    g: int
    b: int

    def to_hex_triplet(self) -> str:
        return f"#{self._hex(self.r)}{self._hex(self.g)}{self._hex(self.b)}"

    @staticmethod
    def _hex(value: int) -> str:
        return format(value, "x")
