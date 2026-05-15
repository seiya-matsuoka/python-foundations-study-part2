# 10. 標準ライブラリの重要機能

## 1. 学習対象

この単位では、Python 標準ライブラリのうち、よく使う代表的な機能を扱う。

- `datetime`
- `math`
- `random`
- `statistics`
- `collections` の代表例
  - `Counter`
  - `defaultdict`
  - `deque`
- `itertools` の代表例
  - `chain`
  - `islice`
  - `product`
  - `groupby` の基礎
- `functools` の最小限
  - `partial`
  - `lru_cache` の基礎

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- `datetime` を使うと、日付、日時、時間差を扱える
- `math` を使うと、数学系の関数や定数を利用できる
- `random` を使うと、乱数やランダムな選択を扱える
- `statistics` を使うと、平均や中央値などの基本的な統計処理を扱える
- `Counter` を使うと、要素ごとの出現回数を数えられる
- `defaultdict` を使うと、キーごとの初期値を簡潔に扱える
- `deque` を使うと、両端への追加や取り出しを扱いやすい
- `itertools` を使うと、反復処理の組み合わせを簡潔に書ける
- `functools.partial` を使うと、引数の一部を固定した関数を作れる
- `functools.lru_cache` を使うと、同じ引数の計算結果をキャッシュできる

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/10_essential_standard_library/
  main.py
  datetime_examples.py
  math_random_statistics_examples.py
  collections_examples.py
  itertools_examples.py
  functools_examples.py
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 10 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `datetime_examples.py`
  - `date`、`datetime`、`timedelta`、文字列変換を扱う
- `math_random_statistics_examples.py`
  - `math`、`random`、`statistics` の代表的な処理を扱う
- `collections_examples.py`
  - `Counter`、`defaultdict`、`deque` を扱う
- `itertools_examples.py`
  - `chain`、`islice`、`product`、`groupby` を扱う
- `functools_examples.py`
  - `partial`、`lru_cache` を扱う

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/10_essential_standard_library/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/10_essential_standard_library/main.py
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
2. `datetime_examples.py`
3. `math_random_statistics_examples.py`
4. `collections_examples.py`
5. `itertools_examples.py`
6. `functools_examples.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、日時、数値処理、コレクション補助、反復処理補助、関数補助の順番で読む。

## 6. 処理の流れ

Unit 10 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. `datetime` のサンプルを実行する
5. `math`、`random`、`statistics` のサンプルを実行する
6. `collections` のサンプルを実行する
7. `itertools` のサンプルを実行する
8. `functools` のサンプルを実行する
9. 各ファイル内の `assert` により、軽い期待値確認を行う

この単位では、標準ライブラリを使って自前実装を減らす考え方を主題にしている。  
各ファイルの `run_...()` 関数は、テーマ別サンプルをまとめて実行するための入口として使う。

## 7. 注目ポイント

### 7-1. `datetime` は日付、日時、時間差を扱える

`datetime_examples.py` では、`date`、`datetime`、`timedelta` を使っている。

```python
release_date = date(2026, 5, 15)
started_at = datetime(2026, 5, 15, 9, 30, 0)
review_period = timedelta(days=7)
review_date = release_date + review_period
```

`date` は日付だけを表す。  
`datetime` は日付と時刻をまとめて表す。

`timedelta` は時間差を表す値で、日付や日時に足したり引いたりできる。  
日時処理を文字列のまま扱うより、専用の型として扱う方が安全で読みやすい。

### 7-2. `random.Random` に seed を渡すと結果を固定できる

`math_random_statistics_examples.py` では、`random.Random(42)` を使っている。

```python
rng = random.Random(42)

random_number = rng.randint(1, 10)
selected_language = rng.choice(["Python", "Java", "SQL"])
```

乱数は通常、実行ごとに結果が変わる。  
学習用コードや確認用コードでは、結果が毎回変わると `assert` が書きにくい。

`Random` に seed を渡すと、同じ順序の乱数を再現できる。  
そのため、この単位ではランダム処理の結果を固定して確認している。

### 7-3. `Counter` は出現回数を簡潔に数えられる

`collections_examples.py` では、単語ごとの出現回数を数えている。

```python
words = ["python", "java", "python", "sql", "python", "sql"]
word_counts = Counter(words)
```

`Counter` を使うと、要素ごとの出現回数を自前で `dict` に集計しなくてよい。  
`word_counts["python"]` のように書くと、該当要素の件数を取得できる。

出現回数の多い順に見たい場合は、`most_common()` を使える。

### 7-4. `defaultdict` はキーごとの list 作成を簡潔にする

`collections_examples.py` では、カテゴリごとの点数を `defaultdict` にまとめている。

```python
scores_by_category: defaultdict[str, list[int]] = defaultdict(list)

for category, score in score_rows:
    scores_by_category[category].append(score)
```

通常の `dict` では、キーが存在するか確認してから `list` を作る必要がある。  
`defaultdict(list)` を使うと、存在しないキーを参照したときに空の `list` が作られる。

キーごとに値を集める処理でよく使う形である。

### 7-5. `itertools.groupby` は事前の並び替えを意識する

`itertools_examples.py` では、売上データをカテゴリごとに集計している。

```python
sorted_sales = sorted(sales, key=itemgetter("category"))

for category, grouped_sales in groupby(sorted_sales, key=itemgetter("category")):
    total = 0
```

`groupby` は、連続した同じキーの要素をグループ化する。  
そのため、同じカテゴリが離れた位置にあると、別グループとして扱われる。

期待通りにカテゴリごとにまとめたい場合は、先に同じキーで並び替えることが多い。

### 7-6. `partial` は引数の一部を固定した関数を作る

`functools_examples.py` では、税率を固定した関数を作っている。

```python
apply_standard_tax = partial(apply_tax, tax_rate=0.1)
apply_reduced_tax = partial(apply_tax, tax_rate=0.08)
```

`partial` は、関数の一部の引数を先に固定した新しい関数を作る。  
この例では、`tax_rate` を固定することで、呼び出し側は価格だけを渡せばよくなる。

同じ関数を少し違う設定で繰り返し使いたい場合に役立つ。

### 7-7. `lru_cache` は同じ引数の再計算を減らせる

`functools_examples.py` では、再帰関数に `lru_cache` を付けている。

```python
@lru_cache(maxsize=32)
def fibonacci(number: int) -> int:
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)
```

`lru_cache` は、同じ引数で呼び出された結果をキャッシュする。  
同じ計算を何度も行う関数では、再計算を減らせる。

今回の `fibonacci` は学習用の例であり、キャッシュの効果が分かりやすいように再帰で書いている。

## 8. 引っかかりやすい点

### 8-1. `datetime` の文字列変換は形式指定が必要になる

`datetime_examples.py` では、`strftime` と `strptime` を使っている。

```python
formatted_datetime = started_at.strftime("%Y-%m-%d %H:%M:%S")
parsed_datetime = datetime.strptime("2026-05-15 09:30:00", "%Y-%m-%d %H:%M:%S")
```

`strftime` は、日時を文字列に変換する。  
`strptime` は、文字列を `datetime` に変換する。

どちらもフォーマット指定が必要であり、文字列の形と指定がずれると正しく変換できない。

### 8-2. `random` はそのままだと結果が固定されない

`math_random_statistics_examples.py` では、`random.Random(42)` を使っている。

```python
rng = random.Random(42)
```

`random.randint()` などを直接使うと、実行ごとに結果が変わる。  
これは実際のランダム処理としては自然だが、学習用の期待値確認では扱いにくい。

結果を固定したい場合は、seed を指定した `Random` オブジェクトを使うと確認しやすい。

### 8-3. `defaultdict` はキー参照だけで値が作られる

`collections_examples.py` では、`defaultdict(list)` を使っている。

```python
scores_by_category: defaultdict[str, list[int]] = defaultdict(list)
```

`defaultdict` は、存在しないキーを参照しただけで初期値を作る。  
便利な一方で、意図せずキーを増やす可能性もある。

存在確認だけが目的の場合は、`in` を使ってキーがあるかを確認する方が安全な場面がある。

### 8-4. `deque(maxlen=...)` は古い要素が自動で消える

`collections_examples.py` では、`deque(maxlen=3)` を使っている。

```python
recent_events: deque[str] = deque(maxlen=3)

recent_events.append("login")
recent_events.append("view")
recent_events.append("edit")
recent_events.append("logout")
```

`maxlen` を指定した `deque` は、最大件数を超えると古い要素が自動で削除される。  
この例では、4件追加しても最後の3件だけが残る。

履歴や直近ログを一定件数だけ持ちたい場合に使える。

### 8-5. `itertools` の戻り値は iterator であることが多い

`itertools_examples.py` では、`chain`、`islice`、`product` の結果を `list` にしている。

```python
all_skills = list(chain(backend_skills, python_skills))
first_five_even_numbers = list(islice(...))
color_size_pairs = list(product(colors, sizes))
```

`itertools` の多くの関数は、すぐに `list` を作るのではなく iterator を返す。  
中身を表示したり `assert` で確認したりしたい場合は、`list()` に変換すると分かりやすい。

大きいデータを扱う場合は、必要な分だけ取り出せることが利点になる。

### 8-6. `lru_cache` は引数が同じ場合に効果が出る

`functools_examples.py` では、同じ引数で `fibonacci(10)` を2回呼び出している。

```python
fibonacci_10 = fibonacci(10)
cache_after_first_call = fibonacci.cache_info()

fibonacci_10_again = fibonacci(10)
cache_after_second_call = fibonacci.cache_info()
```

`lru_cache` は、同じ引数で呼び出した結果を再利用する。  
そのため、引数が毎回異なる処理では効果が出にくい。

キャッシュを使う関数では、同じ入力に対して同じ結果を返すことも重要となる。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- `datetime` で日付、日時、時間差を扱えることを説明できる
- `strftime` と `strptime` の違いを説明できる
- `math`、`random`、`statistics` の基本的な用途を説明できる
- seed を指定した乱数の結果が固定されることを説明できる
- `Counter` で出現回数を数えられることを説明できる
- `defaultdict` でキーごとの値を集められることを説明できる
- `deque` の基本的な用途を説明できる
- `chain`、`islice`、`product`、`groupby` の基本を読める
- `partial` で引数の一部を固定した関数を作れることを説明できる
- `lru_cache` で同じ引数の計算結果をキャッシュできることを説明できる
