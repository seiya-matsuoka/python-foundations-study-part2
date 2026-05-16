"""assert と unittest の基本を確認するサンプル。"""

import io
import unittest


def calculate_grade(score: int) -> str:
    """点数から評価文字列を返す。"""
    if score >= 90:
        return "A"

    if score >= 80:
        return "B"

    if score >= 70:
        return "C"

    return "D"


def is_passing(score: int) -> bool:
    """合格点に達しているかを返す。"""
    return score >= 70


class GradeTestCase(unittest.TestCase):
    """unittest を使った評価関数のテスト。"""

    def test_calculate_grade(self) -> None:
        """点数ごとの評価文字列を確認する。"""
        # self.assertEqual は、期待値と実際の値が等しいことを確認する。
        # 通常の assert より、テスト失敗時の情報が読みやすい。
        self.assertEqual(calculate_grade(95), "A")
        self.assertEqual(calculate_grade(85), "B")
        self.assertEqual(calculate_grade(75), "C")
        self.assertEqual(calculate_grade(60), "D")

    def test_is_passing(self) -> None:
        """合格判定を確認する。"""
        self.assertTrue(is_passing(70))
        self.assertTrue(is_passing(100))
        self.assertFalse(is_passing(69))


def run_unittest_suite() -> tuple[bool, int, int]:
    """GradeTestCase を実行し、成功可否、実行数、失敗数を返す。"""
    # unittest.TestLoader は、TestCase からテストスイートを組み立てる。
    # TextTestRunner は、テストスイートを実行するための runner。
    stream = io.StringIO()
    suite = unittest.TestLoader().loadTestsFromTestCase(GradeTestCase)
    result = unittest.TextTestRunner(stream=stream, verbosity=0).run(suite)

    return result.wasSuccessful(), result.testsRun, len(result.failures)


def run_assertion_and_unittest_examples() -> None:
    """assert と unittest の基本を確認する。"""

    # assert は、簡単な期待値確認に使える。
    # 式が False になると AssertionError が発生する。
    grade = calculate_grade(88)
    passing = is_passing(88)

    print(f"grade: {grade}")
    print(f"passing: {passing}")

    suite_successful, tests_run, failure_count = run_unittest_suite()

    print(f"suite_successful: {suite_successful}")
    print(f"tests_run: {tests_run}")
    print(f"failure_count: {failure_count}")

    assert grade == "B"
    assert passing is True
    assert suite_successful is True
    assert tests_run == 2
    assert failure_count == 0
