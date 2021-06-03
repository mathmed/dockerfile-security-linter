import unittest
from unittest.mock import MagicMock
from src.core.analysis.lexical.Token import Token
from src.core.analysis.lexical.shell.Token import Token as TokenShell
from src.core.rules.Engine import Engine
from src.core.rules.smells.lists.smells import smells


class TestEngine(unittest.TestCase):
    
    def setUp(self):
        self.user_aux_token = Token("user", "any_original", "any_start", "any_end", ["user"])

    def test_engine_should_return_sm01_smell(self):
        sut = Engine([Token("user", "any_original", "any_start", "any_end", ["root"]), self.user_aux_token])

        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM01"],
                    "code": "SM01"
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm02_smell(self):
        sut = Engine([Token("env", "any_original", "any_start", "any_end", [["pass", "''"]]), self.user_aux_token])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM02"],
                    "code": "SM02"
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm03_smell(self):
        sut = Engine([Token("env", "any_original", "any_start", "any_end", [["pass", "pass"]]), self.user_aux_token])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM03"],
                    "code": "SM03"
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm04_smell(self):
        sut = Engine([Token("cmd", "any_original", "any_start", "any_end", ["any", "0.0.0.0"]), self.user_aux_token])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM04"],
                    "code": "SM04"
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm05_smell(self):
        sut = Engine([Token("comment", "any_original", "any_start", "any_end", "fix me"), self.user_aux_token])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM05"],
                    "code": "SM05"
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm06_smell(self):
        sut = Engine([Token("cmd", "any_original", "any_start", "any_end", ["any", "http://127.0.0.0"]), self.user_aux_token])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM06"],
                    "code": "SM06"
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm07_smell(self):
        sut = Engine([Token("run", "any_original", "any_start", "any_end", [TokenShell("usermod", ["(mkpasswd -H md5)"])]), self.user_aux_token])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM07"],
                    "code": "SM07"
                }
        self.assertEqual(sut.run(), [expected])


    def test_engine_should_return_sm08_smell(self):
        sut = Engine([Token("run", "any_original", "any_start", "any_end", [TokenShell("chmod", ["-r", "777", "/"])]), self.user_aux_token])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM08"],
                    "code": "SM08"
                }
        self.assertEqual(sut.run(), [expected])

    def test_engine_should_return_sm09_smell(self):
        sut = Engine([Token("from", "any_original", "any_start", "any_end", ["any:any"]), self.user_aux_token])
        expected = {
                    "command": "any_original", 
                    "start_line": "any_start", 
                    "end_line": "any_end", 
                    "security_smell": smells["SM09"],
                    "code": "SM09"
                }
        self.assertEqual(sut.run(), [expected])
        
if __name__ == '__main__':
    unittest.main()