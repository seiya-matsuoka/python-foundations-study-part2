"""文字列処理を再利用可能な関数としてまとめたモジュール。"""

DEFAULT_SEPARATOR = " / "


def normalize_name(name: str) -> str:
    """前後の空白を取り除き、単語の先頭を大文字にそろえる。"""
    # strip は前後の空白を取り除く。
    # split は連続した空白を区切りとして単語に分ける。
    words = name.strip().split()
    normalized_words = []

    for word in words:
        normalized_words.append(word.capitalize())

    return " ".join(normalized_words)


def build_slug(text: str) -> str:
    """表示名から URL や識別子で使いやすい文字列を作る。"""
    # lower で小文字化し、split / join で空白をハイフンに置き換える。
    # 実務ではより多くの文字種を考慮するが、ここでは学習用に単純化する。
    words = text.strip().lower().split()
    return "-".join(words)


def join_labels(labels: list[str], separator: str = DEFAULT_SEPARATOR) -> str:
    """ラベルの list を1つの文字列に連結する。"""
    return separator.join(labels)
