"""class、__init__、インスタンス属性、インスタンスメソッドを確認するサンプル。"""


class User:
    """学習用のユーザーを表すクラス。"""

    # クラス属性は、クラスに属する属性。
    # すべてのインスタンスで共有する既定値や共通設定を表すときに使える。
    default_status = "active"

    def __init__(self, name: str, age: int) -> None:
        """インスタンス生成時に呼び出される初期化処理。"""
        # self.name や self.age はインスタンス属性。
        # インスタンスごとに異なる値を持てる。
        self.name = name
        self.age = age
        self.status = User.default_status

    def describe(self) -> str:
        """ユーザー情報を表示用の文字列にする。"""
        # インスタンスメソッドの第1引数 self は、呼び出し元のインスタンスを表す。
        # Java の this に近いが、Python では明示的に self と書く。
        return f"{self.name}({self.age}) is {self.status}"

    def is_adult(self) -> bool:
        """成人かどうかを返す。"""
        return self.age >= 18

    def deactivate(self) -> None:
        """ユーザー状態を無効にする。"""
        # インスタンス属性を書き換えると、そのインスタンスの状態が変わる。
        self.status = "inactive"


def run_class_basics() -> None:
    """クラス定義、属性、インスタンスメソッドを確認する。"""

    sora = User("Sora", 20)
    mio = User("Mio", 16)

    sora_description = sora.describe()
    mio_description = mio.describe()

    print(f"sora_description: {sora_description}")
    print(f"mio_description: {mio_description}")
    print(f"sora is adult: {sora.is_adult()}")
    print(f"mio is adult: {mio.is_adult()}")
    print(f"User.default_status: {User.default_status}")

    sora.deactivate()
    deactivated_description = sora.describe()

    print(f"deactivated_description: {deactivated_description}")
    print(f"mio.status: {mio.status}")

    assert sora_description == "Sora(20) is active"
    assert mio_description == "Mio(16) is active"
    assert sora.is_adult() is True
    assert mio.is_adult() is False
    assert User.default_status == "active"
    assert deactivated_description == "Sora(20) is inactive"
    assert mio.status == "active"
