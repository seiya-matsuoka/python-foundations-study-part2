"""classmethod、staticmethod、property を確認するサンプル。"""


class Product:
    """商品を表すクラス。"""

    tax_rate = 0.1

    def __init__(self, name: str, base_price: int) -> None:
        """商品名と税抜価格を受け取って初期化する。"""
        self.name = name
        self.base_price = base_price

    @classmethod
    def from_text(cls, text: str) -> "Product":
        """カンマ区切りの文字列から Product を生成する。"""
        # classmethod の第1引数 cls は、クラス自身を表す。
        # インスタンス生成の別ルートを用意したい場合に使える。
        name, price_text = text.split(",")
        return cls(name.strip(), int(price_text.strip()))

    @staticmethod
    def is_valid_price(price: int) -> bool:
        """価格として有効な値かを判定する。"""
        # staticmethod は、インスタンスにもクラスにも依存しない処理を置く。
        # クラスに関連するが self や cls を使わない処理に向く。
        return price >= 0

    @property
    def tax_included_price(self) -> int:
        """税込価格を属性のように参照できるようにする。"""
        # property は、メソッド呼び出しではなく属性アクセスの形で値を返す。
        # 計算結果を読み取り専用の属性のように見せたい場合に使える。
        return int(self.base_price * (1 + Product.tax_rate))

    @property
    def label(self) -> str:
        """表示用の商品ラベルを返す。"""
        return f"{self.name}: {self.tax_included_price} yen"


def run_method_types_and_property() -> None:
    """classmethod、staticmethod、property の使い分けを確認する。"""

    product = Product("Book", 2000)
    product_from_text = Product.from_text("Pen, 300")

    print(f"product.label: {product.label}")
    print(f"product_from_text.label: {product_from_text.label}")
    print(f"is valid 100: {Product.is_valid_price(100)}")
    print(f"is valid -1: {Product.is_valid_price(-1)}")

    # property はメソッドだが、呼び出し側では属性のように参照する。
    # product.tax_included_price() ではなく product.tax_included_price と書く。
    book_price = product.tax_included_price
    pen_price = product_from_text.tax_included_price

    assert product.name == "Book"
    assert product.base_price == 2000
    assert product.label == "Book: 2200 yen"
    assert product_from_text.name == "Pen"
    assert product_from_text.base_price == 300
    assert product_from_text.label == "Pen: 330 yen"
    assert Product.is_valid_price(100) is True
    assert Product.is_valid_price(-1) is False
    assert book_price == 2200
    assert pen_price == 330
