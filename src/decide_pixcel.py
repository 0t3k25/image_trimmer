def calculate_height_pixcel_num(
    image_width: int, keyboard_width: int, keyboard_height: int
) -> int:
    height_pixcel_num = image_width * (keyboard_height / keyboard_width)
    return int(height_pixcel_num)


def keycap_width_height_pixcel_nun(
    image_width: int,
    image_height: int,
    keyboard_width: int,
    keyboard_height: int,
    keycap_width: int,
    keycap_height: int,
) -> int:
    keycap_width_pixcel_num = int(image_width * (keycap_width / keyboard_width))
    keycap_height_pixcel_num = int(image_height * (keycap_height / keyboard_height))
    return {"width": keycap_width_pixcel_num, "height": keycap_height_pixcel_num}
