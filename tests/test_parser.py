"""
Tokenizerのテスト
"""

from functools import reduce
from unittest import TestCase
from cc9.tokenizer import TokenOperator, Token, TokenKind
from cc9.parser import Node, Parser
from typing import Union


def linked_list_helper(a, b):
    a.next = b
    return b


class TestParser(TestCase):
    def assertion_tree(self, node: Union[Node, None]):

        if node is None:
            return 0

        self.assertion_tree(node.left_hand)
        self.assertion_tree(node.right_hand)
        print(node)

    def test_read_single_string(self):

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
        operator = TokenOperator(token_list[0])

        parser = Parser(operator)
        root = parser.run()

        self.assertion_tree(root)

    def test_read_multiple_string(self):

        token_list = [
            Token(TokenKind.NUMBER, "1"),
            Token(TokenKind.SYMBOL, "=="),
            Token(TokenKind.SYMBOL, "("),
            Token(TokenKind.NUMBER, "12"),
            Token(TokenKind.SYMBOL, "+"),
            Token(TokenKind.NUMBER, "3"),
            Token(TokenKind.SYMBOL, ")"),
            Token(TokenKind.SYMBOL, "*"),
            Token(TokenKind.NUMBER, "4"),
            Token(TokenKind.NUMBER, ">="),
            Token(TokenKind.NUMBER, "0"),
            Token(TokenKind.EOF),
        ]

        reduce(linked_list_helper, token_list)
        operator = TokenOperator(token_list[0])

        parser = Parser(operator)
        root = parser.run()

        self.assertion_tree(root)
