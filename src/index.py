from pathlib import Path

import cv2
import numpy as np

# 受け取ったファイルの形式が正しいか確認
# 画像読み込み
image_path = Path(__file__).parent / "sample.jpeg"
image = cv2.imread(image_path.as_posix())
# 画像の大きさ変更
# image_resized = cv2.resize(image, dsize=(512, 512))
# processing
xs, xt = 300, 700
ys, yt = 10, 1000
trimmed_image = image[xs:xt, ys:yt]
# 画像保存
cv2.imwrite((image_path.parent / "output.jpeg").as_posix(), image_resized)
# 高さ、幅取得
height = image_resized.shape[0]
width = image_resized.shape[1]
# 高さ、幅表示
print(height)
print(width)
keycap_size_configs = {
    "A": [[0, 144], [0, 63]],
    "B": [[0, 144], [0, 164]],
    "C": [[0, 144], [0, 107]],
    "D": [[0, 144], [0, 131]],
    "E": [[0, 144], [0, 174]],
    "F": [[0, 144], [0, 174]],
    "G": [[0, 144], [0, 179]],
    "H": [[0, 144], [0, 228]],
    "I": [[0, 144], [0, 87]],
    "J": [[0, 144], [0, 548]],
}

"""
for i in range(10):
    keycap[i] = [[10 * i, 10 * (i + 1)], [20, 30]]
"""
# キーの作成
# 座標を切る
# 最初の場所を決めて切る、最初の場所がわかれば次の場所もわかるのでそこも同じように切る。
# とりあえず同じ大きさで切っていき、一番小さいキーを作る。
