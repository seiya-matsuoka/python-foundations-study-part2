"""raise による例外送出を確認するサンプル。"""


def require_non_empty_text(text: str) -> str:
    """空ではない文字列を返す。空の場合は ValueError を送出する。"""
    # raise は、条件を満たさない場合に例外を明示的に送出するために使う。
    # 呼び出し側に「この値では処理を続けられない」と伝えられる。
    if text == "":
        raise ValueError("text must not be empty")

    return text


def calculate_discount_price(price: int, discount_rate: float) -> int:
    """割引後の価格を返す。値が不正な場合は ValueError を送出する。"""
    if price < 0:
        raise ValueError("price must be greater than or equal to 0")

    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("discount_rate must be between 0 and 1")

    return int(price * (1 - discount_rate))


def run_raising_exceptions() -> None:
    """raise を使った入力値チェックを確認する。"""

    valid_text = require_non_empty_text("Python")
    print(f"valid_text: {valid_text}")

    try:
        require_non_empty_text("")
    except ValueError as error:
        empty_error_message = str(error)
    else:
        empty_error_message = ""

    print(f"empty_error_message: {empty_error_message}")

    discounted_price = calculate_discount_price(1000, 0.2)
    print(f"discounted_price: {discounted_price}")

    try:
        calculate_discount_price(1000, 1.5)
    except ValueError as error:
        rate_error_message = str(error)
    else:
        rate_error_message = ""

    print(f"rate_error_message: {rate_error_message}")

    assert valid_text == "Python"
    assert empty_error_message == "text must not be empty"
    assert discounted_price == 800
    assert rate_error_message == "discount_rate must be between 0 and 1"
