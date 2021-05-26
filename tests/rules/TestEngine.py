import unittest
from unittest.mock import MagicMock
from src.core.analysis.lexical.Token import Token
from src.core.rules.Engine import Engine
from src.core.rules.smells.smells import smells


class TestEngine(unittest.TestCase):
    
    def test_engine_should_return_sm01_smell(self):
        sut = Engine([Token(["user", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", ["root"]])])
        expected = {
                    "command": "user", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM01"]
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm02_smell(self):
        sut = Engine([Token(["env", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", ["pass", "''"]])])
        expected = {
                    "command": "env", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM02"]
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm03_smell(self):
        sut = Engine([Token(["env", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", ["pass", "pass"]])])
        expected = {
                    "command": "env", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM03"]
                }
        self.assertEqual(sut.run(), [expected])
        
if __name__ == '__main__':
    unittest.main()