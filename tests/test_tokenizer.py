"""
Tokenizerのテスト
"""

from functools import reduce
from unittest import TestCase
from cc9.tokenizer import TokenOperator, tokenize, Token, TokenKind


def linked_list_helper(a, b):
    a.next = b
    return b


class TestTokenizer(TestCase):
    def test_read_single_string(self):
        test_string = "(1 + 3) * 2"

        token_list = [
            Token(TokenKind.SYMBOL, "("),
            Token(TokenKind.NUMBER, "1"),
            Token(TokenKind.SYMBOL, "+"),
            Token(TokenKind.NUMBER, "3"),
            Token(TokenKind.SYMBOL, ")"),
            Token(TokenKind.SYMBOL, "*"),
            Token(TokenKind.NUMBER, "2"),
            Token(TokenKind.EOF),
        ]

        reduce(linked_list_helper, token_list)
        expected_token = token_list[0]

        token = tokenize(test_string)

        while token:
            assert str(token) == str(expected_token)
            token = token.next
            expected_token = expected_token.next

    def test_read_multiple_string(self):

        test_string = "112 == 32 + 160 / 2"

        token_list = [
            Token(TokenKind.NUMBER, "112"),
            Token(TokenKind.SYMBOL, "=="),
            Token(TokenKind.NUMBER, "32"),
            Token(TokenKind.SYMBOL, "+"),
            Token(TokenKind.NUMBER, "160"),
            Token(TokenKind.SYMBOL, "/"),
            Token(TokenKind.NUMBER, "2"),
            Token(TokenKind.EOF),
        ]

        reduce(linked_list_helper, token_list)
        expected_token = token_list[0]

        token = tokenize(test_string)

        while token:
            assert str(token) == str(expected_token)
            token = token.next
            expected_token = expected_token.next

    def test_read_symbols(self):

        test_string = "== != <= >= < > + - * / ( )"

        token_list = [
            Token(TokenKind.SYMBOL, "=="),
            Token(TokenKind.SYMBOL, "!="),
            Token(TokenKind.SYMBOL, "<="),
            Token(TokenKind.SYMBOL, ">="),
            Token(TokenKind.SYMBOL, "<"),
            Token(TokenKind.SYMBOL, ">"),
            Token(TokenKind.SYMBOL, "+"),
            Token(TokenKind.SYMBOL, "-"),
            Token(TokenKind.SYMBOL, "*"),
            Token(TokenKind.SYMBOL, "/"),
            Token(TokenKind.SYMBOL, "("),
            Token(TokenKind.SYMBOL, ")"),
            Token(TokenKind.EOF),
        ]

        reduce(linked_list_helper, token_list)
        expected_token = token_list[0]

        token = tokenize(test_string)

        while token:
            assert str(token) == str(expected_token)
            token = token.next
            expected_token = expected_token.next


class TestTokenOperator(TestCase):
    def setUp(self):
        self.token_list = [
            Token(TokenKind.SYMBOL, "("),
            Token(TokenKind.NUMBER, "1"),
            Token(TokenKind.SYMBOL, "+"),
            Token(TokenKind.NUMBER, "3"),
            Token(TokenKind.SYMBOL, ")"),
            Token(TokenKind.SYMBOL, "*"),
            Token(TokenKind.NUMBER, "2"),
            Token(TokenKind.EOF),
        ]

        reduce(linked_list_helper, self.token_list)
        self.test_token = self.token_list[0]

    def test_proceed_cursor(self):

        operator = TokenOperator(self.token_list[0])
        operator.proceed_cursor()

        assert str(self.token_list[1]) == str(operator.cursor)

    def test_consume(self):

        operator = TokenOperator(self.token_list[0])

        assert operator.consume("(") is True
        assert str(self.token_list[1]) == str(operator.cursor)

        assert operator.consume("1") is True
        assert str(self.token_list[2]) == str(operator.cursor)
