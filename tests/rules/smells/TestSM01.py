import unittest
from src.core.rules.smells.SM01 import SM01
from src.core.rules.smells.smells import smells
from src.core.analysis.lexical.Token import Token

class TestSM01(unittest.TestCase):

    def test_sm01_should_return_false(self):
        sut = SM01(Token(["any_cmd", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", "any_value"]))
        self.assertEqual(sut.validade(), False)

    def test_sm01_should_return_dict(self):
        sut = SM01(Token(["user", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", ["root"]]))
        expected = {
                    "command": "user", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM01"]
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()