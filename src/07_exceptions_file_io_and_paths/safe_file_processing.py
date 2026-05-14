"""例外処理を含むファイル処理を確認するサンプル。"""

from pathlib import Path

UNIT_DIR = Path(__file__).parent
SAMPLE_DATA_DIR = UNIT_DIR / "sample_data"


def load_numbers(path: Path) -> list[int]:
    """テキストファイルから整数だけを読み込む。"""
    numbers = []

    # ファイルが存在しない場合、open は FileNotFoundError を送出する。
    # この関数では、その例外は呼び出し側に伝える。
    with open(path, encoding="utf-8") as file:  # noqa: PTH123
        for line in file:
            stripped_line = line.strip()

            try:
                number = int(stripped_line)
            except ValueError:
                continue

            numbers.append(number)

    return numbers


def require_file(path: Path) -> Path:
    """ファイルが存在することを確認し、存在しなければ例外を送出する。"""
    if not path.exists():
        raise FileNotFoundError(f"file not found: {path}")

    if not path.is_file():
        raise ValueError(f"path is not a file: {path}")

    return path


def run_safe_file_processing() -> None:
    """例外処理を含むファイル処理を確認する。"""

    numbers_path = SAMPLE_DATA_DIR / "numbers.txt"
    checked_path = require_file(numbers_path)

    numbers = load_numbers(checked_path)
    total = sum(numbers)

    print(f"numbers: {numbers}")
    print(f"total: {total}")

    missing_path = SAMPLE_DATA_DIR / "missing.txt"

    try:
        require_file(missing_path)
    except FileNotFoundError as error:
        missing_error_message = str(error)
    else:
        missing_error_message = ""

    print(f"missing_error_message: {missing_error_message}")

    assert checked_path == numbers_path
    assert numbers == [10, 20, 30]
    assert total == 60
    assert "file not found:" in missing_error_message
    assert "missing.txt" in missing_error_message
