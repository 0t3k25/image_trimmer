from pathlib import Path

import cv2
import numpy as np

# 受け取ったファイルの形式が正しいか確認
# 画像読み込み
image_path = Path(__file__).parent / "sample.jpeg"
image = cv2.imread(image_path.as_posix())
# 画像の大きさを1280×720の大きさに変更
print(image.shape)
# 画像の大きさ変更
image_resized = cv2.resize(image, dsize=(1280, 720))
# processing
xs, xt = 0, 144
ys, yt = 0, 82
trimmed_image = image[xs:xt, ys:yt]
# 画像保存
cv2.imwrite((image_path.parent / "output.jpeg").as_posix(), trimmed_image)
# 高さ、幅取得
# height = image_resized.shape[0]
# width = image_resized.shape[1]
# 高さ、幅表示
# print(height)
# print(width)
print(image_resized.shape)
"""
for i in range(10):
    keycap[i] = [[10 * i, 10 * (i + 1)], [20, 30]]
"""
# キーの作成
# 座標を切る
# 最初の場所を決めて切る、最初の場所がわかれば次の場所もわかるのでそこも同じように切る。
# とりあえず同じ大きさで切っていき、一番小さいキーを作る。
keycap = []
# 1行目作成
for i in range(14):
    keycap[i] = [[0, 144], [82 * i, 82 * (i + 1)]]
    # backspacekey対応
    if i == 13:
        keycap[i] = [[0, 144], [82 * i, 1280]]
    trimmed_image = image[
        keycap[i][0][0] : keycap[i][0][1], keycap[i][1][0] : keycap[i][1][1]
    ]
# 2行目作成
for i in range(29):
    keycap[i] = [[0, 144], [82 * i, 82 * (i + 1)]]
    # Tabkey対応
    if i == 0:
        keycap[i] = [[0, 144], [0, 111]]
    elif i == 13:
        keycap[i] = [[0, 144], [111 + 82 * (i - 1), 1280]]
    trimmed_image = image[
        keycap[i][0][0] : keycap[i][0][1], keycap[i][1][0] : keycap[i][1][1]
    ]
    cv2.imwrite((image_path.parent / f"output{i}.jpeg").as_posix(), trimmed_image)
