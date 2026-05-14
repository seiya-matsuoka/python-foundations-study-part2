"""pathlib によるパス操作を確認するサンプル。"""

from pathlib import Path

UNIT_DIR = Path(__file__).parent
SAMPLE_DATA_DIR = UNIT_DIR / "sample_data"


def run_pathlib_operations() -> None:
    """Path の生成、結合、存在確認、名前の取得を確認する。"""

    # Path(__file__) は、この Python ファイル自身のパスを表す。
    # parent を使うと、このファイルがあるディレクトリを取得できる。
    current_file = Path(__file__)
    unit_dir = current_file.parent

    print(f"current_file: {current_file}")
    print(f"unit_dir: {unit_dir}")

    # / 演算子を使うと、パスを自然に結合できる。
    input_path = SAMPLE_DATA_DIR / "input_lines.txt"
    generated_dir = SAMPLE_DATA_DIR / "generated"
    output_path = generated_dir / "pathlib_output.txt"

    print(f"input_path: {input_path}")
    print(f"output_path: {output_path}")

    # exists、is_file、is_dir でパスの状態を確認できる。
    input_exists = input_path.exists()
    input_is_file = input_path.is_file()
    sample_is_dir = SAMPLE_DATA_DIR.is_dir()

    print(f"input_exists: {input_exists}")
    print(f"input_is_file: {input_is_file}")
    print(f"sample_is_dir: {sample_is_dir}")

    # name、stem、suffix はファイル名の一部を取り出すために使える。
    input_name = input_path.name
    input_stem = input_path.stem
    input_suffix = input_path.suffix

    print(f"input_name: {input_name}")
    print(f"input_stem: {input_stem}")
    print(f"input_suffix: {input_suffix}")

    # mkdir を使うとディレクトリを作成できる。
    # exist_ok=True にすると、既に存在していても例外にしない。
    generated_dir.mkdir(exist_ok=True)
    output_path.write_text("pathlib write_text sample\n", encoding="utf-8")

    output_text = output_path.read_text(encoding="utf-8")

    print(f"generated_dir exists: {generated_dir.exists()}")
    print(f"output_text: {output_text.rstrip()}")

    assert unit_dir == UNIT_DIR
    assert input_exists is True
    assert input_is_file is True
    assert sample_is_dir is True
    assert input_name == "input_lines.txt"
    assert input_stem == "input_lines"
    assert input_suffix == ".txt"
    assert generated_dir.exists()
    assert output_text == "pathlib write_text sample\n"
