"""抽象基底クラスと Enum の最小限を確認するサンプル。"""

from abc import ABC, abstractmethod
from enum import Enum


class TaskStatus(Enum):
    """タスク状態を表す Enum。"""

    TODO = "todo"
    DOING = "doing"
    DONE = "done"


class Formatter(ABC):
    """文字列整形を行う抽象基底クラス。"""

    @abstractmethod
    def format(self, text: str) -> str:
        """文字列を整形する。"""
        raise NotImplementedError


class UpperFormatter(Formatter):
    """文字列を大文字にする Formatter。"""

    def format(self, text: str) -> str:
        """文字列を大文字に変換する。"""
        return text.upper()


class PrefixFormatter(Formatter):
    """文字列に接頭辞を付ける Formatter。"""

    def __init__(self, prefix: str) -> None:
        """接頭辞を受け取って初期化する。"""
        self.prefix = prefix

    def format(self, text: str) -> str:
        """文字列に接頭辞を付ける。"""
        return f"{self.prefix}{text}"


def apply_formatter(formatter: Formatter, text: str) -> str:
    """Formatter を使って文字列を整形する。"""
    return formatter.format(text)


def build_status_label(status: TaskStatus) -> str:
    """TaskStatus から表示用ラベルを作る。"""
    if status is TaskStatus.TODO:
        return "未着手"

    if status is TaskStatus.DOING:
        return "作業中"

    return "完了"


def run_abc_and_enum() -> None:
    """抽象基底クラスと Enum の基本を確認する。"""

    upper_formatter = UpperFormatter()
    prefix_formatter = PrefixFormatter("INFO: ")

    upper_text = apply_formatter(upper_formatter, "python")
    prefixed_text = apply_formatter(prefix_formatter, "started")

    print(f"upper_text: {upper_text}")
    print(f"prefixed_text: {prefixed_text}")

    todo_label = build_status_label(TaskStatus.TODO)
    doing_label = build_status_label(TaskStatus.DOING)
    done_label = build_status_label(TaskStatus.DONE)

    print(f"todo_label: {todo_label}")
    print(f"doing_label: {doing_label}")
    print(f"done_label: {done_label}")
    print(f"TaskStatus.TODO.value: {TaskStatus.TODO.value}")

    assert upper_text == "PYTHON"
    assert prefixed_text == "INFO: started"
    assert todo_label == "未着手"
    assert doing_label == "作業中"
    assert done_label == "完了"
    assert TaskStatus.TODO.value == "todo"
    assert TaskStatus("done") is TaskStatus.DONE
