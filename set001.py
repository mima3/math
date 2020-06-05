"""集合のテスト
300以下の自然数のうち以下の値をもとめよ
"""
# ベン図を書くためのインポート
from matplotlib import pyplot as plt
import numpy as np
# 日本語化
# https://qiita.com/yniji/items/3fac25c2ffa316990d0c
from matplotlib_venn import venn3, venn3_circles
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']


s = set(range(1,301))

# 5の倍数
x5 = set(filter(lambda n:n%5 is 0, s))
print(f"5の倍数の数：{len(x5)}")

# 5の倍数ではない数(sとx5の差集合)
x5_diff = s - x5
print(f"5の倍数ではない数：{len(x5_diff)}")


# 8の倍数
x8 = set(filter(lambda n:n%8 is 0, s))
print(f"8の倍数の数：{len(x8)}")


# 5の倍数かつ8の倍数(積集合)
x5_and_8 = x5 & x8
print(f"5の倍数かつ8の倍数：{len(x5_and_8)}")

# 5の倍数または8の倍数(和集合)
x5_or_8 = x5 | x8
print(f"5の倍数または8の倍数の数：{len(x5_or_8)}")

# 5の倍数または8の倍数のどちらか一方に含まれる対称差集合
x5_symdif_x8 = x5 ^ x8
print(f"5の倍数または8の倍数のどちらか一方に含まれる数：{len(x5_symdif_x8)}")

venn3([s, x5, x8], ('300未満の数', '5の倍数', '8の倍数'))
plt.show()