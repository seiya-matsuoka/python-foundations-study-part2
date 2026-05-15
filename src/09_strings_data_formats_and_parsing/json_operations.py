"""json による標準データ形式の読み書きを確認するサンプル。"""

import json
from pathlib import Path
from typing import TypedDict, cast

UNIT_DIR = Path(__file__).parent
SAMPLE_DATA_DIR = UNIT_DIR / "sample_data"
GENERATED_DIR = SAMPLE_DATA_DIR / "generated"


class UserRecord(TypedDict):
    """JSON で扱うユーザーデータの形。"""

    id: int
    name: str
    active: bool


def load_users(path: Path) -> list[UserRecord]:
    """JSON ファイルからユーザー一覧を読み込む。"""
    # json.load は、ファイルオブジェクトから JSON を読み込む。
    # 返り値の型は実行時の JSON 内容に依存するため、ここでは cast で形を明示する。
    with open(path, encoding="utf-8") as file:  # noqa: PTH123
        loaded_data = json.load(file)

    return cast(list[UserRecord], loaded_data)


def write_users(path: Path, users: list[UserRecord]) -> None:
    """ユーザー一覧を JSON ファイルとして書き込む。"""
    # ensure_ascii=False にすると、日本語なども読みやすい形で出力できる。
    # indent=2 にすると、人間が読みやすい整形済み JSON になる。
    with open(path, mode="w", encoding="utf-8") as file:  # noqa: PTH123
        json.dump(users, file, ensure_ascii=False, indent=2)


def run_json_operations() -> None:
    """JSON の読み込み、加工、書き込みを確認する。"""

    input_path = SAMPLE_DATA_DIR / "users.json"
    output_path = GENERATED_DIR / "active_users.json"

    GENERATED_DIR.mkdir(exist_ok=True)

    users = load_users(input_path)
    print(f"users: {users}")

    # JSON から読み込んだデータも、Python 側では list / dict として扱える。
    active_users = [user for user in users if user["active"]]
    print(f"active_users: {active_users}")

    write_users(output_path, active_users)
    written_users = load_users(output_path)

    print(f"written_users: {written_users}")
    print(f"output_path exists: {output_path.exists()}")

    # json.dumps は、Python の値を JSON 文字列へ変換する。
    # ファイルではなく文字列として確認したい場合に使う。
    json_text = json.dumps(active_users, ensure_ascii=False)
    print(f"json_text: {json_text}")

    assert users == [
        {"id": 1, "name": "Sora", "active": True},
        {"id": 2, "name": "Mio", "active": False},
    ]
    assert active_users == [{"id": 1, "name": "Sora", "active": True}]
    assert written_users == [{"id": 1, "name": "Sora", "active": True}]
    assert output_path.exists()
    assert json_text == '[{"id": 1, "name": "Sora", "active": true}]'
