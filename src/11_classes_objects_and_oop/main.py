"""Unit 11 の実行入口。

このファイルは、Unit 11 に含まれる各サンプルを順番に呼び出す。
Python におけるクラス、オブジェクト、オブジェクト指向の基本を確認する入口となる。
"""

from abc_and_enum import run_abc_and_enum
from class_basics import run_class_basics
from composition_and_duck_typing import run_composition_and_duck_typing
from dataclass_examples import run_dataclass_examples
from inheritance_and_super import run_inheritance_and_super
from method_types_and_property import run_method_types_and_property


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
    """Unit 11 全体を順番に実行する。

    この単位では、Python のクラス定義とオブジェクト指向を確認する。
    基本、メソッド種別、dataclass、継承、合成、ABC、Enum を読む。
    """
    print_section("1. class / __init__ / インスタンス属性")
    run_class_basics()

    print_section("2. classmethod / staticmethod / property")
    run_method_types_and_property()

    print_section("3. dataclass / 特殊メソッド")
    run_dataclass_examples()

    print_section("4. 継承 / super() / メソッドオーバーライド")
    run_inheritance_and_super()

    print_section("5. 合成 / duck typing")
    run_composition_and_duck_typing()

    print_section("6. 抽象基底クラス / Enum")
    run_abc_and_enum()


# この条件式は、main.py を直接実行したときだけ main を呼び出すための書き方。
# import されたときに自動実行されないようにするための基本形となる。
if __name__ == "__main__":
    main()
