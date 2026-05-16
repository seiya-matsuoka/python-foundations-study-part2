"""__iter__ と __next__ による独自 iterator を確認するサンプル。"""


class CountDown:
    """指定した数から 1 まで数える iterator。"""

    def __init__(self, start: int) -> None:
        """開始値を受け取って初期化する。"""
        self.current = start

    def __iter__(self) -> "CountDown":
        """iterator 自身を返す。"""
        # iterator は __iter__ で自分自身を返すことが多い。
        # for 文は iter(obj) を呼び、その結果に対して next を繰り返す。
        return self

    def __next__(self) -> int:
        """次の値を返す。残りがなければ StopIteration を送出する。"""
        # __next__ は、次に取り出す値を返すための特殊メソッド。
        # 値がなくなった場合は StopIteration を送出する。
        if self.current <= 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value


class RepeatValue:
    """同じ値を指定回数だけ返す iterable。"""

    def __init__(self, value: str, count: int) -> None:
        """繰り返す値と回数を受け取って初期化する。"""
        self.value = value
        self.count = count

    def __iter__(self):
        """値を指定回数だけ生成する generator を返す。"""
        # __iter__ は、必ずしも self を返す必要はない。
        # ここでは generator を返すことで、for 文で繰り返せる iterable にしている。
        for _ in range(self.count):
            yield self.value


def run_custom_iterator() -> None:
    """__iter__ / __next__ と独自 iterable を確認する。"""

    count_down = CountDown(3)

    first_value = next(count_down)
    second_value = next(count_down)
    remaining_values = list(count_down)

    print(f"first_value: {first_value}")
    print(f"second_value: {second_value}")
    print(f"remaining_values: {remaining_values}")

    # CountDown は iterator 自身が状態を持つため、一度使うと消費される。
    # もう一度 3, 2, 1 を取り出したい場合は、新しい CountDown を作る。
    consumed_values = list(count_down)
    fresh_values = list(CountDown(3))

    print(f"consumed_values: {consumed_values}")
    print(f"fresh_values: {fresh_values}")

    # RepeatValue は __iter__ が generator を返す iterable。
    # list に変換するたびに、新しい generator が作られる。
    repeated = RepeatValue("Python", 3)
    first_repeated = list(repeated)
    second_repeated = list(repeated)

    print(f"first_repeated: {first_repeated}")
    print(f"second_repeated: {second_repeated}")

    assert first_value == 3
    assert second_value == 2
    assert remaining_values == [1]
    assert consumed_values == []
    assert fresh_values == [3, 2, 1]
    assert first_repeated == ["Python", "Python", "Python"]
    assert second_repeated == ["Python", "Python", "Python"]
