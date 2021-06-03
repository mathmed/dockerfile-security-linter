import unittest
from src.core.rules.smells.SM05 import SM05
from src.core.rules.smells.lists.smells import smells
from src.core.analysis.lexical.Token import Token

class TestSM05(unittest.TestCase):

    def test_sm05_should_return_false(self):
        sut = SM05(Token("any", "any_original", "any_start", "any_end", ["any"]))
        self.assertEqual(sut.validade(), False)

    def test_sm05_should_return_dict(self):
        sut = SM05(Token("comment", "any_original", "any_start", "any_end", "fix me"))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM05"],
                    "code": "SM05"
                }
        self.assertEqual(sut.validade(), expected)

if __name__ == '__main__':
    unittest.main()