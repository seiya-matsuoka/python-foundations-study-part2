"""datetime による日時処理の基本を確認するサンプル。"""

from datetime import date, datetime, timedelta


def run_datetime_examples() -> None:
    """date、datetime、timedelta、文字列変換を確認する。"""

    # date は日付だけを表す。
    # 年、月、日を指定して作成できる。
    release_date = date(2026, 5, 15)
    print(f"release_date: {release_date}")

    # datetime は日付と時刻をまとめて表す。
    # ログ時刻や作成日時のような値を扱うときに使える。
    started_at = datetime(2026, 5, 15, 9, 30, 0)
    print(f"started_at: {started_at}")

    # timedelta は日時の差分を表す。
    # 日付や時刻に足したり、引いたりできる。
    review_period = timedelta(days=7)
    review_date = release_date + review_period

    print(f"review_period: {review_period}")
    print(f"review_date: {review_date}")

    # 日付同士の差分も timedelta になる。
    remaining_days = review_date - release_date
    print(f"remaining_days: {remaining_days.days}")

    # strftime は、日時を指定した形式の文字列に変換する。
    formatted_date = release_date.strftime("%Y/%m/%d")
    formatted_datetime = started_at.strftime("%Y-%m-%d %H:%M:%S")

    print(f"formatted_date: {formatted_date}")
    print(f"formatted_datetime: {formatted_datetime}")

    # strptime は、文字列を datetime に変換する。
    # 文字列の形式とフォーマット指定が一致している必要がある。
    parsed_datetime = datetime.strptime(
        "2026-05-15 09:30:00",
        "%Y-%m-%d %H:%M:%S",
    )

    print(f"parsed_datetime: {parsed_datetime}")

    assert release_date == date(2026, 5, 15)
    assert started_at == datetime(2026, 5, 15, 9, 30, 0)
    assert review_date == date(2026, 5, 22)
    assert remaining_days.days == 7
    assert formatted_date == "2026/05/15"
    assert formatted_datetime == "2026-05-15 09:30:00"
    assert parsed_datetime == started_at
