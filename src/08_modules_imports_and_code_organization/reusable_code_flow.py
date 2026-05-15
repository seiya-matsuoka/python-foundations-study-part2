"""再利用可能なコードへの分割を確認するサンプル。"""

from typing import TypedDict

from helpers.price_tools import calculate_tax_included, calculate_total, format_price
from helpers.text_tools import build_slug, normalize_name


class Item(TypedDict):
    """商品情報の形を表す型。"""

    name: str
    slug: str
    price: int


class Order(TypedDict):
    """注文情報の形を表す型。"""

    names: list[str]
    total: int


def build_item(name: str, price: int) -> Item:
    """商品名と税抜価格から商品情報を作る。"""
    # 商品情報を作る処理を関数に分けると、呼び出し側で再利用しやすい。
    normalized_name = normalize_name(name)
    slug = build_slug(normalized_name)
    tax_included_price = calculate_tax_included(price)

    return {
        "name": normalized_name,
        "slug": slug,
        "price": tax_included_price,
    }


def build_order(items: list[Item]) -> Order:
    """商品情報の list から注文情報を作る。"""
    # Item は name, slug, price を持つ商品情報として定義している。
    # そのため、item["price"] は int として扱える。
    prices = []
    names = []

    for item in items:
        prices.append(item["price"])
        names.append(item["name"])

    total = calculate_total(prices)

    return {
        "names": names,
        "total": total,
    }


def run_reusable_code_flow() -> None:
    """処理を小さな関数やモジュールに分けて再利用する流れを確認する。"""

    first_item = build_item(" python book ", 2000)
    second_item = build_item(" sql book ", 2500)

    print(f"first_item: {first_item}")
    print(f"second_item: {second_item}")

    order = build_order([first_item, second_item])
    total_label = format_price(order["total"])

    print(f"order: {order}")
    print(f"total_label: {total_label}")

    assert first_item == {
        "name": "Python Book",
        "slug": "python-book",
        "price": 2200,
    }
    assert second_item == {
        "name": "Sql Book",
        "slug": "sql-book",
        "price": 2750,
    }
    assert order == {
        "names": ["Python Book", "Sql Book"],
        "total": 4950,
    }
    assert total_label == "4950 yen"
