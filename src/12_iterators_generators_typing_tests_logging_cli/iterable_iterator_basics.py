"""iterable と iterator、iter、next の基本を確認するサンプル。"""


def run_iterable_iterator_basics() -> None:
    """iterable と iterator の違い、iter、next の動きを確認する。"""

    # iterable は「for で繰り返せるもの」と考えると入口として理解しやすい。
    # list、tuple、dict、set、文字列などは iterable として扱える。
    languages = ["Python", "Java", "SQL"]

    collected_languages = []

    for language in languages:
        collected_languages.append(language.lower())

    print(f"collected_languages: {collected_languages}")

    # iter は、iterable から iterator を作るための関数。
    # iterator は next で1つずつ値を取り出せるオブジェクト。
    language_iterator = iter(languages)

    first_language = next(language_iterator)
    second_language = next(language_iterator)
    third_language = next(language_iterator)

    print(f"first_language: {first_language}")
    print(f"second_language: {second_language}")
    print(f"third_language: {third_language}")

    # iterator は「現在どこまで取り出したか」という状態を持つ。
    # 取り出し済みの iterator を list にすると、残っている要素だけが得られる。
    partially_used_iterator = iter([10, 20, 30, 40])
    first_number = next(partially_used_iterator)
    remaining_numbers = list(partially_used_iterator)

    print(f"first_number: {first_number}")
    print(f"remaining_numbers: {remaining_numbers}")

    # next は、もう値が残っていない場合に StopIteration を送出する。
    # for 文は内部で StopIteration を見て、ループを終了している。
    empty_iterator = iter([])

    try:
        next(empty_iterator)
    except StopIteration:
        stop_iteration_detected = True
    else:
        stop_iteration_detected = False

    print(f"stop_iteration_detected: {stop_iteration_detected}")

    # dict をそのまま iter すると、キーを順番に取り出す iterator になる。
    # 値やキーと値の組を扱いたい場合は values() や items() を使う。
    user = {
        "name": "Sora",
        "language": "Python",
    }
    user_key_iterator = iter(user)
    first_key = next(user_key_iterator)
    second_key = next(user_key_iterator)

    print(f"first_key: {first_key}")
    print(f"second_key: {second_key}")

    assert collected_languages == ["python", "java", "sql"]
    assert first_language == "Python"
    assert second_language == "Java"
    assert third_language == "SQL"
    assert first_number == 10
    assert remaining_numbers == [20, 30, 40]
    assert stop_iteration_detected is True
    assert first_key == "name"
    assert second_key == "language"
