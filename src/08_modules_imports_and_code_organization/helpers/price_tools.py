"""価格計算を再利用可能な関数としてまとめたモジュール。"""


def calculate_tax_included(price: int, tax_rate: float = 0.1) -> int:
    """税抜価格と税率から税込価格を計算する。"""
    # int で整数にしているため、小数点以下は切り捨てられる。
    # 金額計算の厳密性は別テーマとし、ここでは import 学習用に単純化する。
    return int(price * (1 + tax_rate))


def calculate_total(prices: list[int]) -> int:
    """価格の list から合計金額を計算する。"""
    total = 0

    for price in prices:
        total += price

    return total


def format_price(price: int) -> str:
    """金額を表示用の文字列に整形する。"""
    return f"{price} yen"
