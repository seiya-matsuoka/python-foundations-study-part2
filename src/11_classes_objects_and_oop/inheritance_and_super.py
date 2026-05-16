"""継承、super()、メソッドオーバーライドを確認するサンプル。"""


class Notification:
    """通知の共通情報を持つ基底クラス。"""

    def __init__(self, recipient: str) -> None:
        """通知先を受け取って初期化する。"""
        self.recipient = recipient

    def build_message(self, body: str) -> str:
        """通知メッセージを組み立てる。"""
        return f"To {self.recipient}: {body}"

    def channel_name(self) -> str:
        """通知チャネル名を返す。"""
        return "base"


class EmailNotification(Notification):
    """メール通知を表すクラス。"""

    def __init__(self, recipient: str, subject: str) -> None:
        """通知先と件名を受け取って初期化する。"""
        # super() を使うと、親クラスの初期化処理を呼び出せる。
        super().__init__(recipient)
        self.subject = subject

    def build_message(self, body: str) -> str:
        """メール用の通知メッセージを組み立てる。"""
        # 親クラスの処理を再利用しつつ、子クラス固有の情報を追加する。
        base_message = super().build_message(body)
        return f"[{self.subject}] {base_message}"

    def channel_name(self) -> str:
        """通知チャネル名を返す。"""
        # 親クラスと同じ名前のメソッドを定義すると、オーバーライドになる。
        return "email"


class SmsNotification(Notification):
    """SMS通知を表すクラス。"""

    def channel_name(self) -> str:
        """通知チャネル名を返す。"""
        return "sms"


def run_inheritance_and_super() -> None:
    """継承、super()、メソッドオーバーライドを確認する。"""

    email = EmailNotification("sora@example.com", "Welcome")
    sms = SmsNotification("090-0000-0000")

    email_message = email.build_message("Hello")
    sms_message = sms.build_message("Hi")

    print(f"email_message: {email_message}")
    print(f"sms_message: {sms_message}")
    print(f"email channel: {email.channel_name()}")
    print(f"sms channel: {sms.channel_name()}")

    notifications: list[Notification] = [email, sms]
    channel_names = []

    for notification in notifications:
        channel_names.append(notification.channel_name())

    print(f"channel_names: {channel_names}")

    assert email.recipient == "sora@example.com"
    assert email.subject == "Welcome"
    assert email_message == "[Welcome] To sora@example.com: Hello"
    assert sms_message == "To 090-0000-0000: Hi"
    assert email.channel_name() == "email"
    assert sms.channel_name() == "sms"
    assert channel_names == ["email", "sms"]
