# 08. モジュール・import・コード分割

## 1. 学習対象

この単位では、Pythonにおけるモジュール、import、コード分割の基本を扱う。

- `import`
- `from ... import ...`
- モジュール
- パッケージの基本
- ファイル分割
- `__name__ == "__main__"`
- 実行入口の考え方
- 再利用可能なコードへの分割

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- Python ファイルはモジュールとして読み込める
- `import` を使うと、モジュール全体を読み込める
- `from ... import ...` を使うと、モジュール内の特定の名前を読み込める
- ディレクトリと `__init__.py` を使うと、パッケージとして整理できる
- 処理を複数ファイルへ分けると、役割ごとに読みやすくなる
- `main.py` は実行入口として使える
- `__name__ == "__main__"` は、直接実行された場合だけ処理を動かすために使う
- 再利用したい処理は、関数やモジュールに分けておくと扱いやすい

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/08_modules_imports_and_code_organization/
  main.py
  import_styles.py
  package_usage.py
  reusable_code_flow.py
  entry_point_examples.py
  helpers/
    __init__.py
    text_tools.py
    price_tools.py
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 08 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `import_styles.py`
  - `import` と `from ... import ...` の基本的な使い分けを扱う
- `package_usage.py`
  - `helpers/` パッケージ配下のモジュールを読み込む例を扱う
- `reusable_code_flow.py`
  - 処理を再利用可能な関数やモジュールへ分ける流れを扱う
- `entry_point_examples.py`
  - `__name__` と `__name__ == "__main__"` の挙動を扱う
- `helpers/`
  - 他のファイルから再利用する補助関数を置くパッケージ

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/08_modules_imports_and_code_organization/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/08_modules_imports_and_code_organization/main.py
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
2. `helpers/text_tools.py`
3. `helpers/price_tools.py`
4. `import_styles.py`
5. `package_usage.py`
6. `reusable_code_flow.py`
7. `entry_point_examples.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、再利用される `helpers/` 配下のモジュールを読み、各ファイルがどのように import しているかを確認する。

## 6. 処理の流れ

Unit 08 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. `import` と `from ... import ...` のサンプルを実行する
5. パッケージ配下のモジュールを読み込むサンプルを実行する
6. 再利用可能なコード分割のサンプルを実行する
7. `__name__` と実行入口のサンプルを実行する
8. 各ファイル内の `assert` により、軽い期待値確認を行う

この単位では、複数ファイルに分けたコードを読み込む流れを主題にしている。  
`helpers/` 配下に再利用する関数を置き、他のファイルから import して使う構成にしている。

## 7. 注目ポイント

### 7-1. `import` はモジュール全体を読み込む

`import_styles.py` では、`helpers.text_tools` をモジュールとして読み込んでいる。

```python
import helpers.text_tools as text_tools

normalized_name = text_tools.normalize_name(raw_name)
slug = text_tools.build_slug(normalized_name)
```

`import helpers.text_tools as text_tools` により、`text_tools` という名前でモジュールを扱える。  
関数を呼び出すときは、`text_tools.normalize_name(...)` のようにモジュール名を経由する。

どのモジュールに定義された関数かが見えやすい点が特徴である。

### 7-2. `from ... import ...` は特定の名前を直接読み込む

`import_styles.py` では、価格計算用の関数だけを読み込んでいる。

```python
from helpers.price_tools import calculate_tax_included, format_price

tax_included_price = calculate_tax_included(1000)
formatted_price = format_price(tax_included_price)
```

`from ... import ...` を使うと、モジュール名を毎回書かずに関数を呼び出せる。  
短く書ける一方で、名前の由来が見えにくくなる場合もある。

コードの読みやすさを見ながら、どちらの import が合うかを選ぶ。

### 7-3. `helpers/` はパッケージとして扱える

`package_usage.py` では、`helpers` パッケージからモジュールを読み込んでいる。

```python
from helpers import text_tools
from helpers.price_tools import calculate_total
```

`helpers/` ディレクトリには `__init__.py` を置いている。  
これにより、`helpers` をパッケージとして扱い、その配下のモジュールを import できる。

ファイルが増えた場合は、役割ごとにパッケージへ分けると整理しやすい。

### 7-4. 再利用する処理は別ファイルに分ける

`reusable_code_flow.py` では、`helpers` の関数を組み合わせて商品情報を作っている。

```python
from helpers.price_tools import calculate_tax_included, calculate_total, format_price
from helpers.text_tools import build_slug, normalize_name
```

文字列処理や価格計算を `helpers/` に分けることで、呼び出し側は組み合わせに集中できる。  
同じ処理を複数の場所で使う可能性がある場合は、関数やモジュールとして分けておくと再利用しやすい。

ただし、何でも細かく分ければよいわけではない。  
処理のまとまりや再利用性を見ながら分けることが重要である。

### 7-5. `__name__ == "__main__"` は直接実行時だけ処理するために使う

`entry_point_examples.py` では、ファイル末尾に次の条件式を書いている。

```python
if __name__ == "__main__":
    print(build_execution_message())
```

このファイルを直接実行した場合、`__name__` は `"__main__"` になる。  
一方で、`main.py` から import された場合は、`__name__` はモジュール名になる。

この条件式により、import されたときに不要な処理が自動実行されることを防げる。

## 8. 引っかかりやすい点

### 8-1. import しただけでトップレベルの処理は実行される

Python では、モジュールを import すると、そのファイルのトップレベルの処理が実行される。  
そのため、関数定義や定数定義以外の処理を不用意にトップレベルへ置くと、import 時に実行される。

```python
if __name__ == "__main__":
    main()
```

実行したい処理は、上記のように `__name__ == "__main__"` の条件で囲むと安全である。  
これにより、直接実行時だけ `main()` を呼び出せる。

### 8-2. `from ... import ...` は短いが由来が見えにくいことがある

`import_styles.py` では、次のように関数を直接読み込んでいる。

```python
from helpers.price_tools import calculate_tax_included, format_price
```

この書き方では、呼び出し側で `calculate_tax_included(...)` と直接書ける。  
ただし、関数名だけを見ると、どのモジュールから来たものか分かりにくい場合がある。

短く書けることと、読み手が追いやすいことのバランスを意識する。

### 8-3. パッケージとモジュールの粒度を混同しやすい

Unit 08 では、`helpers/` がパッケージで、`text_tools.py` と `price_tools.py` がモジュールである。

```text
helpers/
  __init__.py
  text_tools.py
  price_tools.py
```

パッケージは、複数のモジュールをまとめるディレクトリとして考えると理解しやすい。  
モジュールは、基本的には1つの `.py` ファイルとして考える。

まずは「ファイルがモジュール」「ディレクトリでまとめたものがパッケージ」という感覚を押さえる。

### 8-4. コードを分けすぎると逆に読みにくくなる

`reusable_code_flow.py` では、文字列処理と価格計算を `helpers/` に分けている。  
これは、複数の場所から使えそうな処理を切り出している例である。

```python
normalized_name = normalize_name(name)
slug = build_slug(normalized_name)
tax_included_price = calculate_tax_included(price)
```

ただし、少ししか使わない処理まで細かく分けすぎると、読むためにファイルを行き来する負担が増える。  
コード分割は、再利用性、責務、読みやすさを見ながら判断する。

### 8-5. 実行する場所によって import の見え方が変わることがある

今回のサンプルは、リポジトリ直下から `main.py` を実行する前提で作っている。

```bash
python src/08_modules_imports_and_code_organization/main.py
```

Python は実行したファイルの場所や `sys.path` によって、import できる範囲が変わることがある。  
この単位では、まず同じ Unit ディレクトリ内での分割と、配下パッケージの import に集中する。

より大きなプロジェクトでのパッケージ設計や配布は、今回の範囲外とする。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- Python ファイルをモジュールとして考えられる
- `import` と `from ... import ...` の違いを説明できる
- モジュール名を経由して関数を呼び出す書き方を読める
- パッケージとモジュールの関係を説明できる
- `__init__.py` の役割を説明できる
- `main.py` を実行入口として使う考え方を説明できる
- `__name__ == "__main__"` の基本的な目的を説明できる
- 再利用したい処理を関数やモジュールに分ける考え方を説明できる
