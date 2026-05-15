"""パッケージの基本を確認するサンプル。"""

from helpers import text_tools
from helpers.price_tools import calculate_total


def build_learning_summary(title: str, labels: list[str], prices: list[int]) -> str:
    """学習項目名、ラベル、金額リストから概要文字列を作る。"""
    # helpers はディレクトリであり、__init__.py を持つためパッケージとして扱える。
    # helpers.text_tools のように、パッケージ配下のモジュールを参照できる。
    normalized_title = text_tools.normalize_name(title)
    slug = text_tools.build_slug(normalized_title)
    joined_labels = text_tools.join_labels(labels)
    total_price = calculate_total(prices)

    return f"{normalized_title} [{slug}] {joined_labels}: {total_price} yen"


def run_package_usage() -> None:
    """パッケージ配下のモジュールを読み込む流れを確認する。"""

    summary = build_learning_summary(
        title="python modules",
        labels=["import", "package", "split"],
        prices=[1000, 2000, 3000],
    )

    print(f"summary: {summary}")

    # __name__ を見ると、読み込まれたモジュール名を確認できる。
    # パッケージ配下のモジュールでは helpers.text_tools のような名前になる。
    text_tools_module_name = text_tools.__name__
    print(f"text_tools.__name__: {text_tools_module_name}")

    assert summary == (
        "Python Modules [python-modules] import / package / split: 6000 yen"
    )
    assert text_tools_module_name == "helpers.text_tools"
