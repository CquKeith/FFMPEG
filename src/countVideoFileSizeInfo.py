# -- coding: utf-8 --
# 统计每个level chunk的大小平均值、方差、协方差
import json

import matplotlib.pyplot as plt
import numpy as np

from FFmpegUtil import *

plot_level_color = ['skyblue', 'blue', 'green', 'red', 'indigo']


def count_chunks_size(dir):
    '''
    统计dir内的所有chunks的大小
    :param dir:
    :return: chunk的大小平均值、方差、协方差
    '''
    chunks_size = []
    # 每个chunk起始秒数
    chunk_start_seconds = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            chunks_size.append(get_file_size(dir + '/' + file))
            chunk_start_seconds.append(file.split('-')[0])

        # 平均值 KB
        avg = np.mean(chunks_size)
        # 方差
        var = np.var(chunks_size)
        # 协方差
        cov = np.cov(chunks_size)
        return avg, var, cov, chunks_size, chunk_start_seconds


def get_file_size(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024)
    return round(fsize, 2)


def get_video_json_info(file_path):
    cmd = "ffprobe -v quiet -print_format json -show_format -show_streams -i %s" % file_path
    my_string = os.popen(cmd).read()
    return my_string


def format_file_size(size):
    '''

    :param size:  unit: Byte
    :return:
    '''
    KB = size / 1024
    MB = KB / 1024
    return round(MB, 2)


def format_bit_rate(bit_rate):
    Kbps = bit_rate / 1000
    Mbps = Kbps / 1000
    return round(Mbps, 2)


def parse_video_info_json(json_obj):
    try:

        duration = round(eval(json_obj['format']['duration']), 3)

        size = eval(json_obj['format']['size'])
        bit_rate = eval(json_obj['format']['bit_rate'])
        formatted_size = format_file_size(size)
        formatted_bit_rate = format_bit_rate(bit_rate)
        print('%s s, %s MB, %s Mbps' % (duration, formatted_size, formatted_bit_rate))
        return duration, formatted_size, formatted_bit_rate
    except Exception:
        print(str(json_obj))


def draw_chunk_size(chunks_start_seconds, chunk_size_list, level):
    '''

    :param chunks_start_seconds:
    :param chunk_size_list:
    :param level:
    :return:
    '''
    # 开始画图
    # sub_axix = filter(lambda x: x % 200 == 0, x_axix)
    plt.title('Chunk Size of Different Quality Level')
    plt.plot(chunks_start_seconds, chunk_size_list, color=plot_level_color[level - 1], label='level %s' % level)
    plt.legend()  # 显示图例

    plt.xlabel('chunk start seconds')
    plt.ylabel('chunk size(KB)')
    plt.show()
    # python 一个折线图绘制多个曲线


def get_all_chunks_path_in_dir(chunks_dir):
    chunks_path = []
    for root, dirs, files in os.walk(chunks_dir):
        for file in files:
            chunks_path.append('%s/%s' % (chunks_dir, file))
    return chunks_path


def get_video_info(file_path):
    json_str = get_video_json_info(file_path)
    return parse_video_info_json(json.loads(json_str))


def plot_my_figure(x, y, title):
    plt.title(title)
    plt.plot(x, y)

    plt.show()


def statics_chunks_info(chunks_dir):
    chunks_file_path = get_all_chunks_path_in_dir(chunks_dir)
    duration_list = []
    chunk_size_list = []
    chunk_bit_rate_list = []
    x = [i + 1 for i in range(len(chunks_file_path))]
    for file_path in chunks_file_path:
        duration, size, bit_rate = get_video_info(file_path)
        duration_list.append(duration)
        chunk_size_list.append(size)
        chunk_bit_rate_list.append(bit_rate)

    print('chunk avg size(KB) : %s' % np.mean(chunk_size_list))

    plot_my_figure(x=x, y=duration_list, title='chunk duration')
    plot_my_figure(x=x, y=chunk_size_list, title='chunk size(MB)')
    plot_my_figure(x=x, y=chunk_bit_rate_list, title='chunk bitrate(Mbps)')


def plot_chunk_size_of_diffent_level():
    # 开始画图
    # sub_axix = filter(lambda x: x % 200 == 0, x_axix)
    plt.title('Chunk Size of Different Quality Level')

    with open("../video/size_statistics.csv", "w", newline='') as f:
        csv_writer = csv.writer(f)
        headers = ["level", "avg size(KB)", "var", "cov"]
        csv_writer.writerow(headers)
        for level in range(1, 6):
            avg, var, cov, chunk_size_list, chunk_start_seconds = count_chunks_size("../video/level%s" % level)
            csv_writer.writerow([level, round(avg,2), round(var,2), cov])
            # draw_chunk_size(chunk_start_seconds,chunk_size_list,i)
            plt.plot(chunk_start_seconds, chunk_size_list, color=plot_level_color[level - 1], label='level %s' % level)

    plt.legend()  # 显示图例

    plt.xlabel('chunk start seconds')
    plt.ylabel('chunk size(KB)')
    plt.show()

    # plt.savefig('../img/size.png', dpi=900)


def main():
    # plot_chunk_size_of_diffent_level()
    statics_chunks_info('../video/level5')


if __name__ == '__main__':
    main()
