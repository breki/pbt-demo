from typing import List


# class CircularBuffer:
#     def __init__(self, buffer_size: int) -> None:
#         self.buffer_size = buffer_size
#         self._buffer: List[int] = []
#         self._start_index = 0
#         self._count = 0
#
#     def push(self, value):
#         self._buffer[self._start_index + self._count] = value
#         self._count += 1


# class CircularBuffer:
#     def __init__(self, buffer_size: int) -> None:
#         self.buffer_size = buffer_size
#         # initialized the array
#         self._buffer: List[int] = [0] * buffer_size
#         self._start_index = 0
#         self._count = 0
#
#     def push(self, value):
#         self._buffer[self._start_index + self._count] = value
#         self._count += 1


class CircularBuffer:
    def __init__(self, buffer_size: int) -> None:
        self.buffer_size = buffer_size
        self._buffer: List[int] = [0] * buffer_size
        self._start_index = 0
        self.count = 0

    def push(self, value: int) -> None:
        index = (self._start_index + self.count) % self.buffer_size
        self._buffer[index] = value
        self.count += 1

    def pop(self) -> int:
        value = self._buffer[self._start_index]
        self._start_index += 1

        if self._start_index == self.buffer_size:
            self._start_index = 0

        self.count -= 1
        return value

    def items(self) -> List[int]:
        if self.count == 0:
            return []

        end_index = self._start_index + self.count

        if end_index <= self.buffer_size:
            return self._buffer[self._start_index:end_index]
        else:
            first_part_end_index = min(end_index, self.buffer_size)

            first_part \
                = self._buffer[self._start_index:first_part_end_index]
            first_part_len = len(first_part)
            second_part = self._buffer[0:self.count-first_part_len]
            return first_part+second_part
