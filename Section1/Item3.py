# bytesとstrの違いを知っておく

# bytesによる出力
a = b'h\x65llo'
print(list(a))
print(a)

# strによる出力
a = 'a\u0300 propos'
print(list(a))
print(a)
print('############################')


# 常にstrを返す関数
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


# https://docs.python.org/ja/3/library/reprlib.html
print(repr(to_str(b'foo')))
print(repr(to_str('bar')))


# 常にbytesを返す関数
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
