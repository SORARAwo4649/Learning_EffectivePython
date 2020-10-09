"""
インデックスではなくアンパックを使う
"""
# 辞書からタプルを作る
print('辞書からタプルを作る')
snack_colors = {
    'chips': 140,
    'popcorn': 80,
    'nuts': 190,
}
items = tuple(snack_colors.items())
print(items)

# タプルの値はインデックスでアクセスできる
# 非推奨
print('インデックスによるアクセス')
item = ('Peanut butter', 'Jelly')
first = item[0]
second = item[1]
print(first, 'and', second)

# アンパック構文による複数代入
# 推奨！！
print('アンパック構文による複数代入')
item = ('Peanut butter', 'Jelly')
first, second = item
print(first, 'and', second)
print('##########################')

"""
リスト、シーケンス、イテラブル内の深いレベルのイテラブルにも使える
深いレベルとはネストのことだと思う
次のコードが推奨されているわけではない
一時変数を使わないのがポイント
"""
print('深いレベルのアンパック')
favorite_snacks = {
    'salty': ('pretzels', 100),
    'sweet': ('cookies', 180),
    'veggie': ('carrots', 20),
}
((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favorite_snacks.items()

print(f'Favorite {type1} is {name1} with {cals1} calories')
print(f'Favorite {type2} is {name2} with {cals2} calories')
print(f'Favorite {type3} is {name3} with {cals3} calories')
print('#######################################')

"""
バブルソートのコードを、インデックスを使ったコードとアンパックを使ったコードとを比較する
"""
print('インデックスを使ったバブルソートのコード')


def bubble_sort(a):
    # 変数名をiではなく_を使っている
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                temp = a[i]
                a[i] = a[i - 1]
                a[i - 1] = temp


names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)

print('アンパックを使ったバブルソートのコード')


def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]


names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)
print('#############################')

"""
forループや内包表記、ジェネレータ式におけるターゲットリスト
インデックスを使うコードとアンパックを使うコードで比較する
"""
# インデックスを使う場合
# 非推奨
print('インデックスを使う場合')
snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'#{i + 1}: {name} has {calories} calories')

# アンパックを使う場合
# 推奨
print('アンパックを使う場合')
for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name} has {calories} calories')
