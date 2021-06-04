import unittest
from src.core.rules.smells.SM11 import SM11
from src.core.rules.smells.lists.smells import smells
from src.core.analysis.lexical.Token import Token
from src.core.analysis.lexical.shell.Token import Token as TokenShell


class TestSM11(unittest.TestCase):

    def test_sm11_should_return_false(self):
        sut = SM11([Token("any", "any_original", "any_start", "any_end", ["any"])])
        self.assertEqual(sut.validade(), False)

    def test_sm11_should_return_dict_on_run_command(self):
        sut = SM11([Token("run", "any_original", "any_start", "any_end",
         [
            TokenShell("wget", ["-o", "exec.sh", "http://any.com/test.sh"]), 
            TokenShell("sh", ["exec.sh"])
        ])
        ])
        
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM11"],
                    "code": "SM11"
                }
        self.assertEqual(sut.validade(), expected)

    def test_sm11_should_return_dict_on_run_command_directly_exec_file(self):
        sut = SM11([Token("run", "any_original", "any_start", "any_end",
         [
            TokenShell("wget", ["-o", "exec.sh", "http://any.com/test.sh"]), 
            TokenShell("./exec.sh", [])
        ])
        ])
        
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM11"],
                    "code": "SM11"
                }
        self.assertEqual(sut.validade(), expected)
        
if __name__ == '__main__':
    unittest.main()