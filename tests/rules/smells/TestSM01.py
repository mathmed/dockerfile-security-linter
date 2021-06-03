import unittest
from src.core.rules.smells.SM01 import SM01
from src.core.rules.smells.lists.smells import smells
from src.core.analysis.lexical.Token import Token

class TestSM01(unittest.TestCase):

    def test_sm01_should_return_false(self):
        sut = SM01([Token("user", "any_original", "any_start", "any_end","any_value")])
        self.assertEqual(sut.validade(), False)

    def test_sm01_should_return_dict(self):
        sut = SM01([Token("user", "any_original", "any_start", "any_end", ["root"])])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM01"],
                    "code": "SM01"
                }
        self.assertEqual(sut.validade(), expected)

    def test_sm01_should_return_dict_on_no_user(self):
        sut = SM01([Token("any", "any_original", "any_start", "any_end", ["any"])])
        expected = {
                    "command": "Não utilização da diretiva USER", 
                    "start_line": "", 
                    "end_line": "", 
                    "security_smell": smells["SM01"],
                    "code": "SM01"
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()