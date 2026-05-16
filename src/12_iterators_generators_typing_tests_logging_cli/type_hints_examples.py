"""型ヒントの基本を確認するサンプル。"""

from typing import Optional, TypeAlias

# type alias は、複雑な型や意味を持たせたい型に名前を付けるために使える。
# Python 3.12 以降には type 文もあるが、ここでは互換性が高い TypeAlias を扱う。
UserId: TypeAlias = int  # noqa: UP040
ScoreMap: TypeAlias = dict[str, int]  # noqa: UP040
MaybeText: TypeAlias = str | None  # noqa: UP040


def find_score(scores: ScoreMap, name: str) -> Optional[int]:  # noqa: UP045
    """名前に対応する点数を返す。見つからない場合は None を返す。"""
    # Optional[int] は int | None と同じ意味で使える。
    # 既存コードやライブラリでは Optional の表記もよく見かける。
    return scores.get(name)


def build_user_label(user_id: UserId, name: str, nickname: MaybeText = None) -> str:
    """ユーザーID、名前、任意のニックネームから表示名を作る。"""
    # nickname は str または None を受け取る。
    # None の可能性がある値は、使う前に分岐して扱うと安全になる。
    if nickname is None:  # noqa: SIM108
        display_name = name
    else:
        display_name = f"{name}({nickname})"

    return f"#{user_id}: {display_name}"


def summarize_scores(scores: list[int]) -> tuple[int, int, float]:
    """点数 list から件数、合計、平均を返す。"""
    # list[int] は int の list を表す。
    # 戻り値の tuple[int, int, float] は、戻る値の並びを型として表している。
    count = len(scores)
    total = sum(scores)

    if count == 0:  # noqa: SIM108
        average = 0.0
    else:
        average = total / count

    return count, total, average


def normalize_tags(tags: set[str]) -> list[str]:
    """タグ set を小文字の sorted list に変換する。"""
    # set[str] や list[str] のように、コレクション内の要素型も書ける。
    # sorted は list を返すため、戻り値は list[str] になる。
    normalized_tags = []

    for tag in tags:
        normalized_tags.append(tag.lower())

    return sorted(normalized_tags)


def run_type_hints_examples() -> None:
    """変数、引数、戻り値、コレクション型、Optional、|、type alias を確認する。"""

    # 変数にも型ヒントを書ける。
    # ただし、型ヒントは主に静的解析やエディタ支援のための情報である。
    user_id: UserId = 101
    scores: ScoreMap = {
        "Sora": 80,
        "Mio": 95,
    }

    sora_score = find_score(scores, "Sora")
    missing_score = find_score(scores, "Ren")

    print(f"sora_score: {sora_score}")
    print(f"missing_score: {missing_score}")

    label_without_nickname = build_user_label(user_id, "Sora")
    label_with_nickname = build_user_label(user_id, "Sora", "sky")

    print(f"label_without_nickname: {label_without_nickname}")
    print(f"label_with_nickname: {label_with_nickname}")

    count, total, average = summarize_scores([80, 95, 70])
    print(f"count: {count}")
    print(f"total: {total}")
    print(f"average: {average}")

    tags = {"Python", "CLI", "python"}
    normalized_tags = normalize_tags(tags)
    print(f"normalized_tags: {normalized_tags}")

    assert user_id == 101
    assert sora_score == 80
    assert missing_score is None
    assert label_without_nickname == "#101: Sora"
    assert label_with_nickname == "#101: Sora(sky)"
    assert count == 3
    assert total == 245
    assert average == 245 / 3
    assert normalized_tags == ["cli", "python", "python"]
