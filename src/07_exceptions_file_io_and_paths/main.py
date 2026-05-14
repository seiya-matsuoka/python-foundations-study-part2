"""Unit 07 の実行入口。

このファイルは、Unit 07 に含まれる各サンプルを順番に呼び出す。
例外処理、ファイル入出力、pathlib によるパス操作を確認する入口となる。
"""

from exception_basics import run_exception_basics
from file_reading_and_writing import run_file_reading_and_writing
from pathlib_operations import run_pathlib_operations
from raising_exceptions import run_raising_exceptions
from safe_file_processing import run_safe_file_processing


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
    """Unit 07 全体を順番に実行する。

    この単位では、例外処理とファイル操作の基本を確認する。
    try / except、raise、with、open、pathlib を順番に読む。
    """
    print_section("1. try / except / else / finally")
    run_exception_basics()

    print_section("2. raise")
    run_raising_exceptions()

    print_section("3. open / with による読み書き")
    run_file_reading_and_writing()

    print_section("4. pathlib によるパス操作")
    run_pathlib_operations()

    print_section("5. 例外処理を含むファイル処理")
    run_safe_file_processing()


# この条件式は、main.py を直接実行したときだけ main を呼び出すための書き方。
# import されたときに自動実行されないようにするための基本形となる。
if __name__ == "__main__":
    main()
