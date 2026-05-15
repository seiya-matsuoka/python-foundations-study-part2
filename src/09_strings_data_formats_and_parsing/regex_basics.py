"""re による正規表現の基礎を確認するサンプル。"""

import re

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def mask_email(text: str) -> str:
    """文字列内のメールアドレスをマスクする。"""
    # r"..." のような raw string は、正規表現でよく使う。
    # バックスラッシュを通常の文字列より扱いやすくするためである。
    return re.sub(EMAIL_PATTERN, "[EMAIL]", text)


def run_regex_basics() -> None:
    """正規表現による検索、抽出、置換を確認する。"""

    text = "Contact sora@example.com or mio@example.org by 2026-05-15."

    # re.search は、条件に合う箇所があるかを探す。
    # 見つかった場合は Match オブジェクト、見つからない場合は None を返す。
    first_match = re.search(EMAIL_PATTERN, text)

    if first_match is None:  # noqa: SIM108
        first_email = ""
    else:
        first_email = first_match.group()

    print(f"first_email: {first_email}")

    # re.findall は、条件に合う文字列をすべて list として返す。
    emails = re.findall(EMAIL_PATTERN, text)
    print(f"emails: {emails}")

    # 日付のように形が決まっている文字列も抽出できる。
    date_match = re.search(r"\d{4}-\d{2}-\d{2}", text)

    if date_match is None:  # noqa: SIM108
        date_text = ""
    else:
        date_text = date_match.group()

    print(f"date_text: {date_text}")

    # re.sub は、正規表現に一致した部分を置換する。
    masked_text = mask_email(text)
    print(f"masked_text: {masked_text}")

    # re.split は、正規表現に一致した区切りで分割する。
    raw_tags = "python, java;sql  pathlib"
    tags = re.split(r"[,;\s]+", raw_tags)

    print(f"tags: {tags}")

    assert first_email == "sora@example.com"
    assert emails == ["sora@example.com", "mio@example.org"]
    assert date_text == "2026-05-15"
    assert masked_text == "Contact [EMAIL] or [EMAIL] by 2026-05-15."
    assert tags == ["python", "java", "sql", "pathlib"]
