"""yield、ジェネレータ関数、ジェネレータ式を確認するサンプル。"""


def generate_even_numbers(limit: int):
    """0 以上 limit 未満の偶数を1つずつ生成する。"""
    # yield を含む関数は、通常の戻り値を返す関数ではなくジェネレータ関数になる。
    # 呼び出した時点では処理全体は実行されず、値が必要になったタイミングで進む。
    number = 0

    while number < limit:
        if number % 2 == 0:
            yield number

        number += 1


def read_until_empty(lines: list[str]):
    """空文字列が出るまで、前後空白を取り除いた行を生成する。"""
    # yield は「途中まで処理して値を返し、次回その続きから再開する」動きになる。
    # ファイル読み込みや大量データ処理のように、少しずつ処理したい場面と相性がよい。
    for line in lines:
        stripped_line = line.strip()

        if stripped_line == "":
            break

        yield stripped_line


def run_generator_examples() -> None:
    """ジェネレータ関数とジェネレータ式の動きを確認する。"""

    even_generator = generate_even_numbers(10)

    first_even = next(even_generator)
    second_even = next(even_generator)
    remaining_even_numbers = list(even_generator)

    print(f"first_even: {first_even}")
    print(f"second_even: {second_even}")
    print(f"remaining_even_numbers: {remaining_even_numbers}")

    # ジェネレータ関数は、for 文でも自然に使える。
    # list に変換すると、生成される値をまとめて確認できる。
    all_even_numbers = list(generate_even_numbers(8))
    print(f"all_even_numbers: {all_even_numbers}")

    raw_lines = ["  Python  ", " Java ", "", "SQL"]
    non_empty_lines = list(read_until_empty(raw_lines))

    print(f"non_empty_lines: {non_empty_lines}")

    # ジェネレータ式は、内包表記に似た書き方で iterator を作る。
    # list を先に作らず、sum などに直接渡せる。
    scores = [80, 95, 70]
    total_score = sum(score for score in scores)
    high_scores = list(score for score in scores if score >= 80)

    print(f"total_score: {total_score}")
    print(f"high_scores: {high_scores}")

    # ジェネレータは一度消費されると、同じ値をもう一度取り出せない。
    # 再利用したい場合は、新しいジェネレータを作り直す。
    word_generator = (word.upper() for word in ["python", "java"])
    upper_words = list(word_generator)
    empty_after_consumed = list(word_generator)

    print(f"upper_words: {upper_words}")
    print(f"empty_after_consumed: {empty_after_consumed}")

    assert first_even == 0
    assert second_even == 2
    assert remaining_even_numbers == [4, 6, 8]
    assert all_even_numbers == [0, 2, 4, 6]
    assert non_empty_lines == ["Python", "Java"]
    assert total_score == 245
    assert high_scores == [80, 95]
    assert upper_words == ["PYTHON", "JAVA"]
    assert empty_after_consumed == []
