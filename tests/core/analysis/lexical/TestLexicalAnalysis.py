import unittest
from src.core.analysis.lexical.LexicalAnalysis import LexicalAnalysis
from src.core.analysis.lexical.Token import Token

class TestLexicalAnalysis(unittest.TestCase):
    def test_convert_tokens(self):
        sut = LexicalAnalysis('any_path')
        tokens = [["any_cmd", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", "any_value"]]
        sut.tokens = tokens
        sut.convert_tokens()
        self.assertEqual(sut.get_tokens()[0].directive, Token(tokens[0]).directive)
        self.assertEqual(sut.get_tokens()[0].original, Token(tokens[0]).original)
        self.assertEqual(sut.get_tokens()[0].start_line, Token(tokens[0]).start_line)
        self.assertEqual(sut.get_tokens()[0].end_line, Token(tokens[0]).end_line)
        self.assertEqual(sut.get_tokens()[0].value, Token(tokens[0]).value)

if __name__ == '__main__':
    unittest.main()