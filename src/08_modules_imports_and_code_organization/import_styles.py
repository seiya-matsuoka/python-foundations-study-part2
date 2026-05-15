"""import と from ... import ... の基本を確認するサンプル。"""

import helpers.text_tools as text_tools
from helpers.price_tools import calculate_tax_included, format_price


def run_import_styles() -> None:
    """モジュール全体の import と、特定関数の import を確認する。"""

    # import helpers.text_tools as text_tools は、
    # モジュール全体を text_tools という名前で読み込む。
    raw_name = "  sora matsuoka  "
    normalized_name = text_tools.normalize_name(raw_name)
    slug = text_tools.build_slug(normalized_name)

    print(f"normalized_name: {normalized_name}")
    print(f"slug: {slug}")

    # from ... import ... は、モジュール内の特定の名前だけを読み込む。
    # ここでは price_tools から2つの関数を直接使えるようにしている。
    tax_included_price = calculate_tax_included(1000)
    formatted_price = format_price(tax_included_price)

    print(f"tax_included_price: {tax_included_price}")
    print(f"formatted_price: {formatted_price}")

    # モジュール名を残す import は、どこから来た関数かが読みやすい。
    # from import は短く書けるが、名前の由来が見えにくくなる場合もある。
    labels = text_tools.join_labels(["Python", "Import", "Module"])
    print(f"labels: {labels}")

    assert normalized_name == "Sora Matsuoka"
    assert slug == "sora-matsuoka"
    assert tax_included_price == 1100
    assert formatted_price == "1100 yen"
    assert labels == "Python / Import / Module"
