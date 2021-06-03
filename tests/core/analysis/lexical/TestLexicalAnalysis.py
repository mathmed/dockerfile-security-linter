import unittest
from src.core.analysis.lexical.LexicalAnalysis import LexicalAnalysis
from src.core.analysis.lexical.Token import Token
from src.core.analysis.lexical.shell.Token import Token as TokenShell

class TestLexicalAnalysis(unittest.TestCase):


    def test_parse(self):
        sut = LexicalAnalysis("FROM any\nUSER root\nENV a=any\nARG a=any\n# comment\nRUN apt install\nENV pass='a' pass2='b'")
        sut.parse()
        tokens = sut.get_tokens()

        self.assertEqual(tokens[0].directive, "from")
        self.assertEqual(tokens[0].value[0], "any")

        self.assertEqual(tokens[1].directive, "user")
        self.assertEqual(tokens[1].value[0], "root")

        self.assertEqual(tokens[2].directive, "env")
        self.assertEqual(tokens[2].value, [("a", "any")])

        self.assertEqual(tokens[3].directive, "arg")
        self.assertEqual(tokens[3].value, [["a", "any"]])

        self.assertEqual(tokens[4].directive, "run")
        self.assertEqual(tokens[4].value[0].directive, "apt")

        self.assertEqual(tokens[5].directive, "env")
        self.assertEqual(tokens[5].value, [["pass", "'a'"], ["pass2", "'b'"]])

        self.assertEqual(tokens[6].directive, "comment")
        self.assertEqual(tokens[6].value, "comment")

    def test_convert_tokens(self):
        sut = LexicalAnalysis('any_path')
        tokens = [["any_cmd", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", "any_value"]]
        sut.tokens = tokens
        sut.process_tokens(tokens)
        token = Token(tokens[0][0],tokens[0][3],tokens[0][4],tokens[0][5],tokens[0][7])
        self.assertEqual(sut.get_tokens()[0].directive, token.directive)
        self.assertEqual(sut.get_tokens()[0].original, token.original)
        self.assertEqual(sut.get_tokens()[0].start_line, token.start_line)
        self.assertEqual(sut.get_tokens()[0].end_line, token.end_line)
        self.assertEqual(sut.get_tokens()[0].value, token.value)

    def test_convert_tokens_with_run_directive(self):
        sut = LexicalAnalysis('any_path')
        tokens = [["run", "any_sub", "any_json", "any_original", "any_start", "any_end", "any_flags", ["apt any"]]]
        sut.tokens = tokens
        sut.process_tokens(tokens)
        token = Token(tokens[0][0],tokens[0][3],tokens[0][4],tokens[0][5],tokens[0][7])
        self.assertEqual(sut.get_tokens()[0].directive, token.directive)
        self.assertEqual(sut.get_tokens()[0].original, token.original)
        self.assertEqual(sut.get_tokens()[0].start_line, token.start_line)
        self.assertEqual(sut.get_tokens()[0].end_line, token.end_line)
        self.assertEqual(sut.get_tokens()[0].value[0].directive, TokenShell("apt", ["any"]).directive)
        self.assertEqual(sut.get_tokens()[0].value[0].value, TokenShell("apt", ["any"]).value)

if __name__ == '__main__':
    unittest.main()