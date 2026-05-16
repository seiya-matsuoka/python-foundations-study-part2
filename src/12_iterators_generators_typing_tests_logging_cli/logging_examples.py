"""logging の基本を確認するサンプル。"""

import io
import logging


def create_memory_logger(name: str) -> tuple[logging.Logger, io.StringIO]:
    """文字列バッファへ出力する logger を作る。"""
    # logging は、print よりも用途や重要度を分けてメッセージを残しやすい。
    # ここでは学習用に StringIO へ出力し、後から内容を確認できるようにする。
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    return logger, stream


def run_batch(logger: logging.Logger, total: int, failed: int) -> str:
    """バッチ処理の結果をログに出力し、状態文字列を返す。"""
    # info は通常の処理状況を出すときに使える。
    # warning は失敗や注意が必要な状況を出すときに使える。
    logger.info("batch started")
    logger.info("total=%s", total)

    if failed > 0:
        logger.warning("failed=%s", failed)
        status = "warning"
    else:
        logger.info("failed=0")
        status = "success"

    logger.info("batch finished")
    return status


def run_logging_examples() -> None:
    """logging のレベル、logger、handler、formatter の基本を確認する。"""

    logger, stream = create_memory_logger("unit12")
    status = run_batch(logger, total=10, failed=1)
    log_text = stream.getvalue()
    log_lines = log_text.splitlines()

    print(f"status: {status}")
    print("log_text:")
    print(log_text, end="")

    # logger の level を WARNING に変えると、INFO は出力されなくなる。
    # ログレベルで、どの重要度以上のログを出すかを制御できる。
    warning_logger, warning_stream = create_memory_logger("unit12.warning")
    warning_logger.setLevel(logging.WARNING)
    warning_status = run_batch(warning_logger, total=5, failed=0)
    warning_log_text = warning_stream.getvalue()

    print(f"warning_status: {warning_status}")
    print(f"warning_log_text: {warning_log_text!r}")

    assert status == "warning"
    assert log_lines == [
        "INFO:unit12:batch started",
        "INFO:unit12:total=10",
        "WARNING:unit12:failed=1",
        "INFO:unit12:batch finished",
    ]
    assert warning_status == "success"
    assert warning_log_text == ""
