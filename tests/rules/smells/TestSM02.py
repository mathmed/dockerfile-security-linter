import unittest
from src.core.rules.smells.SM02 import SM02
from src.core.rules.smells.smells import smells
from src.core.analysis.lexical.Token import Token

class TestSM02(unittest.TestCase):

    def test_sm02_should_return_false(self):
        sut = SM02(Token("env", "any_original", "any_start", "any_end", ["pass", "pass"]))
        self.assertEqual(sut.validade(), False)

    def test_sm02_should_return_dict(self):
        sut = SM02(Token("env", "any_original", "any_start", "any_end", ["pass", "''"]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM02"]
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()