from dataclasses import dataclass


@dataclass(frozen=True)
class RgbColor:
    r: int
    g: int
    b: int

    def to_hex_triplet(self) -> str:
        return f"#{self._hex(self.r)}{self._hex(self.g)}{self._hex(self.b)}"

    @staticmethod
    def from_hex_triplet(hex_triplet: str) -> "RgbColor":
        # todo igor: implement this
        raise NotImplementedError("todo igor")

    @staticmethod
    def _hex(value: int) -> str:
        return format(value, "x")
