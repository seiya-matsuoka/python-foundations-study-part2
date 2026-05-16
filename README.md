# Python Foundations Study - Part 2

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=ffffff">
  <img alt="Python Study" src="https://img.shields.io/badge/Python-Study-1F6FEB">
  <img alt="uv" src="https://img.shields.io/badge/uv-Project%20Manager-DE5FE9">
  <img alt="Ruff" src="https://img.shields.io/badge/Ruff-Lint%20%2F%20Format-D7FF64">
</p>

Python の基礎を、コードリーディング中心で学習するためのリポジトリ。  
Part 2 では、**例外処理 / ファイル入出力 / モジュール分割 / 文字列処理 / 標準データ形式 / 標準ライブラリ / クラス / 型ヒント / テスト / ログ / CLI基礎** を扱う。  
各 Unit ごとにソースコードとドキュメントを用意し、コード、コメント、出力、確認用の `assert` を対応づけながら見返せる形で整理している。

---

## このリポジトリの位置づけ

このリポジトリは、Python基礎学習の後半として作成した `python-foundations-study-part2` である。

今回の Python 学習では、次の2つのリポジトリに分けて進める。

- `python-foundations-study-part1`
  - 前半の学習範囲を扱う
  - 標準寄りの `venv + pip` 構成で環境構築を行う
- `python-foundations-study-part2`
  - 後半の学習範囲を扱う
  - `uv + .venv` 構成で環境構築を行う

Part 2 では、Part 1 で扱った基本構文、コレクション、関数、Pythonらしい書き方を前提に、より実用的な基礎要素を扱う。  
外部ライブラリは扱わず、Python の標準機能、標準ライブラリ、組み込みの開発補助機能を中心に学習する。

---

## 学習目的

このリポジトリでは、主に次の内容を目的として学習を行う。

- `try / except / else / finally`、`raise` による例外処理を読めるようにする
- `open`、`with`、`pathlib` を使ったファイル入出力とパス操作を理解する
- `import`、`from ... import ...`、モジュール、パッケージ、実行入口の基本を理解する
- 文字列処理、正規表現、JSON、CSV の基本操作を読めるようにする
- `datetime`、`collections`、`itertools`、`functools` など標準ライブラリの代表的な使い方に慣れる
- Python におけるクラス定義、`dataclass`、継承、合成、duck typing、特殊メソッドの基本を理解する
- iterable / iterator、ジェネレータ、型ヒントの基本を理解する
- `unittest`、`logging`、`argparse`、`sys` の最小限の使い方を確認する
- ソースコード、コメント、出力結果、`assert` を対応させながら処理を追えるようにする

---

## 学習範囲

このリポジトリで扱う Unit は次の通り。

| Unit | 内容                                                      |
| ---- | --------------------------------------------------------- |
| 07   | 例外処理・ファイル入出力・パス操作                        |
| 08   | モジュール・import・コード分割                            |
| 09   | 文字列処理・データ変換・標準データ形式                    |
| 10   | 標準ライブラリの重要機能                                  |
| 11   | クラス・オブジェクト・オブジェクト指向                    |
| 12   | イテレータ・ジェネレータ・型ヒント・テスト・ログ・CLI基礎 |

### 各 Unit の位置づけ

- **Unit 07: 例外処理・ファイル入出力・パス操作**  
  `try / except / else / finally`、`raise`、組み込み例外、`open`、テキストファイルの読み書き、`with`、`pathlib` を確認する

- **Unit 08: モジュール・import・コード分割**  
  `import`、`from ... import ...`、モジュール、パッケージ、ファイル分割、`__name__ == "__main__"`、実行入口、再利用可能なコード分割を確認する

- **Unit 09: 文字列処理・データ変換・標準データ形式**  
  `split`、`join`、`strip`、`replace`、検索、部分文字列の判定、正規表現の基礎、`json`、`csv` を確認する

- **Unit 10: 標準ライブラリの重要機能**  
  `datetime`、`math`、`random`、`statistics`、`collections`、`itertools`、`functools` の代表的な機能を確認する

- **Unit 11: クラス・オブジェクト・オブジェクト指向**  
  `class`、`__init__`、属性、各種メソッド、`property`、`dataclass`、継承、合成、duck typing、特殊メソッド、抽象基底クラス、`Enum` を確認する

- **Unit 12: イテレータ・ジェネレータ・型ヒント・テスト・ログ・CLI基礎**  
  iterable / iterator、`iter`、`next`、`yield`、ジェネレータ、`__iter__` / `__next__`、型ヒント、`assert`、`unittest`、`logging`、`argparse`、`sys` を確認する

---

## 学習の進め方

基本的な進め方は次の通り。

1. `docs/` の対象 Unit の Markdown を読む
2. `src/<unit>/main.py` を実行する
3. `main.py` から呼び出される各テーマ別ファイルを読む
4. ソースコード内のコメントと出力結果を対応させながら処理を追う
5. 各ファイル末尾の `assert` で、期待値との対応を確認する
6. 必要に応じて値を書き換え、再実行して挙動を確認する

このリポジトリでは、ソースコード単体でも学習できるようにコメントを多めに記載している。  
ドキュメントは、各 Unit の学習対象、読む順番、処理の流れ、注目ポイント、引っかかりやすい点を確認するための補助資料として使う。

---

## 前提環境

- Python 3.13.13
- VS Code
- Python 拡張機能
- Pylance
- Ruff
- uv
- `.venv`

このリポジトリでは、`uv` を使って Python バージョン、仮想環境、依存関係、lock ファイルを管理する。  
学習コード自体は外部ライブラリを使わず、標準機能・標準ライブラリの範囲で動作する。  
`pyproject.toml` は、プロジェクト設定、Ruff 設定、開発用依存関係の管理に使用する。

---

## セットアップ

### 1. uv を確認

```bash
uv --version
```

未インストールの場合は、uv の公式手順に従ってインストールする。

### 2. Python 3.13.13 を用意

```bash
uv python install 3.13.13
```

### 3. 仮想環境と依存関係を同期

```bash
uv sync
```

このコマンドにより、`.venv/` と `uv.lock` が作成・更新される。

### 4. 仮想環境を有効化

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
```

### 5. Python バージョンを確認

```bash
python --version
```

想定するバージョンは次の通り。

```text
Python 3.13.13
```

### 6. uv 経由で Python バージョンを確認

```bash
uv run python --version
```

想定するバージョンは次の通り。

```text
Python 3.13.13
```

---

## 実行方法

### Unit 07: 例外処理・ファイル入出力・パス操作

```bash
python src/07_exceptions_file_io_and_paths/main.py
```

### Unit 08: モジュール・import・コード分割

```bash
python src/08_modules_imports_and_code_organization/main.py
```

### Unit 09: 文字列処理・データ変換・標準データ形式

```bash
python src/09_strings_data_formats_and_parsing/main.py
```

### Unit 10: 標準ライブラリの重要機能

```bash
python src/10_essential_standard_library/main.py
```

### Unit 11: クラス・オブジェクト・オブジェクト指向

```bash
python src/11_classes_objects_and_oop/main.py
```

### Unit 12: イテレータ・ジェネレータ・型ヒント・テスト・ログ・CLI基礎

```bash
python src/12_iterators_generators_typing_tests_logging_cli/main.py
```

### unittest の実行

Unit 12 では、`unittest` の最小限の使い方も扱う。

```bash
python -m unittest src/12_iterators_generators_typing_tests_logging_cli/assertion_and_unittest_examples.py
```

### CLI サンプルの実行

Unit 12 では、`argparse` による CLI 引数処理も扱う。

```bash
python src/12_iterators_generators_typing_tests_logging_cli/cli_examples.py --name Sora --count 2
```

### Ruff による確認

```bash
uv run ruff check .
uv run ruff format --check .
```

必要に応じてフォーマットを実行する。

```bash
uv run ruff format .
```

---

## リポジトリ構成

主要な構成は次の通り。

```text
.
├─ docs/
│  ├─ 07-exceptions-file-io-and-paths.md
│  ├─ 08-modules-imports-and-code-organization.md
│  ├─ 09-strings-data-formats-and-parsing.md
│  ├─ 10-essential-standard-library.md
│  ├─ 11-classes-objects-and-oop.md
│  └─ 12-iterators-generators-typing-tests-logging-cli.md
│
├─ src/
│  ├─ 07_exceptions_file_io_and_paths/
│  ├─ 08_modules_imports_and_code_organization/
│  ├─ 09_strings_data_formats_and_parsing/
│  ├─ 10_essential_standard_library/
│  ├─ 11_classes_objects_and_oop/
│  └─ 12_iterators_generators_typing_tests_logging_cli/
│
├─ .vscode/
│  ├─ extensions.json
│  └─ settings.json
│
├─ .python-version
├─ pyproject.toml
├─ uv.lock
└─ README.md
```

### 各ディレクトリ・ファイルの役割

- `docs/`  
  各 Unit の学習対象、ファイル構成、実行方法、読む順番、処理の流れ、注目ポイント、引っかかりやすい点、確認観点をまとめた Markdown ドキュメントを置く

- `src/`  
  Unit ごとの Python ソースコードを置く  
  各 Unit はディレクトリ単位で分け、`main.py` を実行入口とする

- `.vscode/`  
  VS Code の推奨拡張機能とワークスペース設定を置く

- `.python-version`  
  このリポジトリで使用する Python バージョンを指定するファイル

- `pyproject.toml`  
  uv のプロジェクト設定、Ruff 設定、開発用依存関係を管理するファイル

- `uv.lock`  
  uv によって生成される lock ファイル  
  開発環境の依存関係を再現しやすくするために使用する

---

## ドキュメント

- 例外処理・ファイル入出力・パス操作: [`docs/07-exceptions-file-io-and-paths.md`](docs/07-exceptions-file-io-and-paths.md)
- モジュール・import・コード分割: [`docs/08-modules-imports-and-code-organization.md`](docs/08-modules-imports-and-code-organization.md)
- 文字列処理・データ変換・標準データ形式: [`docs/09-strings-data-formats-and-parsing.md`](docs/09-strings-data-formats-and-parsing.md)
- 標準ライブラリの重要機能: [`docs/10-essential-standard-library.md`](docs/10-essential-standard-library.md)
- クラス・オブジェクト・オブジェクト指向: [`docs/11-classes-objects-and-oop.md`](docs/11-classes-objects-and-oop.md)
- イテレータ・ジェネレータ・型ヒント・テスト・ログ・CLI基礎: [`docs/12-iterators-generators-typing-tests-logging-cli.md`](docs/12-iterators-generators-typing-tests-logging-cli.md)

---

## このリポジトリで確認できること

このリポジトリでは、次の内容を確認できる。

- `try / except / else / finally` の基本を読める
- `raise` による例外送出を説明できる
- `with open(...)` によるファイル読み書きを説明できる
- `pathlib.Path` によるパス操作を読める
- `import`、`from ... import ...`、モジュール、パッケージの基本を説明できる
- `__name__ == "__main__"` と実行入口の考え方を説明できる
- `split`、`join`、`strip`、`replace` などの文字列処理を読める
- 正規表現、JSON、CSV の最小限の使い方を説明できる
- `datetime`、`collections`、`itertools`、`functools` など標準ライブラリの代表例を読める
- `class`、`__init__`、インスタンス属性、インスタンスメソッドの基本を説明できる
- `classmethod`、`staticmethod`、`property`、`dataclass` の基本を説明できる
- 継承、`super()`、合成、duck typing の基本を説明できる
- 特殊メソッド、抽象基底クラス、`Enum` の最小限の使い方を読める
- iterable / iterator、ジェネレータ、型ヒントの基本を説明できる
- `unittest`、`logging`、`argparse`、`sys` の最小限の使い方を確認できる
- ソースコード、コメント、出力、`assert` を対応させながら挙動を確認できる
