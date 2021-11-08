from pathlib import Path

import cv2
import numpy as np

import json

# キーボードの形式(json)のパス

# 値によってどのキーボードの形式か判別
keyboard_mold = open()
# 受け取ったファイルの形式が正しいか確認（あとで書く）

# 画像までのパス
image_path = Path(__file__).parent / "sample.jpeg"
# 画像読み込み
image = cv2.imread(image_path.as_posix())
# 画像の大きさ
image_height = image.shape[0]
image_width = image.shape[1]
print(image.shape)
# 1番小さいキーキャップの縦横比率
letterkey_height: "int" = 1.8
letterkey_width: "int" = 1.8
letterkey_width_height_ratio = letterkey_height / letterkey_width
# tabキー
tabkey_height: "int" = 1.8
tabkey_width: "int" = 2.8
tabkey_width_height_ratio = tabkey_width / tabkey_height
# capsキー
capskey_height: "int" = 1.8
capskey_width: "int" = 3.3
capskey_width_height_ratio = capskey_width / capskey_height
# キーボードの縦の長さ(cm)
total_height = 1.8 * 5
# キーボードの横の長さ(cm)
total_width = 1.8 * 13 + 3.8
# キーボードの縦と横の比率
ratio = total_height / total_width
# 画像の大きさ設定
image = cv2.resize(image, (int(image_width), int(image_width * ratio)))
image_height = image.shape[0]
image_width = image.shape[1]
# letterkeyのピクセル数
letterkey_width_pixel_num = int(image_height / 5)
letterkey_height_pixel_num = int(image_height / 5)
# tabkeyのピクセル数
tabkey_width_pixel_num = int(letterkey_width_pixel_num * tabkey_width_height_ratio)
# capskeyのピクセル数
capskey_width_pixel_num = int(letterkey_width_pixel_num * capskey_width_height_ratio)
# keycap 初期化
# keycap_config = [[[y, dy], [x, dx]]]
keycap_line_1 = [
    [
        [0, letterkey_height_pixel_num],
        [letterkey_width_pixel_num * i, letterkey_width_pixel_num * (i + 1)],
    ]
    for i in range(13)
]  # リスト内包表記
keycap_line_1.append(
    [[0, letterkey_height_pixel_num], [letterkey_width_pixel_num * 13, image_width]]
)  # backspace

keycap_line_2 = [None] * 14
for i in range(14):
    keycap_line_2[i] = [
        [letterkey_height_pixel_num, letterkey_height_pixel_num * 2],
        [letterkey_width_pixel_num * i, letterkey_width_pixel_num * (i + 1)],
    ]
    if i == 0:
        keycap_line_2[i] = [
            [letterkey_height_pixel_num, letterkey_height_pixel_num * 2],
            [0, tabkey_width_pixel_num],
        ]  # Tabkey
    elif i == 13:
        keycap_line_2[i] = [
            [int(image_height / 5), int(image_height / 5) * 2],
            [tabkey_width_pixel_num + letterkey_width_pixel_num * (i - 1), image_width],
        ]  # \|キー

keycap_line_3 = [None] * 14
for i in range(14):
    keycap_line_3[i] = []

keycap = [keycap_line_1, keycap_line_2]
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
print(keycap)
