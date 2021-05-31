import unittest
from src.core.rules.smells.SM03 import SM03
from src.core.rules.smells.helpers.smells import smells
from src.core.analysis.lexical.Token import Token
from src.core.analysis.lexical.shell.Token import Token as TokenShell

class TestSM03(unittest.TestCase):

    def test_sm03_should_return_false(self):
        sut = SM03(Token("env", "any_original", "any_start", "any_end", ["ANY_ENV", "any_env"]))
        self.assertEqual(sut.validade(), False)

    def test_sm03_should_return_dict(self):
        sut = SM03(Token("env", "any_original", "any_start", "any_end", ["ANY_PASS", "any_env"]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM03"]
                }
        self.assertEqual(sut.validade(), expected)

    def test_sm03_should_return_dict_on_shell_command(self):
        sut = SM03(Token("run", "any_original", "any_start", "any_end", [TokenShell("export", ["password='any'"])]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM03"]
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()