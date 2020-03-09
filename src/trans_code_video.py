# -- coding: utf-8 --


from FFmpegUtil import *


def main():
    # 3.将level5的chunks依此转成level4~1的chunks，并统计时间
    trans_chunks_code_to_low_level(input_dir="../video/level5", current_level=5)
    # 将level1~4 移至与level5同层目录
    for level in range(1, 5):
        move_dir("../video/level5/level%s" % (level), "../video")

    # 4. 依次将level4的chunks依次转化成level 3~1，并统计转码时间
    # 5. 直到level 2的chunks全部转化成level 1，并统计转码时间
    for i in range(4, 1, -1):
        trans_chunks_code_to_low_level(input_dir="../video/level%s" % i,current_level=i)


def move_dir(src_dir, des_dir):
    '''
    移动文件夹
    :param src_dir: 源文件夹
    :param des_dir: 目标文件夹
    :return:
    '''
    cmd = "move %s %s" % (src_dir, des_dir)
    return run_command(cmd)


if __name__ == '__main__':
    main()
