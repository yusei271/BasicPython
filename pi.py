text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

# 文字数を計算してリスト化し、文字列に連結する
result = ''.join(map(lambda word: str(len(word.strip(',.'))), text.split()))

# 結果を出力
print(result)
