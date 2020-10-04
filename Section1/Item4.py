# Cスタイルフォーマット文字列とstr.formatは使わずf文字列で埋め込む
print('Cスタイルフォーマットによる記述')
# 2進数と16進数を整数文字列に変換-Cスタイルフォーマット
# ※非推奨
a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))
print('###############################')

# 組み込みのformatとstr.format
print('組み込みformatによる記述')
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

# フォーマット済み文字列 ※推奨
print('フォーマット済み文字列による記述 ※推奨')
key = 'my_var'
value = 1.234
formatted = f'{key} = {value}'
print(formatted)

# f-stringのブレースホルダ
formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

'''
・Cスタイルフォーマットの問題2
文字列にフォーマットする前に値を修正しないといけない場合に、
読んで理解するのが難しいこと(p12)
'''
# f-stringによる問題2の解決
pantry = [
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15)
]
for i, (item, count) in enumerate(pantry):
    # Cスタイルフォーマット
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count)
    )
    print(f'old_style = {old_style}')

    # 組み込みformat
    new_style = '#{}: {:<10s} = {}'.format(
        i+1,
        item.title(),
        round(count)
    )
    print(f'new_style = {new_style}')

    # f-string
    f_string = f'#{i+1}: {item.title():<10s} = {round(count)}'
    print(f'f_string = {f_string}')

    print('#####')
    # assert 条件式, 条件式がFalseの場合に出力するメッセージ
    assert old_style == new_style == f_string
