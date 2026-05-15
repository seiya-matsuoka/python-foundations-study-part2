"""Unit 10 の実行入口。

このファイルは、Unit 10 に含まれる各サンプルを順番に呼び出す。
標準ライブラリの代表的な機能と使いどころを確認する入口となる。
"""

from collections_examples import run_collections_examples
from datetime_examples import run_datetime_examples
from functools_examples import run_functools_examples
from itertools_examples import run_itertools_examples
from math_random_statistics_examples import run_math_random_statistics_examples


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
    """Unit 10 全体を順番に実行する。

    この単位では、標準ライブラリの代表的な機能を確認する。
    日時、数値処理、コレクション補助、反復処理補助、関数補助を読む。
    """
    print_section("1. datetime")
    run_datetime_examples()

    print_section("2. math / random / statistics")
    run_math_random_statistics_examples()

    print_section("3. collections")
    run_collections_examples()

    print_section("4. itertools")
    run_itertools_examples()

    print_section("5. functools")
    run_functools_examples()


# この条件式は、main.py を直接実行したときだけ main を呼び出すための書き方。
# import されたときに自動実行されないようにするための基本形となる。
if __name__ == "__main__":
    main()
