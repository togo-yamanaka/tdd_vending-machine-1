"""
code generator
"""

from typing import List
from token_parser import Node, NodeKind


def generate_code(nodes: List[Node]) -> None:
    """xxx"""
    print(".intel_syntax noprefix")
    print(".globl main")
    print("main:")

    # プロローグ
    # 変数26個分の領域を確保する
    print("    push rbp")
    print("    mov rbp, rsp")
    print("    sub rsp, 208")

    # 抽象構文木からスタックマシンを使ってバイナリコードを生成
    for node in nodes:
        recursive_generate(node)
        print("    pop rax")

    print("    mov rsp, rbp")
    print("    pop rbp")
    print("    ret")


def local_var_generate(node: Node) -> None:
    """ローカル変数をスタックにpushする"""
    if node.kind != NodeKind.LOCAL_VAR:
        raise ValueError("代入の左辺値が変数ではありません")

    print("    mov rax, rbp")
    print(f"    sub rax, {node.offset}")
    print("    push rax")


def recursive_generate(node: Node) -> None:
    """xxx"""
    if node.kind == NodeKind.NUMBER:
        print(f"    push {node.value}")
        return
    elif node.kind == NodeKind.LOCAL_VAR:
        local_var_generate(node)
        print("    pop rax")
        print("    mov rax, [rax]")
        print("    push rax")
        return
    elif node.kind == NodeKind.ASSIGN:
        local_var_generate(node.left_hand)
        recursive_generate(node.right_hand)

        print("    pop rdi")
        print("    pop rax")
        print("    mov [rax], rdi")
        print("    push rdi")
        return
    else:
        pass

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
