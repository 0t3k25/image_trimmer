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

# キーキャップの比率
keycap_height: "int" = 15
keycap_width: "int" = 13
ratio = keycap_width / keycap_height
print(ratio)
# キーの作成
# 座標を切る
# 最初の場所を決めて切る、最初の場所がわかれば次の場所もわかるのでそこも同じように切る。
# とりあえず同じ大きさで切っていき、一番小さいキーを作る。
# keycap 初期化
keycap_line_1 = [[[0, 1], [82 * i, 82 * (i + 1)]] for i in range(13)]  # リスト内包表記
keycap_line_1.append([[0, 144], [82 * 13, 1280]])  # backspace

keycap_line_2 = [None] * 14
for i in range(14):
    keycap_line_2[i] = [[0, 144], [82 * i, 82 * (i + 1)]]
    # Tabkey対応
    if i == 0:
        keycap_line_2[i] = [[0, 144], [0, 111]]
    elif i == 13:
        keycap_line_2[i] = [[0, 144], [111 + 82 * (i - 1), 1280]]

keycap = [keycap_line_1, keycap_line_2]
# 1行目作成
trimmed_image_list = []
for keycap_line in keycap:
    for keycap_range in keycap_line:
        trimmed_image = image[
            keycap_range[0][0] : keycap_range[0][1],
            keycap_range[1][0] : keycap_range[1][1],
        ]
        trimmed_image_list.append(trimmed_image)

for i, image in enumerate(trimmed_image_list):
    cv2.imwrite((image_path.parent / f"output_{i:04}.jpeg").as_posix(), image)


def a(c: int) -> int:
    if c == 1:
        return 1
    else:
        return 2
