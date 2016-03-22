import unittest
from expects import *
from evaluator import Evaluator


class TestMultilineEval(unittest.TestCase):
    def test_executes_preceding_lines_and_evaluates_last_line(self):
        src = """
a=1
b=2
a
"""
        e = Evaluator()

        expect(e.evaluate(src)).to(equal(1))

    def test_returns_nothing_when_last_line_is_not_expression(self):
        src = """
a=1
b=2
"""
        e = Evaluator()

        expect(e.evaluate(src)).to(equal(None))
        expect(e.evaluate('a')).to(equal(1))
        expect(e.evaluate('b')).to(equal(2))

    def test_does_not_pollute_local_namespace(self):
        e = Evaluator()
        e.evaluate('a=1')

        with self.assertRaises(NameError):
            a
