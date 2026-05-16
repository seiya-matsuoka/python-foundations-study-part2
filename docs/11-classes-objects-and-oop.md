# 11. クラス・オブジェクト・オブジェクト指向

## 1. 学習対象

この単位では、Pythonにおけるクラス、オブジェクト、オブジェクト指向の基本を扱う。

- `class`
- `__init__`
- インスタンス属性
- インスタンスメソッド
- クラス属性
- クラスメソッド
- スタティックメソッド
- `property`
- `dataclass`
- `super()`
- 継承
- メソッドオーバーライド
- 合成
- duck typing の基本
- 特殊メソッドの基礎
  - `__repr__`
  - `__str__`
  - `__eq__`
- 抽象基底クラスの最小限
- `Enum` の最小限

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- `class` を使うと、状態と振る舞いをまとめた型を定義できる
- `__init__` は、インスタンス生成時の初期化処理として使う
- インスタンス属性は、インスタンスごとに異なる状態を持てる
- インスタンスメソッドは、`self` を通してインスタンスの状態を扱う
- クラス属性は、クラスに属する共有の値として使える
- `classmethod` は、クラス自身を受け取るメソッドとして使う
- `staticmethod` は、`self` や `cls` を使わない関連処理として使う
- `property` は、計算結果を属性のように見せたい場合に使える
- `dataclass` は、値を持つクラスの定型コードを減らせる
- `super()` は、親クラスの処理を呼び出すために使う
- 継承とメソッドオーバーライドにより、共通処理と差分処理を分けられる
- 合成は、別のオブジェクトを部品として持つ設計である
- duck typing では、継承関係よりも必要な振る舞いを持つかを重視する
- 特殊メソッドにより、文字列表現や等価性を定義できる
- 抽象基底クラスは、実装すべきメソッドの形を定義できる
- `Enum` は、取りうる値を限定した名前付きの定数群として使える

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/11_classes_objects_and_oop/
  main.py
  class_basics.py
  method_types_and_property.py
  dataclass_examples.py
  inheritance_and_super.py
  composition_and_duck_typing.py
  abc_and_enum.py
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 11 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `class_basics.py`
  - `class`、`__init__`、インスタンス属性、インスタンスメソッド、クラス属性を扱う
- `method_types_and_property.py`
  - `classmethod`、`staticmethod`、`property` を扱う
- `dataclass_examples.py`
  - `dataclass`、`__repr__`、`__str__`、`__eq__` を扱う
- `inheritance_and_super.py`
  - 継承、`super()`、メソッドオーバーライドを扱う
- `composition_and_duck_typing.py`
  - 合成、duck typing の基本を扱う
- `abc_and_enum.py`
  - 抽象基底クラス、`Enum` を扱う

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/11_classes_objects_and_oop/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/11_classes_objects_and_oop/main.py
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
2. `class_basics.py`
3. `method_types_and_property.py`
4. `dataclass_examples.py`
5. `inheritance_and_super.py`
6. `composition_and_duck_typing.py`
7. `abc_and_enum.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、クラスの基本、メソッド種別、dataclass、継承、合成、抽象基底クラスと Enum の順番で読む。

## 6. 処理の流れ

Unit 11 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. クラス定義、インスタンス属性、インスタンスメソッドのサンプルを実行する
5. `classmethod`、`staticmethod`、`property` のサンプルを実行する
6. `dataclass` と特殊メソッドのサンプルを実行する
7. 継承、`super()`、メソッドオーバーライドのサンプルを実行する
8. 合成と duck typing のサンプルを実行する
9. 抽象基底クラスと `Enum` のサンプルを実行する
10. 各ファイル内の `assert` により、軽い期待値確認を行う

この単位では、Python におけるオブジェクト指向の基本的な書き方を主題にしている。  
Java のクラス構文と似ている部分もあるが、`self`、`dataclass`、duck typing など Python らしい違いも確認する。

## 7. 注目ポイント

### 7-1. `self` は呼び出し元のインスタンスを表す

`class_basics.py` では、`User` クラスのインスタンス属性を扱う。

```python
def __init__(self, name: str, age: int) -> None:
    self.name = name
    self.age = age
    self.status = User.default_status
```

`self.name` や `self.age` は、インスタンスごとに保持される値である。  
Java の `this` に近いが、Python ではメソッドの第1引数として明示的に `self` を書く。

インスタンスメソッドでは、`self` を通してインスタンス属性を参照したり更新したりする。

### 7-2. `classmethod` は別の生成方法を用意するときに使いやすい

`method_types_and_property.py` では、文字列から `Product` を作成している。

```python
@classmethod
def from_text(cls, text: str) -> "Product":
    name, price_text = text.split(",")
    return cls(name.strip(), int(price_text.strip()))
```

`classmethod` の第1引数 `cls` は、クラス自身を表す。  
この例では、通常の `__init__` とは別に、カンマ区切り文字列からインスタンスを作る入口を用意している。

ファクトリメソッドのような使い方をしたい場合に向いている。

### 7-3. `property` は計算結果を属性のように見せられる

`method_types_and_property.py` では、税込価格を `property` として定義している。

```python
@property
def tax_included_price(self) -> int:
    return int(self.base_price * (1 + Product.tax_rate))
```

`property` を使うと、呼び出し側は `product.tax_included_price` のように属性として参照できる。  
内部では計算しているが、利用側からは値を読むだけの属性に見える。

メソッド呼び出しにするか、`property` にするかは、利用側から見た自然さを考えて選ぶ。

### 7-4. `dataclass` は値を持つクラスの定型コードを減らす

`dataclass_examples.py` では、座標を `dataclass` で定義している。

```python
@dataclass
class Point:
    x: int
    y: int
```

`dataclass` を使うと、`__init__`、`__repr__`、`__eq__` などが自動生成される。  
値を保持することが主目的のクラスでは、通常の `class` より簡潔に書ける。

同じ属性値を持つ `Point` 同士が等しいと判定される点にも注目する。

### 7-5. `super()` は親クラスの処理を再利用する

`inheritance_and_super.py` では、子クラスから親クラスの初期化処理を呼び出している。

```python
class EmailNotification(Notification):
    def __init__(self, recipient: str, subject: str) -> None:
        super().__init__(recipient)
        self.subject = subject
```

`super().__init__(recipient)` により、親クラスの `__init__` を呼び出している。  
共通の初期化処理は親クラスに置き、子クラスでは差分だけを追加できる。

継承では、共通処理と個別処理の分け方が重要となる。

### 7-6. 合成は部品を差し替えやすい

`composition_and_duck_typing.py` では、`ReportService` が送信役を属性として持っている。

```python
class ReportService:
    def __init__(self, sender: Sender) -> None:
        self.sender = sender
```

このように、別のオブジェクトを属性として持つ設計を合成と呼ぶ。  
`ReportService` は送信処理の詳細を知らず、`sender.send(...)` に処理を委譲している。

送信役を `ConsoleSender` や `MemorySender` に差し替えられるため、継承より柔軟に扱える場面がある。

### 7-7. 抽象基底クラスは実装すべき形を示す

`abc_and_enum.py` では、`Formatter` を抽象基底クラスとして定義している。

```python
class Formatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        raise NotImplementedError
```

抽象基底クラスは、子クラスが実装すべきメソッドの形を定義できる。  
`UpperFormatter` や `PrefixFormatter` は、`format` メソッドを実装することで具体的な処理を持つ。

最低限の使い方としては、共通のインターフェースを示したい場合に使える。

## 8. 引っかかりやすい点

### 8-1. クラス属性とインスタンス属性を混同しない

`class_basics.py` では、`default_status` をクラス属性として定義している。

```python
class User:
    default_status = "active"

    def __init__(self, name: str, age: int) -> None:
        self.status = User.default_status
```

`default_status` はクラスに属する値である。  
一方、`self.status` はインスタンスごとの値である。

共通の既定値として使うものと、インスタンスごとに変わる状態は分けて考える。

### 8-2. `staticmethod` は何でも入れる場所ではない

`method_types_and_property.py` では、価格判定を `staticmethod` として定義している。

```python
@staticmethod
def is_valid_price(price: int) -> bool:
    return price >= 0
```

`staticmethod` は、`self` や `cls` を使わない処理をクラス内に置くための仕組みである。  
ただし、クラスと関係が薄い処理まで入れると、責務が分かりにくくなる。

クラスに関連する補助処理かどうかを考えて使う。

### 8-3. `__repr__` と `__str__` は用途が違う

`dataclass_examples.py` では、`Task` に `__repr__` と `__str__` を定義している。

```python
def __repr__(self) -> str:
    return f"Task(title={self.title!r}, priority={self.priority!r})"

def __str__(self) -> str:
    return f"{self.title} / priority={self.priority}"
```

`__repr__` は、開発者向けの表現として使われることが多い。  
`__str__` は、ユーザー向けに読みやすい表現として使われることが多い。

どちらも文字列表現だが、想定する読み手が違う。

### 8-4. 継承は共通化できるが、使いすぎると複雑になる

`inheritance_and_super.py` では、`Notification` を親クラスにしている。

```python
class EmailNotification(Notification):
    def build_message(self, body: str) -> str:
        base_message = super().build_message(body)
        return f"[{self.subject}] {base_message}"
```

継承を使うと、親クラスの共通処理を再利用できる。  
一方で、親子関係が深くなると、どの処理がどこで定義されているか追いにくくなる。

共通処理の再利用だけが目的なら、合成の方が分かりやすい場合もある。

### 8-5. duck typing は「同じ継承元か」ではなく「必要な振る舞いを持つか」を見る

`composition_and_duck_typing.py` では、`deliver_message` が `send` を使っている。

```python
def deliver_message(sender: Sender, message: str) -> str:
    return sender.send(message)
```

重要なのは、渡されたオブジェクトが `send` メソッドを持っていることである。  
同じ親クラスを継承しているかどうかだけが基準ではない。

Python では、このように必要な振る舞いに注目する考え方がよく出てくる。

### 8-6. `Enum` は文字列定数のばらつきを防ぐ

`abc_and_enum.py` では、タスク状態を `Enum` として定義している。

```python
class TaskStatus(Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"
```

文字列を直接あちこちに書くと、タイポや表記ゆれが起きやすい。  
`Enum` を使うと、取りうる値を名前付きでまとめられる。

状態や種別のように候補が決まっている値では、`Enum` が使いやすい場合がある。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- `class` と `__init__` の基本的な役割を説明できる
- インスタンス属性とクラス属性の違いを説明できる
- インスタンスメソッドで `self` を使う理由を説明できる
- `classmethod`、`staticmethod`、`property` の違いを説明できる
- `dataclass` が定型コードを減らすことを説明できる
- `__repr__`、`__str__`、`__eq__` の基礎を説明できる
- 継承、`super()`、メソッドオーバーライドの基本を説明できる
- 合成と継承の違いを説明できる
- duck typing の基本的な考え方を説明できる
- 抽象基底クラスの最小限の使い方を説明できる
- `Enum` の基本的な用途を説明できる
