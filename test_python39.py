from datetime import datetime
from typing import List
from zoneinfo import ZoneInfo

# Python3.9のテストです
"""
10/5 Python3.9.0が公開される
https://www.python.jp/pages/python3.9.html
"""

"""
辞書のマージ演算子
オブジェクトの和から、新しいオブジェクトを作る
"""
print('マージ演算子の結果')
# 基本操作
print({1: 'A'} | {2: 'B'})
# 同じキーがある場合
print({1: 'あ', 2: 'い'} | {2: 'う'})

# set型同士の演算
print({1, 2, 3} | {2, 3, 4})
print('#############################')

# |=代入文
print('|=代入文の結果')
# 左辺の辞書に右辺の辞書を追加することができる
d1 = {1: 'A'}
d1 |= {2: 'B'}
print(d1)

# 右辺にキーと値のシーケンスを指定できる
d1 = {1: 'A'}
d1 |= [(2, 'B'), (3, 'C')]
print(d1)
print('#############################')

"""
removeprefix()メソッドとremevesuffix()メソッドによる文字列操作
"""
print("lsttripの確認")
# lstrip()とrsturip()で文字列の前後の空白を取り除く
s = "   hello   "
print(repr(s))
print(repr(s.lstrip()))

# GithubのコミットログからIssue番号だけを取り出す
print("GithubのコミットログGH-1234からIssue番号だけを取り出す\n"
      "従来の方法")
text = "GH-1234"
if text.startswith("GH-"):
    text = text[3:]

print(text)

# removeprefix()メソッドを使うを使う
print("removeprefix()を使う")
text = "GH-1234"
text = text.removeprefix("GH-")
print(text)

# removesuffix()も使ってみる
print("removesuffix()を使ってみる")
text = "[大安売り]"
print(text)
print(text.removeprefix("[").removesuffix("]"))
print("#############################")

"""
組み込みGeneric型
"""
# これまでのコード
intlist: List[int] = [1, 2, 3]
print(intlist)

# 新しくなったコード
intlist: list[int] = [1, 2, 3]
print(intlist)
print("############################33")

"""
zoneinfoモジュール
"""
tokyo = ZoneInfo("Asia/Tokyo")

now = datetime(2020, 10, 1, 0, 0, 0, tzinfo=tokyo)
print(now.isoformat())
