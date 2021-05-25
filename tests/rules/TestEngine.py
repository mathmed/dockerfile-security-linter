import unittest
from unittest.mock import MagicMock
from src.core.analysis.lexical.Token import Token
from src.core.rules.Engine import Engine
from src.core.rules.smells.smells import smells


class TestEngine(unittest.TestCase):
    
    def test_engine_should_return_valid_smells(self):
        sut = Engine([Token(["user", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", ["root"]])])
        expected = {
                    "command": "user", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM01"]
                }
        self.assertEqual(sut.run(), [expected])
        
if __name__ == '__main__':
    unittest.main()