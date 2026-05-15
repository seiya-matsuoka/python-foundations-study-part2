"""__name__ と実行入口の考え方を確認するサンプル。"""


def get_current_module_name() -> str:
    """このモジュールの __name__ を返す。"""
    # このファイルが main.py から import されると、
    # __name__ は "__main__" ではなく "entry_point_examples" になる。
    return __name__


def build_execution_message() -> str:
    """このモジュールの実行され方を説明する文字列を返す。"""
    if __name__ == "__main__":
        return "entry_point_examples.py is executed directly"

    return "entry_point_examples.py is imported"


def run_entry_point_examples() -> None:
    """__name__ と __name__ == "__main__" の基本を確認する。"""

    module_name = get_current_module_name()
    execution_message = build_execution_message()

    print(f"module_name: {module_name}")
    print(f"execution_message: {execution_message}")

    # main.py から呼び出しているため、このファイルは import された状態になる。
    # そのため __name__ は "__main__" ではなく、モジュール名になる。
    imported_from_main = module_name != "__main__"
    print(f"imported_from_main: {imported_from_main}")

    assert module_name == "entry_point_examples"
    assert execution_message == "entry_point_examples.py is imported"
    assert imported_from_main is True


# このファイルを直接実行した場合だけ、下の処理が実行される。
# main.py から import された場合は実行されない。
if __name__ == "__main__":
    print(build_execution_message())
