"""
代入式で繰り返しを防ぐ
walrus（セイウチ）演算子
a := b 「aウォルラスb」
"""
# ジュースに使うフルーツの籠の中身を表現する
fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}


# レモネードを作るのにレモンを使う
def make_lemonade(count):
    fresh_fruit['lemon'] -= 1
    if fresh_fruit['lemon'] <= 0:
        fresh_fruit.pop('lemon')
    print('レモネード完成！！')


def out_of_stock():
    print('在庫切れ')


# getの第2引数は、第一引数のキーが存在しなかったときの返り値
count = fresh_fruit.get('lemon', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()
