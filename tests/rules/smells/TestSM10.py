import unittest
from src.core.rules.smells.SM10 import SM10
from src.core.rules.smells.lists.smells import smells
from src.core.analysis.lexical.Token import Token
from src.core.analysis.lexical.shell.Token import Token as TokenShell


class TestSM10(unittest.TestCase):

    def test_sm10_should_return_false(self):
        sut = SM10(Token("any", "any_original", "any_start", "any_end", ["any"]))
        self.assertEqual(sut.validade(), False)

    def test_sm10_should_return_dict_on_run_command(self):
        sut = SM10(Token("run", "any_original", "any_start", "any_end", [TokenShell("write", ["any"])]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM10"],
                    "code": "SM10"
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()