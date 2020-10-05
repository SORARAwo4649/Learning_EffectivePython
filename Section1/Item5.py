# 複雑な式の代わりにヘルパー関数を書く(p20)
"""
ヘルパー関数とは、難解な１行を分割する関数(?)で、再利用可能にもする
「パース(解析)する」=>「復号する」で使っているみたい
"""
from urllib.parse import parse_qs

# URLのクエリ文字列を解析する
my_value = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
# reprはデバッグ用の出力で使う
# reprは与えられた値のPython表現を生成する
print(repr(my_value))
# 出力結果の違いが分からない
print('#####')
print(my_value)
print('#######################')

"""
部分式がFalseならor以下を評価する
"""
red = my_value.get('red', [''])[0] or 0
green = my_value.get('green', [''])[0] or 0
opacity = my_value.get('opacity', [''])[0] or 0
"""
https://docs.python.org/ja/3/tutorial/inputoutput.html
「!r」はreprを適用している
"""
print(f'Red:     {red!r}')
print(f'Green:   {green!r}')
print(f'Opacity: {opacity!r}')
# 上下でちょっと違う!!
print('#####')
print(f'Red:     {red}')
print(f'Green:   {green}')
print(f'Opacity: {opacity}')

"""
・上のコードの問題点
文字列が返されたり、数式が返されたりすること
TorFの判別が「良きに計らえ」となっているのが原因かと考える

↓すべての引数値を整数にして数式が使えるようにする
また再利用可能にするためにヘルパー関数を記述する
"""


def get_first_int(values, key, default=0):
    # foundはlistで返される
    found = values.get(key, [''])
    # print(repr(type(found)))
    if found[0]:
        return int(found[0])
    else:
        return default


green = get_first_int(my_value, 'green')
