import unittest
from src.core.rules.smells.SM08 import SM08
from src.core.rules.smells.lists.smells import smells
from src.core.analysis.lexical.Token import Token
from src.core.analysis.lexical.shell.Token import Token as TokenShell

class TestSM08(unittest.TestCase):

    def test_sm08_should_return_false(self):
        sut = SM08(Token("any", "any_original", "any_start", "any_end", ["any"]))
        self.assertEqual(sut.validade(), False)

    def test_sm08_should_return_dict_on_shell_command(self):
        sut = SM08(Token("run", "any_original", "any_start", "any_end", [TokenShell("chmod", ["-r", "777", "/"])]))
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM08"],
                    "code": "SM08"
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()