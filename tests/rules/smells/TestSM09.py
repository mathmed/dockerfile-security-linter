import unittest
from src.core.rules.smells.SM09 import SM09
from src.core.rules.smells.lists.smells import smells
from src.core.analysis.lexical.Token import Token

class TestSM09(unittest.TestCase):

    def test_sm09_should_return_false(self):
        sut = SM09(Token("any", "any_original", "any_start", "any_end", ["any"]))
        self.assertEqual(sut.validade(), False)

    def test_sm09_should_return_dict_on_shell_command(self):
        sut = SM09(Token("from", "any_original", "any_start", "any_end", ["any:any"]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM09"],
                    "code": "SM09"
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()