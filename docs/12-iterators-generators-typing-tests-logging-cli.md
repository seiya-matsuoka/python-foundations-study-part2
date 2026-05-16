# 12. イテレータ・ジェネレータ・型ヒント・テスト・ログ・CLI基礎

## 1. 学習対象

この単位では、Pythonの反復処理の仕組みと、継続学習・実務につながる基礎要素を扱う。

- iterable と iterator の違い
- `iter`
- `next`
- `yield`
- ジェネレータ関数
- ジェネレータ式の再確認
- `__iter__` / `__next__` の基礎
- 型ヒント
  - 変数
  - 関数引数
  - 戻り値
  - コレクション型
  - `Optional`
  - `|`
  - type alias の最小限
- `assert`
- `unittest`
- `logging`
- `argparse`
- `sys` の最小限

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- iterable は、for 文で繰り返せるオブジェクトである
- iterator は、`next` で値を1つずつ取り出せるオブジェクトである
- `iter` は、iterable から iterator を作るために使う
- `next` は、iterator から次の値を取り出すために使う
- `yield` を使うと、値を少しずつ生成するジェネレータ関数を書ける
- `__iter__` と `__next__` を定義すると、独自 iterator を作れる
- 型ヒントは、変数、引数、戻り値、コレクションの要素型に書ける
- `Optional[T]` と `T | None` は、None の可能性がある値を表す
- type alias は、型に意味のある名前を付けるために使える
- `assert` は、簡単な期待値確認に使える
- `unittest` は、標準ライブラリでテストを書くために使える
- `logging` は、重要度を分けてログを出すために使える
- `argparse` は、コマンドライン引数を解析するために使える
- `sys.argv` は、起動時に渡された引数を確認するために使える

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/12_iterators_generators_typing_tests_logging_cli/
  main.py
  iterable_iterator_basics.py
  generator_examples.py
  custom_iterator.py
  type_hints_examples.py
  assertion_and_unittest_examples.py
  logging_examples.py
  cli_examples.py
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 12 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `iterable_iterator_basics.py`
  - iterable、iterator、`iter`、`next`、`StopIteration` を扱う
- `generator_examples.py`
  - `yield`、ジェネレータ関数、ジェネレータ式を扱う
- `custom_iterator.py`
  - `__iter__`、`__next__` による独自 iterator を扱う
- `type_hints_examples.py`
  - 変数、引数、戻り値、コレクション型、`Optional`、`|`、type alias を扱う
- `assertion_and_unittest_examples.py`
  - `assert` と `unittest` の基本を扱う
- `logging_examples.py`
  - `logging` の logger、handler、formatter、ログレベルを扱う
- `cli_examples.py`
  - `argparse` と `sys.argv` の最小限を扱う

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/12_iterators_generators_typing_tests_logging_cli/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/12_iterators_generators_typing_tests_logging_cli/main.py
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
2. `iterable_iterator_basics.py`
3. `generator_examples.py`
4. `custom_iterator.py`
5. `type_hints_examples.py`
6. `assertion_and_unittest_examples.py`
7. `logging_examples.py`
8. `cli_examples.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、反復処理の仕組み、ジェネレータ、独自 iterator、型ヒント、テスト、ログ、CLI の順番で読む。

## 6. 処理の流れ

Unit 12 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. iterable、iterator、`iter`、`next` のサンプルを実行する
5. `yield` とジェネレータ関数のサンプルを実行する
6. `__iter__` / `__next__` による独自 iterator のサンプルを実行する
7. 型ヒントのサンプルを実行する
8. `assert` と `unittest` のサンプルを実行する
9. `logging` のサンプルを実行する
10. `argparse` と `sys` のサンプルを実行する
11. 各ファイル内の `assert` により、軽い期待値確認を行う

この単位では、Python の反復処理の裏側と、実務的な補助要素の入口を主題にしている。  
学習対象が広いため、各ファイルは一つのテーマに絞り、コードリーディングしやすい粒度に分けている。

## 7. 注目ポイント

### 7-1. iterable と iterator は役割が違う

`iterable_iterator_basics.py` では、`list` から iterator を作っている。

```python
languages = ["Python", "Java", "SQL"]
language_iterator = iter(languages)

first_language = next(language_iterator)
second_language = next(language_iterator)
third_language = next(language_iterator)
```

`languages` は iterable であり、for 文で繰り返せる。  
`iter(languages)` によって、`next` で1つずつ取り出せる iterator を作っている。

iterator は現在位置を持つため、`next` を呼ぶたびに次の値へ進む。  
一度取り出した値は、同じ iterator からは再度取り出せない。

### 7-2. `yield` は処理を途中で止めて再開できる

`generator_examples.py` では、偶数を1つずつ生成している。

```python
def generate_even_numbers(limit: int):
    number = 0

    while number < limit:
        if number % 2 == 0:
            yield number

        number += 1
```

`yield` を含む関数は、ジェネレータ関数になる。  
関数を呼び出した時点で全処理が実行されるのではなく、値が必要になったタイミングで進む。

大量データやファイル読み込みのように、少しずつ値を扱いたい場面で重要な考え方である。

### 7-3. `__iter__` と `__next__` で独自 iterator を作れる

`custom_iterator.py` では、`CountDown` が iterator として動作する。

```python
class CountDown:
    def __iter__(self) -> "CountDown":
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value
```

`__iter__` は iterator を返す。  
`__next__` は次の値を返し、値がなくなった場合は `StopIteration` を送出する。

for 文は内部で `iter` と `next` を使っているため、この2つの特殊メソッドを知ると反復処理の仕組みを理解しやすくなる。

### 7-4. 型ヒントは None の可能性を明示できる

`type_hints_examples.py` では、見つからない可能性がある点数を `Optional[int]` として返している。

```python
def find_score(scores: ScoreMap, name: str) -> Optional[int]:
    return scores.get(name)
```

`dict.get` は、キーが存在しない場合に `None` を返すことがある。  
そのため、戻り値の型に `Optional[int]` を書くと、呼び出し側が None の可能性を意識しやすくなる。

Python では `int | None` のような表記も使える。  
どちらも None の可能性を表す型ヒントである。

### 7-5. `unittest` はテストケースとして期待値を整理できる

`assertion_and_unittest_examples.py` では、`unittest.TestCase` を使っている。

```python
class GradeTestCase(unittest.TestCase):
    def test_calculate_grade(self) -> None:
        self.assertEqual(calculate_grade(95), "A")
        self.assertEqual(calculate_grade(85), "B")
```

`unittest` を使うと、確認したい処理をテストメソッドとして整理できる。  
`self.assertEqual` や `self.assertTrue` など、目的に応じた検証メソッドを使える。

このリポジトリでは各ファイル末尾の `assert` を軽い確認に使ってきたが、Unit 12 では標準のテストフレームワークとして `unittest` も扱う。

### 7-6. `logging` は重要度を分けて出力できる

`logging_examples.py` では、`info` と `warning` を使っている。

```python
logger.info("batch started")
logger.info("total=%s", total)

if failed > 0:
    logger.warning("failed=%s", failed)
```

`logging` は、`print` よりも目的別にメッセージを扱いやすい。  
`INFO`、`WARNING` などのレベルを使うことで、重要度を分けて出力できる。

実務では、処理状況、警告、エラーなどをログとして残す場面が多い。

### 7-7. `argparse` は CLI 引数を定義して解析できる

`cli_examples.py` では、`ArgumentParser` にオプションを定義している。

```python
parser = argparse.ArgumentParser(description="Unit 12 CLI sample")
parser.add_argument("--name", default="World", help="表示する名前")
parser.add_argument("--count", type=int, default=1, help="繰り返し回数")
parser.add_argument("--verbose", action="store_true", help="詳細表示を有効にする")
```

`argparse` を使うと、CLI 引数の名前、型、既定値、説明を定義できる。  
`type=int` を指定すると、文字列として渡された引数を整数に変換して扱える。

小さな CLI ツールを作る入口として重要な標準ライブラリである。

## 8. 引っかかりやすい点

### 8-1. iterator は消費される

`iterable_iterator_basics.py` では、途中まで使った iterator を `list` にしている。

```python
partially_used_iterator = iter([10, 20, 30, 40])
first_number = next(partially_used_iterator)
remaining_numbers = list(partially_used_iterator)
```

最初に `next` で `10` を取り出しているため、`remaining_numbers` は `[20, 30, 40]` になる。  
iterator は現在位置を持つため、すでに取り出した値は残らない。

同じ値を何度も繰り返したい場合は、元の iterable から新しい iterator を作る必要がある。

### 8-2. ジェネレータ式も一度消費されると空になる

`generator_examples.py` では、同じ generator を2回 `list` にしている。

```python
word_generator = (word.upper() for word in ["python", "java"])
upper_words = list(word_generator)
empty_after_consumed = list(word_generator)
```

1回目の `list(word_generator)` で、generator の値はすべて取り出される。  
そのため、2回目は空の list になる。

リスト内包表記とは違い、generator は値を保持する list を作っているわけではない点に注意する。

### 8-3. `StopIteration` は反復終了の合図である

`custom_iterator.py` では、値がなくなったときに `StopIteration` を送出している。

```python
if self.current <= 0:
    raise StopIteration
```

`StopIteration` は、iterator の値がもう残っていないことを表す。  
for 文はこの例外を見て、自然にループを終了する。

通常のアプリケーションエラーというより、反復処理の終了を伝える仕組みとして読む。

### 8-4. 型ヒントは実行時の型チェックそのものではない

`type_hints_examples.py` では、変数や関数に型ヒントを書いている。

```python
user_id: UserId = 101
scores: ScoreMap = {
    "Sora": 80,
    "Mio": 95,
}
```

型ヒントは、主にエディタ支援や静的解析のための情報である。  
通常の実行時に、型ヒントどおりかを Python が常に強制するわけではない。

そのため、型ヒントは「読みやすさ」と「ツールによる検出」を助けるものとして理解する。

### 8-5. `assert` と `unittest` は役割が少し違う

`assertion_and_unittest_examples.py` では、通常の `assert` と `unittest` の両方を扱う。

```python
assert grade == "B"

class GradeTestCase(unittest.TestCase):
    def test_calculate_grade(self) -> None:
        self.assertEqual(calculate_grade(95), "A")
```

`assert` は、学習用の軽い期待値確認に使いやすい。  
一方、`unittest` はテストケースとして整理し、複数の観点を継続的に確認する用途に向く。

本格的にテストを書く場合は、テスト対象、テストケース、期待値を分けて管理する。

### 8-6. logger は同じ名前を再利用する

`logging_examples.py` では、`logging.getLogger(name)` を使っている。

```python
logger = logging.getLogger(name)
logger.handlers.clear()
logger.addHandler(handler)
```

`getLogger` は、同じ名前の logger を再利用する。  
学習用コードやテストでは、以前の handler が残るとログが重複することがある。

そのため、このサンプルでは `handlers.clear()` で既存 handler を消してから設定している。

### 8-7. `sys.argv` の先頭はスクリプト名である

`cli_examples.py` では、`sys.argv` の先頭を確認している。

```python
current_argv = sys.argv[:]
script_name = current_argv[0]
```

`sys.argv[0]` には、通常、実行されたスクリプト名が入る。  
実際の引数は `sys.argv[1:]` に入る。

`argparse` は通常、この `sys.argv[1:]` を解析する。  
学習用コードでは、明示的に `args` を渡すことで結果を固定している。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- iterable と iterator の違いを説明できる
- `iter` と `next` の基本的な役割を説明できる
- iterator が消費されることを説明できる
- `yield` を使ったジェネレータ関数を読める
- ジェネレータ式が一度消費されると空になることを説明できる
- `__iter__` / `__next__` による独自 iterator の基本を読める
- 変数、引数、戻り値、コレクション型の型ヒントを読める
- `Optional`、`|`、type alias の基本を説明できる
- `assert` と `unittest` の基本的な違いを説明できる
- `logging` の logger、handler、formatter、ログレベルの入口を説明できる
- `argparse` による CLI 引数定義の基本を説明できる
- `sys.argv` の最小限の役割を説明できる
