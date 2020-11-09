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
    fresh_fruit['lemon'] = count - 1
    if fresh_fruit['lemon'] <= 0:
        fresh_fruit.pop('lemon')
    print('レモネード完成！！')


# サイダーを作るのにはアップルが4個必要らしい
def make_cider(count):
    fresh_fruit['apple'] = count - 4
    if fresh_fruit['apple'] <= 0:
        fresh_fruit.pop('apple')
    print('サイダー完成！！')


# バナナスムージーを作るのにバナナが2本必要
# スライスバナナを作る
def slice_bananas(count):
    fresh_fruit['banana'] -= 2
    fresh_fruit['slice_banana'] += 1


class OutOfBananas(Exception):
    pass


# バナナスムージーを作る
def make_smoothies(count):
    fresh_fruit['slice_banana'] -= 1
    if fresh_fruit['slice_banana'] <= 0:
        fresh_fruit.pop('slice_banana')
    print('バナナスムージー完成！！')


def out_of_stock():
    print('在庫切れ')


# getの第2引数は第一引数のキーが存在しなかったときの返り値
# レモネードの注文
if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()

# サイダーの注文
if (count := fresh_fruit.get('apple', 0)) >= 4:
    make_cider(count)

# バナナスムージーの注文
# バナナの在庫確認
if (count := fresh_fruit.get('banana', 0)) >= 2:
    # スライスバナナの在庫確認
    fresh_fruit['slice_banana'] = 0
    

    # スライスバナナの作成
    slice_bananas(count)
