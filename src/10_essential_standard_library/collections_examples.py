"""collections の代表的な機能を確認するサンプル。"""

from collections import Counter, defaultdict, deque


def run_collections_examples() -> None:
    """Counter、defaultdict、deque の基本的な使い方を確認する。"""

    # Counter は、要素ごとの出現回数を数えるために使える。
    # 自分で dict を用意して数える処理を簡潔に書ける。
    words = ["python", "java", "python", "sql", "python", "sql"]
    word_counts = Counter(words)

    print(f"word_counts: {word_counts}")
    print(f"python count: {word_counts['python']}")

    # most_common は、出現回数が多い順に要素を取り出す。
    most_common_words = word_counts.most_common(2)
    print(f"most_common_words: {most_common_words}")

    # defaultdict は、存在しないキーを参照したときの初期値を決められる。
    # list を指定すると、キーごとに list を作って値を追加しやすい。
    score_rows = [
        ("backend", 80),
        ("frontend", 90),
        ("backend", 75),
        ("database", 85),
    ]
    scores_by_category: defaultdict[str, list[int]] = defaultdict(list)

    for category, score in score_rows:
        scores_by_category[category].append(score)

    print(f"scores_by_category: {dict(scores_by_category)}")

    # deque は、両端への追加や削除に向いたコレクション。
    # maxlen を指定すると、一定件数だけ保持する用途にも使える。
    recent_events: deque[str] = deque(maxlen=3)

    recent_events.append("login")
    recent_events.append("view")
    recent_events.append("edit")
    recent_events.append("logout")

    print(f"recent_events: {list(recent_events)}")

    # appendleft や popleft により、先頭側の追加や取り出しもできる。
    queue: deque[str] = deque()
    queue.append("task-1")
    queue.append("task-2")
    queue.appendleft("urgent-task")

    first_task = queue.popleft()
    second_task = queue.popleft()

    print(f"first_task: {first_task}")
    print(f"second_task: {second_task}")
    print(f"remaining_queue: {list(queue)}")

    assert word_counts == Counter({"python": 3, "sql": 2, "java": 1})
    assert word_counts["python"] == 3
    assert most_common_words == [("python", 3), ("sql", 2)]
    assert dict(scores_by_category) == {
        "backend": [80, 75],
        "frontend": [90],
        "database": [85],
    }
    assert list(recent_events) == ["view", "edit", "logout"]
    assert first_task == "urgent-task"
    assert second_task == "task-1"
    assert list(queue) == ["task-2"]
