"""検索、部分文字列の判定、replace を確認するサンプル。"""


def run_search_and_replace() -> None:
    """文字列検索、部分文字列の判定、置換を確認する。"""

    message = "Learning Python basics with Python examples."

    # in は、部分文字列が含まれるかを確認する。
    # 結果は True / False になる。
    contains_python = "Python" in message
    contains_java = "Java" in message

    print(f"contains_python: {contains_python}")
    print(f"contains_java: {contains_java}")

    # find は、見つかった位置のインデックスを返す。
    # 見つからない場合は -1 を返す。
    python_index = message.find("Python")
    java_index = message.find("Java")

    print(f"python_index: {python_index}")
    print(f"java_index: {java_index}")

    # startswith / endswith は、先頭や末尾の判定に使う。
    starts_with_learning = message.startswith("Learning")
    ends_with_examples = message.endswith("examples.")

    print(f"starts_with_learning: {starts_with_learning}")
    print(f"ends_with_examples: {ends_with_examples}")

    # replace は、指定した文字列を別の文字列に置き換える。
    # 元の文字列は変更されず、新しい文字列が返る。
    replaced_message = message.replace("Python", "JavaScript")

    print(f"message: {message}")
    print(f"replaced_message: {replaced_message}")

    # count は、指定した部分文字列の出現回数を数える。
    python_count = message.count("Python")
    print(f"python_count: {python_count}")

    assert contains_python is True
    assert contains_java is False
    assert python_index == 9
    assert java_index == -1
    assert starts_with_learning is True
    assert ends_with_examples is True
    assert replaced_message == ("Learning JavaScript basics with JavaScript examples.")
    assert message == "Learning Python basics with Python examples."
    assert python_count == 2
