import unittest
from unittest.mock import MagicMock
from src.core.analysis.lexical.Token import Token
from src.core.analysis.lexical.shell.Token import Token as TokenShell
from src.core.rules.Engine import Engine
from src.core.rules.smells.helpers.smells import smells


class TestEngine(unittest.TestCase):
    
    def test_engine_should_return_sm01_smell(self):
        sut = Engine([Token("user", "any_original", "any_start", "any_end", ["root"])])

        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM01"]
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm02_smell(self):
        sut = Engine([Token("env", "any_original", "any_start", "any_end", ["pass", "''"])])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM02"]
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm03_smell(self):
        sut = Engine([Token("env", "any_original", "any_start", "any_end", ["pass", "pass"])])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM03"]
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm04_smell(self):
        sut = Engine([Token("cmd", "any_original", "any_start", "any_end", ["any", "0.0.0.0"])])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM04"]
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm05_smell(self):
        sut = Engine([Token("comment", "any_original", "any_start", "any_end", "fix me")])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM05"]
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm06_smell(self):
        sut = Engine([Token("cmd", "any_original", "any_start", "any_end", ["any", "http://127.0.0.0"])])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM06"]
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm07_smell(self):
        sut = Engine([Token("run", "any_original", "any_start", "any_end", [TokenShell("usermod", ["(mkpasswd -H md5)"])])])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM07"]
                }
        self.assertEqual(sut.run(), [expected])


    def test_engine_should_return_sm08_smell(self):
        sut = Engine([Token("run", "any_original", "any_start", "any_end", [TokenShell("chmod", ["-r", "777", "/"])])])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM08"]
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm09_smell(self):
        sut = Engine([Token("from", "any_original", "any_start", "any_end", ["any:any"])])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM09"]
                }
        self.assertEqual(sut.run(), [expected])
        
if __name__ == '__main__':
    unittest.main()