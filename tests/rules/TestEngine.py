import unittest
from unittest.mock import MagicMock
from src.core.analysis.lexical.Token import Token
from src.core.rules.Engine import Engine

class TestEngine(unittest.TestCase):
    
    def test_engine_should_return_valid_smells(self):
        sut = Engine([Token(["any_cmd", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", "any_value"])])
        sut.validade = MagicMock(return_value="any")
        self.assertEqual(sut.run(), ["any"])
        
if __name__ == '__main__':
    unittest.main()