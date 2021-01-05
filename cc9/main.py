"""
main
"""

import sys

from tokenizer import tokenize, TokenOperator
from token_parser import Parser
from code_generator import generate_code


def main(argv: list) -> int:
    """main関数"""
    if len(argv) != 2:
        raise ValueError("引数の個数が正しくありません")

    operator = TokenOperator(tokenize(argv[1]))
    parser = Parser(operator)
    nodes = parser.run()
    generate_code(nodes)


if __name__ == "__main__":
    main(sys.argv)
