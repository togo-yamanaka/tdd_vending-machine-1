"""
code generator
"""

from token_parser import Node, NodeKind


def generate_code(node: Node) -> None:
    """xxx"""
    print(".intel_syntax noprefix")
    print(".globl main")
    print("main:")

    # 抽象構文木からスタックマシンを使ってバイナリコードを生成
    recursive_generate(node)

    print("    pop rax")
    print("    ret")


def recursive_generate(node: Node):
    """xxx"""
    if node.kind == NodeKind.NUMBER:
        print(f"    push {node.value}")
        return

    recursive_generate(node.left_hand)
    recursive_generate(node.right_hand)

    print("    pop rdi")
    print("    pop rax")

    if node.kind == NodeKind.ADD:  # +
        print("    add rax, rdi")
    elif node.kind == NodeKind.SUB:  # -
        print("    sub rax, rdi")
    elif node.kind == NodeKind.MUL:  # *
        print("    imul rax, rdi")
    elif node.kind == NodeKind.DIV:  # /
        print("    cqo")
        print("    idiv rdi")
    elif node.kind == NodeKind.EQUAL:  # ==
        print("    cmp rax, rdi")
        print("    sete al")
        print("    movzb rax, al")
    elif node.kind == NodeKind.NOT_EQUAL:  # !=
        print("    cmp rax, rdi")
        print("    setne al")
        print("    movzb rax, al")
    elif node.kind == NodeKind.LOWER:  # <
        print("    cmp rax, rdi")
        print("    setl al")
        print("    movzb rax, al")
    elif node.kind == NodeKind.LOWER_EQUAL:  # <=
        print("    cmp rax, rdi")
        print("    setle al")
        print("    movzb rax, al")
    elif node.kind == NodeKind.GREATER:  # >
        print("    cmp rdi, rax")
        print("    setl al")
        print("    movzb rax, al")
    elif node.kind == NodeKind.GREATER_EQUAL:  # >=
        print("    cmp rdi, rax")
        print("    setle al")
        print("    movzb rax, al")
    else:
        raise ValueError(f"コンパイル出来ない記号です -> {node.value}")

    print("    push rax")
