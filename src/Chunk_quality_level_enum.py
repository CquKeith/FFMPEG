def get_bit_rate_by_level(level):
    return QualityLevel.BIT_RATE[level]


def get_width_by_level(level):
    return QualityLevel.WIDTH[level]


def get_height_by_level(level):
    return QualityLevel.HEIGHT[level]


class QualityLevel():
    # bitrates kbps
    BIT_RATEE_LEVEL_5 = 2500
    BIT_RATEE_LEVEL_4 = 2000
    BIT_RATEE_LEVEL_3 = 1500
    BIT_RATEE_LEVEL_2 = 1000
    BIT_RATEE_LEVEL_1 = 500
    BIT_RATE = [0, BIT_RATEE_LEVEL_1, BIT_RATEE_LEVEL_2, BIT_RATEE_LEVEL_3, BIT_RATEE_LEVEL_4, BIT_RATEE_LEVEL_5]

    # resolution width
    WIDTH_LEVEL_5 = 1280
    WIDTH_LEVEL_4 = 640
    WIDTH_LEVEL_3 = 480
    WIDTH_LEVEL_2 = 320
    WIDTH_LEVEL_1 = 192
    WIDTH = [0, WIDTH_LEVEL_1, WIDTH_LEVEL_2, WIDTH_LEVEL_3, WIDTH_LEVEL_4, WIDTH_LEVEL_5]

    # resolution height
    HEIGHT_LEVEL_5 = 720
    HEIGHT_LEVEL_4 = 480
    HEIGHT_LEVEL_3 = 360
    HEIGHT_LEVEL_2 = 240
    HEIGHT_LEVEL_1 = 144
    HEIGHT = [0, HEIGHT_LEVEL_1, HEIGHT_LEVEL_2, HEIGHT_LEVEL_3, HEIGHT_LEVEL_4, HEIGHT_LEVEL_5]
