import unittest
from src.core.analysis.lexical.natural.NaturalAnalysis import NaturalAnalysis

class TestNaturalAnalysis(unittest.TestCase):
    def test_parse_tokens(self):
        sut = NaturalAnalysis("# any comment")
        result = sut.parse()

        self.assertEqual(sut.get_tokens()[0].directive, "comment")
        self.assertEqual(sut.get_tokens()[0].value, "any comment")
    

if __name__ == '__main__':
    unittest.main()