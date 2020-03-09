# -- coding: utf-8 --
# 统计每个level chunk的大小平均值、方差、协方差
import os
import numpy as np
import csv
import matplotlib.pyplot as plt

plot_level_color = ['skyblue','blue','green','red','indigo']

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
            chunks_size.append(get_FileSize(dir + '/' + file))
            chunk_start_seconds.append(file.split('-')[0])

        # 平均值 KB
        avg = np.mean(chunks_size)
        # 方差
        var = np.var(chunks_size)
        # 协方差
        cov = np.cov(chunks_size)
        return avg, var, cov,chunks_size,chunk_start_seconds


def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024)
    return round(fsize, 2)


def draw_chunk_size(chunks_start_seconds,chunk_size_list,level):
    '''

    :param chunks_start_seconds:
    :param chunk_size_list:
    :param level:
    :return:
    '''
    # 开始画图
    # sub_axix = filter(lambda x: x % 200 == 0, x_axix)
    plt.title('Chunk Size of Different Quality Level')
    plt.plot(chunks_start_seconds, chunk_size_list, color=plot_level_color[level-1], label='level %s'%level)
    plt.legend()  # 显示图例

    plt.xlabel('chunk start seconds')
    plt.ylabel('chunk size(KB)')
    plt.show()
    # python 一个折线图绘制多个曲线


def main():
    # 开始画图
    # sub_axix = filter(lambda x: x % 200 == 0, x_axix)
    plt.title('Chunk Size of Different Quality Level')

    with open("../video/size_statistics.csv", "w", newline='') as f:
        csv_writer = csv.writer(f)
        headers = ["level", "avg size(KB)", "var", "cov"]
        csv_writer.writerow(headers)
        for level in range(1, 6):
            avg, var, cov,chunk_size_list,chunk_start_seconds = count_chunks_size("../video/level%s" % level)
            csv_writer.writerow([level, avg, var, cov])
            # draw_chunk_size(chunk_start_seconds,chunk_size_list,i)
            plt.plot(chunk_start_seconds, chunk_size_list, color=plot_level_color[level - 1], label='level %s' % level)

    plt.legend()  # 显示图例

    plt.xlabel('chunk start seconds')
    plt.ylabel('chunk size(KB)')
    plt.show()

    plt.savefig('size.png',dpi=900)

if __name__ == '__main__':
    main()
