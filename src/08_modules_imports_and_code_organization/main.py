"""Unit 08 の実行入口。

このファイルは、Unit 08 に含まれる各サンプルを順番に呼び出す。
import、モジュール、パッケージ、コード分割の基本を確認する入口となる。
"""

from entry_point_examples import run_entry_point_examples
from import_styles import run_import_styles
from package_usage import run_package_usage
from reusable_code_flow import run_reusable_code_flow


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
    """Unit 08 全体を順番に実行する。

    この単位では、複数ファイルに分けたコードの読み込み方を確認する。
    import の基本、パッケージ、エントリーポイント、再利用の流れを読む。
    """
    print_section("1. import と from ... import ...")
    run_import_styles()

    print_section("2. パッケージの基本")
    run_package_usage()

    print_section("3. 再利用可能なコードへの分割")
    run_reusable_code_flow()

    print_section("4. __name__ と実行入口")
    run_entry_point_examples()


# この条件式は、main.py を直接実行したときだけ main を呼び出すための書き方。
# import されたときに自動実行されないようにするための基本形となる。
if __name__ == "__main__":
    main()
