"""dataclass と特殊メソッドの基礎を確認するサンプル。"""

from dataclasses import dataclass


@dataclass
class Point:
    """座標を表す dataclass。"""

    x: int
    y: int


@dataclass(frozen=True)
class Money:
    """金額を表す変更不可の dataclass。"""

    amount: int
    currency: str = "JPY"

    def __str__(self) -> str:
        """ユーザー向けの文字列表現を返す。"""
        return f"{self.amount} {self.currency}"


class Task:
    """特殊メソッドを明示的に定義するタスククラス。"""

    def __init__(self, title: str, priority: int) -> None:
        """タイトルと優先度を受け取って初期化する。"""
        self.title = title
        self.priority = priority

    def __repr__(self) -> str:
        """開発者向けの文字列表現を返す。"""
        return f"Task(title={self.title!r}, priority={self.priority!r})"

    def __str__(self) -> str:
        """ユーザー向けの文字列表現を返す。"""
        return f"{self.title} / priority={self.priority}"

    def __eq__(self, other: object) -> bool:
        """値として等しいかを判定する。"""
        if not isinstance(other, Task):
            return False

        return self.title == other.title and self.priority == other.priority


def run_dataclass_examples() -> None:
    """dataclass、__repr__、__str__、__eq__ を確認する。"""

    first_point = Point(10, 20)
    second_point = Point(10, 20)
    moved_point = Point(99, 20)

    print(f"first_point: {first_point}")
    print(f"second_point: {second_point}")
    print(f"moved_point: {moved_point}")
    print(f"first_point == second_point: {first_point == second_point}")

    # dataclass は、属性定義から __init__ や __repr__、__eq__ を生成する。
    # 同じ属性値を持つ Point 同士は、値として等しいと判定される。
    price = Money(1200)
    print(f"repr(price): {price!r}")
    print(f"str(price): {price}")

    first_task = Task("write docs", 2)
    second_task = Task("write docs", 2)
    third_task = Task("run tests", 1)

    print(f"repr(first_task): {first_task!r}")
    print(f"str(first_task): {first_task}")
    print(f"first_task == second_task: {first_task == second_task}")
    print(f"first_task == third_task: {first_task == third_task}")

    assert first_point == second_point
    assert first_point != moved_point
    assert repr(first_point) == "Point(x=10, y=20)"
    assert str(price) == "1200 JPY"
    assert repr(price) == "Money(amount=1200, currency='JPY')"
    assert repr(first_task) == "Task(title='write docs', priority=2)"
    assert str(first_task) == "write docs / priority=2"
    assert first_task == second_task
    assert first_task != third_task
