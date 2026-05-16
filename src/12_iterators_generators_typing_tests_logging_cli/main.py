"""Unit 12 の実行入口。

このファイルは、Unit 12 に含まれる各サンプルを順番に呼び出す。
反復処理の仕組み、型ヒント、テスト、ログ、CLI 基礎を確認する入口となる。
"""

from assertion_and_unittest_examples import run_assertion_and_unittest_examples
from cli_examples import run_cli_examples
from custom_iterator import run_custom_iterator
from generator_examples import run_generator_examples
from iterable_iterator_basics import run_iterable_iterator_basics
from logging_examples import run_logging_examples
from type_hints_examples import run_type_hints_examples


def print_section(title: str) -> None:
    """表示上の区切りを出力する。

    学習用コードのため、処理のまとまりごとに見出しを出す。
    戻り値はなく、標準出力への表示だけを行う。
    """
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def main() -> None:
    """Unit 12 全体を順番に実行する。

    この単位では、反復処理の仕組みと実務寄りの基礎要素を確認する。
    iterable、iterator、yield、型ヒント、unittest、logging、argparse を読む。
    """
    print_section("1. iterable / iterator / iter / next")
    run_iterable_iterator_basics()

    print_section("2. yield / ジェネレータ関数 / ジェネレータ式")
    run_generator_examples()

    print_section("3. __iter__ / __next__")
    run_custom_iterator()

    print_section("4. 型ヒント")
    run_type_hints_examples()

    print_section("5. assert / unittest")
    run_assertion_and_unittest_examples()

    print_section("6. logging")
    run_logging_examples()

    print_section("7. argparse / sys")
    run_cli_examples()


# この条件式は、main.py を直接実行したときだけ main を呼び出すための書き方。
# import されたときに自動実行されないようにするための基本形となる。
if __name__ == "__main__":
    main()
