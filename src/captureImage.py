# -- coding: utf-8 --
# 捕获视频帧
from FFmpegUtil import *

chunk_file_name = '118-120.avi'


def capture_image(input_file, out_file_dir):
    '''
    截取input_file的[start,end]的每一帧，存储到out_file_dir中
    :param input_file: 要capture的视频文件
    :param start: 从第几帧开始截取
    :param end ：到这一帧结束
    :param out_file_dir: 输出的文件夹
    :return:
    '''
    cmd = "ffmpeg -y -i {} -vf fps=24 {}/%2d.jpeg".format(input_file,out_file_dir)
    print(cmd)
    run_command(cmd)


def main():
    for level in range(1,6):
        out_dir = "../img/level%s"%level
        make_dirs_if_not_exists(out_dir)
        capture_image("../video/level%s/%s"%(level,chunk_file_name),out_dir)


if __name__ == '__main__':
    main()