# coding:utf-8
import time

from FFmpegUtil import *



def testCmd():
    startTimestamp = time.time()
    os.system(r"../dir")
    print("你好")
    endTimestamp = time.time()
    print("time: ", endTimestamp, startTimestamp, endTimestamp - startTimestamp)


def main():
    # 1. 将原视频转成level5的视频 level5.avi
    # trans_video_code(input_file="../../1080p_24fps/big_buck_bunny_1080p_surround.avi",
    #                  width=QualityLevel.WIDTH_LEVEL_5,
    #                  height=QualityLevel.HEIGHT_LEVEL_5,
    #                  rate=QualityLevel.BIT_RATEE_LEVEL_5,
    #                  out_file="../video/level5.avi")

    # 将level5.avi切成大小是2s的chunk
    cutting_video_to_chunks(input_file="../video/level5.avi", chunk_size=2, level=5)


if __name__ == '__main__':
    main()
