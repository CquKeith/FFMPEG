# coding:utf-8

from FFmpegUtil import *
from Chunk_quality_level_enum import *

def testCmd():
    start_timestamp = time.time()
    os.system(r"../dir")
    print("你好")
    end_timestamp = time.time()
    print("time: ", end_timestamp, start_timestamp, end_timestamp - start_timestamp)

def trancode_src_video_to_level5_and_cut_to_chunks():
    # 1. 将原视频转成level5的视频 level5.avi
    trans_video_code(input_file="../../1080p_24fps/big_buck_bunny_1080p_surround.avi",
                     width=QualityLevel.WIDTH_LEVEL_5,
                     height=QualityLevel.HEIGHT_LEVEL_5,
                     rate=QualityLevel.BIT_RATEE_LEVEL_5,
                     out_file="../video/level5.avi")

    # 将level5.avi切成大小是2s的chunk
    cutting_video_to_chunks(input_file="../video/level5.avi", chunk_size=2, level=5)

def cut_source_video_to_chunks():
    # 将原始文件切成大小是2s的chunk

    time = cutting_video_to_chunks(input_file="../../1080p_24fps/big_buck_bunny_1080p_surround.avi", chunk_size=2, level='src')
    print('耗时 %s s' % time)

def main():
    cut_source_video_to_chunks()


if __name__ == '__main__':
    main()
