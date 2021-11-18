class OutputData:
    def __init__(self, keycap_lines, blank_picture):
        self.keycap_lines = keycap_lines
        self.blank_picture = blank_picture

    # トリミング写真結合
    def join_picture(self):
        for keycap_line in self.keycap_lines:
            trimmed_image_list = []
            image_height = keycap_line[0][0][1]  # その列の画像の高さ
            for keycap in keycap_line:
                trimmed_image_list.append(keycap)
                if !=lastnum:
                    append
                else:
                    opencv結合
    # 結合した写真をpdfとして出力
    def create_pdf(self):
        self.keycap_pictures
