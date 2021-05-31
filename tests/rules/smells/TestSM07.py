import unittest
from src.core.rules.smells.SM07 import SM07
from src.core.rules.smells.smells import smells
from src.core.analysis.lexical.Token import Token
from src.core.analysis.lexical.modules.shell.Token import Token as TokenShell

class TestSM07(unittest.TestCase):

    def test_sm07_should_return_false(self):
        sut = SM07(Token("any", "any_original", "any_start", "any_end", ["any"]))
        self.assertEqual(sut.validade(), False)

    def test_sm07_should_return_dict_on_shell_command(self):
        sut = SM07(Token("run", "any_original", "any_start", "any_end", [TokenShell("usermod", ["(mkpasswd -H md5)"])]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM07"]
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()