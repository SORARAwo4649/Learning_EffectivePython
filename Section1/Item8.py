"""
イテレータを並行に処理するにはzipを使う
"""
import itertools


# Pythonでは元となるリストを簡単に取得し、内包式を利用して新たなリストを作れる
print('内包表記を使ってリストから新たなリストを作る')
names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
print(counts)
print('##################################')

"""
元のリストの要素とインデックスを対応させる
2つのリストの処理を並行させたければ、元のリストnameの長さでイテレーションする
"""
# このコードは非推奨
print('rangeを使ってリストの並行処理')
longest_name = None
max_counts = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_counts:
        longest_name = names[i]
        max_counts = count

print(longest_name)

# 上記をenumerateを使って改善
# 改善はされるが非推奨
print('enumerateを使った改善')
longest_name = None
max_count = 0
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

# zipを使った改善
# 推奨
print('zipを使った改善')
max_letters = 0
longest_name = None
for name, count in zip(names, counts):
    if count > max_letters:
        longest_name = name
        max_letters = count

print(max_letters, longest_name)
print('######################################')

"""
zip処理の対象となるリストの長さが同じかどうか革新が持てないなら、
組み込みモジュールitertoolsのzip_longest関数を使う

欠損値のデフォルトはNoneになる
"""
names.append('Rosalind')
for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')
