import unittest
from typing import List

from hypothesis.stateful import RuleBasedStateMachine, rule, \
    precondition, invariant
from hypothesis.strategies import integers

from model_pst.circular_buffer import CircularBuffer

TEST_BUFFER_SIZE = 5


class CircularBufferTester(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.buffer = CircularBuffer(TEST_BUFFER_SIZE)
        self.model: List[int] = []

    @invariant()
    def count_is_never_negative(self):
        assert self.buffer.count >= 0

    @invariant()
    def count_never_exceeds_the_buffer_size(self):
        assert self.buffer.count <= TEST_BUFFER_SIZE

    @invariant()
    def items_are_same(self):
        are_same = self.model == self.buffer.items()

        if not are_same:
            print(f"expected={self.model}, actual_value={self.buffer.items()}")

        assert are_same

    @rule(value=integers())
    @precondition(lambda self: len(self.model) < TEST_BUFFER_SIZE)
    def push(self, value: int):
        self.buffer.push(value)
        self.model.append(value)

    @rule()
    @precondition(lambda self: len(self.model) > 0)
    def pop(self):
        expected_value = self.model.pop(0)
        actual_value = self.buffer.pop()

        assert expected_value == actual_value


CircularBufferTest = CircularBufferTester.TestCase

unittest.main()
