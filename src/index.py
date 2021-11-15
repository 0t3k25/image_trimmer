from pathlib import Path

import json
import decide_pixcel
import cv2
import numpy as np


# キーボードの形式が設定してあるファイルまでのパス
keycap_config_path = Path(__file__).parent.parent / "keyconfig/keycap_config.json"
# json読み込み
keycap_config_json_file = open(keycap_config_path.as_posix(), "r")
keycap_config_json = json.load(keycap_config_json_file)
# 受け取ったファイルの形式が正しいか確認（あとで書く）
# キーボードの大きさ
keyboard_width = 27.2
keyboard_height = 9
# 画像までのパス
image_path = Path(__file__).parent / "sample.jpeg"
# 画像読み込み
image = cv2.imread(image_path.as_posix())
# 画像の大きさ
image_height, image_width = image.shape[:2]
# 画像の高さ決定および変更
mod_image_height = decide_pixcel.caluclate_height_pixcel_num(
    image_width,
    keyboard_width,
    keyboard_height,
)
# 大きさが規定の大きさなら変更しない
if image_height != mod_image_height:
    image = cv2.resize(image, (int(image_width), int(mod_image_height)))
    image_height = image.shape[0]
# ユーザーに登録してもらった値よりそれぞれのキーのピクセル数を出す
keycap_sizes = [
    decide_pixcel.keycap_width_height_pixcel_nun(
        image_width,
        image_height,
        keyboard_width,
        keyboard_height,
        keycap_config["width"],
        keycap_config["height"],
    )
    for keycap_config in keycap_config_json.values()
]
print(keycap_sizes)
# keycap 初期化
# keycap_config = [[[y, dy], [x, dx]]]
# 1列目作成
keycap_line_1 = [
    [
        [0, keycap_sizes[0]["height"]],
        [keycap_sizes[0]["width"] * i, keycap_sizes[0]["width"] * (i + 1)],
    ]
    for i in range(13)
]  # リスト内包表記
keycap_line_1.append(
    [[0, keycap_sizes[0]["height"]], [keycap_sizes[0]["width"] * 13, image_width]]
)  # backspace
# 2列目作成
keycap_line_2 = [None] * 14
for i in range(14):
    keycap_line_2[i] = [
        [keycap_sizes[0]["height"], keycap_sizes[0]["height"] * 2],
        [
            keycap_sizes[1]["width"] + keycap_sizes[0]["width"] * (i - 1),
            keycap_sizes[1]["width"] + keycap_sizes[0]["width"] * i,
        ],
    ]
    if i == 0:
        keycap_line_2[i] = [
            [keycap_sizes[0]["height"], keycap_sizes[0]["height"] * 2],
            [0, keycap_sizes[1]["width"]],
        ]  # Tab
    elif i == 13:
        keycap_line_2[i] = [
            [keycap_sizes[0]["height"], keycap_sizes[0]["height"] * 2],
            [
                keycap_sizes[1]["width"] + keycap_sizes[0]["width"] * (i - 1),
                image_width,
            ],
        ]  # \|
# 3列目作成
keycap_line_3 = [None] * 13
for i in range(13):
    keycap_line_3[i] = [
        [keycap_sizes[0]["height"] * 2, keycap_sizes[0]["height"] * 3],
        [
            keycap_sizes[2]["width"] + keycap_sizes[0]["width"] * (i - 1),
            keycap_sizes[2]["width"] + keycap_sizes[0]["width"] * i,
        ],
    ]
    if i == 0:
        keycap_line_3[i] = [
            [keycap_sizes[0]["height"] * 2, keycap_sizes[0]["height"] * 3],
            [0, keycap_sizes[2]["width"]],
        ]  # Tab
    elif i == 12:
        keycap_line_3[i] = [
            [keycap_sizes[0]["height"] * 2, keycap_sizes[0]["height"] * 3],
            [
                keycap_sizes[2]["width"] + keycap_sizes[0]["width"] * (i - 1),
                image_width,
            ],
        ]  # \|
# 4列目作成
keycap_line_4 = [None] * 12
for i in range(12):
    keycap_line_4[i] = [
        [keycap_sizes[0]["height"] * 3, keycap_sizes[0]["height"] * 4],
        [
            keycap_sizes[3]["width"] + keycap_sizes[0]["width"] * (i - 1),
            keycap_sizes[3]["width"] + keycap_sizes[0]["width"] * i,
        ],
    ]
    if i == 0:
        keycap_line_4[i] = [
            [keycap_sizes[0]["height"] * 3, keycap_sizes[0]["height"] * 4],
            [0, keycap_sizes[3]["width"]],
        ]  # Shift
    elif i == 11:
        keycap_line_4[i] = [
            [keycap_sizes[0]["height"] * 2, keycap_sizes[0]["height"] * 3],
            [
                keycap_sizes[3]["width"] + keycap_sizes[0]["width"] * (i - 1),
                image_width,
            ],
        ]  # Shift
# 5列目作成
keycap_line_5 = [None] * 8
for i in range(8):
    keycap_line_5[i] = [
        [keycap_sizes[0]["height"] * 4, keycap_sizes[0]["height"] * 5],
        [
            keycap_sizes[4]["width"] * i,
            keycap_sizes[4]["width"] * (i + 1),
        ],
    ]
    if i == 3:
        keycap_line_5[i] = [
            [keycap_sizes[0]["height"] * 4, keycap_sizes[0]["height"] * 5],
            [
                keycap_sizes[4]["width"] * i,
                keycap_sizes[4]["width"] * i + keycap_sizes[5]["width"],
            ],
        ]
    elif i == 7:
        keycap_line_5[i] = [
            [keycap_sizes[0]["height"] * 4, keycap_sizes[0]["height"] * 5],
            [
                keycap_sizes[4]["width"] * (i - 1) + keycap_sizes[5]["width"],
                image_width,
            ],
        ]
    elif i > 3:
        keycap_line_5[i] = [
            [keycap_sizes[0]["height"] * 4, keycap_sizes[0]["height"] * 5],
            [
                keycap_sizes[4]["width"] * (i - 1) + keycap_sizes[5]["width"],
                keycap_sizes[4]["width"] * i + keycap_sizes[5]["width"],
            ],
        ]
print(keycap_line_5)
# keycap配列にそれぞれの列を追加
keycap = [keycap_line_1, keycap_line_2, keycap_line_3, keycap_line_4, keycap_line_5]
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
