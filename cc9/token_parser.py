"""
Parserクラス
"""


from __future__ import annotations
from tokenizer import TokenKind, TokenOperator
from enum import IntEnum, auto
from typing import Union


class NodeKind(IntEnum):
    """ノード種別を表す"""

    ADD = auto()  # +
    SUB = auto()  # -
    MUL = auto()  # *
    DIV = auto()  # /
    GREATER = auto()  # >
    GREATER_EQUAL = auto()  # >=
    LOWER = auto()  # <
    LOWER_EQUAL = auto()  # <=
    EQUAL = auto()  # ==
    NOT_EQUAL = auto()  # !=
    NUMBER = auto()  # NUMBER


class Node:
    """抽象構文木クラス"""

    def __init__(self):
        """初期化"""
        self.value: Union[int, str, None] = None
        self.kind: Union[NodeKind, None] = None
        self.left_hand: Union[Node, None] = None
        self.right_hand: Union[Node, None] = None

    def __repr__(self) -> str:
        """文字列型表示を定義"""
        return f"""
        Node(value={self.value}, kind={str(NodeKind(self.kind))},
        left_hand_exist={getattr(self.left_hand, "value", None)},
        right_hand={getattr(self.right_hand, "value", None)})
        """


class Parser:
    """文字列を読み取りノード(抽象構文木)を作成する"""

    def __init__(self, cursor: TokenOperator) -> None:
        """カーソルを設定する"""
        self.cursor = cursor

    def create_new_node(
        self,
        value: Union[str, int, None],
        kind: NodeKind,
        left_hand: Union[Node, None],
        right_hand: Union[Node, None],
    ) -> Node:
        """新たノードを作成する"""
        node = Node()
        node.value = value
        node.kind = kind
        node.right_hand = right_hand
        node.left_hand = left_hand
        return node

    def run(self) -> Node:
        """パーサの実行"""
        node = self.statement(self.cursor)

        if self.cursor.chack_type(TokenKind.EOF) is False:
            raise IndexError("パース出来ていないトークンが存在します")

        return node

    # def program(self, cursor: TokenOperator) -> Node:
    #     pass

    def statement(self, cursor: TokenOperator) -> Node:
        """statement具象構文木"""
        node = self.expression(cursor)

        if cursor.consume(";") is False:
            raise ValueError("プログラムの末尾が;で終わっていません")

        return node

    def expression(self, cursor: TokenOperator) -> Node:
        """expression具象構文木"""
        return self.equality(cursor)

    def equality(self, cursor: TokenOperator) -> Node:
        """equality具象構文木"""
        node = self.relation(cursor)

        while 1:
            if cursor.consume("=="):
                node = self.create_new_node("==", NodeKind.EQUAL, node, self.relation(cursor))
            elif cursor.consume("!="):
                node = self.create_new_node("!=", NodeKind.NOT_EQUAL, node, self.relation(cursor))
            else:
                return node

    def relation(self, cursor: TokenOperator) -> Node:
        """relation具象構文木"""
        node = self.add(cursor)

        while 1:
            if cursor.consume(">="):
                node = self.create_new_node(">=", NodeKind.GREATER_EQUAL, node, self.add(cursor))
            elif cursor.consume(">"):
                node = self.create_new_node(">", NodeKind.GREATER, node, self.add(cursor))
            elif cursor.consume("<="):
                node = self.create_new_node("<=", NodeKind.LOWER_EQUAL, node, self.add(cursor))
            elif cursor.consume("<"):
                node = self.create_new_node("<", NodeKind.LOWER, node, self.add(cursor))
            else:
                return node

    def add(self, cursor: TokenOperator) -> Node:
        """add具象構文木"""
        node = self.mul(cursor)

        while 1:
            if cursor.consume("+"):
                node = self.create_new_node("+", NodeKind.ADD, node, self.mul(cursor))
            elif cursor.consume("-"):
                node = self.create_new_node("-", NodeKind.SUB, node, self.mul(cursor))
            else:
                return node

    def mul(self, cursor: TokenOperator) -> Node:
        """mul具象構文木"""
        node = self.unary(cursor)

        while 1:
            if cursor.consume("*"):
                node = self.create_new_node("*", NodeKind.MUL, node, self.unary(cursor))
            elif cursor.consume("/"):
                node = self.create_new_node("/", NodeKind.DIV, node, self.unary(cursor))
            else:
                return node

    def unary(self, cursor: TokenOperator) -> Node:
        """unary具象構文木"""
        if cursor.consume("+"):
            return self.primary(cursor)
        if cursor.consume("-"):
            return self.create_new_node(
                None,
                NodeKind.SUB,
                self.create_new_node(0, NodeKind.NUMBER, None, None),
                self.primary(cursor),
            )

        return self.primary(cursor)

    def primary(self, cursor: TokenOperator) -> Node:
        """primary具象構文木"""
        if cursor.consume("("):
            node = self.expression(cursor)
            if cursor.consume(")") is False:
                raise ValueError("トークンのカッコが左右で対応していません")
            return node

        if cursor.chack_type(TokenKind.NUMBER) is False:
            raise TypeError("数値型のトークンではありません")

        value = cursor.get_value()
        cursor.proceed_cursor()

        return self.create_new_node(value, NodeKind.NUMBER, None, None)
