"""
forループとwhileループの後のelseブロックは使わない

なぜandじゃなくてelseなのか…
なるほど確かに…
"""
# for-elseの基本的な使い方
print('for-elseの基本的な使い方')
for i in range(3):
    print('Loop', i)
else:
    print('Else Block!')

# breakを実行するとelseはスキップされる
print('breakを実行するとelseはスキップされる')
for i in range(3):
    print('Loop', i)
    if i == 1:
        break
else:
    print('Else block')

# 空のシーケンスでループを回したら、elseがすぐに実行される
print('空のシーケンスでループを回したら、elseがすぐに実行される')
for x in []:
    print('Never runs')
else:
    print('For Else block!!')
print('#################################')

# 互いに素かどうかを判定するコード
# 非推奨
print('互いに素かどうかを判定するコード')
a = 4
b = 9

for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        # coprimeという単語を初めて知った
        print('Not coprime')
else:
    print('Comprime')

"""
上記のcomrimeのコードは使わない
普通はヘルパー関数を使う
ヘルパー関数の例を2つあげる
"""
# comprime関数①
print('comprime関数①')


def comprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
        return True


assert comprime(4, 9)
print(comprime(4, 9))
# assert not comprime(3, 6)
print(not comprime(3, 6))

# comprime関数②
# こっちの方が好き！！
print('comprime関数②')


def comprime(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
        return is_coprime


print(comprime(4, 9))
