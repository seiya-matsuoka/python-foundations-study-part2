"""合成と duck typing の基本を確認するサンプル。"""

from typing import Protocol


class Sender(Protocol):
    """send メソッドを持つオブジェクトの形。"""

    def send(self, message: str) -> str:
        """メッセージを送信する。"""
        ...


class ConsoleSender:
    """コンソール出力の送信役。"""

    def send(self, message: str) -> str:
        """コンソールへ送る想定の文字列を返す。"""
        return f"console: {message}"


class MemorySender:
    """送信内容をメモリ上に保存する送信役。"""

    def __init__(self) -> None:
        """送信履歴を初期化する。"""
        self.messages: list[str] = []

    def send(self, message: str) -> str:
        """メッセージを履歴に保存し、結果文字列を返す。"""
        self.messages.append(message)
        return f"memory: {message}"


class ReportService:
    """レポート作成と送信を行うサービス。"""

    def __init__(self, sender: Sender) -> None:
        """送信役を受け取って初期化する。"""
        # 合成では、別のオブジェクトを属性として持ち、処理を委譲する。
        # 継承よりも、部品を差し替えやすい構成にできる。
        self.sender = sender

    def send_report(self, title: str, lines: list[str]) -> str:
        """レポート本文を組み立てて送信する。"""
        body = "\n".join(lines)
        message = f"{title}\n{body}"
        return self.sender.send(message)


def deliver_message(sender: Sender, message: str) -> str:
    """send メソッドを持つオブジェクトにメッセージを渡す。"""
    # Python では、継承関係よりも「必要なメソッドを持つか」を重視して扱える。
    # これが duck typing の基本的な考え方である。
    return sender.send(message)


def run_composition_and_duck_typing() -> None:
    """合成と duck typing の基本を確認する。"""

    console_sender = ConsoleSender()
    report_service = ReportService(console_sender)

    report_result = report_service.send_report(
        "Daily Report",
        ["created=3", "failed=0"],
    )
    print(f"report_result: {report_result}")

    memory_sender = MemorySender()
    memory_service = ReportService(memory_sender)

    memory_result = memory_service.send_report(
        "Batch Report",
        ["success=10", "error=1"],
    )
    print(f"memory_result: {memory_result}")
    print(f"memory_sender.messages: {memory_sender.messages}")

    console_result = deliver_message(console_sender, "Hello")
    memory_direct_result = deliver_message(memory_sender, "Saved")

    print(f"console_result: {console_result}")
    print(f"memory_direct_result: {memory_direct_result}")

    assert report_result == "console: Daily Report\ncreated=3\nfailed=0"
    assert memory_result == "memory: Batch Report\nsuccess=10\nerror=1"
    assert memory_sender.messages == [
        "Batch Report\nsuccess=10\nerror=1",
        "Saved",
    ]
    assert console_result == "console: Hello"
    assert memory_direct_result == "memory: Saved"
