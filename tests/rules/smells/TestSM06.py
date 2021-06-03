import unittest
from src.core.rules.smells.SM06 import SM06
from src.core.rules.smells.lists.smells import smells
from src.core.analysis.lexical.Token import Token
from src.core.analysis.lexical.shell.Token import Token as TokenShell

class TestSM06(unittest.TestCase):

    def test_sm06_should_return_false(self):
        sut = SM06(Token("any", "any_original", "any_start", "any_end", ["any"]))
        self.assertEqual(sut.validade(), False)

    def test_sm06_should_return_dict(self):
        sut = SM06(Token("cmd", "any_original", "any_start", "any_end", ["http://127.0.0.1", "any_env"]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM06"],
                    "code": "SM06"

                }
        self.assertEqual(sut.validade(), expected)

    def test_sm06_should_return_dict_on_env_directive(self):
        sut = SM06(Token("env", "any_original", "any_start", "any_end", [["any_host", "http://aa.com"]]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM06"],
                    "code": "SM06"
                }
        self.assertEqual(sut.validade(), expected)

    def test_sm06_should_return_dict_on_shell_command(self):
        sut = SM06(Token("run", "any_original", "any_start", "any_end", [TokenShell("npm", ["start", "http://127.0.0.0"])]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM06"],
                    "code": "SM06"
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()