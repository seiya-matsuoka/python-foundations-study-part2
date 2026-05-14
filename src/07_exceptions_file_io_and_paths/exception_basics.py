"""try / except / else / finally の基本を確認するサンプル。"""


def parse_int(text: str) -> int | None:
    """文字列を int に変換する。変換できない場合は None を返す。"""
    try:
        # int 変換に失敗すると ValueError が発生する。
        # try の中には、例外が発生する可能性がある処理を書く。
        number = int(text)
    except ValueError:
        # except は、指定した例外が発生した場合に実行される。
        # ここでは失敗を表す値として None を返す。
        return None
    else:
        # else は、try の中で例外が発生しなかった場合に実行される。
        # 変換に成功した number をここで返す。
        return number
    finally:
        # finally は、成功しても失敗しても必ず実行される。
        # 今回は学習用に、処理が通ったことを表示する。
        print(f"parse_int processed: {text}")


def safe_divide(left: int, right: int) -> float | None:
    """割り算を行う。0 で割ろうとした場合は None を返す。"""
    try:
        result = left / right
    except ZeroDivisionError:
        return None
    else:
        return result
    finally:
        print(f"safe_divide processed: {left} / {right}")


def get_item(items: list[str], index: int) -> str | None:
    """指定した位置の要素を返す。範囲外の場合は None を返す。"""
    try:
        return items[index]
    except IndexError:
        return None


def run_exception_basics() -> None:
    """try / except / else / finally と代表的な組み込み例外を確認する。"""

    parsed_number = parse_int("123")
    failed_number = parse_int("abc")

    print(f"parsed_number: {parsed_number}")
    print(f"failed_number: {failed_number}")

    divided = safe_divide(10, 2)
    zero_divided = safe_divide(10, 0)

    print(f"divided: {divided}")
    print(f"zero_divided: {zero_divided}")

    languages = ["Python", "Java", "SQL"]
    first_language = get_item(languages, 0)
    missing_language = get_item(languages, 10)

    print(f"first_language: {first_language}")
    print(f"missing_language: {missing_language}")

    assert parsed_number == 123
    assert failed_number is None
    assert divided == 5.0
    assert zero_divided is None
    assert first_language == "Python"
    assert missing_language is None
