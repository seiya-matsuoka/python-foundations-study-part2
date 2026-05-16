"""argparse と sys の最小限を確認するサンプル。"""

import argparse
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class CliOptions:
    """CLI 引数を解析した後の値。"""

    name: str
    count: int
    verbose: bool


def create_parser() -> argparse.ArgumentParser:
    """学習用 CLI の ArgumentParser を作る。"""
    # argparse は、コマンドライン引数を定義して解析するための標準ライブラリ。
    # add_argument で、受け付けるオプションや型を定義する。
    parser = argparse.ArgumentParser(description="Unit 12 CLI sample")
    parser.add_argument("--name", default="World", help="表示する名前")
    parser.add_argument("--count", type=int, default=1, help="繰り返し回数")
    parser.add_argument("--verbose", action="store_true", help="詳細表示を有効にする")
    return parser


def parse_options(args: list[str]) -> CliOptions:
    """文字列の引数 list を CliOptions に変換する。"""
    # parse_args は、通常 sys.argv[1:] を解析する。
    # 学習用コードでは、明示的に args を渡すと挙動を固定して確認しやすい。
    parser = create_parser()
    namespace = parser.parse_args(args)

    return CliOptions(
        name=str(namespace.name),
        count=int(namespace.count),
        verbose=bool(namespace.verbose),
    )


def build_messages(options: CliOptions) -> list[str]:
    """CLI オプションから表示メッセージを作る。"""
    messages = []

    for index in range(options.count):
        message = f"Hello, {options.name}!"

        if options.verbose:
            message = f"{index + 1}: {message}"

        messages.append(message)

    return messages


def run_cli_examples() -> None:
    """argparse と sys.argv の最小限を確認する。"""

    # sys.argv は、Python プログラム起動時のコマンドライン引数を持つ list。
    # 先頭には実行されたスクリプト名が入る。
    current_argv = sys.argv[:]
    script_name = current_argv[0]

    print(f"script_name: {script_name}")

    options = parse_options(["--name", "Sora", "--count", "2", "--verbose"])
    messages = build_messages(options)

    print(f"options: {options}")
    print(f"messages: {messages}")

    default_options = parse_options([])
    default_messages = build_messages(default_options)

    print(f"default_options: {default_options}")
    print(f"default_messages: {default_messages}")

    assert isinstance(script_name, str)
    assert options == CliOptions(name="Sora", count=2, verbose=True)
    assert messages == ["1: Hello, Sora!", "2: Hello, Sora!"]
    assert default_options == CliOptions(name="World", count=1, verbose=False)
    assert default_messages == ["Hello, World!"]
