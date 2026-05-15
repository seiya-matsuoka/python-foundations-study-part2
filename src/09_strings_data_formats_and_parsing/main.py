"""Unit 09 の実行入口。

このファイルは、Unit 09 に含まれる各サンプルを順番に呼び出す。
文字列処理、正規表現、JSON、CSV の基本を確認する入口となる。
"""

from csv_operations import run_csv_operations
from json_operations import run_json_operations
from regex_basics import run_regex_basics
from search_and_replace import run_search_and_replace
from string_methods import run_string_methods


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
    """Unit 09 全体を順番に実行する。

    この単位では、文字列の加工、検索、正規表現、JSON、CSV を確認する。
    テキストデータを読み、整形し、標準データ形式として扱う流れを読む。
    """
    print_section("1. split / join / strip")
    run_string_methods()

    print_section("2. replace / 検索 / 部分文字列の判定")
    run_search_and_replace()

    print_section("3. 正規表現の基礎")
    run_regex_basics()

    print_section("4. JSON の読み書き")
    run_json_operations()

    print_section("5. CSV の基本操作")
    run_csv_operations()


# この条件式は、main.py を直接実行したときだけ main を呼び出すための書き方。
# import されたときに自動実行されないようにするための基本形となる。
if __name__ == "__main__":
    main()
