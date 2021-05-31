import unittest
from src.core.rules.smells.SM04 import SM04
from src.core.rules.smells.smells import smells
from src.core.analysis.lexical.Token import Token
from src.core.analysis.lexical.shell.Token import Token as TokenShell

class TestSM04(unittest.TestCase):

    def test_sm04_should_return_false(self):
        sut = SM04(Token("any", "any_original", "any_start", "any_end", ["any"]))
        self.assertEqual(sut.validade(), False)

    def test_sm04_should_return_dict(self):
        sut = SM04(Token("cmd", "any_original", "any_start", "any_end", ["0.0.0.0", "any_env"]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM04"]
                }
        self.assertEqual(sut.validade(), expected)

    def test_sm04_should_return_dict_on_shell_command(self):
        sut = SM04(Token("run", "any_original", "any_start", "any_end", [TokenShell("npm", ["start", "0.0.0.0"])]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM04"]
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()