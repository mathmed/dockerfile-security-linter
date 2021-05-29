import unittest
from src.core.analysis.lexical.modules.shell.ShellLexicalAnalysis import ShellLexicalAnalysis
from src.core.analysis.lexical.modules.shell.Token import Token

class TestShellLexicalAnalysis(unittest.TestCase):
    def test_parse_tokens_one_command(self):
        sut = ShellLexicalAnalysis("apt install git")
        result = sut.parse()

        self.assertEqual(sut.get_tokens()[0].directive, "apt")
        self.assertEqual(sut.get_tokens()[0].value, ["install", "git"])

    def test_parse_tokens_multiple_command(self):
        sut = ShellLexicalAnalysis("apt update && apt install git")
        result = sut.parse()
        self.assertEqual(sut.get_tokens()[0].directive, "apt")
        self.assertEqual(sut.get_tokens()[0].value, ["update"])
        self.assertEqual(sut.get_tokens()[1].directive, "apt")
        self.assertEqual(sut.get_tokens()[1].value, ["install", "git"])

if __name__ == '__main__':
    unittest.main()