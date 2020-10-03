# Cスタイルフォーマット文字列とstr.formatは使わずf文字列で埋め込む

# 2進数と16進数を整数文字列に変換-Cスタイルフォーマット
# ※非推奨
a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))
print('###############################')

# 組み込みのformatとstr.format
# 数値を3桁で区切る、小数点第2位までにする
a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

# センタリング
b = 'my string'
formatted = format(b, '^20s')
print('*', formatted, '*')

# 複数の値をまとめてフォーマットする
key = 'my_var'
value = 1.234
formatted = '{} = {}'.format(key, value)
print(formatted)

print('###############################')
