# 09. 文字列処理・データ変換・標準データ形式

## 1. 学習対象

この単位では、Pythonで頻出する文字列処理、データ変換、標準データ形式を扱う。

- `split`
- `join`
- `strip`
- `replace`
- 検索
- 部分文字列の判定
- 正規表現の基礎
- `json`
- `csv`

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- `strip` は、文字列の前後の空白や改行を取り除く
- `split` は、文字列を指定した区切りで分割する
- `join` は、複数の文字列を指定した区切りで結合する
- `replace` は、文字列の一部を別の文字列に置換する
- `in`、`find`、`startswith`、`endswith` で文字列を検索・判定できる
- `re` を使うと、正規表現で文字列の検索、抽出、置換ができる
- `json` を使うと、Python の値と JSON ファイルを相互に扱える
- `csv` を使うと、表形式のテキストデータを読み書きできる
- ファイルから読み込んだデータは、必要に応じて型変換する

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/09_strings_data_formats_and_parsing/
  main.py
  string_methods.py
  search_and_replace.py
  regex_basics.py
  json_operations.py
  csv_operations.py
  sample_data/
    raw_text.txt
    users.json
    users.csv
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 09 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `string_methods.py`
  - `split`、`join`、`strip` による文字列加工を扱う
- `search_and_replace.py`
  - 部分文字列の判定、検索、`replace` を扱う
- `regex_basics.py`
  - `re.search`、`re.findall`、`re.sub`、`re.split` を扱う
- `json_operations.py`
  - JSON ファイルの読み込み、加工、書き込みを扱う
- `csv_operations.py`
  - CSV ファイルの読み込み、加工、書き込みを扱う
- `sample_data/`
  - 文字列処理、JSON、CSV のサンプルで使用する入力データを置く

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/09_strings_data_formats_and_parsing/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/09_strings_data_formats_and_parsing/main.py
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
2. `string_methods.py`
3. `search_and_replace.py`
4. `regex_basics.py`
5. `json_operations.py`
6. `csv_operations.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、文字列の基本操作、検索と置換、正規表現、JSON、CSV の順番で読む。

## 6. 処理の流れ

Unit 09 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. `split`、`join`、`strip` のサンプルを実行する
5. 検索、部分文字列の判定、`replace` のサンプルを実行する
6. 正規表現のサンプルを実行する
7. JSON の読み書きのサンプルを実行する
8. CSV の読み書きのサンプルを実行する
9. 各ファイル内の `assert` により、軽い期待値確認を行う

この単位では、テキストデータを加工し、標準データ形式として読み書きすることを主題にしている。  
JSON と CSV の出力ファイルは、実行時に `sample_data/generated/` 配下へ生成する。

## 7. 注目ポイント

### 7-1. `strip`、`split`、`join` は文字列加工の基本になる

`string_methods.py` では、カンマ区切りの文字列を整形している。

```python
cleaned_language_line = raw_language_line.strip()
raw_languages = cleaned_language_line.split(",")
languages = [language.strip() for language in raw_languages]
joined_by_slash = " / ".join(languages)
```

`strip` は、文字列の前後にある空白を取り除く。  
`split(",")` は、カンマを区切りとして文字列を分割する。

分割した直後の値には空白が残ることがあるため、各要素にも `strip` を使っている。  
`join` は、複数の文字列を1つの文字列に戻すときに使う。

### 7-2. `replace` は元の文字列を変更しない

`search_and_replace.py` では、`replace` を使って文字列を置換している。

```python
replaced_message = message.replace("Python", "JavaScript")
```

`replace` は、置換後の新しい文字列を返す。  
元の `message` そのものは変更されない。

文字列はイミュータブルな値であるため、加工結果を使いたい場合は戻り値を変数に受け取る。

### 7-3. 正規表現では raw string を使うことが多い

`regex_basics.py` では、メールアドレスのパターンを raw string で書いている。

```python
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
return re.sub(EMAIL_PATTERN, "[EMAIL]", text)
```

正規表現では、バックスラッシュを使うことが多い。  
そのため、`r"..."` の raw string を使うと、通常の文字列より読みやすくなる。

`re.sub` は、正規表現に一致した部分を別の文字列に置換する。

### 7-4. JSON は Python の list / dict と対応しやすい

`json_operations.py` では、JSON ファイルを読み込んでいる。

```python
with open(path, encoding="utf-8") as file:
    loaded_data = json.load(file)

return cast(list[UserRecord], loaded_data)
```

`json.load` は、JSON ファイルを Python の値として読み込む。  
今回の `users.json` は配列形式のため、Python 側では `list` として扱える。

各要素は `dict` のように扱えるため、`user["active"]` のようにキーを指定して値を読める。

### 7-5. JSON を書き出すときは `ensure_ascii` と `indent` を指定できる

`json_operations.py` では、JSON ファイルを書き出している。

```python
json.dump(users, file, ensure_ascii=False, indent=2)
```

`json.dump` は、Python の値を JSON としてファイルへ書き込む。  
`ensure_ascii=False` にすると、日本語なども読みやすい形で出力できる。

`indent=2` を指定すると、人間が読みやすい整形済み JSON になる。

### 7-6. CSV は読み込み時に型変換が必要になる

`csv_operations.py` では、CSV の行を読み込みながら `int` に変換している。

```python
scores.append(
    {
        "id": int(row["id"]),
        "name": row["name"],
        "score": int(row["score"]),
    }
)
```

CSV から読み込んだ値は、基本的に文字列として扱われる。  
そのため、数値として計算したい列は `int` などへ変換する必要がある。

今回の例では、`id` と `score` を `int` に変換している。

## 8. 引っかかりやすい点

### 8-1. `split(",")` しただけでは前後の空白は残る

`string_methods.py` では、カンマで分割した後に各要素を整えている。

```python
raw_languages = cleaned_language_line.split(",")
languages = [language.strip() for language in raw_languages]
```

`split(",")` は、カンマで文字列を分けるだけである。  
区切りの前後にある空白は自動では消えない。

そのため、分割後の各要素に対しても `strip` を使うことが多い。

### 8-2. `find` は見つからない場合に `-1` を返す

`search_and_replace.py` では、存在しない文字列を `find` している。

```python
java_index = message.find("Java")
```

`find` は、見つかった場合に開始位置のインデックスを返す。  
見つからない場合は `-1` を返す。

見つからない可能性がある場合は、`-1` を想定して処理する必要がある。

### 8-3. 正規表現は便利だが複雑にしすぎると読みにくい

`regex_basics.py` では、メールアドレスや日付のように形が決まった文字列を扱う。

```python
date_match = re.search(r"\d{4}-\d{2}-\d{2}", text)
```

正規表現は、パターンに合う文字列を探す場合に便利である。  
一方で、複雑な正規表現は読みづらくなりやすい。

まずは、メールアドレス、日付、区切り文字のように、用途を絞って読むのがよい。

### 8-4. `json.load` と `json.loads` は入力が違う

`json_operations.py` では、ファイルから JSON を読み込んでいる。

```python
with open(path, encoding="utf-8") as file:
    loaded_data = json.load(file)
```

`json.load` は、ファイルオブジェクトから JSON を読み込む。  
一方、`json.loads` は、JSON 形式の文字列から読み込む。

ファイルを読むのか、文字列を読むのかで使う関数が変わる。

### 8-5. `json.dump` と `json.dumps` は出力先が違う

`json_operations.py` では、ファイルへの書き込みと文字列化の両方を扱う。

```python
json.dump(users, file, ensure_ascii=False, indent=2)
json_text = json.dumps(active_users, ensure_ascii=False)
```

`json.dump` は、Python の値を JSON としてファイルへ書き込む。  
`json.dumps` は、Python の値を JSON 形式の文字列に変換する。

`s` が付く方は string と覚えると区別しやすい。

### 8-6. CSV の値は文字列として読み込まれる

`csv_operations.py` では、CSV の値を `int` に変換している。

```python
"id": int(row["id"]),
"score": int(row["score"]),
```

CSV はテキストデータのため、読み込んだ時点の値は文字列である。  
数値として合計や平均を出したい場合は、明示的な型変換が必要になる。

変換を忘れると、文字列結合になったり、計算でエラーになったりする。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- `strip`、`split`、`join` の基本的な使い方を説明できる
- `replace` が新しい文字列を返すことを説明できる
- `in`、`find`、`startswith`、`endswith` の用途を説明できる
- 正規表現で文字列を検索、抽出、置換できることを説明できる
- `json.load` と `json.loads` の違いを説明できる
- `json.dump` と `json.dumps` の違いを説明できる
- JSON が Python の `list` / `dict` と対応しやすいことを説明できる
- `csv.DictReader` と `csv.DictWriter` の基本を読める
- CSV から読み込んだ値に型変換が必要なことを説明できる
