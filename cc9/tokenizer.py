"""
Tokenizerクラス
"""

from __future__ import annotations
from enum import IntEnum, auto
from typing import Union
import re


class TokenKind(IntEnum):
    """トークンの種別"""

    SYMBOL = auto()
    NUMBER = auto()
    IDENTIFIER = auto()
    EOF = auto()


class Token:
    """トークンクラス"""

    def __init__(self, token_type: TokenKind = None, value: Union[str, int, None] = None) -> None:
        """初期化"""
        self.type = token_type
        self.value = value
        self.next: Union[Token, None] = None

    def __repr__(self) -> str:
        """理解しやすい形で標準出力する"""
        return (
            f"Token(type={self.type}, value={self.value}, is_next={isinstance(self.next, Token)})"
        )


class TokenOperator:
    """トークンを操作するクラス"""

    def __init__(self, token: Token) -> None:
        """初期化"""
        if isinstance(token, Token) is False:
            raise ValueError("受け取ったオブジェクトはTokenではありません")
        self.cursor = token

    def get_value(self) -> Union[str, int, None]:
        """カーソルが指すトークンの値を取得する"""
        return self.cursor.value

    def proceed_cursor(self) -> None:
        """現在のトークンが指しているカーソルを進める"""
        if isinstance(self.cursor.next, Token):
            self.cursor = self.cursor.next
        else:
            raise IndexError("現在のカーソルの次にトークンがありません")

    def check_value(self, value: Union[int, str]) -> bool:
        """カーソルが指しているトークンが期待の値を持つか調べる"""
        return self.cursor.value == value

    def chack_type(self, kind: TokenKind):
        """カーソルが指しているトークンが期待の値を持つか調べる"""
        return self.cursor.type == kind

    def consume(self, value) -> bool:
        """
        カーソルが指すトークンの値とvalueを比較する

        比較が一致するときはTrueを返してカーソルを進める
        そうでないときはFalseを返す
        """
        if result := self.check_value(value):
            self.proceed_cursor()
        return result


def tokenize(input_str: str) -> Union[Token, None]:
    """文字列を読み込み、トークンにを返す"""
    head = Token()
    cursor = head

    i = 0
    while i <= (len(input_str) - 1):
        if input_str[i] == " ":
            i += 1
            continue

        symbol = "=="
        if re_obj := re.match(symbol, input_str[i:]):
            value = re_obj.group()
            cursor.next = Token(token_type=TokenKind.SYMBOL, value=value)

            cursor = cursor.next
            i += len(value)
            continue
        symbol = "!="
        if re_obj := re.match(symbol, input_str[i:]):
            value = re_obj.group()
            cursor.next = Token(token_type=TokenKind.SYMBOL, value=value)

            cursor = cursor.next
            i += len(value)
            continue
        symbol = ">="
        if re_obj := re.match(symbol, input_str[i:]):
            value = re_obj.group()
            cursor.next = Token(token_type=TokenKind.SYMBOL, value=value)

            cursor = cursor.next
            i += len(value)
            continue
        symbol = "<="
        if re_obj := re.match(symbol, input_str[i:]):
            value = re_obj.group()
            cursor.next = Token(token_type=TokenKind.SYMBOL, value=value)

            cursor = cursor.next
            i += len(value)
            continue

        if input_str[i] in ("+", "-", "*", "/", "(", ")", ">", "<", ";", "="):
            cursor.next = Token(token_type=TokenKind.SYMBOL, value=input_str[i])

            cursor = cursor.next
            i += 1
            continue

        if re_obj := re.match("[a-z]", input_str[i:]):
            value = re_obj.group()
            cursor.next = Token(token_type=TokenKind.IDENTIFIER, value=value)

            cursor = cursor.next
            i += len(value)
            continue

        if str.isdecimal(input_str[i]):
            value = re.match("[0-9]+", input_str[i:]).group()
            cursor.next = Token(token_type=TokenKind.NUMBER, value=int(value))

            cursor = cursor.next
            i += len(value)
            continue

        raise ValueError(f"トークナイズ出来ない文字列です -> {input_str[i]}")

    cursor.next = Token(TokenKind.EOF)

    return head.next
