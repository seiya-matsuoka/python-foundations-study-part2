"""split、join、strip による文字列処理を確認するサンプル。"""


def run_string_methods() -> None:
    """split、join、strip を使った文字列加工を確認する。"""

    # strip は、文字列の前後にある空白や改行を取り除く。
    # 入力ファイルやフォーム入力では、前後に余計な空白が含まれることがある。
    raw_language_line = "  Python, Java, SQL  "
    cleaned_language_line = raw_language_line.strip()

    print(f"raw_language_line: {raw_language_line!r}")
    print(f"cleaned_language_line: {cleaned_language_line!r}")

    # split は、指定した区切り文字で文字列を分割する。
    # ここではカンマ区切りの文字列を list にしている。
    raw_languages = cleaned_language_line.split(",")

    # 分割した直後は、各要素の前後に空白が残ることがある。
    # 内包表記と strip を組み合わせて、各要素を整える。
    languages = [language.strip() for language in raw_languages]

    print(f"raw_languages: {raw_languages}")
    print(f"languages: {languages}")

    # join は、複数の文字列を指定した区切り文字で結合する。
    # list[str] を1つの文字列に戻したい場合に使う。
    joined_by_slash = " / ".join(languages)
    joined_by_new_line = "\n".join(languages)

    print(f"joined_by_slash: {joined_by_slash}")
    print(f"joined_by_new_line:\n{joined_by_new_line}")

    # split は、引数を省略すると連続する空白をまとめて区切りとして扱う。
    # 単語単位で分割したい場合に使いやすい。
    sentence = "Python   is  easy to read"
    words = sentence.split()

    print(f"words: {words}")

    assert cleaned_language_line == "Python, Java, SQL"
    assert raw_languages == ["Python", " Java", " SQL"]
    assert languages == ["Python", "Java", "SQL"]
    assert joined_by_slash == "Python / Java / SQL"
    assert joined_by_new_line == "Python\nJava\nSQL"
    assert words == ["Python", "is", "easy", "to", "read"]
