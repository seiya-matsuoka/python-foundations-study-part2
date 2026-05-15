"""itertools の代表的な機能を確認するサンプル。"""

from itertools import chain, groupby, islice, product
from operator import itemgetter
from typing import TypedDict


class SaleRecord(TypedDict):
    """売上データの形。"""

    category: str
    item: str
    amount: int


def run_itertools_examples() -> None:
    """chain、islice、product、groupby の基本的な使い方を確認する。"""

    # chain は、複数の iterable を1つにつなげて扱える。
    backend_skills = ["Java", "Spring"]
    python_skills = ["Python", "Django"]
    all_skills = list(chain(backend_skills, python_skills))

    print(f"all_skills: {all_skills}")

    # islice は、iterator から一部だけを取り出す。
    # 大きいデータや無限に続くような iterator の一部を見るときに使える。
    numbers = range(1, 100)
    first_five_even_numbers = list(
        islice(
            (number for number in numbers if number % 2 == 0),
            5,
        )
    )

    print(f"first_five_even_numbers: {first_five_even_numbers}")

    # product は、複数の iterable の組み合わせを作る。
    # 全組み合わせを確認したい場合に使える。
    colors = ["red", "blue"]
    sizes = ["S", "M", "L"]
    color_size_pairs = list(product(colors, sizes))

    print(f"color_size_pairs: {color_size_pairs}")

    # groupby は、連続した同じキーの要素をグループ化する。
    # 期待通りに使うには、先に同じキーで並び替えておくことが多い。
    sales: list[SaleRecord] = [
        {"category": "book", "item": "Python", "amount": 2000},
        {"category": "tool", "item": "Keyboard", "amount": 8000},
        {"category": "book", "item": "SQL", "amount": 1800},
        {"category": "tool", "item": "Mouse", "amount": 3000},
    ]
    sorted_sales = sorted(sales, key=itemgetter("category"))

    totals_by_category = {}

    for category, grouped_sales in groupby(sorted_sales, key=itemgetter("category")):
        total = 0

        for sale in grouped_sales:
            total += sale["amount"]

        totals_by_category[category] = total

    print(f"totals_by_category: {totals_by_category}")

    assert all_skills == ["Java", "Spring", "Python", "Django"]
    assert first_five_even_numbers == [2, 4, 6, 8, 10]
    assert color_size_pairs == [
        ("red", "S"),
        ("red", "M"),
        ("red", "L"),
        ("blue", "S"),
        ("blue", "M"),
        ("blue", "L"),
    ]
    assert totals_by_category == {
        "book": 3800,
        "tool": 11000,
    }
