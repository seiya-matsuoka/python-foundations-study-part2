"""csv による表形式データの読み書きを確認するサンプル。"""

import csv
from pathlib import Path
from typing import TypedDict

UNIT_DIR = Path(__file__).parent
SAMPLE_DATA_DIR = UNIT_DIR / "sample_data"
GENERATED_DIR = SAMPLE_DATA_DIR / "generated"


class ScoreRecord(TypedDict):
    """CSV から読み込んだ点数データの形。"""

    id: int
    name: str
    score: int


def load_scores(path: Path) -> list[ScoreRecord]:
    """CSV ファイルから点数一覧を読み込む。"""
    scores = []

    # csv.DictReader は、ヘッダー行をキーとして各行を dict で返す。
    # CSV から読んだ値は文字列になるため、必要に応じて型変換する。
    with open(path, encoding="utf-8", newline="") as file:  # noqa: PTH123
        reader = csv.DictReader(file)

        for row in reader:
            scores.append(
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "score": int(row["score"]),
                }
            )

    return scores


def write_scores(path: Path, scores: list[ScoreRecord]) -> None:
    """点数一覧を CSV ファイルとして書き込む。"""
    fieldnames = ["id", "name", "score"]

    with open(path, mode="w", encoding="utf-8", newline="") as file:  # noqa: PTH123
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for score in scores:
            writer.writerow(score)


def run_csv_operations() -> None:
    """CSV の読み込み、加工、書き込みを確認する。"""

    input_path = SAMPLE_DATA_DIR / "users.csv"
    output_path = GENERATED_DIR / "passed_users.csv"

    GENERATED_DIR.mkdir(exist_ok=True)

    scores = load_scores(input_path)
    print(f"scores: {scores}")

    passed_scores = [score for score in scores if score["score"] >= 80]
    print(f"passed_scores: {passed_scores}")

    write_scores(output_path, passed_scores)
    written_scores = load_scores(output_path)

    print(f"written_scores: {written_scores}")
    print(f"output_path exists: {output_path.exists()}")

    # CSV は表形式のテキストデータとして扱える。
    # 数値として扱いたい列は、読み込み時に int などへ変換する。
    average_score = sum(score["score"] for score in scores) / len(scores)
    print(f"average_score: {average_score}")

    assert scores == [
        {"id": 1, "name": "Sora", "score": 80},
        {"id": 2, "name": "Mio", "score": 95},
        {"id": 3, "name": "Ren", "score": 70},
    ]
    assert passed_scores == [
        {"id": 1, "name": "Sora", "score": 80},
        {"id": 2, "name": "Mio", "score": 95},
    ]
    assert written_scores == passed_scores
    assert output_path.exists()
    assert average_score == 245 / 3
