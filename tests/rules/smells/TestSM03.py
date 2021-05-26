import unittest
from src.core.rules.smells.SM03 import SM03
from src.core.rules.smells.smells import smells
from src.core.analysis.lexical.Token import Token

class TestSM03(unittest.TestCase):

    def test_sm02_should_return_false(self):
        sut = SM03(Token(["env", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", ["ANY_ENV", "pass"]]))
        self.assertEqual(sut.validade(), False)

    def test_sm02_should_return_dict(self):
        sut = SM03(Token(["env", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", ["pass", "'ANY_PASS'"]]))
        expected = {
                    "command": "env", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM03"]
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()