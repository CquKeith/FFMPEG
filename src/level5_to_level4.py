# -- coding: utf-8 --
# test level5 transcode to level4

from FFmpegUtil import *

def main():
    # 1. 将原视频转成level5的视频 level5.avi
    trans_video_code(input_file="../../1080p_24fps/big_buck_bunny_1080p_surround.avi",
                     width=QualityLevel.WIDTH_LEVEL_5,
                     height=QualityLevel.HEIGHT_LEVEL_5,
                     rate=QualityLevel.BIT_RATEE_LEVEL_5,
                     out_file="../video/level5.avi")


if __name__ == '__main__':
    main()