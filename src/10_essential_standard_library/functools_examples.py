"""functools の代表的な機能を確認するサンプル。"""

from functools import lru_cache, partial


def apply_tax(price: int, tax_rate: float) -> int:
    """税率を適用した税込価格を返す。"""
    return int(price * (1 + tax_rate))


@lru_cache(maxsize=32)
def fibonacci(number: int) -> int:
    """lru_cache の効果を確認するためのフィボナッチ数計算。"""
    # この関数は学習用に再帰で書いている。
    # lru_cache により、同じ引数の計算結果がキャッシュされる。
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


def run_functools_examples() -> None:
    """partial と lru_cache の基本的な使い方を確認する。"""

    # partial は、関数の一部の引数を先に固定した新しい関数を作る。
    # ここでは税率を固定して、税込価格を計算する関数を作っている。
    apply_standard_tax = partial(apply_tax, tax_rate=0.1)
    apply_reduced_tax = partial(apply_tax, tax_rate=0.08)

    standard_tax_price = apply_standard_tax(1000)
    reduced_tax_price = apply_reduced_tax(1000)

    print(f"standard_tax_price: {standard_tax_price}")
    print(f"reduced_tax_price: {reduced_tax_price}")

    # lru_cache は、同じ引数で呼び出した結果をキャッシュする。
    # 再帰や重い計算を含む関数で使うと、再計算を減らせる。
    fibonacci.cache_clear()

    fibonacci_10 = fibonacci(10)
    cache_after_first_call = fibonacci.cache_info()

    fibonacci_10_again = fibonacci(10)
    cache_after_second_call = fibonacci.cache_info()

    print(f"fibonacci_10: {fibonacci_10}")
    print(f"fibonacci_10_again: {fibonacci_10_again}")
    print(f"cache_after_first_call: {cache_after_first_call}")
    print(f"cache_after_second_call: {cache_after_second_call}")

    assert standard_tax_price == 1100
    assert reduced_tax_price == 1080
    assert fibonacci_10 == 55
    assert fibonacci_10_again == 55
    assert cache_after_second_call.hits > cache_after_first_call.hits
