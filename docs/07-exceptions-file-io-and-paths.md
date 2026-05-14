# 07. 例外処理・ファイル入出力・パス操作

## 1. 学習対象

この単位では、Pythonの例外処理、テキストファイル入出力、pathlib によるパス操作を扱う。

- `try / except / else / finally`
- `raise`
- 組み込み例外の代表例
- `open`
- テキストファイルの読み書き
- `with`
- `pathlib`
- パスの生成・結合・存在確認などの基本操作

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- `try` には、例外が発生する可能性がある処理を書く
- `except` は、指定した例外が発生した場合に実行される
- `else` は、例外が発生しなかった場合に実行される
- `finally` は、成功しても失敗しても実行される
- `raise` を使うと、条件を満たさない場合に例外を明示的に送出できる
- `open` と `with` を使うと、テキストファイルを安全に読み書きできる
- `pathlib.Path` を使うと、パスの生成や結合をオブジェクトとして扱える
- `exists()`、`is_file()`、`is_dir()` でパスの状態を確認できる
- ファイル処理では `FileNotFoundError` や `ValueError` などを意識する

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/07_exceptions_file_io_and_paths/
  main.py
  exception_basics.py
  raising_exceptions.py
  file_reading_and_writing.py
  pathlib_operations.py
  safe_file_processing.py
  sample_data/
    input_lines.txt
    numbers.txt
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 07 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `exception_basics.py`
  - `try / except / else / finally` と代表的な組み込み例外を扱う
- `raising_exceptions.py`
  - `raise` による例外送出と入力値チェックを扱う
- `file_reading_and_writing.py`
  - `open`、`with`、テキストファイルの読み書きを扱う
- `pathlib_operations.py`
  - `pathlib.Path` によるパス生成、結合、存在確認、書き込みを扱う
- `safe_file_processing.py`
  - ファイル処理と例外処理を組み合わせた例を扱う
- `sample_data/`
  - ファイル入出力のサンプルで使用する入力データを置く

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/07_exceptions_file_io_and_paths/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/07_exceptions_file_io_and_paths/main.py
```

Ruff の確認は次のコマンドで行う。

```bash
uv run ruff check .
uv run ruff format --check .
```

必要に応じてフォーマットを実行する。

```bash
uv run ruff format .
```

## 5. コードを読む順番

次の順番で読むと、内容を追いやすい。

1. `main.py`
2. `exception_basics.py`
3. `raising_exceptions.py`
4. `file_reading_and_writing.py`
5. `pathlib_operations.py`
6. `safe_file_processing.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、例外処理の基本、例外送出、ファイル読み書き、pathlib、例外処理を含むファイル処理の順番で読む。

## 6. 処理の流れ

Unit 07 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. `try / except / else / finally` のサンプルを実行する
5. `raise` のサンプルを実行する
6. `open` と `with` によるファイル読み書きのサンプルを実行する
7. `pathlib` によるパス操作のサンプルを実行する
8. 例外処理を含むファイル処理のサンプルを実行する
9. 各ファイル内の `assert` により、軽い期待値確認を行う

この単位では、失敗する可能性がある処理を安全に扱うことを主題にしている。  
ファイル入出力では、`sample_data/` の入力ファイルを読み取り、`sample_data/generated/` に出力ファイルを生成する。

## 7. 注目ポイント

### 7-1. `try / except / else / finally` は役割が分かれている

`exception_basics.py` では、文字列を `int` に変換する処理を扱う。

```python
try:
    number = int(text)
except ValueError:
    return None
else:
    return number
finally:
    print(f"parse_int processed: {text}")
```

`try` には、例外が発生する可能性がある処理を書く。  
`except ValueError` は、`int(text)` が失敗した場合に実行される。

`else` は、例外が発生しなかった場合に実行される。  
`finally` は、成功しても失敗しても最後に実行される。

### 7-2. `raise` は不正な値を明示的に拒否できる

`raising_exceptions.py` では、空文字列を拒否する処理を扱う。

```python
def require_non_empty_text(text: str) -> str:
    if text == "":
        raise ValueError("text must not be empty")

    return text
```

`raise ValueError(...)` により、関数側から明示的に例外を送出している。  
これにより、呼び出し側は `try / except` で失敗を扱える。

不正な値で処理を続けるより、早い段階で例外にする方が安全な場面がある。

### 7-3. `with open(...)` はファイルを安全に扱う基本形

`file_reading_and_writing.py` では、`with` を使ってファイルを開いている。

```python
with open(path, encoding="utf-8") as file:
    lines = file.readlines()
```

`with` を使うと、処理が終わったあとにファイルを閉じる処理を任せられる。  
例外が発生した場合でも、リソース管理を安全に行いやすい。

ファイルを扱うときは、`encoding="utf-8"` のように文字コードを明示しておくと前提が読みやすい。

### 7-4. `pathlib` では `/` でパスを結合できる

`pathlib_operations.py` では、`Path` を使ってパスを組み立てている。

```python
input_path = SAMPLE_DATA_DIR / "input_lines.txt"
generated_dir = SAMPLE_DATA_DIR / "generated"
output_path = generated_dir / "pathlib_output.txt"
```

`pathlib.Path` では、`/` 演算子でパスを結合できる。  
文字列結合でパスを作るより、パスとしての意図が分かりやすい。

`exists()`、`is_file()`、`is_dir()` などを使うと、パスの状態も確認できる。

### 7-5. ファイル処理では存在確認と例外処理を組み合わせる

`safe_file_processing.py` では、ファイルが存在するかを確認している。

```python
def require_file(path: Path) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"file not found: {path}")

    if not path.is_file():
        raise ValueError(f"path is not a file: {path}")

    return path
```

`Path.exists()` で存在確認を行い、存在しない場合は `FileNotFoundError` を送出している。  
存在していてもファイルではない場合は `ValueError` として扱う。

このように、パス操作と例外処理を組み合わせると、失敗時の理由を明確にできる。

## 8. 引っかかりやすい点

### 8-1. すべての例外を広く捕まえすぎない

`exception_basics.py` では、`ValueError` や `ZeroDivisionError` のように、想定する例外を指定している。

```python
try:
    result = left / right
except ZeroDivisionError:
    return None
```

`except Exception:` のように広く捕まえすぎると、本来気づくべきバグまで隠してしまうことがある。  
まずは、発生しうる例外をできるだけ具体的に指定する方が読みやすい。

### 8-2. `finally` は return の有無に関係なく実行される

`exception_basics.py` では、`except` や `else` の中で `return` している。

```python
except ValueError:
    return None
else:
    return number
finally:
    print(f"parse_int processed: {text}")
```

`return` があっても、`finally` は実行される。  
そのため、後片付けやログ出力など、成功・失敗に関係なく行いたい処理を書く場所として使える。

ただし、`finally` に複雑な処理を書きすぎると、制御の流れが読みにくくなる。

### 8-3. `raise` した例外は呼び出し側で扱う必要がある

`raising_exceptions.py` では、`require_non_empty_text("")` を `try / except` で囲んでいる。

```python
try:
    require_non_empty_text("")
except ValueError as error:
    empty_error_message = str(error)
else:
    empty_error_message = ""
```

`raise` で送出された例外をどこでも処理しない場合、プログラムはそこで停止する。  
そのため、失敗する可能性がある呼び出しでは、必要に応じて `try / except` を使う。

どこで例外を処理するかは、処理の責務を考えて決める。

### 8-4. `open` で書き込む前に親ディレクトリが必要になる

`file_reading_and_writing.py` では、書き込み前にディレクトリを作成している。

```python
GENERATED_DIR.mkdir(exist_ok=True)

write_text_file(output_path, cleaned_lines)
```

`open(path, mode="w")` はファイルを作成できるが、存在しない親ディレクトリまでは作成しない。  
そのため、出力先ディレクトリがない場合は、先に `mkdir` で作る必要がある。

`pathlib` の `mkdir(exist_ok=True)` を使うと、既に存在していても例外にせず進められる。

### 8-5. `Path.exists()` だけではファイルかディレクトリか分からない

`pathlib_operations.py` では、存在確認と種類の確認を分けている。

```python
input_exists = input_path.exists()
input_is_file = input_path.is_file()
sample_is_dir = SAMPLE_DATA_DIR.is_dir()
```

`exists()` は、パスが存在するかだけを確認する。  
そのパスがファイルかディレクトリかは、`is_file()` や `is_dir()` で確認する。

ファイルとして読み込みたい場合は、存在確認だけでなく `is_file()` も見ると安全になる。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- `try / except / else / finally` の役割を説明できる
- 代表的な組み込み例外の例を読める
- `raise` を使って不正な値を明示的に拒否できることを説明できる
- `with open(...)` によるファイル読み込みを読める
- `with open(..., mode="w")` によるファイル書き込みを読める
- `with open(..., mode="a")` による追記を読める
- `pathlib.Path` によるパス生成と結合を読める
- `exists()`、`is_file()`、`is_dir()` の違いを説明できる
- ファイル入出力と例外処理を組み合わせた処理を読める
