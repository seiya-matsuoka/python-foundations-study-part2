"""math、random、statistics の基本を確認するサンプル。"""

import math
import random
import statistics


def run_math_random_statistics_examples() -> None:
    """数値処理、乱数、統計の基本的な関数を確認する。"""

    # math は数学系の関数や定数を提供する。
    # 平方根、切り上げ、切り捨てなどを自前で実装せずに使える。
    square_root = math.sqrt(81)
    rounded_up = math.ceil(3.2)
    rounded_down = math.floor(3.8)
    circle_area = math.pi * 3 * 3

    print(f"square_root: {square_root}")
    print(f"rounded_up: {rounded_up}")
    print(f"rounded_down: {rounded_down}")
    print(f"circle_area: {circle_area}")

    # random は乱数を扱う標準ライブラリ。
    # 学習用やテスト用では、Random に seed を渡すと結果を固定できる。
    rng = random.Random(42)

    random_number = rng.randint(1, 10)
    selected_language = rng.choice(["Python", "Java", "SQL"])
    shuffled_numbers = [1, 2, 3, 4, 5]
    rng.shuffle(shuffled_numbers)

    print(f"random_number: {random_number}")
    print(f"selected_language: {selected_language}")
    print(f"shuffled_numbers: {shuffled_numbers}")

    # statistics は平均、中央値などの基本的な統計処理を提供する。
    scores = [80, 95, 70, 85, 90]
    average_score = statistics.mean(scores)
    median_score = statistics.median(scores)
    highest_frequency = statistics.mode([1, 2, 2, 3, 3, 3])

    print(f"average_score: {average_score}")
    print(f"median_score: {median_score}")
    print(f"highest_frequency: {highest_frequency}")

    assert square_root == 9
    assert rounded_up == 4
    assert rounded_down == 3
    assert round(circle_area, 2) == 28.27
    assert random_number == 2
    assert selected_language == "Python"
    assert shuffled_numbers == [4, 5, 1, 2, 3]
    assert average_score == 84
    assert median_score == 85
    assert highest_frequency == 3
