"""
rangeではなくenumerateを使う
"""
from random import randint


# rangeは整数集合上をループするのに役に立つ
# 再現性を与えたいならseed値を設定する
print('rangeは整数集合上をループ')
random_bits = 0
for i in range(64):
    if randint(0, 1):
        # シフト
        # random_bits = random_bits | 1 << i
        random_bits |= 1 << i

print(bin(random_bits))
print('##################################')

# 文字列のリストはシーケンスを直接ループできる
print('文字列のリストを直接ループ')
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print(f'{flavor} is delicious')

print('#####################################')

"""
リスト中の要素のインデックスが必要なときを考える
例として、フレーバーのランキングを出力する
"""
# まずはrangeを使ってみる
print('rangeを使ったフレーバーのランキング')
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i + 1}: {flavor}')

# 次にenumerateを使う
# ポイントはyieldする点
print('enumerateを使ったフレーバーのランキング')
for i, flavor in enumerate(flavor_list):
    print(f'{i + 1}: {flavor}')
